# Document token and component contract

This contract keeps generated sales documents visually consistent. It contains public document
tokens only and is not a product implementation specification.

## Tokens

```css
:root {
  --ink: #0F0F14;
  --paper: #FFFFFF;
  --soft: #F7F7F7;
  --soft-2: #F0F0F0;
  --line: #E6E6E6;
  --muted: #666666;
  --quiet: #999999;
  --accent: #F67900; /* replace with one approved accent */
  --radius-small: 6px;
  --radius-card: 12px;
}
```

The accent may be one of the approved values in [BRAND_SYSTEM.md](BRAND_SYSTEM.md). Use one
accent only. Do not change logo colors.

## Type roles

| Role | Guidance |
|---|---|
| Display | Helvetica Neue Light, 34-44 pt on A4 |
| Section heading | Helvetica Neue Light, 20-26 pt |
| Subhead | Helvetica Neue Regular, 11-14 pt |
| Body | Helvetica Neue Regular, 9.5-11 pt |
| Label | Helvetica Neue Medium, 8-9 pt, short uppercase |
| Numeric | Same role with tabular numerals |

## Components

| Component | Required content | States |
|---|---|---|
| Cover | outcome, customer, date, sender | light or dark |
| Evidence card | metric, label, scope, source date | measured, supplied, estimated, inferred |
| Comparison bar | name, value, shared scale | neutral, highlighted |
| Status pill | text label | observed, verified, scheduled, waiting, needs approval |
| Quiet panel | short context or limitation | neutral only |
| Step | number, action, owner, timing | planned, active, complete, blocked |
| Investment card | authorized price, period, scope | standard, recommended |
| CTA | one action and owner | primary only |
| Footer | customer, confidentiality if instructed, page | standard |

Status must never be communicated by color alone.

## Layout

- A4: `210mm x 297mm`, zero print margin, internal page padding.
- Use a simple column grid and consistent alignment.
- Cards and rows use `break-inside: avoid`.
- Keep a stable footer area.
- Resolve overflow by editing content, never by global print scaling.

## Tests

Before handover:

1. Render at 100% scale.
2. Confirm the intended page count.
3. Inspect every page visually.
4. Check that all evidence labels and sources are legible.
5. Confirm one accent, exact logo assets and no private data.
6. Confirm reduced-motion behavior for interactive HTML when motion is present.
