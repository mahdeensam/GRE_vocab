from flask import Flask, render_template, jsonify, request
import random
import json
import os

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', total=len(WORDS))

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
