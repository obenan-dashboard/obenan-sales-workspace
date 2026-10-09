"""The agentic closing pair is locked copy in every deck template."""

from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ("templates/deck/EXISTING_CLIENT_REVIEW.html", "templates/deck/DECK_SKELETON.html")
FILM = "https://www.youtube.com/watch?v=9WCTYK-iHb0"
LOCKED = (
    "Soon, AI agents will book, order and pay. Get your locations ready for the questions "
    "and actions they bring.",
    "See it in three minutes.",
    "Visa secures the payment.",
    "Obenan gets the business ready to take the order.",
    "Confirms it's really the customer, swaps the card for a secure agent token, and checks "
    "every instruction before any money moves.",
    "Does the work on the business side: a menu and products the agent can read, a cart with "
    "the confirmed total, and the order delivered into the business's own checkout, ready to fulfil.",
    "Agent-led transactions are pilot-stage.",
    "Obenan does not process payments.",
)


class Sections(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages, self.links = [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section" and "page" in attrs.get("class", "").split():
            self.pages.append(attrs.get("data-page"))
        if tag == "a":
            self.links.append(attrs.get("href"))


def parse(path):
    parser = Sections()
    parser.feed((ROOT / path).read_text())
    return parser


class ClosingPairTests(unittest.TestCase):
    def test_every_deck_carries_the_locked_copy(self):
        for path in TEMPLATES:
            text = " ".join(unescape((ROOT / path).read_text()).split())
            for line in LOCKED:
                with self.subTest(template=path, line=line):
                    self.assertIn(line, text)

    def test_film_is_a_clickable_link_on_every_deck(self):
        for path in TEMPLATES:
            with self.subTest(template=path):
                self.assertGreaterEqual(parse(path).links.count(FILM), 2)

    def test_pair_closes_the_review_and_precedes_the_prospect_decision(self):
        self.assertEqual(parse(TEMPLATES[0]).pages[-2:], ["next", "film"])
        self.assertEqual(parse(TEMPLATES[1]).pages[-3:], ["next", "film", "decision"])

    def test_film_thumbnail_is_linked_not_stored(self):
        stored = [p for p in (ROOT / "assets").rglob("*") if "9WCTYK" in p.name or "visa" in p.name.lower()]
        self.assertEqual(stored, [])


if __name__ == "__main__":
    unittest.main()
