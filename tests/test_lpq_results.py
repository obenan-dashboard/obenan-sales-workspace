"""Curated proof consistency, not independent revalidation of source-system data."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def rows(card):
    result = {}
    for line in card.splitlines():
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells and cells[0] in {
            'Google views', 'Direction requests', 'Website clicks', 'Call clicks',
            'Menu clicks', 'Booking actions', 'Food-order actions', 'Conversations', 'Total actions',
            'Automatic review replies', 'Profile post publications', 'Reports delivered'}:
            result[cells[0]] = [None if c == 'Not recorded' else int(c.replace(',', ''))
                                for c in cells[1:5]]
    return result


class LPQResultsTests(unittest.TestCase):
    def setUp(self):
        self.card = (ROOT / 'knowledge/proof/LE_PAIN_QUOTIDIEN.md').read_text()

    def test_dated_totals_reconcile_to_annual_components(self):
        r = rows(self.card)
        expected = {
            'Google views': 189905522, 'Direction requests': 3373300,
            'Website clicks': 1396645, 'Call clicks': 386454,
            'Menu clicks': 715614, 'Booking actions': 737,
            'Food-order actions': 13075, 'Conversations': 10, 'Total actions': 5885835,
            'Automatic review replies': 67452, 'Profile post publications': 128096,
            'Reports delivered': 28729,
        }
        self.assertEqual(set(r), set(expected))
        for label, total in expected.items():
            with self.subTest(label=label):
                self.assertEqual(r[label][3], total)
                self.assertEqual(sum(x for x in r[label][:3] if x is not None), total)
        components = ['Direction requests', 'Website clicks', 'Call clicks',
                      'Menu clicks', 'Booking actions', 'Food-order actions', 'Conversations']
        for i in range(4):
            self.assertEqual(sum(r[k][i] for k in components), r['Total actions'][i])
        self.assertIn('1 September 2023 to 31 August 2026', self.card)
        self.assertIn('213 profiles across 20 countries', self.card)
        self.assertIn('2026-09-25', self.card)

    def test_search_correction_is_scoped_not_complete_audit(self):
        self.assertIn('93,541,653', self.card)
        self.assertIn('116,551,232', self.card)
        self.assertIn('659,649', self.card)
        self.assertIn('79.7%', self.card)
        self.assertAlmostEqual(100 * (93541653 - 659649) / 116551232, 79.7, delta=.05)
        self.assertIn('top 50 keywords', self.card)
        self.assertIn('not a full-query audit', self.card)
        self.assertIn('not the share of actions', self.card)

    def test_growth_keeps_denominators_gaps_and_declines(self):
        for wording in ['175 same-store profiles', '160 restaurants', '125 restaurants',
                        '9.2%', '26.4%', 'April and May 2024',
                        'Website and call clicks fell', 'not causal attribution']:
            self.assertIn(wording, self.card)
        values = re.search(r'\| Same-store website and call clicks \| ([\d,]+) \| ([\d,]+) \|', self.card)
        self.assertIsNotNone(values)
        before, after = (int(v.replace(',', '')) for v in values.groups())
        self.assertEqual((before, after), (634970, 538308))
        self.assertLess(after, before)

    def test_models_are_not_financial_outcomes(self):
        for phrase in ['not actual ad spend', 'not incremental revenue',
                       'not a guaranteed lower bound', 'not measured labor savings',
                       'not financial ROI', 'not unique guests']:
            self.assertIn(phrase, self.card)
        self.assertAlmostEqual((67452 * 3 + 128096 + 28729 * 5) / 60, 7902, delta=1)
        self.assertIn('historical, differently scoped', self.card)

    def test_ad_model_keeps_the_unrounded_search_fraction(self):
        self.assertIn('93,541,653 / 116,551,232', self.card)
        self.assertEqual(round(5885835 * (93541653 / 116551232) * 2.05 / 1.1104), 8721088)
        self.assertNotEqual(round(5885835 * .8026 * 2.05 / 1.1104), 8721088)

    def test_current_retrieval_does_not_repeat_superseded_export(self):
        voice = (ROOT / 'knowledge/voice/HOUSE_VOICE.md').read_text()
        register = (ROOT / 'knowledge/proof/PUBLIC_PROOF_REGISTER.md').read_text().split('### Campos Coffee')[0]
        self.assertNotIn('6.2 million', voice)
        self.assertNotIn('6.2 million', register)
        self.assertIn('LE_PAIN_QUOTIDIEN.md', voice)
        self.assertIn('LE_PAIN_QUOTIDIEN.md', register)


if __name__ == '__main__':
    unittest.main()
