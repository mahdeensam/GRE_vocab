/* ── GRE Quant – Interactivity ──────────────── */

// ── Favorites (localStorage) ───────────────────
function getFavs() {
  try { return JSON.parse(localStorage.getItem('gre_favorites') || '[]'); }
  catch { return []; }
}
function saveFavs(favs) {
  localStorage.setItem('gre_favorites', JSON.stringify(favs));
}
function isFav(qKey) {
  return getFavs().includes(qKey);
}
function toggleFav(qKey) {
  var favs = getFavs();
  var idx = favs.indexOf(qKey);
  if (idx === -1) { favs.push(qKey); } else { favs.splice(idx, 1); }
  saveFavs(favs);
  var btn = document.querySelector('.fav-btn[data-qkey="' + qKey + '"]');
  if (btn) btn.classList.toggle('fav-active', favs.includes(qKey));
}

// ── Learned (localStorage) ────────────────────
function getLearned() {
  try { return JSON.parse(localStorage.getItem('gre_learned') || '[]'); }
  catch { return []; }
}
function saveLearned(list) {
  localStorage.setItem('gre_learned', JSON.stringify(list));
}
function toggleLearned(qKey) {
  var list = getLearned();
  var idx = list.indexOf(qKey);
  if (idx === -1) { list.push(qKey); } else { list.splice(idx, 1); }
  saveLearned(list);
  var btn = document.querySelector('.learned-btn[data-qkey="' + qKey + '"]');
  if (btn) btn.classList.toggle('learned-active', list.includes(qKey));
}

// ── Ratings (localStorage) ────────────────────
function getRatings() {
  try { return JSON.parse(localStorage.getItem('gre_ratings') || '{}'); }
  catch { return {}; }
}
function saveRatings(ratings) {
  localStorage.setItem('gre_ratings', JSON.stringify(ratings));
}
function rateQuestion(qKey, rating) {
  var ratings = getRatings();
  var existing = ratings[qKey] || { count: 0 };
  ratings[qKey] = {
    rating: rating,
    date: new Date().toISOString().slice(0, 10),
    count: existing.count + 1
  };
  saveRatings(ratings);
}

// ── Utilities ─────────────────────────────────
function getQuestionType(q, sectionType) {
  if (q.qtyA !== undefined) return 'qc';
  if (q.choices) {
    if (sectionType && /select one or more|select all/i.test(sectionType)) return 'mc-multi';
    return 'mc-single';
  }
  return 'numeric';
}

function buildQuestionIndex() {
  if (!window.ALL_TOPICS) return [];
  var index = [];
  ALL_TOPICS.forEach(function(topic) {
    topic.sections.forEach(function(section, si) {
      section.questions.forEach(function(q) {
        var qKey = topic.id + '_' + si + '_' + q.id;
        index.push({
          q: q,
          section: section,
          topic: topic,
          si: si,
          qKey: qKey,
          qType: getQuestionType(q, section.type)
        });
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

// ── MathJax Helper ─────────────────────────────
function typesetMath(elements) {
  // MathJax already fully loaded
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise(elements).catch(function() {});
    return;
  }
  // MathJax config exists but library still loading — poll until ready
  var attempts = 0;
  var poll = setInterval(function() {
    attempts++;
    if (window.MathJax && MathJax.typesetPromise) {
      clearInterval(poll);
      MathJax.typesetPromise(elements).catch(function() {});
    } else if (attempts > 50) {
      clearInterval(poll); // give up after ~5s
    }
  }, 100);
}

// ── Answer Reveal ──────────────────────────────
function toggleAnswer(qKey) {
  var box = document.getElementById('ans-' + qKey);
  if (!box) return;
  var isHidden = box.classList.toggle('answer-visible');
  // Update button text
  var btn = box.previousElementSibling;
  if (btn && btn.classList.contains('reveal-btn')) {
    btn.textContent = isHidden ? 'Hide Answer' : 'Show Answer';
  }
  // Re-typeset MathJax if present
  if (isHidden) typesetMath([box]);
}

// ── Sidebar: Toggle Category Group ─────────────
function toggleSidebarGroup(btn) {
  var group = btn.closest('.sidebar-group');
  if (group) group.classList.toggle('open');
}

// ── Mobile Menu Toggle ─────────────────────────
function toggleMobileMenu() {
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('sidebar-overlay');
  if (sidebar) sidebar.classList.toggle('mobile-open');
  if (overlay) overlay.classList.toggle('mobile-open');
}

// ── Type Filter Tabs (Topic Pages) ─────────────
function initTypeFilters() {
  var header = document.querySelector('.topic-header');
  var sections = document.querySelectorAll('.question-section');
  if (!header || sections.length === 0) return;

  // Detect types present in sections
  var typeCounts = { all: 0, qc: 0, 'mc-single': 0, 'mc-multi': 0, numeric: 0 };
  sections.forEach(function(sec) {
    var titleEl = sec.querySelector('.section-title');
    if (!titleEl) return;
    var sType = titleEl.textContent.trim();
    var qType = detectSectionType(sType);
    sec.setAttribute('data-qtype', qType);
    var count = sec.querySelectorAll('.question-card').length;
    typeCounts[qType] += count;
    typeCounts.all += count;
  });

  // Build tab bar
  var tabs = [
    { key: 'all', label: 'All', count: typeCounts.all },
    { key: 'qc', label: 'QC', count: typeCounts.qc },
    { key: 'mc-single', label: 'MC Single', count: typeCounts['mc-single'] },
    { key: 'mc-multi', label: 'MC Multi', count: typeCounts['mc-multi'] },
    { key: 'numeric', label: 'Numeric Entry', count: typeCounts.numeric }
  ];

  var tabBar = document.createElement('div');
  tabBar.className = 'type-filter-tabs';

  tabs.forEach(function(t) {
    if (t.key !== 'all' && t.count === 0) return;
    var btn = document.createElement('button');
    btn.className = 'type-tab' + (t.key === 'all' ? ' active' : '');
    btn.setAttribute('data-filter', t.key);
    btn.innerHTML = t.label + ' <span class="type-tab-count">' + t.count + '</span>';
    btn.onclick = function() { filterByType(t.key, tabBar); };
    tabBar.appendChild(btn);
  });

  header.after(tabBar);
}

function detectSectionType(sectionTitle) {
  var s = sectionTitle.toLowerCase();
  if (s.indexOf('quantitative comparison') !== -1) return 'qc';
  if (s.indexOf('select one or more') !== -1 || s.indexOf('select all') !== -1) return 'mc-multi';
  if (s.indexOf('multiple choice') !== -1 || s.indexOf('single answer') !== -1) return 'mc-single';
  if (s.indexOf('numeric') !== -1) return 'numeric';
  return 'mc-single';
}

function filterByType(type, tabBar) {
  tabBar.querySelectorAll('.type-tab').forEach(function(t) {
    t.classList.toggle('active', t.getAttribute('data-filter') === type);
  });
  document.querySelectorAll('.question-section').forEach(function(sec) {
    if (type === 'all') {
      sec.style.display = '';
    } else {
      sec.style.display = sec.getAttribute('data-qtype') === type ? '' : 'none';
    }
  });
}

// ── Flashcard Hub ──────────────────────────────
function initFlashcardHub() {
  var container = document.getElementById('flashcard-hub');
  if (!container || !window.ALL_TOPICS || !window.ALL_CATEGORIES) return;

  var index = buildQuestionIndex();
  var ratings = getRatings();
  var html = '';

  // ── By Category ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Category</h2><div class="deck-grid">';
  ALL_CATEGORIES.forEach(function(cat) {
    var count = index.filter(function(item) { return item.topic.category === cat.id; }).length;
    html += deckCard(cat.icon, cat.name, Math.min(count, 50) + ' questions', '/quant/flashcards/study?deck=category&id=' + cat.id);
  });
  html += '</div></div>';

  // ── By Question Type ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Question Type</h2><div class="deck-grid">';
  var typeDecks = [
    { key: 'qc', icon: 'AB', name: 'Quantitative Comparison' },
    { key: 'mc-single', icon: '1', name: 'MC — Single Answer' },
    { key: 'mc-multi', icon: '+', name: 'MC — Select All' },
    { key: 'numeric', icon: '#', name: 'Numeric Entry' }
  ];
  typeDecks.forEach(function(td) {
    var count = index.filter(function(item) { return item.qType === td.key; }).length;
    html += deckCard(td.icon, td.name, Math.min(count, 50) + ' questions', '/quant/flashcards/study?deck=type&id=' + td.key);
  });
  html += '</div></div>';

  // ── Smart Decks ──
  var reviewCount = Object.keys(ratings).filter(function(k) {
    return ratings[k].rating === 'again' || ratings[k].rating === 'hard';
  }).length;
  html += '<div class="deck-group"><h2 class="deck-group-title">Smart Decks</h2><div class="deck-grid">';
  html += deckCard('&#9881;', 'Smart Review', reviewCount + ' to review', '/quant/flashcards/study?deck=smart');
  html += deckCard('&#127922;', 'Random Mix', '50 questions', '/quant/flashcards/study?deck=random');
  html += '</div></div>';

  container.innerHTML = html;
}

function deckCard(icon, title, subtitle, href) {
  return '<a class="deck-card" href="' + href + '">'
    + '<div class="deck-icon">' + icon + '</div>'
    + '<div class="deck-title">' + escHtml(title) + '</div>'
    + '<div class="deck-subtitle">' + subtitle + '</div>'
    + '</a>';
}

// ── Study Engine ───────────────────────────────
var studyState = {
  deck: [],
  current: 0,
  results: [],
  timerStart: 0,
  timerId: null
};

function initStudy() {
  var container = document.getElementById('study-container');
  if (!container || !window.ALL_TOPICS) return;

  var params = new URLSearchParams(window.location.search);
  var deckType = params.get('deck');
  if (!deckType) return;

  var deck = buildDeck(deckType, params.get('id'));
  if (deck.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-icon">&#128218;</div><h2>No questions in this deck</h2><p>Try rating some questions first, or pick another deck.</p><a href="/quant/flashcards" class="summary-btn">Back to Decks</a></div>';
    return;
  }

  studyState.deck = deck;
  studyState.current = 0;
  studyState.results = [];
  renderCard(container);
}

function buildDeck(type, id) {
  var index = buildQuestionIndex();

  if (type === 'category') {
    var filtered = index.filter(function(item) { return item.topic.category === id; });
    return shuffle(filtered).slice(0, 50);
  }
  if (type === 'type') {
    var filtered = index.filter(function(item) { return item.qType === id; });
    return shuffle(filtered).slice(0, 50);
  }
  if (type === 'smart') {
    var ratings = getRatings();
    var filtered = index.filter(function(item) {
      var r = ratings[item.qKey];
      return r && (r.rating === 'again' || r.rating === 'hard');
    });
    return shuffle(filtered);
  }
  if (type === 'random') {
    return shuffle(index).slice(0, 50);
  }
  if (type === 'weak') {
    // Study weak areas: all questions from a specific topic
    var filtered = index.filter(function(item) { return item.topic.id === id; });
    return shuffle(filtered).slice(0, 50);
  }
  return [];
}

function renderCard(container) {
  if (!container) container = document.getElementById('study-container');
  var item = studyState.deck[studyState.current];
  var total = studyState.deck.length;
  var num = studyState.current + 1;

  var pct = Math.round((num / total) * 100);

  var h = '<div class="study-progress">';
  h += '<div class="study-progress-bar"><div class="study-progress-fill" style="width:' + pct + '%"></div></div>';
  h += '<div class="study-progress-text">' + num + ' / ' + total + '</div>';
  h += '<div class="study-timer" id="study-timer">0:00</div>';
  h += '</div>';

  h += '<div class="flashcard-wrapper">';
  h += '<div class="flashcard-topic-label">' + escHtml(item.topic.title) + ' &bull; Q' + item.q.id + '</div>';
  h += renderFlashcardContent(item);
  h += '<div id="flashcard-answer" class="flashcard-answer-reveal" style="display:none;">';
  if (item.q.answer) {
    h += '<div class="answer-text">Answer: ' + item.q.answer + '</div>';
    if (item.q.explanation) h += '<div class="explanation-text">' + item.q.explanation + '</div>';
    if (item.q.common_mistake) h += '<div class="mistake-box">&#9888; Common Mistake: ' + item.q.common_mistake + '</div>';
  } else {
    h += '<div class="answer-text" style="color:var(--muted);">No answer available for this question.</div>';
  }
  h += '<div class="rate-buttons">';
  h += '<button class="rate-btn rate-easy" onclick="rateAndNext(\'easy\')">Easy</button>';
  h += '<button class="rate-btn rate-hard" onclick="rateAndNext(\'hard\')">Hard</button>';
  h += '<button class="rate-btn rate-again" onclick="rateAndNext(\'again\')">Again</button>';
  h += '</div>';
  h += '</div>';
  h += '<button class="study-flip-btn" id="flip-btn" onclick="revealAnswer()">Show Answer</button>';
  h += '</div>';

  container.innerHTML = h;

  // Start timer
  studyState.timerStart = Date.now();
  if (studyState.timerId) clearInterval(studyState.timerId);
  studyState.timerId = setInterval(updateTimer, 1000);

  // Typeset MathJax
  typesetMath([container]);
}

function renderFlashcardContent(item) {
  var q = item.q;
  var h = '<div class="flashcard-question">';

  // Show section instructions (contains charts/graphs for DI questions)
  if (item.section && item.section.instructions) {
    h += '<div class="section-instructions flashcard-instructions">' + item.section.instructions + '</div>';
  }

  if (q.stem) h += '<div class="q-stem">' + q.stem + '</div>';

  if (q.qtyA !== undefined) {
    h += '<table class="qc-table"><thead><tr><th>Quantity A</th><th>Quantity B</th></tr></thead>';
    h += '<tbody><tr><td>' + q.qtyA + '</td><td>' + q.qtyB + '</td></tr></tbody></table>';
  }

  if (q.choices) {
    h += '<ul class="choices">';
    q.choices.forEach(function(c) { h += '<li>' + c + '</li>'; });
    h += '</ul>';
  }

  if (!q.qtyA && !q.choices) {
    h += '<div class="numeric-entry"><label>Your answer: <input type="text" class="entry-box" placeholder="___"></label></div>';
  }

  h += '</div>';
  return h;
}

function revealAnswer() {
  var answerEl = document.getElementById('flashcard-answer');
  var flipBtn = document.getElementById('flip-btn');
  if (answerEl) answerEl.style.display = 'block';
  if (flipBtn) flipBtn.style.display = 'none';

  // Typeset MathJax in answer
  if (answerEl) typesetMath([answerEl]);
}

function rateAndNext(rating) {
  var item = studyState.deck[studyState.current];
  rateQuestion(item.qKey, rating);
  studyState.results.push({ qKey: item.qKey, rating: rating });

  studyState.current++;
  if (studyState.current >= studyState.deck.length) {
    if (studyState.timerId) clearInterval(studyState.timerId);
    renderSummary();
  } else {
    renderCard();
  }
}

function renderSummary() {
  var container = document.getElementById('study-container');
  if (!container) return;

  var easy = 0, hard = 0, again = 0;
  studyState.results.forEach(function(r) {
    if (r.rating === 'easy') easy++;
    else if (r.rating === 'hard') hard++;
    else again++;
  });
  var total = studyState.results.length;

  var h = '<div class="study-summary">';
  h += '<h2>Session Complete!</h2>';
  h += '<p class="summary-subtitle">' + total + ' questions reviewed</p>';
  h += '<div class="summary-stats">';
  h += '<div class="summary-stat summary-stat-easy"><div class="summary-stat-num">' + easy + '</div><div class="summary-stat-label">Easy</div><div class="summary-stat-pct">' + (total ? Math.round(easy / total * 100) : 0) + '%</div></div>';
  h += '<div class="summary-stat summary-stat-hard"><div class="summary-stat-num">' + hard + '</div><div class="summary-stat-label">Hard</div><div class="summary-stat-pct">' + (total ? Math.round(hard / total * 100) : 0) + '%</div></div>';
  h += '<div class="summary-stat summary-stat-again"><div class="summary-stat-num">' + again + '</div><div class="summary-stat-label">Again</div><div class="summary-stat-pct">' + (total ? Math.round(again / total * 100) : 0) + '%</div></div>';
  h += '</div>';
  h += '<div class="summary-actions">';
  h += '<a href="/quant/flashcards" class="summary-btn">Back to Decks</a>';
  h += '<a href="/quant/dashboard" class="summary-btn summary-btn-accent">View Dashboard</a>';
  h += '</div>';
  h += '</div>';

  container.innerHTML = h;
}

function updateTimer() {
  var el = document.getElementById('study-timer');
  if (!el) return;
  var elapsed = Math.floor((Date.now() - studyState.timerStart) / 1000);
  var min = Math.floor(elapsed / 60);
  var sec = elapsed % 60;
  el.textContent = min + ':' + (sec < 10 ? '0' : '') + sec;
}

// ── Dashboard ──────────────────────────────────
function initDashboard() {
  var container = document.getElementById('dashboard-container');
  if (!container || !window.ALL_TOPICS || !window.ALL_CATEGORIES) return;

  var index = buildQuestionIndex();
  var ratings = getRatings();
  var favs = getFavs();
  var learned = getLearned();

  var html = '';

  // ── Overview Stats ──
  var ratedCount = Object.keys(ratings).length;
  html += '<div class="stat-grid">';
  html += statCard('Total Questions', index.length, '&#128218;');
  html += statCard('Learned', learned.length, '&#10003;');
  html += statCard('Favorited', favs.length, '&#9829;');
  html += statCard('Rated', ratedCount, '&#9733;');
  html += '</div>';

  // ── Performance by Category ──
  html += '<h2 class="dashboard-section-title">Performance by Category</h2>';
  html += '<div class="chart-container">';
  ALL_CATEGORIES.forEach(function(cat) {
    var catItems = index.filter(function(item) { return item.topic.category === cat.id; });
    var counts = countRatings(catItems, ratings);
    html += renderChartRow(cat.name, counts, catItems.length);
  });
  html += '</div>';

  // ── Performance by Question Type ──
  html += '<h2 class="dashboard-section-title">Performance by Question Type</h2>';
  html += '<div class="chart-container">';
  var types = [
    { key: 'qc', name: 'Quantitative Comparison' },
    { key: 'mc-single', name: 'MC — Single Answer' },
    { key: 'mc-multi', name: 'MC — Select All' },
    { key: 'numeric', name: 'Numeric Entry' }
  ];
  types.forEach(function(t) {
    var typeItems = index.filter(function(item) { return item.qType === t.key; });
    var counts = countRatings(typeItems, ratings);
    html += renderChartRow(t.name, counts, typeItems.length);
  });
  html += '</div>';

  // ── Weakest Areas ──
  html += '<h2 class="dashboard-section-title">Weakest Areas</h2>';
  html += renderWeakestAreas(index, ratings);

  container.innerHTML = html;
}

function statCard(label, value, icon) {
  return '<div class="stat-card"><div class="stat-card-icon">' + icon + '</div><div class="stat-card-value">' + value + '</div><div class="stat-card-label">' + label + '</div></div>';
}

function countRatings(items, ratings) {
  var easy = 0, hard = 0, again = 0;
  items.forEach(function(item) {
    var r = ratings[item.qKey];
    if (!r) return;
    if (r.rating === 'easy') easy++;
    else if (r.rating === 'hard') hard++;
    else again++;
  });
  return { easy: easy, hard: hard, again: again };
}

function renderChartRow(label, counts, total) {
  var rated = counts.easy + counts.hard + counts.again;
  var h = '<div class="chart-row">';
  h += '<div class="chart-label">' + label + '</div>';
  h += '<div class="stacked-bar-wrap">';
  if (rated === 0) {
    h += '<div class="stacked-bar"><div class="bar-empty" style="width:100%"></div></div>';
  } else {
    h += '<div class="stacked-bar">';
    if (counts.easy > 0) h += '<div class="bar-easy" style="width:' + (counts.easy / rated * 100) + '%" title="Easy: ' + counts.easy + '">' + (counts.easy / rated >= 0.1 ? counts.easy : '') + '</div>';
    if (counts.hard > 0) h += '<div class="bar-hard" style="width:' + (counts.hard / rated * 100) + '%" title="Hard: ' + counts.hard + '">' + (counts.hard / rated >= 0.1 ? counts.hard : '') + '</div>';
    if (counts.again > 0) h += '<div class="bar-again" style="width:' + (counts.again / rated * 100) + '%" title="Again: ' + counts.again + '">' + (counts.again / rated >= 0.1 ? counts.again : '') + '</div>';
    h += '</div>';
  }
  h += '<div class="chart-rated-text">' + rated + ' / ' + total + ' rated</div>';
  h += '</div></div>';
  return h;
}

function renderWeakestAreas(index, ratings) {
  // Group by topic, count "again" ratings
  var topicAgain = {};
  index.forEach(function(item) {
    var r = ratings[item.qKey];
    if (!r || r.rating !== 'again') return;
    var tid = item.topic.id;
    if (!topicAgain[tid]) topicAgain[tid] = { title: item.topic.title, icon: item.topic.icon, id: tid, count: 0 };
    topicAgain[tid].count++;
  });

  var sorted = Object.values(topicAgain).sort(function(a, b) { return b.count - a.count; });

  if (sorted.length === 0) {
    return '<div class="empty-state" style="padding:2rem;"><p>No weak areas detected yet. Start studying with flashcards to see your weak spots!</p></div>';
  }

  var h = '<div class="weak-list">';
  sorted.forEach(function(item) {
    h += '<div class="weak-item">';
    h += '<span class="weak-icon">' + escHtml(item.icon) + '</span>';
    h += '<span class="weak-title">' + escHtml(item.title) + '</span>';
    h += '<span class="weak-count">' + item.count + ' "Again"</span>';
    h += '<a href="/quant/flashcards/study?deck=weak&id=' + item.id + '" class="study-weak-btn">Study</a>';
    h += '</div>';
  });
  h += '</div>';
  return h;
}

// ══════════════════════════════════════════════════
// ── Self-Assessment ("What I Know") ──────────────
// ══════════════════════════════════════════════════

// ── Assessment Storage ──────────────────────────
function getAssessment() {
  try { return JSON.parse(localStorage.getItem('gre_self_assessment') || '{}'); }
  catch { return {}; }
}
function saveAssessment(data) {
  localStorage.setItem('gre_self_assessment', JSON.stringify(data));
}
function assessQuestion(qKey, level) {
  var data = getAssessment();
  data[qKey] = { level: level, date: new Date().toISOString().slice(0, 10) };
  saveAssessment(data);
}

// ── Assessment Hub ──────────────────────────────
function initAssessmentHub() {
  var container = document.getElementById('assessment-hub');
  if (!container || !window.ALL_TOPICS || !window.ALL_CATEGORIES) return;

  var index = buildQuestionIndex();
  var assess = getAssessment();
  var total = index.length;

  // Count overall stats
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

  // ── Overview Stats (5-col grid) ──
  html += '<div class="assess-stat-grid">';
  html += assessStatCard('Total', total, '&#128218;', '');
  html += assessStatCard('Assessed', assessed, '&#9733;', '');
  html += assessStatCard('I Know', know, '&#10003;', 'know');
  html += assessStatCard('Shaky', shaky, '&#8776;', 'shaky');
  html += assessStatCard('Need to Study', study, '&#10007;', 'study');
  html += '</div>';

  // ── Deck Selection: By Category ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Category</h2><div class="deck-grid">';
  ALL_CATEGORIES.forEach(function(cat) {
    var count = index.filter(function(item) { return item.topic.category === cat.id; }).length;
    html += assessDeckCard(cat.icon, cat.name, Math.min(count, 50) + ' questions', '/quant/assessment/test?deck=category&id=' + cat.id);
  });
  html += '</div></div>';

  // ── Deck Selection: By Question Type ──
  html += '<div class="deck-group"><h2 class="deck-group-title">By Question Type</h2><div class="deck-grid">';
  var typeDecks = [
    { key: 'qc', icon: 'AB', name: 'Quantitative Comparison' },
    { key: 'mc-single', icon: '1', name: 'MC — Single Answer' },
    { key: 'mc-multi', icon: '+', name: 'MC — Select All' },
    { key: 'numeric', icon: '#', name: 'Numeric Entry' }
  ];
  typeDecks.forEach(function(td) {
    var count = index.filter(function(item) { return item.qType === td.key; }).length;
    html += assessDeckCard(td.icon, td.name, Math.min(count, 50) + ' questions', '/quant/assessment/test?deck=type&id=' + td.key);
  });
  html += '</div></div>';

  // ── Smart Decks ──
  var unassessedCount = index.filter(function(item) { return !assess[item.qKey]; }).length;
  var weakCount = index.filter(function(item) {
    var a = assess[item.qKey];
    return a && (a.level === 'shaky' || a.level === 'study');
  }).length;
  html += '<div class="deck-group"><h2 class="deck-group-title">Smart Decks</h2><div class="deck-grid">';
  html += assessDeckCard('&#10067;', 'Unassessed Only', unassessedCount + ' remaining', '/quant/assessment/test?deck=unassessed');
  html += assessDeckCard('&#128260;', 'Reassess Weak', weakCount + ' to reassess', '/quant/assessment/test?deck=reassess');
  html += assessDeckCard('&#127922;', 'Random Mix', '50 questions', '/quant/assessment/test?deck=random');
  html += assessDeckCard('&#128221;', 'Full Assessment', total + ' questions', '/quant/assessment/test?deck=full');
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
  html += '<h3 class="assess-chart-subtitle" style="margin-top:1.25rem;">By Question Type</h3>';
  var types = [
    { key: 'qc', name: 'Quantitative Comparison' },
    { key: 'mc-single', name: 'MC — Single Answer' },
    { key: 'mc-multi', name: 'MC — Select All' },
    { key: 'numeric', name: 'Numeric Entry' }
  ];
  types.forEach(function(t) {
    var typeItems = index.filter(function(item) { return item.qType === t.key; });
    var counts = countAssessment(typeItems, assess);
    html += renderAssessChartRow(t.name, counts, typeItems.length);
  });
  html += '</div>';

  // ── What to Study Recommendations ──
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
    if (counts.know > 0) h += '<div class="bar-know" style="width:' + (counts.know / rated * 100) + '%" title="I Know: ' + counts.know + '">' + (counts.know / rated >= 0.1 ? counts.know : '') + '</div>';
    if (counts.shaky > 0) h += '<div class="bar-shaky" style="width:' + (counts.shaky / rated * 100) + '%" title="Shaky: ' + counts.shaky + '">' + (counts.shaky / rated >= 0.1 ? counts.shaky : '') + '</div>';
    if (counts.study > 0) h += '<div class="bar-study" style="width:' + (counts.study / rated * 100) + '%" title="Need to Study: ' + counts.study + '">' + (counts.study / rated >= 0.1 ? counts.study : '') + '</div>';
    h += '</div>';
  }
  h += '<div class="chart-rated-text">' + rated + ' / ' + total + ' assessed</div>';
  h += '</div></div>';
  return h;
}

function renderStudyRecommendations(index, assess) {
  // Group by topic, count shaky + study
  var topicStats = {};
  index.forEach(function(item) {
    var a = assess[item.qKey];
    if (!a || a.level === 'know') return;
    var tid = item.topic.id;
    if (!topicStats[tid]) topicStats[tid] = { title: item.topic.title, icon: item.topic.icon, id: tid, study: 0, shaky: 0 };
    if (a.level === 'study') topicStats[tid].study++;
    else if (a.level === 'shaky') topicStats[tid].shaky++;
  });

  var sorted = Object.values(topicStats).sort(function(a, b) {
    return (b.study + b.shaky) - (a.study + a.shaky);
  });

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
    h += '<a href="/quant/flashcards/study?deck=weak&id=' + item.id + '" class="study-weak-btn">Study Now</a>';
    h += '</div>';
  });
  h += '</div>';
  return h;
}

// ── Assessment Test Engine ──────────────────────
var assessState = {
  deck: [],
  current: 0,
  results: []
};

function initAssessmentTest() {
  var container = document.getElementById('assessment-container');
  if (!container || !window.ALL_TOPICS) return;

  var params = new URLSearchParams(window.location.search);
  var deckType = params.get('deck');
  if (!deckType) return;

  var deck = buildAssessmentDeck(deckType, params.get('id'));
  if (deck.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-icon">&#9733;</div><h2>No questions in this deck</h2><p>Try picking another deck or assess some questions first.</p><a href="/quant/assessment" class="summary-btn">Back to What I Know</a></div>';
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

  // Helper: prioritise unassessed questions, then fill with assessed (no repeats)
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
    var filtered = index.filter(function(item) { return item.topic.category === id; });
    return prioritiseUnassessed(filtered, 50);
  }
  if (type === 'type') {
    var filtered = index.filter(function(item) { return item.qType === id; });
    return prioritiseUnassessed(filtered, 50);
  }
  if (type === 'unassessed') {
    var filtered = index.filter(function(item) { return !assess[item.qKey]; });
    return shuffle(filtered).slice(0, 50);
  }
  if (type === 'reassess') {
    var filtered = index.filter(function(item) {
      var a = assess[item.qKey];
      return a && (a.level === 'shaky' || a.level === 'study');
    });
    return shuffle(filtered).slice(0, 50);
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
  h += renderFlashcardContent(item);

  // No answer section — only confidence buttons
  h += '<div class="assess-btn-row">';
  h += '<button class="assess-btn assess-know" onclick="assessAndNext(\'know\')">I Know This</button>';
  h += '<button class="assess-btn assess-shaky" onclick="assessAndNext(\'shaky\')">Shaky</button>';
  h += '<button class="assess-btn assess-study" onclick="assessAndNext(\'study\')">Need to Study</button>';
  h += '</div>';
  h += '</div>';

  container.innerHTML = h;
  typesetMath([container]);
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

  // Per-topic breakdown for "What to Study"
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
    h += '<div class="assess-summary-recs">';
    h += '<h3>What to Study</h3>';
    h += '<div class="weak-list">';
    sorted.forEach(function(item) {
      h += '<div class="weak-item">';
      h += '<span class="weak-icon">' + escHtml(item.icon) + '</span>';
      h += '<span class="weak-title">' + escHtml(item.title) + '</span>';
      if (item.study > 0) h += '<span class="assess-need-count">' + item.study + ' need study</span>';
      if (item.shaky > 0) h += '<span class="assess-shaky-count">' + item.shaky + ' shaky</span>';
      h += '<a href="/quant/flashcards/study?deck=weak&id=' + item.id + '" class="study-weak-btn">Study Now</a>';
      h += '</div>';
    });
    h += '</div></div>';
  }

  h += '<div class="summary-actions">';
  h += '<a href="/quant/assessment" class="summary-btn">Back to What I Know</a>';
  h += '<a href="/quant/assessment" class="summary-btn summary-btn-assess">View Knowledge Map</a>';
  h += '</div>';
  h += '</div>';

  container.innerHTML = h;
}

// ── On Page Load ───────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  // Restore favorite heart states
  var favs = getFavs();
  document.querySelectorAll('.fav-btn').forEach(function(btn) {
    if (favs.includes(btn.dataset.qkey)) {
      btn.classList.add('fav-active');
    }
  });

  // Restore learned states
  var learned = getLearned();
  document.querySelectorAll('.learned-btn').forEach(function(btn) {
    if (learned.includes(btn.dataset.qkey)) {
      btn.classList.add('learned-active');
    }
  });

  // ── Homepage: update fav count + learned progress ──
  var homeFavCount = document.getElementById('home-fav-count');
  if (homeFavCount) {
    homeFavCount.textContent = favs.length + ' saved';
  }

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

  // ── Sidebar: scroll active link into view ──────
  var activeLink = document.querySelector('.sidebar-link.active');
  if (activeLink) {
    activeLink.scrollIntoView({ block: 'center', behavior: 'instant' });
  }

  // ── Favorites Page Logic ───────────────────
  var favContainer = document.getElementById('favorites-container');
  if (favContainer && window.ALL_TOPICS) {
    renderFavorites();
  }

  // ── Init new features ─────────────────────
  initTypeFilters();
  initFlashcardHub();
  initStudy();
  initDashboard();
  initAssessmentHub();
  initAssessmentTest();
});

// ── Favorites Page Rendering ─────────────────
function renderFavorites() {
  var container = document.getElementById('favorites-container');
  if (!container || !window.ALL_TOPICS) return;

  var favs = getFavs();
  if (favs.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-icon">&#9825;</div><h2>No favorites yet</h2><p>Click the heart icon on any question to add it here.</p></div>';
    updateFavCount(0);
    return;
  }

  var html = '';
  var totalFound = 0;

  ALL_TOPICS.forEach(function(topic) {
    var topicQuestions = [];
    topic.sections.forEach(function(section, si) {
      section.questions.forEach(function(q) {
        var qKey = topic.id + '_' + si + '_' + q.id;
        if (favs.includes(qKey)) {
          topicQuestions.push({ q: q, section: section, si: si, qKey: qKey });
        }
      });
    });

    if (topicQuestions.length === 0) return;
    totalFound += topicQuestions.length;

    html += '<div class="fav-topic-group">';
    html += '<h2 class="fav-topic-title"><span class="topic-badge">' + escHtml(topic.icon) + '</span> ' + escHtml(topic.title) + '</h2>';

    topicQuestions.forEach(function(item) {
      html += renderQuestionCard(item.q, item.section, item.qKey);
    });

    html += '</div>';
  });

  if (totalFound === 0) {
    container.innerHTML = '<div class="empty-state"><div class="empty-icon">&#9825;</div><h2>No favorites yet</h2><p>Click the heart icon on any question to add it here.</p></div>';
  } else {
    container.innerHTML = html;
  }
  updateFavCount(totalFound);

  // Typeset MathJax
  typesetMath([container]);

  // Re-apply fav + learned states
  var allFavs = getFavs();
  var allLearned = getLearned();
  container.querySelectorAll('.fav-btn').forEach(function(btn) {
    if (allFavs.includes(btn.dataset.qkey)) btn.classList.add('fav-active');
  });
  container.querySelectorAll('.learned-btn').forEach(function(btn) {
    if (allLearned.includes(btn.dataset.qkey)) btn.classList.add('learned-active');
  });
}

function updateFavCount(count) {
  var el = document.getElementById('fav-count');
  if (el) el.textContent = count + ' question' + (count !== 1 ? 's' : '');
}

function renderQuestionCard(q, _section, qKey) {
  var h = '<div class="question-card" id="q' + qKey + '">';
  // Fav button
  h += '<button class="fav-btn" data-qkey="' + qKey + '" onclick="toggleFav(\'' + qKey + '\')" title="Toggle favorite">&#9829;</button>';
  // Learned button
  h += '<button class="learned-btn" data-qkey="' + qKey + '" onclick="toggleLearned(\'' + qKey + '\')" title="Mark as learned">&#10003;</button>';
  h += '<div class="q-number">Q' + q.id + '</div>';
  h += '<div class="q-body">';

  // Stem
  if (q.stem) h += '<div class="q-stem">' + q.stem + '</div>';

  // QC table
  if (q.qtyA !== undefined) {
    h += '<table class="qc-table"><thead><tr><th>Quantity A</th><th>Quantity B</th></tr></thead>';
    h += '<tbody><tr><td>' + q.qtyA + '</td><td>' + q.qtyB + '</td></tr></tbody></table>';
  }

  // Choices
  if (q.choices) {
    h += '<ul class="choices">';
    q.choices.forEach(function(c) { h += '<li>' + c + '</li>'; });
    h += '</ul>';
  }

  // Numeric entry
  if (!q.qtyA && !q.choices) {
    h += '<div class="numeric-entry"><label>Your answer: <input type="text" class="entry-box" placeholder="___"></label></div>';
  }

  // Answer reveal
  if (q.answer) {
    h += '<button class="reveal-btn" onclick="toggleAnswer(\'' + qKey + '\')">Show Answer</button>';
    h += '<div class="answer-box" id="ans-' + qKey + '">';
    h += '<div class="answer-text">Answer: ' + q.answer + '</div>';
    if (q.explanation) h += '<div class="explanation-text">' + q.explanation + '</div>';
    if (q.common_mistake) h += '<div class="mistake-box">&#9888; Common Mistake: ' + q.common_mistake + '</div>';
    h += '</div>';
  }

  h += '</div></div>';
  return h;
}
