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

# Website customer logos and merged-change review

Acceptance criteria, 9 October 2026:

- Review merged PRs 2 and 3 against current source, CI and fresh tests; report guardrail
  failures separately from content errors. Do not silently rewrite locked closing copy.
- Copy exactly the nine founder-authorized Demo logos, byte-for-byte, from the website repo.
  Record source commit, public paths, checksums and Seven's reuse approval in one asset index.
- Make logos available to URL-only agents and use a static, uncropped logo group on the
  prospect proof page. Keep the reporting template customer-first and page counts unchanged.
- Customer information Seven explicitly stores for public sharing is usable named proof,
  not a privacy blocker. Keep unapproved source records, contacts and credentials separate.
- Test asset integrity, SVG safety and template image/alt coverage before implementation.
  Check changed and closing pages in rendered PDFs and preserve readable links.
- Website source stays read-only. Local sales branch only; no push, send or deployment.

Progress:

- [x] Verify PRs 2 and 3 merged; main CI succeeds at 8fecd01. Fresh baseline: 31 tests pass.
- [x] Reproduce two validation gaps in an isolated source copy: fragment-based partner
  allowlisting accepts an unrelated endorsement claim; raw-HTML copy tests accept approved
  text hidden in comments. These are enforcement gaps, not evidence the current copy is wrong.
- [x] Record failing logo tests: two missing-index errors and one missing-template-image
  failure before implementation. Add exact assets, approval, retrieval and static print layout.
- [x] Verify all nine source hashes against live public assets, with byte-for-byte matches.
  Website checkout remains unchanged. All 34 tests, public safety/local links and whitespace
  checks pass. Prospect/review renders remain 10/11 A4 pages. Inspect prospect proof page 7,
  closing pages 8/9 and review closing pages 10/11; assets and film thumbnails are visible,
  footer bounds remain within the page, and PDF link annotations survive.
  The two merged validation gaps remain outstanding; no change to locked closing wording.
  No commit, push, deployment, customer send or shared-project refresh.

# LPQ three-year success story publication

Acceptance criteria, 9 October 2026:

- Read the supplied Intelligence route and its pinned source artifact; reconcile it with
  the original LPQ evidence pack. Record source hash, measurement periods and retrieval date.
- Publish approved, named aggregate proof in the existing LPQ card. Keep the transcript once.
  Lead with discovery and measured actions, not reviews or modeled financial return.
- Preserve annual denominators, brand-classification coverage, missing Google months,
  menu-reporting changes and the negative same-store results. Label estimates as estimates.
- Supersede older, differently scoped figures without silently deleting their history.
  Do not publish raw records, credentials, contact details or invoices.
- Add tests before the card update, including period reconciliation and misleading-copy
  negative cases. Keep pending logo changes and unchanged template page counts.
- Validate, independently review, push a PR and merge eligible green checks under Seven's
  explicit publication instruction. Intelligence and website sources remain read-only.

Progress:

- [x] Fresh baseline: 34 tests pass. Intelligence source at e558d0a matches the local
  artifact byte for byte and its recorded SHA-256. Live route returns the email-verification
  gate; no authenticated live-story verification is claimed.
- [x] Five new tests failed before the card update. The arithmetic check then detected the
  omitted conversations; restore the ten from the saved E01 aggregate. Independent review
  caught rounding in the ad formula; add a failing regression and replace the rounded share
  with its exact fraction. Curated proof, source custody and retrieval updates are complete.
- [x] Independent source/diff review has no remaining new blockers. All 40 tests, public
  safety/local links and whitespace checks pass. Existing 10/11-page template renders and
  unchanged logo layout remain verified. The two prior guardrail gaps remain documented.
- [ ] Validate, review, push and merge the sales repository change set.
