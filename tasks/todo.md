# Existing-client review standard

Acceptance criteria, 8 October 2026:

- URL-only agents route Reporting and existing-client Upsell through one review playbook.
- A ten-page A4 template follows the supplied customer-first reference, not a generic pitch.
- Discovery classification, activation date, matched prior-year window, stale scores and review growth have executable negative tests.
- Delivered work and estimated effort are separate from scheduled work; no false time-saving floor.
- Customer-facing performance pages exclude pricing, partner names and internal history.
- Approved anonymous aggregate proof is usable; naming permission is independent.
- Public-safety checks, unit tests and all ten rendered pages pass before review.
- Work stays on a branch and review PR. No customer send or main-branch push.

Progress:

- [x] Read reference prompt, source evidence and all ten reference PDF pages.
- [x] Confirm aggregate publication permission with Seven; naming remains pending.
- [x] Record failing regression tests before implementation: 16 initial tests failed (1 routing failure, 15 missing-implementation errors). Later malformed-input tests also failed before repair.
- [x] Implement routing, playbook, template, methods and proof permissions.
- [x] Validate: 20 tests pass; public-safety/link scan and diff whitespace check pass. A4 output has ten pages, all inspected; dollars preserved. Customer builds remain ignored/private.
- [x] Submit [draft PR 1](https://github.com/obenan-dashboard/obenan-sales-workspace/pull/1) and attach it to this chat. Main unchanged; no customer send. Shared-project refresh and URL-only experiment follow approval/merge.

# Named customer proof and LPQ testimonial

Acceptance criteria, 9 October 2026:

- Record Seven's explicit permission to publish named success stories; do not confuse it with
  permission to expose raw records, photos, logos or unrelated quotes.
- Store LPQ's supplied transcript once, with the public video, chapter timestamps and Joost's
  role at recording. Lead prospect PDF proof with his exact technology quote.
- Keep early pilot observations, rollout ambitions and conditional staffing estimates distinct
  from verified outcomes. Do not treat historical interview statements as current capabilities.
- Make the card discoverable from the agent entry point and generic deck; preserve the
  discovery-first, customer-first existing-client reporting standard.
- Preserve existing metrics and filenames. Update named Campos approval without inventing
  customer-signed permission. Check quotes against the original supplied transcript.
- Validate tests, public safety, local links and whitespace. Local branch only; no send or push.

Progress:

- [x] Read the entire supplied transcript and approval. Public video fetch is unavailable;
  quote verification uses the supplied transcript, not claimed playback.
- [x] Record test-first failures: all four new editorial checks failed before implementation
  (one failed retrieval assertion and three missing-card/approval errors).
- [x] Update proof records, retrieval instructions and the generic testimonial page.
- [x] Validate: 27 tests pass; public-safety/local-link scan and whitespace checks pass.
  Full stored transcript matches the attachment after timestamp/whitespace normalization.
  Generic template remains eight A4 pages; changed quote page inspected with no clipping.
  Exact quotation survives PDF text extraction; video link survives as a PDF annotation.
  These checks establish source/template consistency, not guaranteed future agent behavior.
  No commit, push, customer send or shared-project refresh.
