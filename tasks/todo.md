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
- [x] Push the validated, reviewed change set and submit
  [PR 4](https://github.com/obenan-dashboard/obenan-sales-workspace/pull/4) for Seven-authorized
  publication. Its exact-head checks and merged state are recorded in GitHub; these
  preparatory records do not claim a website deployment or customer send.

# LPQ video preview

Acceptance criteria, 9 October 2026:

- Every surface shows Joost's interview as a preview: Seven's approved still with a play
  icon, the whole image linked to the 2:24 moment. Never a text-only panel or placeholder.
- Keep the QR code idea from the other agent's rendering: "Scan to watch" beside the
  preview, plus the printed URL, for readers on paper. The QR never replaces the preview.
- Store one canonical still with the icon baked in and one QR SVG, with checksums, source
  and the decoded destination. Record the narrow still approval in the proof register.
- Bind the rule in the LPQ card, entry point and asset library; the prospect deck carries
  the block for agents to copy. Tests fail before implementation.
- Validate tests, public safety, links and the rendered A4 page; PR and merge under Seven's
  instruction to ship it to the repo.

Progress:

- [x] Three new tests failed before implementation (1 failure, 2 errors).
- [x] Still cropped to 16:9 at 1600 x 900 with the deck's play-icon geometry; QR generated
  as SVG and decoded back to the 2:24 URL.
- [x] Validate: 51 tests pass; public safety, local links, whitespace and dash scans pass.
  Prospect deck stays ten A4 pages; page 7 inspected: still, centred icon and QR visible,
  QR decoded from the rendered page, and the PDF link annotation opens 2:24.
- [x] Submit [PR 6](https://github.com/obenan-dashboard/obenan-sales-workspace/pull/6) and merge
  on a green validate check, under Seven's instruction to ship the rule to the repo.

# Urban Fork Group success story

Acceptance criteria, 12 October 2026:

- AC-URBAN-1: Publish one named card for the supplied 12-location Google portfolio,
  comparing April to September 2025 with the same months in 2026. Preserve all table values.
- AC-URBAN-2: Check rounded growth, absolute increases and impression totals. Preserve
  the reported interaction total and disclose the unresolved seven-action baseline gap.
- AC-URBAN-3: Lead with reported bookings and Maps visibility. Do not equate clicks with
  completed calls, direction requests with visits, bookings with fulfilled reservations,
  or growth with causal revenue. Do not imply action-to-impression efficiency improved.
- AC-URBAN-4: Preserve the supplied aggregate screenshot unchanged with its checksum.
  Separate summary-supplied location count from image-backed figures. Geography, activation
  date, stable same-store coverage and source-system definitions are unverified.
- AC-URBAN-5: Record Seven's publication approval and scoped asset permissions; link one
  canonical card from the proof index and entry point. Keep other stories/templates intact.
- AC-URBAN-6: Add failing tests first, verify the input/output and claim matrix, obtain
  independent review, then push a PR and merge only after exact-head checks pass. No customer
  send, customer-account write, website deployment or unrelated change.

Progress:

- [x] Confirm clean main at fa19425; baseline 58 tests pass. Seven authorized publication
  after being informed of the baseline discrepancy. Publish with that limitation, not a
  fabricated reconciliation.
- [x] Write seven regression tests before implementation; first run failed with seven
  missing-card errors. Add card/source/approval and retrieval links. Full suite now passes
  65 tests; public-safety/local-link and whitespace checks pass. Missing or corrupted
  booking rows cannot match the approved values. The source image checksum matches.
  Requirements review caught that the opening still led with total impressions. Add a
  failing first-sentence regression, then lead with reported bookings and Maps impressions.
- [x] Run all checks and independent review. All 65 tests, public-safety/local-link and
  whitespace checks pass. Evidence, public-safety and requirements reviews approve the
  documentary change. Nine adverse artifact/source mutations were rejected in review.
- [x] Prepare the validated change set for Seven-authorized publication through a PR.
  Merge requires green exact-head checks; GitHub is the authority for final release state,
  not this preparatory record. AC-to-test coverage was mapped manually; the shared helper
  checks zero criteria in this task-file format and is not traceability proof.

# Frisby Colombia success story

Acceptance criteria, 12 October 2026:

- AC-FRISBY-1: Store one named proof card for 213 Colombian locations, comparing April to
  September 2026 with October 2025 to March 2026. Preserve all supplied table values.
- AC-FRISBY-2: Reconcile impressions, interaction components, absolute increases, rounded
  growth and the interactions-per-impression ratio against the supplied screenshot.
- AC-FRISBY-3: Lead with Google visibility and measured actions. Call clicks are not
  completed calls; direction requests are not verified visits. Do not claim causality,
  unique guests, revenue, nonbrand discovery or a year-on-year comparison.
- AC-FRISBY-4: Preserve the supplied aggregate screenshot unchanged with its checksum.
  Separate screenshot-backed figures from the colleague-reported mobile breakdown and
  location count. Source-system refresh, activation date and same-store coverage are unknown.
- AC-FRISBY-5: Record Seven's public name/metrics/source-image approval, asset boundaries,
  measurement window and review date. Link the canonical story from the proof index and
  agent entry point. No duplicate metrics in playbooks or private handoffs.
- AC-FRISBY-6: Preserve prior stories and templates; pass all tests, public-safety/local-link
  validation and diff checks. Independently review, push a PR and merge green checks under
  Seven's instruction. Log a pointer in the private sales-harness without committing its
  unrelated changes. No customer send, website deployment or customer-account mutation.

Progress:

- [x] Read approval and source; existing baseline: 51 tests pass.
- [x] Record new failing regression tests before adding the story: seven missing-card errors.
- [x] Add the canonical card, source screenshot, approvals and retrieval links.
- [x] Verify arithmetic, source integrity, scope, compatibility and public safety: 58 tests
  pass; public-safety/local-link validation and diff whitespace pass. Independent evidence
  and public-safety reviews approve the change. Requirements review found that a corrupted
  ratio row escaped the tests; add the missing assertion against the stored row. Manual
  AC-to-test mapping is in test names; the shared spec helper does not parse this task format.
  All three independent reviews now approve; missing and corrupted ratio rows fail validation.
- [x] Independently review, push [PR 7](https://github.com/obenan-dashboard/obenan-sales-workspace/pull/7)
  and log the private pointer. Seven authorized merge after exact-head CI passes. GitHub
  is the authority for the final merge state; this preparation record does not assert it.

# Country account index

Acceptance criteria, 13 October 2026:

- AC-COUNTRY-1: Publish one canonical JSON index with brand and country only. No account
  identifiers, location counts, contacts, status fields, raw exports or query text.
- AC-COUNTRY-2: Normalize country aliases and deduplicate brand-country pairs. Retain
  accents and source account display names. Do not invent countries for missing values.
- AC-COUNTRY-3: Country is the location market, not account headquarters or whole-chain
  coverage. Preserve multiple countries per account. Exclude own/internal and unverified
  personal labels; hold country conflicts privately.
- AC-COUNTRY-4: Record Seven's explicit names-and-countries publication approval, dated
  source, review date, asset limits and retrieval instructions for country-specific decks.
- AC-COUNTRY-5: Preserve prior stories/templates, pass existing tests and public safety,
  independently review the documentary change and publish through a green pull request.

Progress:

- [x] Inspect read-only SQL scope and receive the full 556-row CSV export.
- [x] Record failing artifact checks before adding the index: four missing-file errors.
- [x] Normalize and reconcile privately; add approved public extract and retrieval links.
- [x] Verify source reconciliation and public scope: 70 tests, public-safety/local-link
  validation and diff checks pass. Evidence, public-safety and requirements reviews approve.
  Requirements review exposed missing corruption checks; canonical country validation and
  a reviewed-snapshot pin now reject invented countries, held personal labels, private
  fields, duplicates, aliases, email labels, missing rows and plausible wrong markets.
- [x] Prepare the independently reviewed branch for publication. Seven authorized the
  public index; merge only after exact-head CI passes. GitHub is the authority for final
  publication; this preparation record does not assert a merge.

# White-label screens

Acceptance criteria, 14 October 2026:

- AC-WL-1: Store six captures of the live agency instance supplied by Ceren for Don's agency
  presentations, with checksums and source in one index. No capture metadata.
- AC-WL-2: Mask the underlying customer location (name, address, imagery, metrics, scores),
  any competitor name, the operator's name and personal browser detail. Never name the
  underlying customer in the repository.
- AC-WL-3: Ceren chose to keep Findri's logo and domain visible. Record that publication as
  `PENDING` Seven's approval; screens are not customer-facing until `APPROVED`.
- AC-WL-4: State where Obenan stays visible (Google consent, Terms and Privacy Policy,
  email) so agents never promise a fully invisible supplier. No implementation detail.
- AC-WL-5: Link the index from the entry point and asset library. Preserve prior stories and
  templates; pass tests, public-safety/local-link validation and whitespace checks; open a PR
  for Seven's review. No merge, send or customer-account change.

Progress:

- [x] Baseline: 70 tests pass at 6d879d2.
- [x] Six new tests failed before implementation (4 failures, 8 errors).
- [x] Mask, strip metadata and inspect all six images; add index, register entry, product
  UI boundaries and retrieval links.
- [x] Validate: 76 tests, public-safety/local-link validation and whitespace checks pass.
  Open the PR for Seven's review; GitHub is the authority for merge state.
- [x] Seven's instruction to merge, relayed by Ceren on 14 October, recorded as approval in
  the register (`APPROVED`, review 2027-01-14). Merge on a green exact-head check.

# Decision Pack standard

Spec: `spec/features/decision-pack-standard/decision-pack-standard.md`.

- [x] Confirm public sales workspace target; isolate changes from the live shared checkout.
- [x] Read the full supplied standard and current routing, design and claim boundaries.
- [x] Record acceptance criteria and baseline: 76 tests pass before this change.
- [x] Write and run seven failing instruction contracts before implementation: three failures
  and six missing-file errors. Existing template digests still match the base revision.
- [x] Add the canonical standard, operator prompt and routing with explicit compatibility.
- [x] Validate the exact staged export: 83 tests and public-safety/local-link checks pass.
  Worktree-local `.git` metadata is not part of that export; the scanner itself is unchanged.
  Whitespace and AC traceability pass: one spec, seven AC IDs, no missing annotations.
  Both deck hashes and all existing proof/assets are unchanged from the base revision.
- [x] Independent fidelity, public-safety and requirements reviews all APPROVE. Tests verify
  instruction contracts, not model compliance; the missing-input/NONE matrix also received
  manual source-to-standard review. No customer pack was built or claimed validated.
- [x] Prepare the reviewed branch for a draft pull request. Human approval is required before
  merge; GitHub is the authority for publication state. No customer send or deployment.
