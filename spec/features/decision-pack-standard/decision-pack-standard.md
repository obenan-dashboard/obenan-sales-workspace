---
status: in-review
---

# Decision Pack standard

## Request

Encode Seven's supplied Decision Pack design and explanation standard in the public sales
workspace. Target confirmed on 14 October 2026. This implements reusable instructions, not a
customer pack or a new rendering engine.

## Acceptance criteria

- **AC-DPACK-1:** An agent starting at the repository URL can select Decision pack, retrieve
  one router row and reach one canonical standard and one copyable operator prompt. Ordinary
  Reporting, Upsell and priced Proposal routes remain available and unchanged.
- **AC-DPACK-2:** Intake captures all twelve operator fields plus reference-bundle paths.
  Ask once for missing inputs, record gaps privately and proceed only with sourced work.
  NONE permits an unpriced pack, never an inferred price or naming permission. Commercial
  hard stops and human-only sending remain binding.
- **AC-DPACK-3:** The standard preserves meeting-led page order, purpose/outcome/scope,
  example-shape-only reuse, page grammar, one display number, cover authorship, native
  language, small next step, appendix rules and the exact blue visual profile. No fixed
  customer page count is introduced.
- **AC-DPACK-4:** The build procedure requires isolated extraction, source-bound generation,
  two customer-specific gates after every change, PDF rendering and inspection, immutable
  sent versions, hashes, EVIDENCE, private reviewer note and dated account updates. It does
  not claim that repository tests have inspected or validated any customer PDF.
- **AC-DPACK-5:** Preserve naming and price authority, prohibited wording, measured versus
  inferred outcomes, pilot distinctions, no presenter content in customer files and read-only
  external systems. Publish no private paths, example facts, correspondence or account data.
- **AC-DPACK-6:** Preserve the existing ten-page and eleven-page HTML templates and all proof
  cards byte-for-byte. The new profile has explicit precedence: existing review evidence
  rules still apply to performance packs, but a deliberately selected Decision Pack uses its
  own meeting-led layout. Do not inject proof or partner pages without intake authority.
- **AC-DPACK-7:** Write regression contracts before implementation, retain the failing result,
  pass the complete suite and public validation, and obtain independent requirements,
  fidelity and public-safety reviews. Publish a pull request for human review, not a merge.

## Verification matrix

| Case | Expected outcome |
| --- | --- |
| Explicit Decision Pack | One route to the standard and operator prompt |
| Routine results review | Existing Reporting/ECR route and eleven-page template |
| Priced SME proposal | Existing Proposal input hard stops |
| Missing authority or example | Ask once, private gap, no fabricated input or claimed inspection |
| NONE for prices or names | Unpriced unit description, no unrelated named proof or partner page |
| Approved proof requested | Existing register and separately approved assets, no metric removal |
| Source changed or either gate nonzero | Build fails; no ready-to-send claim |
| Prior sent deck | New revision path; old bytes preserved |

## Scope and limits

Documentation and routing only. Contract tests inspect the instructions that agents consume;
they cannot prove a model obeys them. Manual source-to-standard review is required. There is
no customer build in this change, so render, arithmetic and leak gates must be implemented and
run for each actual pack. No new dependencies, services, customer writes, website changes,
sends or deployments. No external runtime call is introduced, so no sequence diagram is
needed. Human approval through the pull request is the next action before merge.
