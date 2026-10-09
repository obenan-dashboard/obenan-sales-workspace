# Status

What in this repository is settled, what is carried with a caveat, and what is open.

Last updated: 2026-10-09.

## Settled

- **Sanitized for team use on 2026-10-05.** The house voice playbook, the worked example and
  the deck skeleton were originally written against real accounts. Contacts, introducers,
  account IDs, cities and uncleared customer names were removed or replaced with placeholders.
  The craft and the reasoning were kept.

- **Published for public read access on 2026-10-06.** Real account identifiers, unapproved
  metrics, internal customer structure, security observations and partner-confidential names
  were removed. Approved Le Pain Quotidien metrics remain governed by the public proof
  register.

- Public-safety and local-link validation runs on every push to `main` and on pull requests.

- The four engagement modes and their spines (`knowledge/engagement/ENGAGEMENT_MODES.md`).
- The MCP evidence sequence (`knowledge/engagement/MCP_EVIDENCE_RUNBOOK.md`), proven against a
  live account.
- Language and claim boundaries (`knowledge/product/LANGUAGE_AND_CLAIM_BOUNDARIES.md`).
- The sales-craft modules, adapted from Wolfgang's playbook on 2026-10-05. The personal
  Wolfgang voice files are optional calibration, never a default sender identity.
- The deck skeleton, derived from a shipped A4 deck.
- The proposal generator now follows the public design canon: ink rather than pure black, one
  accent color, no decorative gradient and more than 100 supported destinations.

## Review-standard change set

- Existing-client Reporting and Upsell now route through one discovery-first playbook and
  ten-page A4 template, based on the operator-selected results review.
- The template reuses the supplied Obenan closing component, with an explicit illustration
  and pilot-stage boundary. Customer photos and source PDFs remain private.
- 9 October: both deck templates end on the locked agentic closing pair, What comes next and
  the public agentic-commerce film page. The results review is now eleven pages; the prospect
  deck is ten. See `knowledge/engagement/AGENTIC_CLOSING.md`.
- Regression tests check brand reclassification, dates, historical scores, review growth,
  delivered work and mandatory routing. Consistency checks cannot independently verify
  sources or guarantee an agent follows the narrative; human copy and visual review remain.
- Seven approved specialty-coffee aggregates on 8 October and named success stories on
  9 October. Campos Coffee's dated card preserves both growth and declines; scheduled work
  and inferred automation are labelled. Campos logos, quotes and images remain pending.
- The review's orange accent and stronger headline weights are a bounded template exception,
  not a replacement for the general brand system.
- [PR 1](https://github.com/obenan-dashboard/obenan-sales-workspace/pull/1) merged on 8 October.
  This is repository delivery, not evidence of a customer send or shared Claude project refresh.

## Named-proof change set

- Seven confirmed Joost's testimonial approval on 9 October. The LPQ proof card stores the
  supplied complete transcript, exact excerpts, timestamps and historical-scope boundaries.
- Prospect proof pages lead with Joost's technology quote. Existing-client reviews still
  lead with that customer's own discovery evidence. LPQ metrics are unchanged.
- Naming approval is recorded per customer, not assumed from anonymization. Raw records and
  unapproved imagery remain private. Reviewed and approved on 9 October; no customer send.

## Carried with a caveat

- **Two voices live side by side.** `HOUSE_VOICE.md` is Obenan's. The Wolfgang files are a
  personal and German SME module. Pick one per deliverable. This is a convention, not a guard.
- **Product UI coverage is intentionally bounded.** The public repository contains a
  sales-safe overview, not route maps, customer counts, security findings or internal audits.

## Open

- **Logo authority.** The design workspace records logo authority as unresolved. This
  repository ships the canonical marks used on the website and on shipped decks, and keeps the
  legacy marks separately. Founder decision.

- Whether SME proposals are a deliberate design exception with their own register, or should
  converge on the main design principles. Founder decision.
- External agencies and resellers must use per-account or otherwise least-privileged MCP access.
  Agency-wide credentials are not approved for public-repository users.
- Whether `knowledge/sales/` should gain short working versions of The Diamond, SKINN and SSP.
  The long-form sources live in the private workspace and are deliberately not copied here.
