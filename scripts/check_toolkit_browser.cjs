#!/usr/bin/env node
// Browser check for the sales toolkit examples (AC-8, AC-9, AC-11).
//
//   node scripts/check_toolkit_browser.cjs [--out DIR]
//
// Builds every example into a temporary folder outside the repository, serves it on a
// random loopback port and drives system Chrome through playwright-core. Writes captures,
// PDFs and receipt.json to DIR (default out/toolkit, ignored by git). Exits 1 on any failure.
// The held film is used when TOOLKIT_FILM_DIR (or out/private-film) holds the reviewed copy;
// otherwise film checks are reported as skipped, never as passed.
'use strict';
const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const cp = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const TOOLS = path.join(ROOT, 'out/.tools/node_modules');
const EXAMPLES = ['coffee', 'banking', 'fitness'];
const WIDTHS = [390, 768, 1440, 1920];
const FILM = 'obenan-concept-film-720p.mp4';

function need(name) {
  const paths = [process.env.PLAYWRIGHT_CORE ? path.dirname(process.env.PLAYWRIGHT_CORE) : null, TOOLS, ROOT]
    .filter(Boolean);
  try {
    if (name === 'playwright-core' && process.env.PLAYWRIGHT_CORE) return require(process.env.PLAYWRIGHT_CORE);
    return require(require.resolve(name, { paths }));
  } catch (err) {
    console.error(`Missing ${name}. Install the pinned tools first:\n` +
      '  npm install --no-save --no-package-lock --prefix out/.tools ' +
      'playwright-core@1.56.1 qrcode@1.5.4 jsqr@1.4.0 pngjs@7.0.0');
    process.exit(2);
  }
}

function chromePath() {
  const candidates = [process.env.CHROME,
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium'];
  const found = candidates.find((c) => c && fs.existsSync(c));
  if (!found) { console.error('No Chrome found. Set CHROME to a Chrome or Chromium binary.'); process.exit(2); }
  return found;
}

const outArg = process.argv.indexOf('--out');
const OUT = path.resolve(outArg > 0 ? process.argv[outArg + 1] : path.join(ROOT, 'out/toolkit'));
const filmDir = process.env.TOOLKIT_FILM_DIR || path.join(ROOT, 'out/private-film');
const haveFilm = fs.existsSync(path.join(filmDir, FILM));

const results = [];
function record(name, ok, detail) {
  results.push({ name, ok: ok === null ? 'skipped' : ok, detail });
  const mark = ok === null ? 'SKIP' : ok ? 'PASS' : 'FAIL';
  console.log(`${mark} ${name}${detail ? `: ${detail}` : ''}`);
}
function check(name, ok, detail) { record(name, Boolean(ok), detail); }

function build(example, dest, extra = []) {
  cp.execFileSync('node', [path.join(ROOT, 'scripts/build_toolkit_example.cjs'),
    '--example', example, '--out', dest, ...extra], { stdio: ['ignore', 'ignore', 'inherit'] });
}

const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp4': 'video/mp4', '.md': 'text/plain; charset=utf-8' };

function serve(dir) {
  const server = http.createServer((req, res) => {
    const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    const file = path.join(dir, rel.endsWith('/') ? `${rel}index.html` : rel);
    if (!file.startsWith(dir) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      res.writeHead(404); res.end(); return;
    }
    const size = fs.statSync(file).size;
    const type = TYPES[path.extname(file)] || 'application/octet-stream';
    const range = /bytes=(\d*)-(\d*)/.exec(req.headers.range || '');
    if (range) {
      const start = range[1] ? Number(range[1]) : 0;
      const end = range[2] ? Number(range[2]) : size - 1;
      res.writeHead(206, { 'Content-Type': type, 'Accept-Ranges': 'bytes',
        'Content-Range': `bytes ${start}-${end}/${size}`, 'Content-Length': end - start + 1 });
      fs.createReadStream(file, { start, end }).pipe(res);
      return;
    }
    res.writeHead(200, { 'Content-Type': type, 'Accept-Ranges': 'bytes', 'Content-Length': size });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise((resolve) => server.listen(0, '127.0.0.1', () => resolve(server)));
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Watches one page for console errors, page errors and failed or missing assets.
function watch(page, label) {
  const problems = [];
  page.on('console', (m) => {
    // Chrome asks every origin for /favicon.ico; the toolkit has none and needs none.
    if (m.type() === 'error' && !/\/favicon\.ico$/.test(m.location().url || '')) problems.push(`console: ${m.text()}`);
  });
  page.on('pageerror', (e) => problems.push(`pageerror: ${e.message}`));
  page.on('requestfailed', (r) => {
    const why = r.failure() && r.failure().errorText;
    // An aborted media request after a seek or navigation is not a missing asset.
    if (why === 'net::ERR_ABORTED' && /\.mp4$/.test(r.url())) return;
    problems.push(`requestfailed: ${r.url()} ${why}`);
  });
  page.on('response', (r) => { if (r.status() >= 400 && !/\/favicon\.ico$/.test(r.url())) problems.push(`http ${r.status()}: ${r.url()}`); });
  return () => record(`${label} console and assets clean`, problems.length === 0, problems.join(' | '));
}

// Every section must have height and visible text; nothing may sit at opacity 0.
async function noBlank(page, label) {
  const blanks = await page.$$eval('section.tk, header.tk-cover', (els) => els.filter((s) => {
    const r = s.getBoundingClientRect();
    return r.height < 40 || s.innerText.trim().length < 20;
  }).map((s) => s.getAttribute('data-section') || 'cover'));
  const hidden = await page.$$eval('.tk-msg, .tk-state:not([hidden]), .tk-review:not([data-clone])',
    (els) => els.filter((e) => Number(getComputedStyle(e).opacity) < 0.99).length);
  check(`${label} no blank section`, blanks.length === 0 && hidden === 0,
    blanks.length || hidden ? `blank=${blanks.join(',')} transparent=${hidden}` : '');
}

async function overflow(page, label) {
  const o = await page.evaluate(() => {
    const wide = [];
    document.querySelectorAll('body *').forEach((e) => {
      const r = e.getBoundingClientRect();
      if (r.width && r.right > innerWidth + 1) wide.push(e.className || e.tagName);
    });
    // Tables must fit without sideways scrolling, and visible images must fill their column.
    const tables = [...document.querySelectorAll('.tk-table-wrap')].filter((t) => t.scrollWidth > t.clientWidth + 1).length;
    const narrow = [...document.querySelectorAll('.tk img')].filter((i) => {
      if (!i.getClientRects().length || i.closest('.tk-print-only')) return false;
      const box = i.parentElement.clientWidth;
      return box > 0 && i.naturalWidth > 0 && i.getBoundingClientRect().width < Math.min(box, i.naturalWidth) * 0.9;
    }).map((i) => i.getAttribute('src'));
    return { scroll: document.documentElement.scrollWidth, width: innerWidth, wide: wide.slice(0, 5), tables, narrow };
  });
  check(`${label} no horizontal overflow`, o.scroll <= o.width && o.wide.length === 0 && o.tables === 0,
    `scrollWidth ${o.scroll} of ${o.width}; tables scrolling sideways ${o.tables}${o.wide.length ? ` wide: ${o.wide.join(', ')}` : ''}`);
  check(`${label} images fill their column`, o.narrow.length === 0, o.narrow.length ? `shrunk: ${o.narrow.join(', ')}` : 'all visible images fill their column');
}

async function fastScroll(page, label) {
  await page.evaluate(async () => {
    const step = Math.max(400, innerHeight);
    for (let y = 0; y < document.body.scrollHeight; y += step) { window.scrollTo(0, y); await new Promise(requestAnimationFrame); }
    window.scrollTo(0, 0);
  });
  await sleep(700);
  await noBlank(page, `${label} fast-scroll`);
}

async function keyboard(page, label) {
  const tab = page.locator('[data-section="compare"] [role="tab"]').first();
  if (await tab.count()) {
    await tab.focus();
    await page.keyboard.press('ArrowRight');
    const s1 = await page.evaluate(() => ({
      focused: document.activeElement.id,
      selected: [...document.querySelectorAll('[data-section="compare"] [role="tab"]')].map((t) => t.getAttribute('aria-selected')),
      hidden: [...document.querySelectorAll('[data-section="compare"] [role="tabpanel"]')].map((p) => p.hidden),
    }));
    await page.keyboard.press('Home');
    const s2 = await page.evaluate(() => document.activeElement.getAttribute('aria-selected'));
    check(`${label} keyboard tabs`, s1.selected.join() === 'false,true' && s1.hidden.join() === 'true,false'
      && s1.focused === 'tab-pro' && s2 === 'true', JSON.stringify(s1));
  }
  const filters = page.locator('.tk-filter');
  if (await filters.count()) {
    const last = filters.nth((await filters.count()) - 1);
    const type = await last.getAttribute('data-type');
    await last.focus();
    await page.keyboard.press('Enter');
    const shown = await page.$$eval('[data-section="portfolio"] tbody tr', (rows) => rows.filter((r) => !r.hidden).map((r) => r.dataset.type));
    const status = await page.textContent('[data-section="portfolio"] [data-role="shown"]');
    await filters.first().focus();
    await page.keyboard.press('Space');
    const all = await page.$$eval('[data-section="portfolio"] tbody tr', (rows) => rows.filter((r) => !r.hidden).length);
    const total = await page.$$eval('[data-section="portfolio"] tbody tr', (rows) => rows.length);
    check(`${label} keyboard filters`, shown.length > 0 && shown.every((t) => t === type) && all === total
      && status.includes(`Showing ${shown.length} of ${total}`), `${type}: ${shown.length}, all: ${all}/${total}`);
  }
}

async function unknownSort(page, label) {
  const cols = await page.$$eval('[data-section="portfolio"] thead th', (ths) => ths.length);
  if (!cols) return;
  const bad = [];
  let tested = 0;
  for (let c = 0; c < cols; c++) {
    const hasUnknown = await page.$$eval('[data-section="portfolio"] tbody tr',
      (rows, col) => rows.some((r) => r.cells[col].classList.contains('tk-unknown')), c);
    if (!hasUnknown) continue;
    tested++;
    for (const dir of ['ascending', 'descending']) {
      await page.click(`[data-section="portfolio"] thead th:nth-child(${c + 1}) button`);
      const got = await page.$$eval('[data-section="portfolio"] thead th', (ths, col) => ths[col].getAttribute('aria-sort'), c);
      const order = await page.$$eval('[data-section="portfolio"] tbody tr', (rows, col) => rows.map((r) => r.cells[col].classList.contains('tk-unknown')), c);
      const firstUnknown = order.indexOf(true);
      if (got !== dir || order.slice(firstUnknown).includes(false)) bad.push(`col ${c} ${dir}`);
    }
  }
  check(`${label} Unknown sorts last both ways`, tested > 0 && bad.length === 0, `${tested} columns with Unknown${bad.length ? `; wrong: ${bad.join(', ')}` : ''}`);
}

async function stream(page, label) {
  if (!(await page.locator('[data-section="reviews"] .tk-stream').count())) return;
  await page.locator('[data-section="reviews"]').scrollIntoViewIfNeeded();
  await page.mouse.move(0, 0);
  const y = () => page.$eval('.tk-stream-track', (t) => new DOMMatrix(getComputedStyle(t).transform).m42);
  const a = await y(); await sleep(800); const b = await y();
  const unique = await page.$$eval('.tk-review:not([data-clone])', (e) => e.length);
  const clones = await page.$$eval('.tk-review[data-clone][aria-hidden="true"]', (e) => e.length);
  await page.click('[data-action="pause"]');
  await page.mouse.move(0, 0);
  const c = await y(); await sleep(800); const d = await y();
  const pressed = await page.getAttribute('[data-action="pause"]', 'aria-pressed');
  await page.click('[data-action="pause"]');
  await page.mouse.move(0, 0);
  check(`${label} review cards move`, b < a, `translateY ${a.toFixed(1)} to ${b.toFixed(1)}; ${unique} unique, ${clones} hidden clones`);
  check(`${label} pause stops the stream`, Math.abs(d - c) < 0.5 && pressed === 'true', `translateY ${c.toFixed(1)} to ${d.toFixed(1)}`);
}

async function chat(page, label) {
  const section = page.locator('[data-section="assistant"]');
  if (!(await section.count())) return;
  // First entry on a fresh load: the fast-scroll pass has already played this page's chat once.
  await page.reload({ waitUntil: 'load' });
  await sleep(200);
  const seen = await page.evaluate(() => new Promise((resolve) => {
    const msgs = [...document.querySelectorAll('[data-section="assistant"] .tk-msg')];
    const log = [];
    const t0 = performance.now();
    const pending = new Set();
    let questionVisible = true;
    const mo = new MutationObserver(() => msgs.forEach((m, i) => {
      if (i === 0 && Number(getComputedStyle(m).opacity) < 0.99) questionVisible = false;
      if (m.classList.contains('is-pending')) { pending.add(i); return; }
      if (pending.has(i) && m.classList.contains('is-shown')) { pending.delete(i); log.push({ i, on: true, t: Math.round(performance.now() - t0) }); }
    }));
    msgs.forEach((m) => mo.observe(m, { attributes: true, attributeFilter: ['class'] }));
    document.querySelector('[data-section="assistant"] .tk-chat').scrollIntoView({ block: 'center' });
    setTimeout(() => { mo.disconnect(); resolve({ log, n: msgs.length, questionVisible }); }, 5200);
  }));
  const shownOrder = seen.log.filter((l) => l.on).map((l) => l.i);
  const ordered = seen.questionVisible && shownOrder.join() === [...Array(seen.n).keys()].slice(1).join();
  check(`${label} chat sequence plays in order`, ordered, `revealed ${shownOrder.join(',')} at ${seen.log.filter((l) => l.on).map((l) => `${l.t}ms`).join(', ')}`);
  await page.click('[data-section="assistant"] [data-action="replay"]');
  await sleep(150);
  const pending = await page.$$eval('[data-section="assistant"] .tk-msg.is-pending', (e) => e.length);
  await sleep(4200);
  const done = await page.$$eval('[data-section="assistant"] .tk-msg', (e) => e.every((m) => !m.classList.contains('is-pending') && Number(getComputedStyle(m).opacity) > 0.99));
  check(`${label} replay restarts and finishes`, pending === seen.n - 1 && done, `${pending} pending after replay`);
  // Re-entry: scroll away and back; the finished answer stays.
  await page.evaluate(() => window.scrollTo(0, 0)); await sleep(300);
  await section.scrollIntoViewIfNeeded(); await sleep(300);
  const kept = await page.$$eval('[data-section="assistant"] .tk-msg.is-pending', (e) => e.length);
  check(`${label} re-entry keeps the answer`, kept === 0);
  // Leaving mid-play finishes immediately.
  await page.click('[data-section="assistant"] [data-action="replay"]');
  await page.evaluate(() => window.scrollTo(0, 0)); await sleep(400);
  const left = await page.$$eval('[data-section="assistant"] .tk-msg.is-pending', (e) => e.length);
  check(`${label} leaving mid-play finishes the answer`, left === 0);
}

const CASES = [
  // [label, cost, value, rates, expected output] Rates are percentages.
  ['float trap 1.10 / 0.10', '1.10', '0.10', ['100', '100'], '11'],
  ['decimal comma', '1,10', '0,10', ['100', '100'], '11'],
  ['empty', '', '', ['', ''], '?'],
  ['invalid text', 'abc', '5', ['10', '10'], '?'],
  ['zero contribution', '100', '0', ['10', '10'], '?'],
  ['zero rate', '100', '5', ['0', '10'], '?'],
  ['rate above 100', '100', '5', ['100.01', '10'], '?'],
  ['three decimals', '100.001', '5', ['10', '10'], '?'],
  ['negative', '-100', '5', ['10', '10'], '?'],
  ['boundary 100 percent', '100', '5', ['100', '100'], '20'],
  ['rounds up, never down', '100', '3', ['10', '10'], '34'],
  ['zero cost', '0', '5', ['10', '10'], '0'],
];
async function businessCase(page, label) {
  const form = page.locator('[data-section="business-case"] form');
  if (!(await form.count())) return;
  const rates = await form.locator('[data-role="rate"]').count();
  const bad = [];
  for (const [name, cost, value, rs, want] of CASES) {
    await form.locator('[data-role="cost"]').fill(cost);
    await form.locator('[data-role="value"]').fill(value);
    for (let i = 0; i < rates; i++) await form.locator('[data-role="rate"]').nth(i).fill(rs[i]);
    const out = (await form.locator('output').textContent()).trim();
    const got = out.split(' ')[0];
    if (got !== want) bad.push(`${name}: got ${out}`);
  }
  // Full chain for the float trap: 1.10 / 0.10 = 11, then 11 at 10% = 110, then 110 at 10% = 1100.
  await form.locator('[data-role="cost"]').fill('1.10');
  await form.locator('[data-role="value"]').fill('0.10');
  for (let i = 0; i < rates; i++) await form.locator('[data-role="rate"]').nth(i).fill('10');
  const note = await form.locator('[data-role="note"]').textContent();
  const chain = ['11', '110', '1100'].slice(0, rates + 1);
  const chainOk = chain.every((n) => new RegExp(`\\b${n} `).test(note));
  check(`${label} business case exact`, bad.length === 0 && chainOk, bad.length ? bad.join('; ') : `${CASES.length} cases; chain: ${note}`);
  for (const sel of ['[data-role="cost"]', '[data-role="value"]']) await form.locator(sel).fill('');
  for (let i = 0; i < rates; i++) await form.locator('[data-role="rate"]').nth(i).fill('');
}

async function video(page, label, filmPresent) {
  if (!filmPresent) { record(`${label} video currentTime advances`, null, 'held film not supplied'); return; }
  const before = await page.evaluate(() => performance.getEntriesByType('resource').filter((r) => r.name.endsWith('.mp4')).length);
  const attrs = await page.$eval('video', (v) => ({ preload: v.getAttribute('preload'), controls: v.controls, autoplay: v.autoplay, poster: !!v.poster }));
  await page.locator('video').scrollIntoViewIfNeeded();
  const t = await page.evaluate(async () => {
    const v = document.querySelector('video');
    await v.play();
    const t0 = v.currentTime;
    await new Promise((r) => setTimeout(r, 2500));
    v.pause();
    return { t0, t1: v.currentTime, duration: v.duration };
  });
  check(`${label} video loads politely`, before === 0 && attrs.preload === 'none' && attrs.controls && !attrs.autoplay && attrs.poster,
    `mp4 requests before play: ${before}; ${JSON.stringify(attrs)}`);
  check(`${label} video currentTime advances`, t.t1 - t.t0 > 1.5, `currentTime ${t.t0.toFixed(2)} to ${t.t1.toFixed(2)} of ${t.duration.toFixed(1)} s`);
}

async function printChecks(page, label) {
  await page.emulateMedia({ media: 'print' });
  const p = await page.evaluate(() => {
    const visible = (e) => getComputedStyle(e).display !== 'none' && e.getClientRects().length > 0;
    return {
      controls: [...document.querySelectorAll('button, .tk-controls, .tk-tabs, video, [data-clone]')].filter(visible).length,
      states: [...document.querySelectorAll('.tk-state')].filter(visible).length,
      statesTotal: document.querySelectorAll('.tk-state').length,
      reviews: [...document.querySelectorAll('.tk-review')].filter(visible).length,
      unique: document.querySelectorAll('.tk-review:not([data-clone])').length,
      msgs: [...document.querySelectorAll('.tk-msg')].filter((m) => visible(m) && Number(getComputedStyle(m).opacity) > 0.99).length,
      msgsTotal: document.querySelectorAll('.tk-msg').length,
      rows: [...document.querySelectorAll('.tk-table tbody tr')].filter(visible).length,
      rowsTotal: document.querySelectorAll('.tk-table tbody tr').length,
    };
  });
  // Table header sort buttons are part of the header text in print, so count other controls only.
  const headerButtons = await page.$$eval('.tk-table th button', (b) => b.length);
  check(`${label} print shows both states, reviews once, full chat and every row, no controls`,
    p.controls === headerButtons && p.states === p.statesTotal && p.reviews === p.unique
      && p.msgs === p.msgsTotal && p.rows === p.rowsTotal, JSON.stringify(p));
  await page.emulateMedia({ media: null });
}

// A printed page should not stop short: every page but the last must carry content past 45% of its height.
function pageFill(pdfFile, label) {
  let tmp;
  try {
    tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'obenan-fill-'));
    cp.execFileSync('pdftoppm', ['-r', '20', '-gray', pdfFile, path.join(tmp, 'p')]);
  } catch (err) {
    record(`${label} pages are filled`, null, 'pdftoppm (poppler) not installed');
    return;
  }
  const fills = fs.readdirSync(tmp).filter((f) => f.endsWith('.pgm')).sort().map((f) => {
    const buf = fs.readFileSync(path.join(tmp, f));
    const head = buf.toString('latin1', 0, 64).split(/\s+/);
    const [w, h] = [Number(head[1]), Number(head[2])];
    const data = buf.subarray(buf.length - w * h);
    let last = 0;
    for (let y = 0; y < h; y += 1) {
      for (let x = 0; x < w; x += 1) if (data[y * w + x] < 235) { last = y; break; }
    }
    return Math.round((100 * last) / h);
  });
  fs.rmSync(tmp, { recursive: true, force: true });
  const short = fills.slice(0, -1).filter((f) => f < 45).length + fills.filter((f) => f === 0).length;
  check(`${label} pages are filled, none blank`, short === 0, `${fills.length} pages, content ends at ${fills.join('%, ')}% of each page`);
}

// Links in a handed-over PDF must open on any machine. Only files named *-loopback.pdf are diagnostic.
function publicLinks(pdfFile, label) {
  let urls;
  try {
    urls = cp.execFileSync('pdfinfo', ['-url', pdfFile], { encoding: 'utf8' }).split('\n').slice(1)
      .map((l) => l.trim().split(/\s+/).pop()).filter(Boolean);
  } catch (err) {
    record(`${label} links open outside this machine`, null, 'pdfinfo (poppler) not installed');
    return;
  }
  const local = urls.filter((u) => /^(file:|https?:\/\/(127\.|localhost|\[::1\]|0\.0\.0\.0))/i.test(u) || !/^(https?|mailto):/i.test(u));
  check(`${label} links open outside this machine`, local.length === 0, local.length ? local.join(', ') : `${urls.length} links: ${[...new Set(urls)].join(', ')}`);
}

function pdfPages(pdfFile) {
  const n = Number(/Pages:\s+(\d+)/.exec(cp.execFileSync('pdfinfo', [pdfFile], { encoding: 'utf8' }))[1]);
  return Array.from({ length: n }, (_, i) => cp.execFileSync('pdftotext', ['-f', `${i + 1}`, '-l', `${i + 1}`, pdfFile, '-'], { encoding: 'utf8' }).replace(/\s+/g, ' '));
}

// The business case reads as one unit: its label, every input, the result and the note on one printed page.
async function caseTogether(page, pdfFile, label) {
  const parts = await page.$$eval('[data-section="business-case"] .tk-label, [data-section="business-case"] form label, [data-section="business-case"] .tk-result p',
    (els) => els.map((e) => e.textContent.replace(/\s+/g, ' ').trim().slice(0, 40)));
  let pages;
  try { pages = pdfPages(pdfFile); } catch (err) {
    record(`${label} business case prints on one page`, null, 'pdftotext (poppler) not installed');
    return;
  }
  const holding = parts.map((t) => pages.map((p, i) => (p.includes(t) ? i + 1 : 0)).filter(Boolean));
  const same = holding.every((h) => h.length === 1) && new Set(holding.map((h) => h[0])).size === 1;
  check(`${label} business case prints on one page`, parts.length >= 5 && same,
    `${pages.length} pages; ${parts.map((t, i) => `"${t}" p${holding[i].join('/') || 'none'}`).join('; ')}`);
}

async function qr(page, url, pdfFile, label) {
  const jsQR = need('jsqr');
  const { PNG } = need('pngjs');
  await page.emulateMedia({ media: 'print' });
  const shot = await page.locator('.tk-qr').screenshot({ scale: 'device' });
  const png = PNG.sync.read(shot);
  const code = jsQR(new Uint8ClampedArray(png.data), png.width, png.height);
  const link = await page.getAttribute('.tk-film-link', 'href');
  const posterLink = await page.$eval('.tk-print-only a img.tk-poster', (img) => img.parentNode.getAttribute('href'));
  await page.emulateMedia({ media: null });
  const res = await page.request.get(url);
  let annots = null;
  try {
    annots = cp.execFileSync('pdfinfo', ['-url', pdfFile], { encoding: 'utf8' }).split('\n').filter((l) => l.trim().endsWith(url)).length;
  } catch (err) {
    record(`${label} PDF link annotations`, null, 'pdfinfo (poppler) not installed');
  }
  check(`${label} QR decodes to the link`, code && code.data === url && link === url && posterLink === url,
    `decoded ${code ? code.data : 'nothing'}`);
  check(`${label} film address serves video`, res.status() === 200 && /video\/mp4/.test(res.headers()['content-type']), `${res.status()} ${res.headers()['content-type']}`);
  if (annots !== null) check(`${label} PDF poster and link are clickable`, annots >= 2, `${annots} link annotations to the address`);
}

(async () => {
  const { chromium } = need('playwright-core');
  fs.mkdirSync(OUT, { recursive: true });
  const site = fs.mkdtempSync(path.join(os.tmpdir(), 'obenan-toolkit-'));
  for (const ex of EXAMPLES) build(ex, path.join(site, ex));
  if (haveFilm) build('coffee', path.join(site, 'coffee-film'), ['--film-dir', filmDir]);
  const server = await serve(site);
  const base = `http://127.0.0.1:${server.address().port}`;
  if (haveFilm) {
    // Mechanism check only: a loopback address stands in for an approved public one.
    build('coffee', path.join(site, 'coffee-film-url'), ['--film-dir', filmDir, '--film-url', `${base}/coffee-film/film/${FILM}`]);
  }
  console.log(`Serving ${site} at ${base}`);
  const browser = await chromium.launch({ executablePath: chromePath(), args: ['--autoplay-policy=no-user-gesture-required'] });

  for (const ex of EXAMPLES) {
    for (const w of WIDTHS) {
      const label = `${ex} ${w}px`;
      const ctx = await browser.newContext({ viewport: { width: w, height: w < 500 ? 844 : w < 1000 ? 1024 : 1000 } });
      const page = await ctx.newPage();
      const done = watch(page, label);
      await page.goto(`${base}/${ex}/index.html`, { waitUntil: 'load' });
      await overflow(page, label);
      await fastScroll(page, label);
      await keyboard(page, `${label} keyboard`);
      if (w === 1440 || w === 390) {
        await unknownSort(page, label);
        await stream(page, label);
        await chat(page, label);
        await businessCase(page, label);
      }
      await page.evaluate(() => window.scrollTo(0, 0));
      await sleep(300);
      await page.screenshot({ path: path.join(OUT, `${ex}-${w}.png`), fullPage: true });
      if (w === 1440) await printChecks(page, label);
      done();
      await ctx.close();
    }
  }

  for (const ex of EXAMPLES) {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
    const page = await ctx.newPage();
    await page.goto(`${base}/${ex}/index.html`, { waitUntil: 'load' });
    const r = await page.evaluate(() => ({
      moving: document.querySelectorAll('.tk-stream.is-moving').length,
      clones: document.querySelectorAll('[data-clone]').length,
      pending: document.querySelectorAll('.tk-msg.is-pending').length,
      pauseDisabled: [...document.querySelectorAll('[data-action="pause"]')].every((b) => b.disabled),
    }));
    if (await page.locator('[data-action="replay"]').count()) {
      await page.click('[data-action="replay"]');
      r.pendingAfterReplay = await page.$$eval('.tk-msg.is-pending', (e) => e.length);
    }
    check(`${ex} reduced-motion holds everything still and complete`, r.moving === 0 && r.clones === 0 && r.pending === 0
      && r.pauseDisabled && !r.pendingAfterReplay, JSON.stringify(r));
    await noBlank(page, `${ex} reduced-motion`);
    await ctx.close();

    const nojs = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
    const np = await nojs.newPage();
    await np.goto(`${base}/${ex}/index.html`, { waitUntil: 'load' });
    const n = await np.evaluate(() => ({
      controls: [...document.querySelectorAll('.tk-controls, .tk-tabs')].filter((e) => getComputedStyle(e).display !== 'none').length,
      states: [...document.querySelectorAll('.tk-state')].filter((e) => getComputedStyle(e).display !== 'none').length,
      total: document.querySelectorAll('.tk-state').length,
    }));
    check(`${ex} no-js shows every state with controls hidden`, n.controls === 0 && n.states === n.total, JSON.stringify(n));
    await noBlank(np, `${ex} no-js`);
    await np.screenshot({ path: path.join(OUT, `${ex}-390-no-js.png`), fullPage: true });
    await nojs.close();
  }

  // PDFs: the public coffee build, and when the film is held here, a private build with its poster.
  const pdfCtx = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  const pdfPage = await pdfCtx.newPage();
  const pdfs = [['coffee', 'coffee.pdf']];
  if (haveFilm) pdfs.push(['coffee-film', 'coffee-with-film-poster.pdf'], ['coffee-film-url', 'coffee-film-url-loopback.pdf']);
  for (const [dir, name] of pdfs) {
    await pdfPage.goto(`${base}/${dir}/index.html`, { waitUntil: 'load' });
    await printChecks(pdfPage, `${dir} pdf`);
    await pdfPage.pdf({ path: path.join(OUT, name), format: 'A4', printBackground: true, preferCSSPageSize: true });
    record(`${dir} pdf written`, true, path.join(OUT, name));
    pageFill(path.join(OUT, name), `${dir} pdf`);
    if (!name.includes('loopback')) publicLinks(path.join(OUT, name), `${dir} pdf`);
  }
  // Business case cohesion, blank and filled, for every example that has a calculator.
  for (const ex of EXAMPLES) {
    await pdfPage.goto(`${base}/${ex}/index.html`, { waitUntil: 'load' });
    const form = pdfPage.locator('[data-section="business-case"] form');
    if (!(await form.count())) continue;
    for (const state of ['blank', 'filled']) {
      if (state === 'filled') {
        await form.locator('[data-role="cost"]').fill('900');
        await form.locator('[data-role="value"]').fill('45');
        const rates = await form.locator('[data-role="rate"]').count();
        for (let i = 0; i < rates; i++) await form.locator('[data-role="rate"]').nth(i).fill('20');
      }
      const file = path.join(OUT, `${ex}-business-case-${state}.pdf`);
      await pdfPage.pdf({ path: file, format: 'A4', printBackground: true, preferCSSPageSize: true });
      await caseTogether(pdfPage, file, `${ex} ${state} pdf`);
      pageFill(file, `${ex} ${state} pdf`);
      publicLinks(file, `${ex} ${state} pdf`);
    }
  }
  if (haveFilm) {
    const vp = await pdfCtx.newPage();
    const done = watch(vp, 'coffee-film 1440px');
    await vp.goto(`${base}/coffee-film/index.html`, { waitUntil: 'load' });
    await video(vp, 'coffee-film 1440px', true);
    done();
    await pdfPage.goto(`${base}/coffee-film-url/index.html`, { waitUntil: 'load' });
    await qr(pdfPage, `${base}/coffee-film/film/${FILM}`, path.join(OUT, 'coffee-film-url-loopback.pdf'), 'coffee-film-url');
  } else {
    record('video currentTime advances', null, 'held film not supplied; set TOOLKIT_FILM_DIR');
    record('QR decodes to the link (jsQR)', null, 'held film not supplied');
  }
  await pdfCtx.close();
  await browser.close();
  server.close();
  fs.rmSync(site, { recursive: true, force: true });

  const failed = results.filter((r) => r.ok === false);
  const skipped = results.filter((r) => r.ok === 'skipped');
  fs.writeFileSync(path.join(OUT, 'receipt.json'), `${JSON.stringify({ date: new Date().toISOString(), widths: WIDTHS, results }, null, 2)}\n`);
  console.log(`\n${results.length - failed.length - skipped.length} passed, ${failed.length} failed, ${skipped.length} skipped. Receipt: ${path.join(OUT, 'receipt.json')}`);
  process.exit(failed.length ? 1 : 0);
})().catch((err) => { console.error(err); process.exit(1); });
