/* Obenan sales toolkit behaviour. Progressive enhancement: every section is complete without this file. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');
  var motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  function still() { return motion.matches; }
  function all(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }

  /* B. Observed and proposed: an ARIA tablist over two complete panels. */
  all('[data-section="compare"]').forEach(function (section) {
    var tabs = all('[role="tab"]', section);
    var states = section.querySelector('.tk-states');
    if (!tabs.length || !states) return;
    states.classList.add('is-tabbed');
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        panel.hidden = !on;
        if (on && !still()) { panel.classList.remove('tk-state-in'); void panel.offsetWidth; panel.classList.add('tk-state-in'); }
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab, false); });
      tab.addEventListener('keydown', function (e) {
        var next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
        if (next === undefined) return;
        e.preventDefault();
        select(tabs[(next + tabs.length) % tabs.length], true);
      });
    });
    select(tabs[0], false);
  });

  /* C. Review stream: clones are decorative (aria-hidden, never counted, never printed). */
  all('[data-section="reviews"] .tk-stream').forEach(function (stream) {
    var track = stream.querySelector('.tk-stream-track');
    var toggle = stream.parentNode.querySelector('[data-action="pause"]');
    var clones = [];
    function start() {
      if (clones.length) return;
      all('.tk-review', track).forEach(function (card) {
        var copy = card.cloneNode(true);
        copy.setAttribute('aria-hidden', 'true');
        copy.setAttribute('data-clone', '');
        track.appendChild(copy);
        clones.push(copy);
      });
      stream.classList.add('is-moving');
    }
    function stop() {
      clones.forEach(function (c) { c.remove(); });
      clones = [];
      stream.classList.remove('is-moving', 'is-paused');
    }
    function apply() { if (still()) stop(); else start(); sync(); }
    function sync() {
      if (!toggle) return;
      var paused = !stream.classList.contains('is-moving') || stream.classList.contains('is-paused');
      toggle.textContent = paused ? 'Play stream' : 'Pause stream';
      toggle.setAttribute('aria-pressed', String(paused));
      toggle.disabled = still();
    }
    if (toggle) toggle.addEventListener('click', function () {
      stream.classList.toggle('is-paused');
      sync();
    });
    motion.addEventListener('change', apply);
    apply();
  });

  /* D. Portfolio explorer: filter by unit type, sort by column. Unknown always sorts last. */
  all('[data-section="portfolio"]').forEach(function (section) {
    var table = section.querySelector('.tk-table');
    var body = table.tBodies[0];
    var rows = all('tr', body);
    var filters = all('.tk-filter', section);
    var status = section.querySelector('[data-role="shown"]');
    function show(type) {
      var n = 0;
      rows.forEach(function (r) {
        var on = type === 'all' || r.getAttribute('data-type') === type;
        r.hidden = !on;
        if (on) n++;
      });
      filters.forEach(function (f) { f.setAttribute('aria-pressed', String(f.getAttribute('data-type') === type)); });
      if (status) status.textContent = 'Showing ' + n + ' of ' + rows.length + ' rows.';
    }
    filters.forEach(function (f) { f.addEventListener('click', function () { show(f.getAttribute('data-type')); }); });
    all('th button', table).forEach(function (button, col) {
      button.addEventListener('click', function () {
        var th = button.parentNode;
        var dir = th.getAttribute('aria-sort') === 'ascending' ? 'descending' : 'ascending';
        all('th', table).forEach(function (h) { h.removeAttribute('aria-sort'); });
        th.setAttribute('aria-sort', dir);
        var sign = dir === 'ascending' ? 1 : -1;
        rows.sort(function (a, b) {
          var x = a.cells[col], y = b.cells[col];
          var ux = x.classList.contains('tk-unknown'), uy = y.classList.contains('tk-unknown');
          if (ux || uy) return ux === uy ? 0 : ux ? 1 : -1;
          var vx = x.getAttribute('data-value') || x.textContent.trim();
          var vy = y.getAttribute('data-value') || y.textContent.trim();
          return sign * vx.localeCompare(vy, undefined, { numeric: true });
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
    if (filters.length) show('all');
  });

  /* E. Assistant walkthrough: reveal prepared blocks in order. Leaving the section finishes it. */
  all('[data-section="assistant"]').forEach(function (section) {
    var chat = section.querySelector('.tk-chat');
    var msgs = all('.tk-msg', chat);
    var replay = section.querySelector('[data-action="replay"]');
    var timers = [];
    var state = 'idle';
    function clear() { timers.forEach(clearTimeout); timers = []; }
    function finish() {
      clear();
      msgs.forEach(function (m) { m.classList.remove('is-pending'); m.classList.add('is-shown'); });
      chat.classList.remove('is-playing');
      chat.setAttribute('aria-busy', 'false');
      state = 'done';
    }
    function play() {
      clear();
      if (still()) { finish(); return; }
      state = 'playing';
      chat.classList.add('is-playing');
      chat.setAttribute('aria-busy', 'true');
      msgs.forEach(function (m, i) {
        m.classList.remove('is-shown');
        if (i > 0) m.classList.add('is-pending');
      });
      msgs.slice(1).forEach(function (m, i) {
        timers.push(setTimeout(function () {
          m.classList.remove('is-pending');
          m.classList.add('is-shown');
          if (i === msgs.length - 2) finish();
        }, 1200 + i * 1100));
      });
    }
    if (replay) replay.addEventListener('click', play);
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && e.intersectionRatio >= 0.35 && state === 'idle') play();
        if (!e.isIntersecting && state === 'playing') finish();
      });
    }, { threshold: [0, 0.35] }).observe(chat);
    window.addEventListener('beforeprint', finish);
  });

  /* F. Business case: exact integer arithmetic on buyer inputs. Money in cents, rates in basis points. */
  function units(text, places) {
    var t = String(text).replace(/\s/g, '').replace(',', '.');
    var m = /^(\d+)(?:\.(\d+))?$/.exec(t);
    if (!m || (m[2] || '').length > places) return null;
    return BigInt(m[1] + (m[2] || '').padEnd(places, '0'));
  }
  function ceilDiv(a, b) { return (a + b - 1n) / b; }
  all('[data-section="business-case"] form').forEach(function (form) {
    var out = form.querySelector('output');
    var note = form.querySelector('[data-role="note"]');
    var cost = form.querySelector('[data-role="cost"]');
    var value = form.querySelector('[data-role="value"]');
    var rates = all('[data-role="rate"]', form);
    function run() {
      var c = units(cost.value, 2), v = units(value.value, 2);
      var rs = rates.map(function (r) { return units(r.value, 2); });
      var ok = c !== null && v !== null && v > 0n && rs.every(function (r) { return r !== null && r > 0n && r <= 10000n; });
      if (!ok) { out.textContent = '?'; note.textContent = form.getAttribute('data-waiting'); return; }
      var need = ceilDiv(c, v);
      var parts = [need.toString() + ' ' + form.getAttribute('data-unit')];
      rs.forEach(function (r, i) {
        need = ceilDiv(need * 10000n, r);
        parts.push(need.toString() + ' ' + rates[i].getAttribute('data-unit'));
      });
      out.textContent = parts[0];
      note.textContent = 'Break-even threshold, not a forecast: ' + parts.join(', which needs ') + '.';
    }
    form.addEventListener('input', run);
    form.addEventListener('submit', function (e) { e.preventDefault(); run(); });
    run();
  });
})();
