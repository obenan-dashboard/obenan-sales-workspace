#!/usr/bin/env node
// Builds one toolkit example into a self-contained folder outside the repository.
//
//   node scripts/build_toolkit_example.cjs --example coffee --out DIR
//        [--film-dir DIR] [--film-url URL]
//
// Without --film-dir the teaser section is left out: the concept film is held privately
// (assets/product-film/README.md). With --film-dir the rendition and poster must match the
// checksums recorded in that README. --film-url adds a clickable poster, link and QR to the
// printed page; pass it only for an approved, working public address.
//
// --out must be a new or empty folder; the build refuses anything else before writing.
// Images and styles are copied into the folder. Links to repository documents open their
// public source at SOURCE_COMMIT, so they work in a PDF or a copy on any machine. Move the pin
// to a newer public commit when a linked document changes; the tests check the text matches.
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..');
const SECTIONS = path.join(ROOT, 'templates/sections');
const EXAMPLES = ['coffee', 'banking', 'fitness'];
const FILM = 'obenan-concept-film-720p.mp4';
const POSTER = 'obenan-concept-film-poster.jpg';
const SOURCE_COMMIT = '2d8572a07b590a84f85840092733e76a36faeb26';
const SOURCE = `https://github.com/obenan-dashboard/obenan-sales-workspace/blob/${SOURCE_COMMIT}/`;

function fail(message) {
  process.stderr.write(`build_toolkit_example: ${message}\n`);
  process.exit(1);
}

function args(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!/^--(example|out|film-dir|film-url)$/.test(key) || value === undefined) {
      fail(`unknown or incomplete option ${key}`);
    }
    out[key.slice(2)] = value;
  }
  if (!EXAMPLES.includes(out.example)) fail(`--example must be one of ${EXAMPLES.join(', ')}`);
  if (!out.out) fail('--out is required');
  if (out['film-url'] && !out['film-dir']) fail('--film-url needs --film-dir');
  if (out['film-url'] && !/^https?:\/\/[^\s"'<>]+$/.test(out['film-url'])) fail('--film-url must be an http(s) address');
  return out;
}

function sha256(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

// The README's held-files table is the single record of the approved checksums.
function recordedDigests() {
  const readme = fs.readFileSync(path.join(ROOT, 'assets/product-film/README.md'), 'utf8');
  const digest = (name) => {
    const row = readme.split('\n').find((l) => l.startsWith(`| \`${name}\``));
    const m = row && row.match(/`([0-9a-f]{64})`/);
    if (!m) fail(`no recorded checksum for ${name} in assets/product-film/README.md`);
    return m[1];
  };
  return { [FILM]: digest(FILM), [POSTER]: digest(POSTER) };
}

function escapeAttr(s) {
  return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
}

function qrSvg(url) {
  const tools = path.join(ROOT, 'out/.tools/node_modules');
  let qrcode;
  try {
    qrcode = require(require.resolve('qrcode', { paths: [tools, ROOT] }));
  } catch (err) {
    fail('--film-url needs the qrcode package; see knowledge/engagement/SALES_TOOLKIT.md');
  }
  return new Promise((resolve, reject) => {
    qrcode.toString(url, { type: 'svg', errorCorrectionLevel: 'M', margin: 2 }, (err, svg) =>
      (err ? reject(err) : resolve(svg)));
  });
}

async function filmMarkup(opts, outDir) {
  const dir = opts['film-dir'];
  const want = recordedDigests();
  for (const name of [FILM, POSTER]) {
    const file = path.join(dir, name);
    if (!fs.existsSync(file)) fail(`missing ${name} in --film-dir`);
    if (sha256(file) !== want[name]) fail(`checksum of ${name} does not match assets/product-film/README.md`);
  }
  const url = opts['film-url'];
  const qr = url ? await qrSvg(url) : null;
  return {
    files: [[path.join(dir, FILM), `film/${FILM}`], [path.join(dir, POSTER), `film/${POSTER}`]],
    qr,
    html: [
      '    <div class="tk-stage">',
      `      <video controls muted playsinline preload="none" poster="film/${POSTER}" aria-describedby="teaser-desc">`,
      `        <source src="film/${FILM}" type="video/mp4">`,
      '      </video>',
      '    </div>',
      '    <div class="tk-print-only">',
      url ? `      <a href="${escapeAttr(url)}">` : '',
      `      <img class="tk-poster" src="film/${POSTER}" alt="Still from the concept product film: an assistant asks how it can help">`,
      url ? '      </a>' : '',
      url ? [
        '      <div class="tk-film-meta">',
        '        <img class="tk-qr" src="film/qr.svg" alt="QR code for the concept product film address">',
        `        <p>Scan or open <a class="tk-film-link" href="${escapeAttr(url)}">${escapeAttr(url)}</a></p>`,
        '      </div>',
      ].join('\n') : '      <p class="tk-film-meta">Shown in the meeting. No public address is approved for this film yet.</p>',
      '    </div>',
    ].filter(Boolean).join('\n'),
  };
}

// Copies each local src target into files/<repository path>; points each local href at its
// pinned public source.
function localise(html, copies) {
  return html.replace(/((?:src|href)=")([^"]+)(")/g, (whole, pre, ref, post) => {
    if (/^(https?:|mailto:|data:|#)/.test(ref) || /^(toolkit\.(css|js)|[a-z]+\.css|fonts\/|film\/)/.test(ref)) return whole;
    const [target, hash] = ref.split('#');
    const source = path.resolve(SECTIONS, decodeURIComponent(target));
    const rel = path.relative(ROOT, source);
    if (rel.startsWith('..') || path.isAbsolute(rel) || !fs.existsSync(source)) {
      fail(`local reference ${ref} does not resolve inside the repository`);
    }
    const repoPath = rel.split(path.sep).join('/');
    if (pre.startsWith('href')) return `${pre}${SOURCE}${repoPath}${hash ? `#${hash}` : ''}${post}`;
    const dest = `files/${repoPath}`;
    copies.push([source, dest]);
    return `${pre}${dest}${hash ? `#${hash}` : ''}${post}`;
  });
}

async function main() {
  const opts = args(process.argv.slice(2));
  const outDir = path.resolve(opts.out);
  if (!path.relative(ROOT, outDir).startsWith('..')) {
    process.stderr.write('build_toolkit_example: note: --out is inside the repository; keep builds outside it\n');
  }
  if (fs.existsSync(outDir)) {
    if (!fs.statSync(outDir).isDirectory()) fail(`--out ${opts.out} is not a folder`);
    if (fs.readdirSync(outDir).length) fail(`--out ${opts.out} is not empty; choose a new or empty folder so no earlier files survive`);
  }
  let html = fs.readFileSync(path.join(SECTIONS, `${opts.example}.html`), 'utf8');
  const copies = [
    [path.join(SECTIONS, 'toolkit.css'), 'toolkit.css'],
    [path.join(SECTIONS, 'toolkit.js'), 'toolkit.js'],
  ];
  const own = path.join(SECTIONS, `${opts.example}.css`);
  if (fs.existsSync(own)) {
    copies.push([own, `${opts.example}.css`]);
    for (const f of fs.readdirSync(path.join(SECTIONS, 'fonts'))) copies.push([path.join(SECTIONS, 'fonts', f), `fonts/${f}`]);
  }
  const teaser = /\n<section class="tk[^"]*" data-section="teaser"[\s\S]*?<\/section>\n/;
  const slot = /    <div class="tk-film"[^>]*>[\s\S]*?<\/div>\n/;
  let qr = null;
  if (teaser.test(html)) {
    if (opts['film-dir']) {
      const film = await filmMarkup(opts, outDir);
      if (!slot.test(html)) fail('teaser section has no tk-film slot');
      html = html.replace(slot, `${film.html}\n`);
      copies.push(...film.files);
      qr = film.qr;
    } else {
      html = html.replace(teaser, '\n');
    }
  }
  html = localise(html, copies);

  fs.mkdirSync(outDir, { recursive: true });
  for (const [source, dest] of copies) {
    const target = path.join(outDir, dest);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.copyFileSync(source, target);
  }
  if (qr) fs.writeFileSync(path.join(outDir, 'film/qr.svg'), qr);
  fs.writeFileSync(path.join(outDir, 'index.html'), html);
  process.stdout.write(`${path.join(outDir, 'index.html')}\n`);
}

main().catch((err) => fail(err.message));
