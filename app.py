from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, jsonify, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.middleware.proxy_fix import ProxyFix
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


class UserWordProgress(db.Model):
    __tablename__ = 'user_word_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(20), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'word', name='uq_user_word'),)


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


# --- Word data ---
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


# --- Page routes ---
@app.route('/')
def index():
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


# --- Auth routes ---
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


# --- Progress API ---
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
