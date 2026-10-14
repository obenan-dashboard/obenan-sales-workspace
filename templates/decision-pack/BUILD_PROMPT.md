# Decision Pack operator prompt

Copy the block into your agent, fill the fields and provide authorized source paths. Keep
the filled brief and all account evidence in a private workspace, not this public repo.
The [canonical standard](../../knowledge/engagement/DECISION_PACK.md) supplies the rules;
this prompt is intake, not a second design specification.

```text
Read https://github.com/obenan-dashboard/obenan-sales-workspace and follow START_HERE.md.
Task type: Decision pack. Read knowledge/engagement/DECISION_PACK.md and its router row.
Treat the shared sales workspace as read only. Build in the private account workspace.

Prospect: [name and how addressed on the page]
Occasion: [post-meeting pack | first pitch | proposal | performance review]
What we learned: [meeting date, authorized notes/transcript path, their questions in their words]
Account folder: [private account directory]
Build folder: [new private revision directory; never overwrite a sent pack]
Workspace: [local sales workspace path or repository URL; read only]
Language: [native writing language]
Deliverable: [PDF for sending | PDF plus interactive HTML]
Commercial authority: [exact prices permitted to print, or NONE]
Public naming rights: [exact names, logos, images and claims permitted in this pack, or NONE]
Known sensitivities: [providers, partners, people or other customers never to name]
Reviewer and sender: [human who approves and sends]
Example bundle: [PDF, generator, two gates, EVIDENCE, brief and private-note paths]

Ask once about blank fields or a missing example; record gaps privately. Continue with
sourced work only. Do not invent price, permission, partner, capability or example inspection.
NONE for commercial authority means an unpriced pack; describe the unit and leave price to
the human's covering message. If a safe customer pack cannot be built, return a private page
plan and missing-input list. All account evidence stays private.

First propose the page list in the order of our buyer's questions. Use the standard's blue
profile and a meeting-led length, not an automatic product pitch or fixed page count.
Build with a source-bound generator and two customer-specific gates. Render and view every
page, run both gates after every change and record actual outputs and hashes in EVIDENCE.md.
Keep the customer HTML/PDF free of presenter notes and controls. Bring those files and the
separate private reviewer note to the human. Update account STATUS.md and DECISIONS_LOG.md.
Draft only. Do not send, publish or change email, CRM, calendar or customer-account data.
```
