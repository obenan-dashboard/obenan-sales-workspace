# Task router

Layer 1 routing reference. Not a mandatory full read: retrieve the legend plus the single row
for your task type, then stop. The mandatory bundle is `../START_HERE.md`, `../AGENTS.md`,
`../STATUS.md`, and for Claude Code `../CLAUDE.md`.

```bash
rg -n "^\| Upsell" knowledge/TASK_ROUTER.md
```

"Do not preload" means retrieve only on a trigger, then cite. Proceed states (PASS, PARTIAL,
STOP) and the hard stops are in `../AGENTS.md`.

## Legend, relative to the repository root

- **LCB** `knowledge/product/LANGUAGE_AND_CLAIM_BOUNDARIES.md`; **BU** `knowledge/product/BUSINESS_UNITS.md`;
  **VP** `knowledge/product/VALUE_PROPOSITION.md`; **FO** `knowledge/product/FEATURES_OVERVIEW.md`
- **PR** `knowledge/proof/PUBLIC_PROOF_REGISTER.md`
- **EM** `knowledge/engagement/ENGAGEMENT_MODES.md`; **AD** `knowledge/engagement/ANALYSIS_DOCTRINE.md`; **MCP** `knowledge/engagement/MCP_EVIDENCE_RUNBOOK.md`
- **ECR** `knowledge/engagement/EXISTING_CLIENT_REVIEW.md`; **RDECK** `templates/deck/EXISTING_CLIENT_REVIEW.html`
- **HV** `knowledge/voice/HOUSE_VOICE.md`; **WW** `Wolfgang-Written.md`; **WV1** `Wolfgang-Verbal-Part1.md`;
  **WV2** `Wolfgang-Verbal-Part2.md`; **WTF** `Wolfgang-ToneFingerprint.md`, all under `knowledge/voice/`
- **OBJ** `knowledge/sales/SalesObjection.md`; **PSY** `knowledge/sales/SalesPsychology.md`;
  **CB** `knowledge/sales/ConversationBrain.md`; **CP** `knowledge/sales/ConversationPatterns.md`;
  **ODF** `knowledge/sales/OperationalDiagnosticFramework.md`; **SAP** `knowledge/sales/SalesAgentPrompt.md`
- **DP** `reference/design/DESIGN_PRINCIPLES_2026.md`; **BS** `reference/design/BRAND_SYSTEM.md`;
  **DC** `reference/design/DESIGN_CORE.md`; **ADG** `reference/design/APPLIED_DESIGN_GUIDE.md`;
  **TCC** `reference/design/TOKEN_COMPONENT_CONTRACT.md`; **BAL** `reference/design/BRAND_ASSET_LIBRARY.md`
- **MC** `reference/messaging/MESSAGING_CORE.md`; **AMG** `reference/messaging/APPLIED_MESSAGING_GUIDE.md`
- **UI** `reference/product-ui/PRODUCT_UI_OVERVIEW.md`
- **LOGO** `assets/logos/Logo.svg` (the wave mark used on shipped decks); full lockups `assets/logos/Logo_Dark.svg`, `Logo_Light.svg`
- **DECK** `templates/deck/DECK_SKELETON.html`; **PG** `templates/proposal/PROPOSAL_GENERATOR.md`;
  **PP** `templates/proposal/PROPOSAL_PROCEDURE.md`; **DRC** `templates/proposal/DESIGN_RECONCILIATION.md`
- **EX** `examples/WORKED_EXAMPLE_upsell_brief.md`

## Rows

| Task type | Mandatory | Task-specific | Only when relevant | Do not preload | Gates | Proceed |
| --- | --- | --- | --- | --- | --- | --- |
| Win-back | LCB, EM | CB, OBJ, PSY, HV | PR if naming another customer, MCP if they were a customer, ODF, AD | UI, DP, BS, PG, PP | What actually ended it, from the record. Never assert an inferred churn reason. | PARTIAL if the end reason is unverified. Say so. |
| Upsell | LCB, EM, MCP, ECR | ODF, PSY, HV, FO, AD | PR for reusable proof, OBJ, BU, RDECK for a results review, DP, BS, LOGO | UI unless the gap is a product screen | Discovery first. Reclassify raw search labels; date scores; matched review baseline. Verify entity count. Separate pricing and expansion pitch from the review PDF. | PARTIAL without live/supplied evidence. STOP on unauthorized commercial terms. |
| Reporting | LCB, MCP, AD, ECR | EM, ODF, HV | PR for reusable proof, PSY, RDECK for rendered reviews, DP, BS, LOGO | UI, PG, PP, OBJ | Verified activation/cutoff and matched baseline. Declines visible. No raw Discovery-as-nonbrand claim, stale current score or scheduled-as-delivered work. | PARTIAL if evidence is incomplete. No causality. Check ledger, actual copy and every rendered page. |
| New pitch | LCB, EM | HV, PSY, CP, VP, MC | PR if naming another customer, ODF, OBJ, AD, DECK, DP, BS, LOGO, EX | UI, PG, PP | One finding about their own estate, done before the meeting. | PASS only with a real finding. Otherwise it is a template. |
| Proposal | LCB, PG, PP, DRC | EM, VP, FO | HV or WW, DECK, DP, BS, LOGO | UI, CP, EX | Transcript, Language, LOCATIONS, PRICING all present. | STOP if any input is missing. Write the recap first. |
| Meeting recap | LCB, PP | SAP, CB | WV1, WV2, HV | UI, DP, BS, PG, DECK | Transcript only. Never invent a commitment. | PASS. Flag missing proposal inputs at the end. |
| Outreach | LCB, HV | CP, PSY, OBJ | SAP, EM, MCP | UI, DP, BS, PG, PP, DECK | One clear next step. One voice, never blended. | PASS. Ready-to-send copy only. |

## Notes on two rows

**Upsell** and **Reporting** both depend on MCP evidence. Without it they become assertion,
which is the failure mode this repository exists to prevent.

For a customer performance document, ECR and RDECK take precedence over the generic DECK.
Use the supplied reference layout, never a new-business product pitch. Connector access is
not required to read this repo; without authorized evidence, produce only a labelled template.

**Proposal** is the only row where the design reconciliation (DRC) is mandatory. The proposal
generator carries a visual system that predates the current design principles, and DRC says
which wins.

**Product questions** route to UI. It is a sales-safe surface overview, not an engineering or
security audit. If a question requires implementation detail, stop and route it internally.

**Anything rendered** uses LOGO, never a redrawn or recoloured mark. The `legacy/` marks are
for identification only, not for new documents.
