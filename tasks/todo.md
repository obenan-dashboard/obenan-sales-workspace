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
