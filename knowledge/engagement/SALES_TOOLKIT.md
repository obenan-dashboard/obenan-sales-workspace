# Sales toolkit: interactive sections

Six reusable sections for pitch pages and their PDFs, in one shared stylesheet and script:
`templates/sections/toolkit.css` and `templates/sections/toolkit.js`. Three worked examples
show how the buyer's question changes which sections appear and in what order:
[coffee](../../templates/sections/coffee.html), [banking](../../templates/sections/banking.html)
and [fitness](../../templates/sections/fitness.html).

The examples use synthetic names and rows. They are teaching material, not customer pages.
Customer builds live in a private workspace, never in this repository.

## Start here

1. **Name the job.** Task, audience, vertical, language and the buyer's question in their words.
2. **Pick a recipe** below. It is a starting order, not a fixed page count. Drop any section
   that does not answer the question. Reviews never make up most of a page.
3. **Collect evidence privately.** Each figure needs a source and a date in your private
   `EVIDENCE.md`. Missing values stay `Unknown`, never zero.
4. **Build the closest example** into a private folder outside the repository with
   `node scripts/build_toolkit_example.cjs --example coffee --out DIR`. `DIR` must be new or
   empty; the build refuses anything else before writing. It copies `toolkit.css`, `toolkit.js`
   and every referenced image. Links to repository documents open their public source on GitHub,
   pinned to a commit, so they work in the PDF and on any machine. Replace synthetic rows with
   checked findings in the built copy. Keep every disclosure label.
5. **Render, check and hand over** with the commands at the end. A person reviews and sends.

## Vertical reference guide

Each example is a port of one earlier Obenan pitch site, so an agency agent reuses a proven
layout instead of designing a new one. The source repositories are private references; their
customer names, figures, photographs and logos are never copied.

| | Coffee and restaurants | Banking | Fitness |
| --- | --- | --- | --- |
| Example | `templates/sections/coffee.html` + `coffee.css` | `templates/sections/banking.html` + `banking.css` | `templates/sections/fitness.html` + `fitness.css` |
| Source reference and commit | `bluestonelane` at `20461fe00a66` | `yapikredi` at `157e4c1a2b68` (layout), with `isbank` at `d8b55b890a3b` and `akbank` at `b725cbf51f6a` | `trainmore` at `3b9f41443d16` |
| Typography | Nunito Sans, vendored | Inter, vendored | Inter, vendored |
| Reusable sections | proof, compare, portfolio, reviews, network, teaser, assistant, business case | portfolio, compare (evidence cases), assistant, network (governance cards), business case (owners and weeks, no calculator) | compare (with the headquarters strip), teaser, assistant, portfolio, business case (calculator, decision steps, measurement) |
| Logos | `assets/logos/Logo.svg` on light, `assets/logos/Logo_Light.svg` on dark; directory tiles from `assets/directory-logos/` | `assets/logos/Logo.svg` | `assets/logos/Logo_Light.svg` on the black hero and footer |
| Media | LPQ interview still `assets/video-previews/lpq-joost-interview.jpg` and its QR, linked at 2:24; approved dashboard preview included by default | None. No bank photographs | Approved dashboard preview included by default. No club photographs |
| Restrictions | Quote the LPQ and Campos cards verbatim from the proof register. Roster counts from `directories.json`. No delivery promise beyond the destinations that apply to an account | No bank name, logo, photo or figure. Branches and ATMs counted apart. No calculator, no cost or outcome | No club name, logo, photo or figure. Inputs start empty; the result is a threshold, not a forecast |

`assets/logos/Logo_Dark.svg` is the third approved logo file; use only these three Obenan logo
files. Reuse approved customer marks within the scope recorded in
`assets/customer-logos/README.md` and the public proof register. Unapproved source-prospect
logos remain excluded.

Exact build commands, from the repository root, each into a new or empty folder:

```bash
node scripts/build_toolkit_example.cjs --example coffee --out DIR
node scripts/build_toolkit_example.cjs --example banking --out DIR
node scripts/build_toolkit_example.cjs --example fitness --out DIR
```

## Video: approved assets

- **Usable:** the Le Pain Quotidien interview with Joost is usable in decks and pages today. Use the approved still
  `assets/video-previews/lpq-joost-interview.jpg` with its play icon, the QR
  `assets/video-previews/lpq-joost-interview-qr.svg` labelled "Scan to watch" and the caption with
  its printed address, beside his verbatim quote from
  [the LPQ card](../proof/LE_PAIN_QUOTIDIEN.md). Never a text-only panel.
- **Usable:** the [Obenan dashboard preview](../../assets/product-film/README.md) is approved
  by Seven for public sales reuse on 2026-11-03. The silent video, poster and public QR are
  included in this repository and in coffee and fitness builds by default. They are a
  product demonstration, not the prospect's account or customer-results proof. Do not ask
  for the superseded approval checklist again. Keep the teaser separate from the scripted
  assistant section, and keep its short disclosure on screen and in print.

## Copy-paste instruction for an agency agent

```text
Read https://github.com/obenan-dashboard/obenan-sales-workspace and follow START_HERE.md.
Task type: Interactive sections. Read knowledge/engagement/SALES_TOOLKIT.md and its router row.
Treat the shared workspace as read only. Build in a private folder outside the repository.

Buyer and audience: [company, who reads it, language]
Vertical: [coffee and restaurants | banking | fitness | other]
Buyer question: [in their words]
Evidence: [private paths to checked findings, with sources and dates]
Naming and proof rights: [approved proof cards, or NONE]
Commercial authority: [exact prices permitted, or NONE]
Output: [web page | PDF | both]
Reviewer and sender: [human who approves and sends]

Pick the sections that answer the buyer question, in that order. Build the closest example
with scripts/build_toolkit_example.cjs. Preserve its vertical stylesheet, fonts, layout and motion
alongside the shared toolkit.css and toolkit.js. Adapt evidence and copy, not the design. Keep every
disclosure label on screen and in print. Missing values read Unknown. Quote approved proof
exactly. Inputs in the business case start empty. Render the PDF with Chrome, view every page,
run the checks and record sources in a private EVIDENCE.md. Draft only. Send nothing.
```

## The six sections

Each section is a `<section class="tk" data-section="...">` with a `<p class="tk-label">`
disclosure as its first child. Without JavaScript every section is complete and readable;
the script only adds motion and controls. Print shows the static form.

| Section | `data-section` | Use it when | Print form | Adapt |
| --- | --- | --- | --- | --- |
| Product teaser | `teaser` | The buyer has not seen the product. One headline, one film. | Poster, public link and QR | Keep the label "Obenan dashboard preview". Never quote a number from the film. |
| Observed and proposed | `compare` | One location shows a concrete gap. | Both states side by side | Observed comes from a dated check. Proposed is a proposal, never shown as achieved. |
| Review stream | `reviews` | Guest experience is part of the question. | Static grid of cards | Themes, not reviewer names. State "N unique"; the motion copies never count. |
| Portfolio explorer | `portfolio` | Many locations and the buyer asks where. | Full table | One row per location. Separate types (cafés and kiosks, branches and ATMs, clubs and studios). Unknown is not zero. |
| Assistant walkthrough | `assistant` | The buyer asks how an answer would look. | Full conversation | Question, response, conclusion. Label it a scripted demonstration, not a live connection. Use only facts already on the page. |
| Business case | `business-case` | The buyer asks what would have to be true, or who decides. | Blank inputs and owners | Buyer inputs only, empty by default. The result is a break-even threshold. Owners and next steps, no prices unless authorised. |

Two supporting blocks reuse approved material: the **directory network** (`network`) shows
the existing channel images and the roster counts, and **proof** (`proof`) quotes an approved
card from [the proof register](../proof/PUBLIC_PROOF_REGISTER.md) exactly as written.

## Recipes

| Recipe | Buyer question | Starting order |
| --- | --- | --- |
| Coffee and restaurants | Can guests find the right café, the current menu and the real hours, and is every café consistent? | proof, compare, portfolio, reviews, network, teaser, assistant, business case |
| Banking | Who owns the truth about each branch and each ATM? | portfolio, compare, assistant, network, business case (governance, no calculator) |
| Fitness | Do people nearby understand the offer well enough to book a trial, and do trials become memberships? | compare, teaser, assistant, portfolio, business case (trial to membership threshold) |

**Coffee and restaurants:** discovery, menus, consistency between locations and the guest
experience. Lead with a real gap at one café.

**Banking:** count branches and ATMs separately; an ATM inside a branch is its own row.
Accurate information and network governance come first: who approves hours, services,
closures and public wording. Read `knowledge/product/BUSINESS_UNITS.md` for the unit types.

**Fitness:** club discovery, an offer people understand and trial to membership measurement.
The calculator chains contribution per membership, trial conversion and booking rate.

## Evidence and claims

- Read current values from their source. Roster counts come from
  `reference/directories/directories.json`; a listed destination is not necessarily active.
- Quote proof cards verbatim. Never restate them in new words or add a number.
- Never state guaranteed results, savings, return figures, invented visibility scores,
  promised rating rises, review counts as search share or scale claims without a source.
- Never ask only happy guests for reviews, and never present a scripted answer as live.
- Keep private exports, account identifiers, reviewer identities and unapproved quotes out of
  this repository. Language rules: `knowledge/product/LANGUAGE_AND_CLAIM_BOUNDARIES.md`.
- In a Decision Pack, the narrow toolkit exception in
  [DECISION_PACK.md](DECISION_PACK.md) keeps these labels; every other rule there stands.

## Film

[The dashboard preview](../../assets/product-film/README.md) is bundled and publicly usable.
The usual build commands include its video, poster, public link and QR automatically.
No private copy or extra installation is required. To intentionally omit the teaser:

```bash
node scripts/build_toolkit_example.cjs --example coffee --out DIR --no-film
```

The build verifies the rendition, poster and default QR against the README checksums. The
film uses `preload="none"`, visible controls and no autoplay. PDFs show the poster with a
clickable public link and QR. Optional `--film-dir DIR` still accepts a checksum-matched copy;
`--film-url URL` uses an approved alternate address and generates its QR with the pinned
`qrcode` tool below. Neither option may be combined with `--no-film`.
[DESCRIPTION.md](../../assets/product-film/DESCRIPTION.md) is the scene by scene text.

## Build and check

Needs Node 18 or later, Python 3, ripgrep (`rg`) and Google Chrome or Chromium. The tests and
the validator fail on purpose when `rg` is missing. `pdftoppm` (poppler) is optional and adds
the PDF page fill check. From the repository root:

```bash
python3 -m unittest discover -s tests -v
bash scripts/validate_public_repo.sh
npm install --no-save --no-package-lock --prefix out/.tools \
  playwright-core@1.56.1 qrcode@1.5.4 jsqr@1.4.0 pngjs@7.0.0
node scripts/check_toolkit_browser.cjs
```

The npm step installs pinned tools into the ignored `out/.tools`; no package file is added.
The browser check builds every example into a temporary folder, serves it on a loopback port
and tests 390, 768, 1440 and 1920 px, keyboard tabs and filters, Unknown sorting, the business
case arithmetic, the chat replay, the review stream pause, reduced motion, no JavaScript, fast
scrolling and the A4 PDF. It writes captures, PDFs and `receipt.json` to `out/toolkit/` and
exits 1 on any failure. It fails a PDF with a local link or a business case split across
pages. Only `coffee-film-url-loopback.pdf` may carry a loopback address: it is a diagnostic of
the film link mechanism, never a handover file. Set `CHROME=/path/to/chrome` if Chrome is not found.
Default coffee and fitness playback, public QR destinations and PDF links are mandatory
checks, including in CI. Missing approved media fails the check; it is never silently skipped.

To preview one build, serve the build folder on loopback and open it:

```bash
toolkit_preview_dir=$(mktemp -d)
node scripts/build_toolkit_example.cjs --example coffee --out "$toolkit_preview_dir"
python3 -m http.server 8765 --bind 127.0.0.1 --directory "$toolkit_preview_dir"
```

Then open `http://127.0.0.1:8765/`. Render the PDF from the build with Chrome headless
`--print-to-pdf` (see `CLAUDE.md`), or use `out/toolkit/coffee.pdf` from the check. Open the PDF
and read every page.

## Coffee source map

The coffee example is a port of the `bluestonelane` pitch site at `20461fe00a66`, not a new
design. `templates/sections/coffee.css` carries its colour tokens and Nunito Sans, scoped to
`.v-coffee`; the fonts are vendored with their OFL licences in `templates/sections/fonts/`.
Banking and fitness do not link it; they carry their own ported stylesheets, mapped below.

| Coffee section | Source section |
| --- | --- |
| Cover | `HeroSection`: white bar with centred logo, navy box, uppercase headline, stats row |
| `proof` | `Testimonial`: pill, split card with video and quote, three supporting cards |
| `compare` | `InternalProof`: two bordered cards, arrow between, insight line |
| `portfolio` | `PortfolioIntelligence`: summary cards, table card, filter footer |
| `reviews` | `Reputation`: accented headline, three column review wall with fades, grey box |
| `network` | `Services`: ONE UPDATE circle, connector, logo tiles, closing line |
| `teaser` | `Testimonial` video frame: centred heading, large rounded stage |
| `assistant` | `TalkToData`: eyebrow, light headline, dark two pane chat shell |
| `business-case` | `CTA`: uppercase headline, white cards, numbered checklist |
| Footer | `FooterSection`: navy band, light logo |

### Intentional differences

- No hero photograph; the stage is a powder-blue gradient, since the source photo is not ours to publish.
- Observed and proposed keep the toolkit tabs on screen (keyboard support); both cards show side by side without JavaScript and in print.
- The proof card shows Le Pain Quotidien's approved still, QR and quotes in place of the source's video and figures; the Campos card follows. No source result figures are reused.
- Review cards carry theme chips only: no stars, reviewer names or reply markers.
- The network drops the source's update-time claim and uses roster counts (104, 93 more beyond the 11 tiles).
- The assistant shell is unbranded: no model or provider names, no stats strip, a mint avatar, and the sidebar is hidden on phones.
- The business case drops the "Prepared by" name block and the source's analysis figures.
- Arrival motion is CSS only and tied to scroll position, so fast scrolling never leaves content hidden.

## Banking source map

The banking example is a port of the bank pitch sites: the layout and tokens of `yapikredi` at
`157e4c1a2b68`, which shares its section set with `isbank` at `d8b55b890a3b` and `akbank` at
`b725cbf51f6a`. `templates/sections/banking.css` carries the source colour tokens (primary
`209 100% 29%`, accent `173 77% 32%`), gradients, shadows and Inter, scoped to `.v-banking`
with a `bk-` prefix.

| Banking section | Source section |
| --- | --- |
| Cover | `HeroSection`: grid backdrop, lockup, large two line headline, chips, dated line |
| `portfolio` | `VisibilityCrisisSection`: tally cards, then one table card with filters in its head |
| `compare` | `DuplicatesSection` and `SmokingGunsSection`: evidence cases, one open, two collapsible |
| `assistant` | `AIDataChatSection`: dark two pane chat shell, avatar, titled answer with a data table |
| `network` | `GovernanceLayerSection`: six governance cards |
| `business-case` | `ExecutionPlanSection`: numbered steps, two responsibility panels, four week line |
| Footer | `ClosingCTASection`: closing band with logo |

### Intentional differences

- No bank name, logo, photograph or figure; every row is synthetic and labelled.
- The hero has no metric cards from the source; its chips count the sample only.
- Evidence cases use native `details`, so they open without JavaScript and print open.
- The assistant shell carries no model or provider name and hides its sidebar on phones and in print.
- The governance cards drop the source's channel claims and use the roster counts (104, 4 inactive).
- The execution plan has no prices, dates or outcome figures; the weeks are an example to agree.
- No calculator: the banking question is who approves what, not a cost threshold.

## Fitness source map

The fitness example is a port of the `trainmore` pitch site at `3b9f41443d16`.
`templates/sections/fitness.css` carries its colour tokens (primary `344 96% 52%`, CTA
`174 72% 40%`, status colours, black navy) and Inter, scoped to `.v-fitness` with an `fm-` prefix.

| Fitness section | Source section |
| --- | --- |
| Header bar | Index sticky header: page title and the membership case link |
| Cover | `HeroSection`: black field, ruled top line, very large headline, two actions, stat grid, watch callout |
| `compare` | `PreviewSection`: pill toggle, dashed observed card, green bordered proposed card, "What headquarters does" strip |
| `teaser` | `TimelineSection`: black band, outlined pill, gradient rule |
| `assistant` | Source card language: bordered card, black question, teal working line |
| `portfolio` | `ClubStoriesSection`: watch boxes with large numbers, then the club table |
| `business-case` | `BusinessCaseSection` and `DecisionSection`: "Entered by" inputs, black result panel, numbered decision steps, "How it would be measured" |
| Footer | `ClosingSection`: black band, light logo, proposal line |

### Intentional differences

- No hero photograph; the source photo is a club's own and not ours to publish. The black gradient stays.
- No club name, logo or figure; the stat grid counts the synthetic sample only.
- The source's "Book a trial" button is not reproduced as a control; the proposed state describes the booking link instead.
- The calculator keeps the toolkit's four empty inputs and threshold wording instead of the source's prefilled figures.
- The source timeline's schedule and the club story numbers are dropped; only their visual language is reused.
- The teaser band includes the approved dashboard preview by default; `--no-film` omits it.

## Where the mechanics came from

Patterns were reused from earlier pitch sites; their data, logins, analytics and claims were not.

| Mechanic | Source repository and commit |
| --- | --- |
| Tabs, threshold calculator, decision wording | `trainmore` at `3b9f41443d16` |
| Review stream, sortable location table | `bluestonelane` at `20461fe00a66` |
| Scroll triggered reveal with reduced motion end state | `isbank` at `d8b55b890a3b` |
| Paginated review grid | `akbank` at `b725cbf51f6a` |
| Timed assistant reveal | `yapikredi` at `157e4c1a2b68` |
