/* ══════════════════════════════════════════════════
   GRE Verbal Practice — Interactivity
   (Adapted from quant-app.js for verbal question types)
   ══════════════════════════════════════════════════ */

// ── Favorites (localStorage) ──────────────────────
function getFavs() {
  try { return JSON.parse(localStorage.getItem('gre_verbal_favorites') || '[]'); }
  catch(e) { return []; }
}
function saveFavs(favs) { localStorage.setItem('gre_verbal_favorites', JSON.stringify(favs)); }
function isFav(qKey) { return getFavs().includes(qKey); }
function toggleFav(qKey) {
  var favs = getFavs();
  var idx = favs.indexOf(qKey);
  if (idx === -1) favs.push(qKey); else favs.splice(idx, 1);
  saveFavs(favs);
  var btn = document.querySelector('.fav-btn[data-qkey="' + qKey + '"]');
  if (btn) btn.classList.toggle('fav-active', favs.includes(qKey));
}

// ── Learned (localStorage) ────────────────────────
function getLearned() {
  try { return JSON.parse(localStorage.getItem('gre_verbal_learned') || '[]'); }
  catch(e) { return []; }
}
function saveLearned(list) { localStorage.setItem('gre_verbal_learned', JSON.stringify(list)); }
function toggleLearned(qKey) {
  var list = getLearned();
  var idx = list.indexOf(qKey);
  if (idx === -1) list.push(qKey); else list.splice(idx, 1);
  saveLearned(list);
  var btn = document.querySelector('.learned-btn[data-qkey="' + qKey + '"]');
  if (btn) btn.classList.toggle('learned-active', list.includes(qKey));
}

// ── Assessment Storage ────────────────────────────
function getAssessment() {
  try { return JSON.parse(localStorage.getItem('gre_verbal_assessment') || '{}'); }
  catch(e) { return {}; }
}
function saveAssessment(data) { localStorage.setItem('gre_verbal_assessment', JSON.stringify(data)); }
function assessQuestion(qKey, level) {
  var data = getAssessment();
  data[qKey] = { level: level, date: new Date().toISOString().slice(0, 10) };
  saveAssessment(data);
}

// ── Ratings (localStorage) ────────────────────────
function getRatings() {
  try { return JSON.parse(localStorage.getItem('gre_verbal_ratings') || '{}'); }
  catch(e) { return {}; }
}
function saveRatings(ratings) { localStorage.setItem('gre_verbal_ratings', JSON.stringify(ratings)); }
function rateQuestion(qKey, rating) {
  var ratings = getRatings();
  var existing = ratings[qKey] || { count: 0 };
  ratings[qKey] = { rating: rating, date: new Date().toISOString().slice(0, 10), count: existing.count + 1 };
  saveRatings(ratings);
}

// ── Utilities ─────────────────────────────────────
function buildQuestionIndex() {
  if (!window.ALL_TOPICS) return [];
  var index = [];
  ALL_TOPICS.forEach(function(topic) {
    topic.sections.forEach(function(section, si) {
      section.questions.forEach(function(q) {
        var qKey = topic.id + '_' + si + '_' + q.id;
        index.push({ q: q, section: section, topic: topic, si: si, qKey: qKey });
      });
    });
  });
  return index;
}

function shuffle(arr) {
  var a = arr.slice();
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
  }
  return a;
}

function escHtml(str) {
  var d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

// ── Answer Reveal ─────────────────────────────────
function toggleAnswer(qKey) {
  var box = document.getElementById('ans-' + qKey);
  if (!box) return;
  var isVisible = box.classList.toggle('answer-visible');
  var btn = box.previousElementSibling;
  if (btn && btn.classList.contains('reveal-btn')) {
    btn.textContent = isVisible ? 'Hide Answer' : 'Show Answer';
  }
}

// ── Sidebar Toggle ────────────────────────────────
function toggleSidebarGroup(btn) {
  var group = btn.closest('.sidebar-group');
  if (group) group.classList.toggle('open');
}
function toggleMobileMenu() {
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('sidebar-overlay');
  if (sidebar) sidebar.classList.toggle('mobile-open');
  if (overlay) overlay.classList.toggle('mobile-open');
}

// ══════════════════════════════════════════════════
// ── Assessment Hub ────────────────────────────────
// ══════════════════════════════════════════════════
function initAssessmentHub() {
  var container = document.getElementById('assessment-hub');
  if (!container || !window.ALL_TOPICS || !window.ALL_CATEGORIES) return;

  var index = buildQuestionIndex();
  var assess = getAssessment();
  var total = index.length;

  var know = 0, shaky = 0, study = 0;
  index.forEach(function(item) {
    var a = assess[item.qKey];
    if (!a) return;
    if (a.level === 'know') know++;
    else if (a.level === 'shaky') shaky++;
    else study++;
  });
  var assessed = know + shaky + study;

  var html = '';

  // ── Stats Grid ──
  html += '<div class="assess-stat-grid">';
  html += assessStatCard('Total', total, '&#128218;', '');
  html += assessStatCard('Assessed', assessed, '&#9733;', '');
  html += assessStatCard('I Know', know, '&#10003;', 'know');
  html += assessStatCard('Shaky', shaky, '&#8776;', 'shaky');
  html += assessStatCard('Need to Study', study, '&#10007;', 'study');
  html += '</div>';

  // ── Deck: By Category ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Category</h2><div class="deck-grid">';
  ALL_CATEGORIES.forEach(function(cat) {
    var count = index.filter(function(item) { return item.topic.category === cat.id; }).length;
    html += assessDeckCard(cat.icon, cat.name, count + ' questions', '/verbal/practice/assessment/test?deck=category&id=' + cat.id);
  });
  html += '</div></div>';

  // ── Deck: By Topic ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Topic</h2><div class="deck-grid">';
  ALL_TOPICS.forEach(function(topic) {
    var count = 0;
    topic.sections.forEach(function(s) { count += s.questions.length; });
    html += assessDeckCard(topic.icon, topic.title, count + ' questions', '/verbal/practice/assessment/test?deck=topic&id=' + topic.id);
  });
  html += '</div></div>';

  // ── Smart Decks ──
  var unassessedCount = index.filter(function(item) { return !assess[item.qKey]; }).length;
  var weakCount = index.filter(function(item) {
    var a = assess[item.qKey];
    return a && (a.level === 'shaky' || a.level === 'study');
  }).length;
  html += '<div class="deck-group"><h2 class="deck-group-title">Smart Decks</h2><div class="deck-grid">';
  html += assessDeckCard('&#10067;', 'Unassessed Only', unassessedCount + ' remaining', '/verbal/practice/assessment/test?deck=unassessed');
  html += assessDeckCard('&#128260;', 'Reassess Weak', weakCount + ' to reassess', '/verbal/practice/assessment/test?deck=reassess');
  html += assessDeckCard('&#127922;', 'Random Mix', '50 questions', '/verbal/practice/assessment/test?deck=random');
  html += assessDeckCard('&#128221;', 'Full Assessment', total + ' questions', '/verbal/practice/assessment/test?deck=full');
  html += '</div></div>';

  // ── Knowledge Map ──
  html += '<h2 class="deck-group-title">Knowledge Map</h2>';
  html += '<div class="chart-container">';
  html += '<h3 class="assess-chart-subtitle">By Category</h3>';
  ALL_CATEGORIES.forEach(function(cat) {
    var catItems = index.filter(function(item) { return item.topic.category === cat.id; });
    var counts = countAssessment(catItems, assess);
    html += renderAssessChartRow(cat.name, counts, catItems.length);
  });
  html += '<h3 class="assess-chart-subtitle" style="margin-top:1.25rem;">By Topic</h3>';
  ALL_TOPICS.forEach(function(topic) {
    var topicItems = index.filter(function(item) { return item.topic.id === topic.id; });
    var counts = countAssessment(topicItems, assess);
    html += renderAssessChartRow(topic.title, counts, topicItems.length);
  });
  html += '</div>';

  // ── What to Study ──
  html += renderStudyRecommendations(index, assess);

  container.innerHTML = html;
}

function assessStatCard(label, value, icon, colorClass) {
  var cls = 'stat-card';
  if (colorClass) cls += ' assess-stat-' + colorClass;
  return '<div class="' + cls + '"><div class="stat-card-icon">' + icon + '</div><div class="stat-card-value">' + value + '</div><div class="stat-card-label">' + label + '</div></div>';
}

function assessDeckCard(icon, title, subtitle, href) {
  return '<a class="deck-card" href="' + href + '">'
    + '<div class="deck-icon assess-deck-icon">' + icon + '</div>'
    + '<div class="deck-title">' + escHtml(title) + '</div>'
    + '<div class="deck-subtitle">' + subtitle + '</div>'
    + '</a>';
}

function countAssessment(items, assess) {
  var know = 0, shaky = 0, study = 0;
  items.forEach(function(item) {
    var a = assess[item.qKey];
    if (!a) return;
    if (a.level === 'know') know++;
    else if (a.level === 'shaky') shaky++;
    else study++;
  });
  return { know: know, shaky: shaky, study: study };
}

function renderAssessChartRow(label, counts, total) {
  var rated = counts.know + counts.shaky + counts.study;
  var h = '<div class="chart-row">';
  h += '<div class="chart-label">' + label + '</div>';
  h += '<div class="stacked-bar-wrap">';
  if (rated === 0) {
    h += '<div class="stacked-bar"><div class="bar-empty" style="width:100%"></div></div>';
  } else {
    h += '<div class="stacked-bar">';
    if (counts.know > 0) h += '<div class="bar-know" style="width:' + (counts.know / rated * 100) + '%">' + (counts.know / rated >= 0.1 ? counts.know : '') + '</div>';
    if (counts.shaky > 0) h += '<div class="bar-shaky" style="width:' + (counts.shaky / rated * 100) + '%">' + (counts.shaky / rated >= 0.1 ? counts.shaky : '') + '</div>';
    if (counts.study > 0) h += '<div class="bar-study" style="width:' + (counts.study / rated * 100) + '%">' + (counts.study / rated >= 0.1 ? counts.study : '') + '</div>';
    h += '</div>';
  }
  h += '<div class="chart-rated-text">' + rated + ' / ' + total + ' assessed</div>';
  h += '</div></div>';
  return h;
}

function renderStudyRecommendations(index, assess) {
  var topicStats = {};
  index.forEach(function(item) {
    var a = assess[item.qKey];
    if (!a || a.level === 'know') return;
    var tid = item.topic.id;
    if (!topicStats[tid]) topicStats[tid] = { title: item.topic.title, icon: item.topic.icon, id: tid, study: 0, shaky: 0 };
    if (a.level === 'study') topicStats[tid].study++;
    else if (a.level === 'shaky') topicStats[tid].shaky++;
  });

  var sorted = Object.values(topicStats).sort(function(a, b) { return (b.study + b.shaky) - (a.study + a.shaky); });

  if (sorted.length === 0) {
    return '<h2 class="deck-group-title" style="margin-top:1.5rem;">What to Study</h2>'
      + '<div class="empty-state" style="padding:2rem;"><p>No weak areas detected yet. Start a self-assessment to build your knowledge map!</p></div>';
  }

  var h = '<h2 class="deck-group-title" style="margin-top:1.5rem;">What to Study</h2>';
  h += '<div class="weak-list">';
  sorted.forEach(function(item) {
    h += '<div class="weak-item">';
    h += '<span class="weak-icon">' + escHtml(item.icon) + '</span>';
    h += '<span class="weak-title">' + escHtml(item.title) + '</span>';
    if (item.study > 0) h += '<span class="assess-need-count">' + item.study + ' need study</span>';
    if (item.shaky > 0) h += '<span class="assess-shaky-count">' + item.shaky + ' shaky</span>';
    h += '<a href="/verbal/practice/topic/' + item.id + '" class="study-weak-btn">Practice</a>';
    h += '</div>';
  });
  h += '</div>';
  return h;
}

// ══════════════════════════════════════════════════
// ── Assessment Test Engine ────────────────────────
// ══════════════════════════════════════════════════
var assessState = { deck: [], current: 0, results: [] };

function initAssessmentTest() {
  var container = document.getElementById('assessment-container');
  if (!container || !window.ALL_TOPICS) return;

  var params = new URLSearchParams(window.location.search);
  var deckType = params.get('deck');
  if (!deckType) return;

  var deck = buildAssessmentDeck(deckType, params.get('id'));
  if (deck.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-icon">&#9733;</div><h2>No questions in this deck</h2><p>Try picking another deck.</p><a href="/verbal/practice/assessment" class="summary-btn">Back to What I Know</a></div>';
    return;
  }

  assessState.deck = deck;
  assessState.current = 0;
  assessState.results = [];
  renderAssessmentCard(container);
}

function buildAssessmentDeck(type, id) {
  var index = buildQuestionIndex();
  var assess = getAssessment();

  function prioritiseUnassessed(pool, limit) {
    var unseen = pool.filter(function(item) { return !assess[item.qKey]; });
    var seen   = pool.filter(function(item) { return !!assess[item.qKey]; });
    var deck   = shuffle(unseen);
    if (deck.length < limit) {
      deck = deck.concat(shuffle(seen).slice(0, limit - deck.length));
    }
    return deck.slice(0, limit);
  }

  if (type === 'category') {
    return prioritiseUnassessed(index.filter(function(item) { return item.topic.category === id; }), 50);
  }
  if (type === 'topic') {
    return prioritiseUnassessed(index.filter(function(item) { return item.topic.id === id; }), 50);
  }
  if (type === 'unassessed') {
    return shuffle(index.filter(function(item) { return !assess[item.qKey]; })).slice(0, 50);
  }
  if (type === 'reassess') {
    return shuffle(index.filter(function(item) {
      var a = assess[item.qKey];
      return a && (a.level === 'shaky' || a.level === 'study');
    })).slice(0, 50);
  }
  if (type === 'random') {
    return prioritiseUnassessed(index, 50);
  }
  if (type === 'full') {
    return prioritiseUnassessed(index, index.length);
  }
  return [];
}

function renderAssessmentCard(container) {
  if (!container) container = document.getElementById('assessment-container');
  var item = assessState.deck[assessState.current];
  var total = assessState.deck.length;
  var num = assessState.current + 1;
  var pct = Math.round((num / total) * 100);

  var h = '<div class="study-progress">';
  h += '<div class="study-progress-bar"><div class="assess-progress-fill" style="width:' + pct + '%"></div></div>';
  h += '<div class="study-progress-text">' + num + ' / ' + total + '</div>';
  h += '</div>';

  h += '<div class="flashcard-wrapper">';
  h += '<div class="flashcard-topic-label">' + escHtml(item.topic.title) + ' &bull; Q' + item.q.id + '</div>';

  // Show passage if present
  if (item.section && item.section.passage) {
    h += '<div class="passage-box"><div class="passage-label">Passage</div>' + escHtml(item.section.passage) + '</div>';
  }

  // Show question
  if (item.q.stem) h += '<div class="q-stem">' + item.q.stem + '</div>';

  // Show choices
  if (item.q.blank_choices) {
    var numBlanks = item.q.blank_choices.length;
    h += '<div class="blank-choices-container cols-' + numBlanks + '">';
    item.q.blank_choices.forEach(function(group, gi) {
      h += '<div class="blank-group"><div class="blank-group-label">Blank (' + (gi === 0 ? 'i' : gi === 1 ? 'ii' : 'iii') + ')</div><ul>';
      group.forEach(function(c) { h += '<li>' + escHtml(c) + '</li>'; });
      h += '</ul></div>';
    });
    h += '</div>';
  } else if (item.q.choices) {
    h += '<ul class="choices">';
    item.q.choices.forEach(function(c) { h += '<li>' + escHtml(c) + '</li>'; });
    h += '</ul>';
  }

  h += '<div class="assess-btn-row">';
  h += '<button class="assess-btn assess-know" onclick="assessAndNext(\'know\')">I Know This</button>';
  h += '<button class="assess-btn assess-shaky" onclick="assessAndNext(\'shaky\')">Shaky</button>';
  h += '<button class="assess-btn assess-study" onclick="assessAndNext(\'study\')">Need to Study</button>';
  h += '</div>';
  h += '</div>';

  container.innerHTML = h;
}

function assessAndNext(level) {
  var item = assessState.deck[assessState.current];
  assessQuestion(item.qKey, level);
  assessState.results.push({ qKey: item.qKey, level: level });

  assessState.current++;
  if (assessState.current >= assessState.deck.length) {
    renderAssessmentSummary();
  } else {
    renderAssessmentCard();
  }
}

function renderAssessmentSummary() {
  var container = document.getElementById('assessment-container');
  if (!container) return;

  var know = 0, shaky = 0, study = 0;
  assessState.results.forEach(function(r) {
    if (r.level === 'know') know++;
    else if (r.level === 'shaky') shaky++;
    else study++;
  });
  var total = assessState.results.length;

  var h = '<div class="study-summary">';
  h += '<h2>Assessment Complete!</h2>';
  h += '<p class="summary-subtitle">' + total + ' questions assessed</p>';
  h += '<div class="summary-stats">';
  h += '<div class="summary-stat assess-summary-know"><div class="summary-stat-num">' + know + '</div><div class="summary-stat-label">I Know</div><div class="summary-stat-pct">' + (total ? Math.round(know / total * 100) : 0) + '%</div></div>';
  h += '<div class="summary-stat assess-summary-shaky"><div class="summary-stat-num">' + shaky + '</div><div class="summary-stat-label">Shaky</div><div class="summary-stat-pct">' + (total ? Math.round(shaky / total * 100) : 0) + '%</div></div>';
  h += '<div class="summary-stat assess-summary-study"><div class="summary-stat-num">' + study + '</div><div class="summary-stat-label">Need to Study</div><div class="summary-stat-pct">' + (total ? Math.round(study / total * 100) : 0) + '%</div></div>';
  h += '</div>';

  // Per-topic breakdown
  var topicStats = {};
  assessState.results.forEach(function(r) {
    if (r.level === 'know') return;
    var item = assessState.deck.filter(function(d) { return d.qKey === r.qKey; })[0];
    if (!item) return;
    var tid = item.topic.id;
    if (!topicStats[tid]) topicStats[tid] = { title: item.topic.title, icon: item.topic.icon, id: tid, study: 0, shaky: 0 };
    if (r.level === 'study') topicStats[tid].study++;
    else topicStats[tid].shaky++;
  });
  var sorted = Object.values(topicStats).sort(function(a, b) { return (b.study + b.shaky) - (a.study + a.shaky); });

  if (sorted.length > 0) {
    h += '<div class="assess-summary-recs"><h3>What to Study</h3><div class="weak-list">';
    sorted.forEach(function(item) {
      h += '<div class="weak-item">';
      h += '<span class="weak-icon">' + escHtml(item.icon) + '</span>';
      h += '<span class="weak-title">' + escHtml(item.title) + '</span>';
      if (item.study > 0) h += '<span class="assess-need-count">' + item.study + ' need study</span>';
      if (item.shaky > 0) h += '<span class="assess-shaky-count">' + item.shaky + ' shaky</span>';
      h += '<a href="/verbal/practice/topic/' + item.id + '" class="study-weak-btn">Practice</a>';
      h += '</div>';
    });
    h += '</div></div>';
  }

  h += '<div class="summary-actions">';
  h += '<a href="/verbal/practice/assessment" class="summary-btn">Back to What I Know</a>';
  h += '<a href="/verbal/practice/assessment" class="summary-btn summary-btn-assess">View Knowledge Map</a>';
  h += '</div>';
  h += '</div>';

  container.innerHTML = h;
}

// ══════════════════════════════════════════════════
// ── On Page Load ──────────────────────────────────
// ══════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', function() {
  // Restore favorite + learned states
  var favs = getFavs();
  document.querySelectorAll('.fav-btn').forEach(function(btn) {
    if (favs.includes(btn.dataset.qkey)) btn.classList.add('fav-active');
  });
  var learned = getLearned();
  document.querySelectorAll('.learned-btn').forEach(function(btn) {
    if (learned.includes(btn.dataset.qkey)) btn.classList.add('learned-active');
  });

  // Homepage: update fav count + learned progress
  var homeFavCount = document.getElementById('home-fav-count');
  if (homeFavCount) homeFavCount.textContent = favs.length + ' saved';

  document.querySelectorAll('.topic-card[data-topic-id]').forEach(function(card) {
    var topicId = card.dataset.topicId;
    var total = parseInt(card.dataset.total) || 0;
    var count = learned.filter(function(key) { return key.startsWith(topicId + '_'); }).length;
    var el = card.querySelector('.topic-progress');
    if (el && total > 0) {
      var pct = Math.round(count / total * 100);
      el.innerHTML = '<div class="progress-bar"><div class="progress-fill" style="width:' + pct + '%"></div></div>'
        + '<span class="progress-text">' + count + '/' + total + ' learned</span>';
    }
  });

  // Scroll active sidebar link into view
  var activeLink = document.querySelector('.sidebar-link.active');
  if (activeLink) activeLink.scrollIntoView({ block: 'center', behavior: 'instant' });

  // Init features
  initAssessmentHub();
  initAssessmentTest();
});
