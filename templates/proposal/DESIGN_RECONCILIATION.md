# Design and fact reconciliation

The proposal generator was reconciled with the public Obenan design principles and product
canon on 2026-10-06. These decisions are now applied directly in the generator.

## 1. Pure black against ink

The public design principles specify ink `#0F0F14` and state that pure black is never used.

**Use `#0F0F14` for headlines and the system's secondary grey for body.** Pure black on white
reads harsher in print and is the one rule the design system is most explicit about.

## 2. Six-colour gradient against one accent

The proposal generator uses **exactly one accent hue per document** and no decorative
gradients.

The full brand palette remains available for identity assets, but a proposal uses one accent.

## 3. Directory count

The public product canon states more than 100 supported destinations, with coverage varying by
destination and country.

**Use the product canon number.** A figure in a customer proposal has to match what the
product file says, and the proposal is the document most likely to be checked.

## Worth adopting in the other direction

The proposal generator's banned-word list is stricter than ours and should be merged into
`../../knowledge/product/LANGUAGE_AND_CLAIM_BOUNDARIES.md`: `affordable`, `cheap`, `budget`, `solution`, `synergy`,
`leverage`, `software`, `tool`, `platform`, `contract`, `learn more`, `discover`, `explore`,
`end-to-end`, `cutting-edge`, `robust`, `industry leader`, `best-in-class`.

The preferred replacements are good: `accessible`, `agreement`, `engagement`, `AI colleague`,
`AI team`, `autonomous system`. Note `agreement` rather than `contract`, which we do not
currently carry anywhere else.
