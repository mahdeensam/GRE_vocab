from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, jsonify, request, redirect, session, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.middleware.proxy_fix import ProxyFix
from openai import OpenAI
from datetime import datetime
import random
import json
import os
import secrets

app = Flask(__name__)

# Tell Flask it's behind Render's reverse proxy (HTTPS termination)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# --- Config ---
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

# Database: prefer DATABASE_URL (Render PostgreSQL), fallback to local SQLite
database_url = os.environ.get('DATABASE_URL', 'sqlite:///data-dev.sqlite')
# Render uses postgres:// but SQLAlchemy needs postgresql://
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Pool settings for production PostgreSQL
if database_url.startswith('postgresql://'):
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': 5,
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }

# Session cookie config
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = not os.environ.get('FLASK_DEBUG')
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Google OAuth config
app.config['GOOGLE_CLIENT_ID'] = os.environ.get('GOOGLE_CLIENT_ID', '')
app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get('GOOGLE_CLIENT_SECRET', '')
app.config['GOOGLE_REDIRECT_URI'] = os.environ.get('GOOGLE_REDIRECT_URI', 'http://localhost:5000/auth/callback')

# --- Extensions ---
db = SQLAlchemy(app)
login_manager = LoginManager(app)


# --- Models ---
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    google_sub = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))
    picture = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    progress = db.relationship('UserWordProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    quant_progress = db.relationship('UserQuantProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')


class UserWordProgress(db.Model):
    __tablename__ = 'user_word_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(20), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'word', name='uq_user_word'),)


class UserQuantProgress(db.Model):
    __tablename__ = 'user_quant_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_key = db.Column(db.String(200), nullable=False)
    data_type = db.Column(db.String(20), nullable=False)  # 'favorite', 'learned', 'rating', 'assessment'
    value = db.Column(db.String(50), nullable=False)       # e.g. 'true', 'easy', 'hard', 'know', 'shaky'
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'question_key', 'data_type', name='uq_user_quant'),)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# Create tables (retry-safe — won't crash app if DB is still starting)
def init_db():
    try:
        with app.app_context():
            db.create_all()
            app.logger.info('Database tables created.')
    except Exception as e:
        app.logger.warning(f'Could not create tables on startup: {e}')

init_db()

@app.before_request
def ensure_tables():
    if not getattr(app, '_db_ready', False):
        try:
            db.create_all()
            app._db_ready = True
        except Exception:
            pass


# ═══════════════════════════════════════════════
# VERBAL DATA
# ═══════════════════════════════════════════════
def load_memory_hooks():
    path = os.path.join(os.path.dirname(__file__), 'memory_hooks.json')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

MEMORY_HOOKS = load_memory_hooks()

def load_words():
    path = os.path.join(os.path.dirname(__file__), 'words.json')
    with open(path, 'r', encoding='utf-8') as f:
        raw_words = json.load(f)
    words = []
    for w in raw_words:
        hook_data = MEMORY_HOOKS.get(w['word'].lower(), {})
        w['memory_hook'] = hook_data.get('hook', '')
        w['hook_type'] = hook_data.get('type', '')
        words.append(w)
    return words

WORDS = load_words()

def load_concept_groups():
    path = os.path.join(os.path.dirname(__file__), 'concept_groups.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

CONCEPT_GROUPS = load_concept_groups()

def load_lookalikes():
    path = os.path.join(os.path.dirname(__file__), 'lookalikes.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

LOOKALIKES = load_lookalikes()


# ═══════════════════════════════════════════════
# QUANT DATA (lazy-loaded to avoid worker boot crash on constrained hosts)
# ═══════════════════════════════════════════════
_quant_loaded = False
QUANT_TOPICS = []
QUANT_CATEGORIES = []

def _ensure_quant():
    global _quant_loaded, QUANT_TOPICS, QUANT_CATEGORIES
    if _quant_loaded:
        return
    try:
        from quant_data import TOPICS, CATEGORIES
        QUANT_TOPICS.extend(TOPICS)
        QUANT_CATEGORIES.extend(CATEGORIES)
        _quant_loaded = True
    except Exception as e:
        app.logger.error(f'Failed to load quant data: {e}')

def _build_topics_json():
    _ensure_quant()
    from quant_data import _build_topics_json as _btj
    return _btj()

def _build_categories_json():
    _ensure_quant()
    from quant_data import _build_categories_json as _bcj
    return _bcj()


# ═══════════════════════════════════════════════
# VERBAL PRACTICE DATA (lazy-loaded like quant)
# ═══════════════════════════════════════════════
_verbal_practice_loaded = False
VERBAL_TOPICS = []
VERBAL_CATEGORIES = []

def _ensure_verbal_practice():
    global _verbal_practice_loaded, VERBAL_TOPICS, VERBAL_CATEGORIES
    if _verbal_practice_loaded:
        return
    try:
        from verbal_data import VERBAL_TOPICS as VT, VERBAL_CATEGORIES as VC
        VERBAL_TOPICS.extend(VT)
        VERBAL_CATEGORIES.extend(VC)
        _verbal_practice_loaded = True
    except Exception as e:
        app.logger.error(f'Failed to load verbal practice data: {e}')

def _build_verbal_topics_json():
    _ensure_verbal_practice()
    from verbal_data import _build_verbal_topics_json as _bvtj
    return _bvtj()

def _build_verbal_categories_json():
    _ensure_verbal_practice()
    from verbal_data import _build_verbal_categories_json as _bvcj
    return _bvcj()


# ═══════════════════════════════════════════════
# LANDING PAGE
# ═══════════════════════════════════════════════
@app.route('/')
def landing():
    _ensure_quant()
    verbal_hook_count = sum(1 for w in WORDS if w.get('memory_hook'))
    quant_q_count = sum(sum(len(s['questions']) for s in t['sections']) for t in QUANT_TOPICS)
    return render_template('landing.html',
                           verbal_word_count=len(WORDS),
                           verbal_group_count=len(CONCEPT_GROUPS),
                           verbal_hook_count=verbal_hook_count,
                           quant_question_count=quant_q_count,
                           quant_topic_count=len(QUANT_TOPICS),
                           quant_category_count=len(QUANT_CATEGORIES))


# ═══════════════════════════════════════════════
# VERBAL ROUTES
# ═══════════════════════════════════════════════
@app.route('/verbal')
def verbal():
    hook_count = sum(1 for w in WORDS if w.get('memory_hook'))
    return render_template('index.html', total=len(WORDS),
                           concept_group_count=len(CONCEPT_GROUPS),
                           hook_count=hook_count)


# --- Word API ---
@app.route('/api/words')
def api_words():
    q = request.args.get('q', '').lower()
    if q:
        filtered = [w for w in WORDS if q in w['word'].lower() or q in w['meaning'].lower() or q in w.get('memory_hook', '').lower()]
    else:
        filtered = WORDS
    return jsonify(filtered)

@app.route('/api/flashcard')
def api_flashcard():
    return jsonify(random.choice(WORDS))

@app.route('/api/flashcards/batch')
def api_flashcard_batch():
    count = min(int(request.args.get('count', 20)), len(WORDS))
    return jsonify(random.sample(WORDS, count))

@app.route('/api/concept-groups')
def api_concept_groups():
    return jsonify(CONCEPT_GROUPS)

@app.route('/api/lookalikes')
def api_lookalikes():
    return jsonify(LOOKALIKES)


# ═══════════════════════════════════════════════
# QUANT ROUTES
# ═══════════════════════════════════════════════
@app.route('/quant')
@app.route('/quant/')
def quant_index():
    _ensure_quant()
    cat_counts = {}
    total_q = 0
    for c in QUANT_CATEGORIES:
        cat_counts[c['id']] = {'topics': 0, 'questions': 0}
    for t in QUANT_TOPICS:
        qc = sum(len(s['questions']) for s in t['sections'])
        total_q += qc
        cat_counts[t['category']]['topics'] += 1
        cat_counts[t['category']]['questions'] += qc
    return render_template('quant/index.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           cat_counts=cat_counts, total_q=total_q)

@app.route('/quant/topic/<topic_id>')
def quant_topic(topic_id):
    _ensure_quant()
    t = next((t for t in QUANT_TOPICS if t['id'] == topic_id), None)
    if t is None:
        return 'Topic not found', 404
    return render_template('quant/topic.html', topic=t, topics=QUANT_TOPICS, categories=QUANT_CATEGORIES)

@app.route('/quant/favorites')
def quant_favorites():
    _ensure_quant()
    topics_data = _build_topics_json()
    return render_template('quant/favorites.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data))

@app.route('/quant/flashcards')
def quant_flashcards():
    _ensure_quant()
    topics_data = _build_topics_json()
    categories_data = _build_categories_json()
    return render_template('quant/flashcards.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))

@app.route('/quant/flashcards/study')
def quant_flashcard_study():
    _ensure_quant()
    topics_data = _build_topics_json()
    categories_data = _build_categories_json()
    return render_template('quant/study.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))

@app.route('/quant/dashboard')
def quant_dashboard():
    _ensure_quant()
    topics_data = _build_topics_json()
    categories_data = _build_categories_json()
    return render_template('quant/dashboard.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))

@app.route('/quant/assessment')
def quant_assessment():
    _ensure_quant()
    topics_data = _build_topics_json()
    categories_data = _build_categories_json()
    return render_template('quant/assessment.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))

@app.route('/quant/assessment/test')
def quant_assessment_test():
    _ensure_quant()
    topics_data = _build_topics_json()
    categories_data = _build_categories_json()
    return render_template('quant/assessment_test.html', topics=QUANT_TOPICS, categories=QUANT_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))


# ═══════════════════════════════════════════════
# VERBAL PRACTICE ROUTES
# ═══════════════════════════════════════════════
@app.route('/verbal/practice')
@app.route('/verbal/practice/')
def verbal_practice_index():
    _ensure_verbal_practice()
    cat_counts = {}
    total_q = 0
    for c in VERBAL_CATEGORIES:
        cat_counts[c['id']] = {'topics': 0, 'questions': 0}
    for t in VERBAL_TOPICS:
        qc = sum(len(s['questions']) for s in t['sections'])
        total_q += qc
        cat_counts[t['category']]['topics'] += 1
        cat_counts[t['category']]['questions'] += qc
    return render_template('verbal/practice_index.html', topics=VERBAL_TOPICS, categories=VERBAL_CATEGORIES,
                           cat_counts=cat_counts, total_q=total_q)

@app.route('/verbal/practice/topic/<topic_id>')
def verbal_practice_topic(topic_id):
    _ensure_verbal_practice()
    t = next((t for t in VERBAL_TOPICS if t['id'] == topic_id), None)
    if t is None:
        return 'Topic not found', 404
    return render_template('verbal/practice_topic.html', topic=t, topics=VERBAL_TOPICS, categories=VERBAL_CATEGORIES)

@app.route('/verbal/practice/assessment')
def verbal_practice_assessment():
    _ensure_verbal_practice()
    topics_data = _build_verbal_topics_json()
    categories_data = _build_verbal_categories_json()
    return render_template('verbal/practice_assessment.html', topics=VERBAL_TOPICS, categories=VERBAL_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))

@app.route('/verbal/practice/assessment/test')
def verbal_practice_assessment_test():
    _ensure_verbal_practice()
    topics_data = _build_verbal_topics_json()
    categories_data = _build_verbal_categories_json()
    return render_template('verbal/practice_assessment_test.html', topics=VERBAL_TOPICS, categories=VERBAL_CATEGORIES,
                           topics_json=json.dumps(topics_data),
                           categories_json=json.dumps(categories_data))


# ═══════════════════════════════════════════════
# AUTH ROUTES
# ═══════════════════════════════════════════════
@app.route('/auth/google')
def auth_google():
    from google_auth import GoogleOAuthManager
    state = secrets.token_urlsafe(32)
    session['oauth_state'] = state
    oauth = GoogleOAuthManager()
    url = oauth.get_authorization_url(state=state)
    return redirect(url)

@app.route('/auth/callback')
def auth_callback():
    from google_auth import GoogleOAuthManager, GoogleOAuthError
    import traceback

    # Validate state
    state = request.args.get('state')
    saved_state = session.pop('oauth_state', None)
    if not state or state != saved_state:
        app.logger.error(f'OAuth state mismatch: got={state}, saved={saved_state}')
        return f'Auth error: state mismatch (got={state is not None}, saved={saved_state is not None})', 400

    code = request.args.get('code')
    if not code:
        return 'Auth error: no code from Google', 400

    try:
        oauth = GoogleOAuthManager()
        token_data = oauth.exchange_code_for_tokens(code)
        access_token = token_data.get('access_token')
        if not access_token:
            app.logger.error(f'No access_token in response: {token_data}')
            return 'Auth error: no access token', 400

        user_info = oauth.get_user_info(access_token)
    except Exception as e:
        app.logger.error(f'OAuth exchange failed: {traceback.format_exc()}')
        return f'Auth error: {e}', 500

    google_sub = user_info.get('sub')
    if not google_sub:
        return f'Auth error: no sub in user info: {user_info}', 400

    try:
        # Find or create user
        user = User.query.filter_by(google_sub=google_sub).first()
        if user:
            user.email = user_info.get('email', user.email)
            user.name = user_info.get('name', user.name)
            user.picture = user_info.get('picture', user.picture)
            user.last_login = datetime.utcnow()
        else:
            user = User(
                google_sub=google_sub,
                email=user_info.get('email', ''),
                name=user_info.get('name', ''),
                picture=user_info.get('picture', ''),
            )
            db.session.add(user)

        db.session.commit()
        login_user(user, remember=True)
    except Exception as e:
        app.logger.error(f'DB/login failed: {traceback.format_exc()}')
        return f'Auth error (DB): {e}', 500

    return redirect('/')

@app.route('/auth/logout')
def auth_logout():
    logout_user()
    return redirect('/')

@app.route('/auth/debug')
def auth_debug():
    return jsonify({
        'has_client_id': bool(app.config.get('GOOGLE_CLIENT_ID')),
        'has_client_secret': bool(app.config.get('GOOGLE_CLIENT_SECRET')),
        'redirect_uri': app.config.get('GOOGLE_REDIRECT_URI'),
        'database_url_type': 'postgresql' if 'postgresql' in app.config.get('SQLALCHEMY_DATABASE_URI', '') else 'sqlite',
        'has_secret_key': bool(app.config.get('SECRET_KEY')),
    })

@app.route('/auth/me')
def auth_me():
    if current_user.is_authenticated:
        return jsonify({'user': {
            'id': current_user.id,
            'name': current_user.name,
            'email': current_user.email,
            'picture': current_user.picture,
        }})
    return jsonify({'user': None})


# ═══════════════════════════════════════════════
# VERBAL PROGRESS API
# ═══════════════════════════════════════════════
@app.route('/api/progress')
def get_progress():
    if not current_user.is_authenticated:
        return jsonify({'tags': {}})
    rows = UserWordProgress.query.filter_by(user_id=current_user.id).all()
    tags = {r.word: r.tag for r in rows}
    return jsonify({'tags': tags})

@app.route('/api/progress', methods=['POST'])
def save_progress():
    if not current_user.is_authenticated:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()
    if not data or 'tags' not in data:
        return jsonify({'error': 'Missing tags'}), 400

    incoming_tags = data['tags']

    # Full replace: delete all existing, insert new
    UserWordProgress.query.filter_by(user_id=current_user.id).delete()
    for word, tag in incoming_tags.items():
        if tag in ('learning', 'learned', 'confused', 'hard'):
            db.session.add(UserWordProgress(
                user_id=current_user.id,
                word=word,
                tag=tag,
            ))
    db.session.commit()

    # Return updated tags
    rows = UserWordProgress.query.filter_by(user_id=current_user.id).all()
    tags = {r.word: r.tag for r in rows}
    return jsonify({'tags': tags})


# ═══════════════════════════════════════════════
# QUANT PROGRESS API
# ═══════════════════════════════════════════════
@app.route('/api/quant/progress')
def get_quant_progress():
    if not current_user.is_authenticated:
        return jsonify({'favorites': [], 'learned': [], 'ratings': {}, 'assessment': {}})

    rows = UserQuantProgress.query.filter_by(user_id=current_user.id).all()
    favorites = []
    learned = []
    ratings = {}
    assessment = {}
    for r in rows:
        if r.data_type == 'favorite':
            favorites.append(r.question_key)
        elif r.data_type == 'learned':
            learned.append(r.question_key)
        elif r.data_type == 'rating':
            ratings[r.question_key] = json.loads(r.value)
        elif r.data_type == 'assessment':
            assessment[r.question_key] = json.loads(r.value)
    return jsonify({'favorites': favorites, 'learned': learned, 'ratings': ratings, 'assessment': assessment})

@app.route('/api/quant/progress', methods=['POST'])
def save_quant_progress():
    if not current_user.is_authenticated:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing data'}), 400

    # Full replace: delete all existing, insert new
    UserQuantProgress.query.filter_by(user_id=current_user.id).delete()

    for qkey in data.get('favorites', []):
        db.session.add(UserQuantProgress(
            user_id=current_user.id, question_key=qkey,
            data_type='favorite', value='true'))

    for qkey in data.get('learned', []):
        db.session.add(UserQuantProgress(
            user_id=current_user.id, question_key=qkey,
            data_type='learned', value='true'))

    for qkey, val in data.get('ratings', {}).items():
        db.session.add(UserQuantProgress(
            user_id=current_user.id, question_key=qkey,
            data_type='rating', value=json.dumps(val)))

    for qkey, val in data.get('assessment', {}).items():
        db.session.add(UserQuantProgress(
            user_id=current_user.id, question_key=qkey,
            data_type='assessment', value=json.dumps(val)))

    db.session.commit()
    return jsonify({'ok': True})


# ═══════════════════════════════════════════════
# TTS API
# ═══════════════════════════════════════════════
openai_client = None
def get_openai():
    global openai_client
    if openai_client is None:
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            return None
        openai_client = OpenAI(api_key=api_key)
    return openai_client

@app.route('/api/tts', methods=['POST'])
def tts():
    client = get_openai()
    if not client:
        return jsonify({'error': 'TTS not configured'}), 503

    data = request.get_json()
    text = data.get('text', '')[:1000]  # limit length
    if not text:
        return jsonify({'error': 'No text'}), 400

    response = client.audio.speech.create(
        model='tts-1-hd',
        voice='fable',
        input=text,
        speed=0.85,
    )

    return Response(response.content, mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
