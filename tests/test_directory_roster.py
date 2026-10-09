"""The directory roster mirror: every destination, its logo, its live links and the homepage map."""

from hashlib import sha256
from pathlib import Path
import json
import re
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1]
LOGOS = ROOT / "assets/directory-logos"
DATA = ROOT / "reference/directories/directories.json"
LISTING = ROOT / "reference/directories/DIRECTORY_ROSTER.md"
ROSTER = "https://www.obenan.ai/directories-and-platforms/"
GUIDES = {
    "GOOGLE": "google", "APPLE_MAPS": "apple-maps", "BING": "bing", "YELP_API": "yelp",
    "FACEBOOK": "facebook", "TRIP_ADVISOR": "tripadvisor", "CYLEX": "cylex", "FIND_OPEN": "cylex",
}
HOMEPAGE_SURFACES = [
    "GOOGLE_MAPS", "APPLE_MAPS", "BING", "YELP_API", "TRIP_ADVISOR", "FACEBOOK", "INSTAGRAM",
    "NOKIA_HERE", "TOMTOM", "FOURSQUARE", "WAZE", "ALEXA", "UBER", "NEXT_DOOR", "MAP_QUEST",
    "YELLOW_PAGES", "INFOBEL", "CYLEX", "MEINESTADT", "NAVMII",
]


def roster():
    return json.loads(DATA.read_text())


def logo_records():
    return re.findall(r"^\| \[([^]]+)\]\(([A-Z0-9_]+\.png)\) \| `([a-f0-9]{64})` \| (.+) \|$",
                      (LOGOS / "README.md").read_text(), re.M)


def listing_rows():
    return re.findall(
        r'^\| <img src="\.\./\.\./assets/directory-logos/([A-Z0-9_]+)\.png" width="24" '
        r'height="24" alt="([^"]+)"> \| \[([^]]+)\]\(([^)]+)\) \| (Sent by interface|Sent by export) '
        r"\| (.*) \|$", LISTING.read_text(), re.M)


def png_size(path):
    head = path.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", head[16:24])


class DirectoryRosterTests(unittest.TestCase):
    def test_roster_holds_104_unique_destinations_with_public_counts(self):
        data = roster()
        rows = data["destinations"]
        self.assertEqual(len(rows), 104)
        self.assertEqual(len({row["key"] for row in rows}), 104)
        self.assertEqual(sum(not row["inactive"] for row in rows), 100)
        self.assertEqual(sum(row["connection"] == "interface" for row in rows), 90)
        self.assertEqual(sum(row["connection"] == "export" for row in rows), 14)
        self.assertEqual(data["counts"], {"destinations": 104, "active": 100, "inactive": 4,
                                          "sentByInterface": 90, "sentByExport": 14})

    def test_no_per_destination_capability_claims_are_exported(self):
        for row in roster()["destinations"]:
            with self.subTest(key=row["key"]):
                for word in ("review", "repl", "question", "post", "updating"):
                    self.assertFalse(any(word in field.lower() for field in row), row)

    def test_every_destination_links_to_its_live_roster_letter(self):
        for row in roster()["destinations"]:
            with self.subTest(key=row["key"]):
                letter = re.sub(r"^[^A-Za-z0-9]+", "", row["name"])[:1].upper()
                self.assertEqual(row["letter"], letter if re.fullmatch(r"[A-Z]", letter) else "#")
                self.assertEqual(row["rosterUrl"], f"{ROSTER}#roster-{row['letter']}")

    def test_guide_links_match_the_published_platform_guides(self):
        guides = {row["key"]: row["guideUrl"] for row in roster()["destinations"] if row["guideUrl"]}
        self.assertEqual(guides, {key: f"{ROSTER}{slug}/" for key, slug in GUIDES.items()})

    def test_shared_records_name_their_parent(self):
        rows = roster()["destinations"]
        keys = {row["key"] for row in rows}
        for row in rows:
            with self.subTest(key=row["key"]):
                self.assertEqual(row["parentKey"] is None, row["sharesRecordWith"] is None)
                if row["parentKey"] in keys:
                    parent = next(r for r in rows if r["key"] == row["parentKey"])
                    self.assertEqual(row["sharesRecordWith"], parent["name"])

    def test_every_destination_has_exactly_one_logo_matching_recorded_bytes(self):
        records = logo_records()
        keys = {row["key"] for row in roster()["destinations"]}
        self.assertEqual(len(records), 104)
        self.assertEqual({file for _, file, _, _ in records}, {f"{key}.png" for key in keys})
        self.assertEqual({p.name for p in LOGOS.iterdir() if p.name != "README.md"},
                         {f"{key}.png" for key in keys})
        names = {row["key"]: row["name"] for row in roster()["destinations"]}
        for name, file, digest, _ in records:
            with self.subTest(file=file):
                self.assertEqual(name, names[file[:-4]])
                self.assertEqual(sha256((LOGOS / file).read_bytes()).hexdigest(), digest)
                size = png_size(LOGOS / file)
                self.assertIsNotNone(size)
                self.assertEqual(size[0], size[1])
                self.assertGreaterEqual(size[0], 64)
        for row in roster()["destinations"]:
            self.assertEqual(row["logo"], f"assets/directory-logos/{row['key']}.png")

    def test_listing_shows_every_destination_once_with_logo_and_live_link(self):
        rows = {row["key"]: row for row in roster()["destinations"]}
        listed = listing_rows()
        self.assertEqual(len(listed), 104)
        self.assertEqual({key for key, *_ in listed}, set(rows))
        for key, alt, name, url, connection, notes in listed:
            with self.subTest(key=key):
                row = rows[key]
                self.assertEqual((alt, name, url), (row["name"], row["name"], row["rosterUrl"]))
                self.assertEqual(connection, f"Sent by {row['connection']}")
                self.assertEqual("Inactive in the roster" in notes, row["inactive"])
                if row["sharesRecordWith"]:
                    self.assertIn(f"Shares the {row['sharesRecordWith']} record", notes)
                if row["guideUrl"]:
                    self.assertIn(f"]({row['guideUrl']})", notes)

    def test_homepage_channel_map_is_kept_with_its_twenty_surfaces(self):
        data = roster()
        home = data["homepage"]
        self.assertEqual(home["url"], "https://www.obenan.ai/")
        self.assertEqual(home["surfaces"], HOMEPAGE_SURFACES)
        self.assertEqual(home["moreDirectories"], data["counts"]["active"] - len(HOMEPAGE_SURFACES))
        flagged = [row["key"] for row in data["destinations"] if row["homepageSurface"]]
        self.assertEqual(set(flagged), set(HOMEPAGE_SURFACES))
        for image in home["images"]:
            with self.subTest(image=image):
                self.assertIsNotNone(png_size(ROOT / image))
                self.assertIn(Path(image).name, LISTING.read_text())


if __name__ == "__main__":
    unittest.main()
