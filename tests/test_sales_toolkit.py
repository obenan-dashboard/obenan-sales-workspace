"""Static contracts for the sales toolkit sections. Browser behaviour: scripts/check_toolkit_browser.cjs."""

from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import os
import re
import subprocess
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = "knowledge/engagement/SALES_TOOLKIT.md"
SECTIONS = ROOT / "templates/sections"
EXAMPLES = ("coffee", "banking", "fitness")
FILM = ROOT / "assets/product-film"
BUILD = ROOT / "scripts/build_toolkit_example.cjs"
HELD_RENDITION = "1d1dc9d8120d892aedefb1418b6cf7596cf14c03513c5db7d8f9c7fcb4f1dee0"
HELD_FILM = Path(os.environ.get("TOOLKIT_FILM_DIR", ROOT / "out/private-film"))


def build(example, out, *extra):
    return subprocess.run(["node", str(BUILD), "--example", example, "--out", str(out), *extra],
                          capture_output=True, text=True)


def local_refs(html):
    refs = re.findall(r'(?:src|href|poster)=["\']([^"\']+)["\']', html)
    return [r for r in refs if not re.match(r"^(https?:|mailto:|data:|#)", r)]
DEMO_SECTIONS = {"teaser", "compare", "reviews", "portfolio", "assistant", "business-case"}


def read(path):
    return (ROOT / path).read_text()


class Page(HTMLParser):
    """Collects sections, their disclosure labels and review cards from one example."""

    def __init__(self):
        super().__init__()
        self.sections, self.labels, self.cards, self.stack = [], {}, [], []
        self.links, self.inline_style, self.inline_script, self.videos = [], 0, 0, []
        self.in_label = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "section" and "data-section" in a:
            self.sections.append(a["data-section"])
        if "tk-label" in classes:
            self.in_label = self.sections[-1] if self.sections else None
            self.labels.setdefault(self.in_label, "")
        if "tk-review" in classes:
            self.cards.append(a.get("data-theme"))
        if tag == "link":
            self.links.append(a.get("href"))
        if tag == "style":
            self.inline_style += 1
        if tag == "script" and "src" not in a:
            self.inline_script += 1
        if tag == "script" and "src" in a:
            self.links.append(a["src"])
        if tag == "video":
            self.videos.append(a)
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()
        if tag == "p":
            self.in_label = None

    def handle_data(self, data):
        if self.in_label is not None:
            self.labels[self.in_label] += data


def page(name):
    p = Page()
    p.feed((SECTIONS / f"{name}.html").read_text())
    return p


def text(name):
    body = (SECTIONS / f"{name}.html").read_text()
    return " ".join(re.sub(r"<[^>]+>", " ", body).split())


class SalesToolkitTests(unittest.TestCase):
    def test_AC_TOOLKIT_1_entry_points_reach_one_toolkit_document(self):
        for path in ("START_HERE.md", "README.md", "knowledge/TASK_ROUTER.md",
                     "templates/decision-pack/BUILD_PROMPT.md"):
            with self.subTest(path=path):
                self.assertIn("SALES_TOOLKIT.md", read(path))
        rows = [l for l in read("knowledge/TASK_ROUTER.md").splitlines()
                if l.startswith("| Interactive sections |")]
        self.assertEqual(len(rows), 1)
        doc = read(DOC)
        for phrase in ("Product teaser", "Observed and proposed", "Review stream",
                       "Portfolio explorer", "Assistant walkthrough", "Business case",
                       "Coffee and restaurants", "Banking", "Fitness",
                       "python3 -m unittest discover -s tests -v",
                       "bash scripts/validate_public_repo.sh",
                       "node scripts/check_toolkit_browser.cjs", "```text"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, doc)
        self.assertNotRegex(doc, r"/Users/|[–—]")
        self.assertFalse((ROOT / "templates/sections/BUILD_PROMPT.md").exists())

    def test_AC_TOOLKIT_2_examples_use_only_shared_implementation(self):
        for name in EXAMPLES:
            with self.subTest(example=name):
                p = page(name)
                self.assertEqual(p.inline_style, 0)
                self.assertEqual(p.inline_script, 0)
                self.assertIn("toolkit.css", p.links)
                self.assertIn("toolkit.js", p.links)
                self.assertNotIn('style="', (SECTIONS / f"{name}.html").read_text())
        coffee = page("coffee").sections
        self.assertIn("teaser", coffee)
        self.assertIn("assistant", coffee)
        self.assertNotEqual(coffee.index("teaser"), coffee.index("assistant"))
        self.assertEqual(set(coffee) & DEMO_SECTIONS, DEMO_SECTIONS)

    def test_AC_TOOLKIT_3_recipes_vary_by_buyer_question(self):
        orders = {name: page(name).sections for name in EXAMPLES}
        self.assertEqual(len({tuple(o) for o in orders.values()}), 3)
        self.assertGreater(len({len(o) for o in orders.values()}), 1)
        for name, order in orders.items():
            with self.subTest(example=name):
                self.assertLess(order.count("reviews") * 2, len(order))
        coffee, bank, gym = (text(n).lower() for n in EXAMPLES)
        for word in ("discovery", "menu", "consisten", "guest"):
            self.assertIn(word, coffee)
        for word in ("branches", "atms", "governance"):
            self.assertIn(word, bank)
        self.assertRegex(bank, r"\d+ branches")
        self.assertRegex(bank, r"\d+ atms")
        for word in ("club", "offer", "trial", "membership"):
            self.assertIn(word, gym)

    def test_AC_TOOLKIT_4_demonstrations_are_disclosed_and_the_exception_is_narrow(self):
        for name in EXAMPLES:
            p = page(name)
            for section in set(p.sections) & DEMO_SECTIONS:
                with self.subTest(example=name, section=section):
                    self.assertTrue(p.labels.get(section, "").strip())
        coffee = page("coffee").labels
        self.assertIn("Scripted demonstration", coffee["assistant"])
        self.assertIn("not a live", coffee["assistant"])
        self.assertIn("Concept product film", coffee["teaser"])
        self.assertIn("Proposed", coffee["compare"])
        css = (SECTIONS / "toolkit.css").read_text()
        self.assertNotRegex(css, r"\.tk-label[^{]*\{[^}]*display:\s*none")
        pack = " ".join(read("knowledge/engagement/DECISION_PACK.md").split())
        for phrase in ("no presenter notes or controls", "Toolkit exception",
                       "templates/sections", "Every other customer page rule stands"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, pack)

    def test_AC_TOOLKIT_5_claims_proof_counts_and_unknowns(self):
        banned = (r"guarantee", r"\bROI\b", r"savings", r"visibility score", r"score of",
                  r"rating will", r"live MCP connection is", r"never sleeps", r"AI-powered",
                  r"all-in-one", r"set it and forget it", r"24/7", r"Learn more",
                  r"review management tool", r"\bSEO\b", r"[\u2013\u2014]")
        for name in EXAMPLES:
            body = text(name)
            for pattern in banned:
                with self.subTest(example=name, pattern=pattern):
                    self.assertNotRegex(body, re.compile(pattern, re.I))
            with self.subTest(example=name, check="unknown"):
                self.assertIn("Unknown", body)
        card = " ".join(read("knowledge/proof/SPECIALTY_COFFEE_TWO_CAFES.md").split())
        quote = re.search(r'<blockquote class="tk-quote"[^>]*>\s*<p>(.*?)</p>',
                          (SECTIONS / "coffee.html").read_text(), re.S).group(1)
        self.assertIn(" ".join(quote.split()), card)
        counts = json.loads(read("reference/directories/directories.json"))["counts"]
        coffee = text("coffee")
        self.assertIn(f"{counts['destinations']} destinations", coffee)
        self.assertIn(f"{counts['inactive']} marked inactive", coffee)
        for name in EXAMPLES:
            p = page(name)
            if not p.cards:
                continue
            stated = re.search(r"(\d+) unique", p.labels["reviews"])
            with self.subTest(example=name):
                self.assertIsNotNone(stated)
                self.assertEqual(int(stated.group(1)), len(p.cards))
                self.assertEqual(len(set(p.cards)), len(p.cards))

    def test_AC_TOOLKIT_6_film_stays_private_and_traced(self):
        public = [p for p in ROOT.rglob("*") if p.is_file()
                  and not {".git", "out", "node_modules"} & set(p.relative_to(ROOT).parts)
                  and p.suffix.lower() in {".mp4", ".mov", ".webm"}]
        self.assertEqual(public, [])
        self.assertEqual(sorted(f.name for f in FILM.iterdir()), ["DESCRIPTION.md", "README.md"])
        readme = (FILM / "README.md").read_text()
        for digest in (HELD_RENDITION,
                       "99d690e2953e0f7ddb2b960e999f9a9e86975635fa728b99a8ee5ec6bcd4e16a",
                       "d56eaf5ecccdf210f69130667f8236f285b2e65257e1f5bcdc99c8598ae595c1"):
            self.assertIn(digest, readme)
        for phrase in ("Approval needed", "restaurant", "hotel", "photo", "audio"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, readme)
        self.assertNotRegex(readme, r"/Users/|[\u2013\u2014]")
        for name in EXAMPLES:
            body = (SECTIONS / f"{name}.html").read_text()
            with self.subTest(example=name):
                self.assertNotIn("<video", body)
                self.assertNotIn("obenan-concept-film-qr", body)
        self.assertIn("data-film", (SECTIONS / "coffee.html").read_text())

    def test_AC_TOOLKIT_6_build_refuses_an_unrecorded_film(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "film"
            fake.mkdir()
            (fake / "obenan-concept-film-720p.mp4").write_bytes(b"not the reviewed film")
            (fake / "obenan-concept-film-poster.jpg").write_bytes(b"not a poster")
            result = build("coffee", Path(tmp) / "site", "--film-dir", str(fake))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("checksum", result.stderr)
            self.assertFalse((Path(tmp) / "site" / "index.html").exists())

    def test_AC_TOOLKIT_6_build_without_film_leaves_the_teaser_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = build("coffee", Path(tmp) / "site")
            self.assertEqual(result.returncode, 0, result.stderr)
            html = (Path(tmp) / "site/index.html").read_text()
            self.assertNotIn('data-section="teaser"', html)
            self.assertNotIn("<video", html)
            self.assertIn('data-section="assistant"', html)

    def test_AC_TOOLKIT_6_build_with_the_held_film_loads_it_politely(self):
        if not (HELD_FILM / "obenan-concept-film-720p.mp4").exists():
            self.skipTest("held film not supplied on this machine; set TOOLKIT_FILM_DIR")
        with tempfile.TemporaryDirectory() as tmp:
            result = build("coffee", Path(tmp) / "site", "--film-dir", str(HELD_FILM))
            self.assertEqual(result.returncode, 0, result.stderr)
            html = (Path(tmp) / "site/index.html").read_text()
            video = re.search(r"<video[^>]*>", html).group(0)
            self.assertIn('preload="none"', video)
            self.assertIn("controls", video)
            self.assertIn("poster=", video)
            self.assertNotIn("autoplay", video)
            self.assertIn('class="tk-poster"', html)

    def test_AC_TOOLKIT_11_built_examples_are_self_contained(self):
        for name in EXAMPLES:
            with self.subTest(example=name), tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "site"
                result = build(name, out)
                self.assertEqual(result.returncode, 0, result.stderr)
                for page in out.rglob("*.html"):
                    html = page.read_text()
                    self.assertNotRegex(html, r"/Users/|file:|\.\./")
                    for ref in local_refs(html):
                        target = (page.parent / ref.split("#")[0]).resolve()
                        self.assertTrue(target.is_file(), f"{page.name}: {ref}")
                        self.assertTrue(target.is_relative_to(out.resolve()), ref)
                for f in out.rglob("*"):
                    if f.suffix in {".md", ".css", ".js"}:
                        self.assertNotRegex(f.read_text(), r"/Users/", f.name)

    def test_AC_TOOLKIT_8_and_9_browser_check_is_present_and_documented(self):
        script = (ROOT / "scripts/check_toolkit_browser.cjs").read_text()
        for check in ("overflow", "currentTime", "replay", "reduced-motion", "no-js",
                      "fast-scroll", "keyboard", "Unknown", "1.10", "pdf", "jsQR"):
            with self.subTest(check=check):
                self.assertIn(check, script)
        self.assertIn("node scripts/build_toolkit_example.cjs", read(DOC))

    def test_AC_TOOLKIT_7_business_case_inputs_start_empty(self):
        for name in EXAMPLES:
            body = (SECTIONS / f"{name}.html").read_text()
            for tag in re.findall(r"<input[^>]*>", body):
                with self.subTest(example=name, tag=tag):
                    self.assertNotRegex(tag, r'\svalue="[^"]')
        js = (SECTIONS / "toolkit.js").read_text()
        self.assertIn("BigInt", js)
        self.assertNotIn("parseFloat", js)
        self.assertNotIn("innerHTML", js)

    def test_AC_TOOLKIT_10_pinned_templates_unchanged(self):
        pins = {
            "templates/deck/DECK_SKELETON.html":
                "9353847caf985db6fb1569b349fd4d84e654b19375e9be29f0cd28e4cc35c0a7",
            "templates/deck/EXISTING_CLIENT_REVIEW.html":
                "c4de4ed1197f3bfdbe4f7c9e66783cfdfaec2db7129f55664c335eb3b9596360",
        }
        for path, digest in pins.items():
            self.assertEqual(sha256((ROOT / path).read_bytes()).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main()
