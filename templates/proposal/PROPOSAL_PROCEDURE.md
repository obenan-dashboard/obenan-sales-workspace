# SME Proposal Procedure

Source: Wolfgang Sales Agent V2, reconciled for the public workspace on 2026-10-06.

Use this file together with `PROPOSAL_GENERATOR.md` when generating meeting recaps or proposal
HTML that will be exported as a PDF.

## Goal
- Produce either a meeting recap or a proposal that is correct on content, on-brand in tone, and flawless in PDF export.
- Flawless means exactly 4 pages, no overflow onto a fifth page, no cut-off cards, rows, CTA, or footer, and no broken page splits inside cards, pricing blocks, or grids.

## Required Inputs
- meeting transcript or recap
- prospect and business facts
- `Language`
- `LOCATIONS`
- `PRICING`
- sales rep details
- proposal date

Do not draft from vague memory. If the transcript is missing, stop and ask for it. If proposal pricing or language inputs are missing, write the recap first and flag the gaps.

## Operating Sequence
1. Extract facts from the meeting transcript only.
2. Decide `du` or `Sie` from the transcript and keep it consistent.
3. If the task is recap, write the recap and flag missing proposal inputs.
4. If the task is proposal, choose the correct language mode from the input.
5. Choose the correct branch: single-location or multi-location.
6. Confirm all pricing values before writing.
7. Build a page plan before drafting copy.
8. Write short copy to fit the page plan.
9. Build the HTML on a fixed A4 layout.
10. Run the fit audit before final output.
11. If anything risks overflow, compress and rebuild.
12. Deliver the final output only when all checks pass.

## Page Plan
- Page 1: wordmark-only cover, outcome headline, short subtitle, 2 by 2 meta grid, optional compact location strip.
- Page 2: 2 short situation paragraphs, 4 diagnostic cards, 1 short insight box, 1 compact stakes comparison.
- Page 3: 6 short service items, 3 steps.
- Page 4: 2 pricing cards, 3 timeline items, 5 next-step rows, 1 CTA block, 1 footer.

Do not add extra sections. Do not move content across pages. For multi-location proposals, adapt inside the same 4-page structure.

## Meeting Recap Standard
- Output a concise recap before the proposal when requested or when key proposal inputs are still missing.
- Use this order: `Meeting Summary`, `What we learned`, `Current setup`, `Key gaps / diagnosis`, `Commercial frame`, `Agreed next steps`, `Proposal inputs confirmed`, `Open questions`.
- Keep recap language aligned with the meeting language.
- Include only grounded facts and stated next steps.

## Fixed Layout Rules

```css
@page { size: A4; margin: 0; }
html, body { margin: 0; padding: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; padding: 52px 60px; overflow: hidden; display: flex; flex-direction: column; break-after: page; page-break-after: always; }
.page:last-child { break-after: auto; page-break-after: auto; }
.card, .grid, .row, .timeline-item, .pricing-card, .cta, .location-strip { break-inside: avoid; page-break-inside: avoid; }
.footer { margin-top: auto; }
```

Do not rely on browser print scaling. The document must fit at 100%.

## Conservative Copy Limits
- cover subtitle: max 18 words
- situation paragraph: max 75 words each
- diagnostic card: max 42 words
- insight box: max 45 words
- stakes card: one short paragraph each
- service item description: max 32 words
- timeline item description: max 24 words
- next-step row label: ideally 3 to 6 words
- CTA contact line: one line only

Shorter is better than tighter.

## Proposal-Stage Rules
- Never use audit-stage CTAs inside a proposal. Use commitment-stage CTAs only.
- English proposals must be fully English. German proposals must be fully German.
- Multi-location proposals must show the location network clearly, but without adding a fifth page.
- Pricing must never be improvised. Use the provided inputs only.
- The wordmark stays wordmark-only. No square icon.

## Page 4 Safety Rules
- Keep section gaps tight and consistent.
- Keep timeline copy to one short sentence each.
- Keep next-step row labels compact.
- Keep owner and timing compact.
- Keep the CTA to headline plus one contact line.
- Anchor the footer at the bottom with flex layout.
- Never let the CTA or footer spill to a fifth page.

## Fit Audit
- If the task is recap, the recap is factual, structured, and names any missing proposal inputs.
- There are exactly 4 `.page` sections.
- The proposal language matches the input.
- `du` or `Sie` matches the transcript.
- The correct single-location or multi-location branch is used.
- All pricing values come from `PRICING`.
- Page 1 fits the optional location strip safely.
- Page 2 fits the 4-card grid, insight box, and stakes block.
- Page 3 fits 6 service items plus 3 steps.
- Page 4 fits pricing, timeline, 5 next-step rows, CTA, and footer together.
- No section depends on print scaling, and no row or card can split across pages.
- No text block looks dense or compressed.

If any answer is no, revise before output.

## Compression Order
1. shorten subtitle
2. shorten diagnostic card copy
3. shorten stakes copy
4. shorten service descriptions
5. shorten timeline copy
6. shorten next-step labels
7. reduce vertical gaps slightly

Do not reduce required items, shrink the whole page, add a fifth page, mix languages, or leave pricing as placeholders.

## Final Gate
Do not deliver the HTML if page count is likely to exceed 4, page 4 feels crowded, the CTA and footer are not clearly safe, the proposal language is mixed, the wrong CTA stage is used, the pricing is missing or improvised, or the copy reads stuffed into the layout.

Do not deliver the recap if it invents decisions that were not made or hides open questions that still block the proposal.

When in doubt, choose the shorter version.
