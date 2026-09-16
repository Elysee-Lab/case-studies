# Mission Control Room — E2E UI Makeover Audit

**Date:** 2026-09-16  
**Branch:** `mcr-figma-makeover`  
**Scope:** design audit + information architecture + Figma-ready design contract  
**Source of truth for narrative:** existing approved MCR case-study specification and current `mission-control-room/index.html`  
**Rule:** redesign presentation and hierarchy without inventing new business claims, metrics, system capabilities or confidential detail.

---

## 1. Product lens

Mission Control Room is not a SaaS marketing page and not a dashboard product demo. It is a portfolio case study for a senior hiring manager / transformation leader who needs to understand, quickly and credibly, how Eliza moved from a noisy inquiry problem to a measurable operating model and only then to an AI-enabled decision-support layer.

### User + job

**Primary reader:** senior AI / transformation / growth / RevOps / product stakeholder.  
**Job:** decide whether Eliza can connect strategy, process, ownership, measurement, AI, governance and hands-on delivery in a complex enterprise context.

### First-read object

**From Noise to Measurable Revenue**

The reader should immediately understand that this is a multi-year transformation story, not an AI feature showcase.

### Primary action

Continue through the story and understand the transformation logic, evidence and operating-system thinking.

### Density decision

**Editorial + evidence-led.** Spacious around the thesis and major transitions; denser only inside diagrams and proof surfaces where density communicates system complexity.

### Core narrative

`noise → human intelligence → operating model → measurement → attribution → automation → Mission Control Room → human control → outcomes`

### Forbidden defaults

- equal-weight card galleries for fundamentally different ideas;
- decorative SaaS dashboard UI where no actual product decision is being demonstrated;
- giant rounded cards as the default container for every section;
- pill overload;
- floating panels used only as decoration;
- gradients used as visual polish without semantic meaning;
- tiny annotation text that becomes illegible on laptop/mobile;
- mobile as a naive vertical stack of desktop cards;
- every section carrying the same visual weight;
- technical architecture dominating the business-transformation story.

---

## 2. Baseline implementation audit

### What is working and should be preserved

**KEEP**

1. Strong core title and thesis: `From Noise to Measurable Revenue`.
2. Warm off-white canvas and dark ink create an editorial rather than generic-corporate base.
3. Lime as a high-attention signal works conceptually for surfacing value / signal.
4. Blue and teal already provide useful distinction between system / action / validated movement.
5. EN / PL switch and sticky section navigation are valuable and should remain.
6. Existing public-safe narrative is materially strong and should not be rewritten merely to fit a new layout.
7. Existing reduced-motion rule should remain.
8. Existing separation between demonstrated history, built capability and future state should remain explicit.
9. Human Control Room is the most product-specific UI moment and should become more prominent, not less.
10. Inquiry-to-outcome attribution chain is a distinctive business-system concept worth elevating.

### Structural UI problems

**REDESIGN**

1. **The page behaves too much like a component gallery.** `card`, `stage`, `state`, `node`, `layer`, `challenge`, `claim`, `skill`, `panel` and `pill` are all competing container types. The visual grammar fragments rather than accumulates.
2. **Rounded-container inflation.** 17–30 px radii appear on almost every object. This weakens hierarchy because important system surfaces and secondary explanatory content look equally designed.
3. **Hero visual is over-composed.** A main panel plus rotated label plus rotated note creates visual energy but does not communicate the transformation thesis efficiently enough. It reads more like a startup landing hero than an executive case study.
4. **Equal-weight grids flatten priority.** `.g2/.g3/.g4`, five-stage timeline, four red-team challenges and tag clouds make very different ideas feel equally important.
5. **Navigation is functional but visually pill-heavy.** The current active-nav treatment adds another dark pill to a page already rich in pills and rounded containers.
6. **Typography is visually bold but not sufficiently role-based.** Display, evidence, annotation and technical labels need clearer semantic roles rather than primarily size/weight differences.
7. **Diagrams are technically readable but visually generic.** Chains of rounded rectangles and arrows do not yet create a memorable MCR-specific system language.
8. **The page does not sufficiently distinguish transformation history from product architecture.** A reader can encounter technical detail before fully absorbing why the product existed.
9. **The current mobile solution mostly resolves overflow, not narrative priority.** Converting chains/grids to one column prevents breakage but creates long repetitive scrolling and loses relationships between steps.
10. **Too many surfaces have similar white/translucent fills, borders and shadows.** This makes the eye work harder to identify proof vs context vs interaction.

### Elements to remove or merge

**REMOVE / MERGE**

1. Merge repeated explanatory card grids where the content can become one editorial narrative plus one stronger visual.
2. Reduce generic skill-pill density in the final capability section; capabilities should be grouped by meaningful competency families.
3. Remove decorative floating/rotated hero notes unless each carries unique evidence not visible elsewhere.
4. Merge repeated before/after explanations into one canonical operating-model transformation visual.
5. Merge attribution explanations into one canonical evidence-chain section rather than repeating similar flow patterns.
6. Remove repeated micro-badges where status can be communicated through typography or a concise legend.

---

## 3. Section-by-section disposition

The current approved narrative contains ~20 topic sections. The makeover should preserve the substance while consolidating the visual story into seven chapters.

### Chapter 01 — The hidden commercial problem

**Contains:** original sections 1–3.  
**KEEP:** enterprise context, `Noise does not mean no value`, manual human review as prototype.  
**REDESIGN:** replace multiple cards with a single opening story sequence.

**Signature visual:** `NOISE → SIGNAL` field.

- left: large field of low-value inquiry noise;
- one or two highlighted commercially meaningful signals;
- middle: human intelligence / manual review;
- right: protected opportunity / follow-up;
- supporting annotation: AI is not present yet.

**Reader takeaway:** valuable opportunities were hidden in aggregate noise; the first solution was human pattern recognition, not automation.

### Chapter 02 — Building the operating capability

**Contains:** original sections 4, 7, 8.  
**KEEP:** regional Lead Qualification capability, ownership, qualification, routing, follow-up, SLA, change management.  
**MERGE:** avoid separate card grids for every operating-model concept.

**Signature visual:** transformation timeline + operating model.

- manual protection of valuable inquiries;
- regional capability;
- defined ownership / qualification / routing;
- SLA / feedback loop;
- progressive automation;
- Mission Control appears only after operating logic is established.

**Secondary visual:** Before → Target operating model.

### Chapter 03 — Measurement changed the conversation

**Contains:** original sections 5–6.  
**KEEP:** Power BI measurement, move from activity to outcome, executive case studies linked to seven-figure outcomes, attribution becoming part of operating model.  
**REDESIGN:** make evidence the first visual object rather than supporting copy.

**Signature visual:** evidence ledger.

- source / inquiry;
- qualified signal;
- follow-up;
- opportunity;
- outcome evidence;
- executive proof.

One prominent public-safe evidence statement should carry more visual weight than secondary metrics.

### Chapter 04 — Why a parallel intelligence layer

**Contains:** original sections 9–10.  
**KEEP:** existing systems were powerful but interconnected; testing outside core stack reduced risk; experiment remained valuable even if later rebuilt elsewhere.  
**REDESIGN:** replace explanatory cards with one architecture comparison.

**Signature visual:** `CORE SYSTEMS | PARALLEL INTELLIGENCE LAYER | LEARNING BACK INTO CORE`.

The diagram must make explicit that Mission Control does not replace the CRM and is not an uncontrolled shadow system.

### Chapter 05 — What Mission Control Room actually does

**Contains:** original sections 11–12.  
**KEEP:** intake, preparation, enrichment, interpretation, qualification, human decision, routing/output, learning, governance, analytics, specialist-agent separation.  
**REDESIGN HEAVILY:** current layer rows / generic boxes should become a purposeful system blueprint.

**Signature visual:** system spine.

`Sources → Prepare → Research → Interpret → Decision support → Human review → Approved output → Outcome feedback`

Use detail-on-demand visually: only 5–7 first-order nodes in the main flow; supporting capabilities appear as subordinate annotations rather than equal boxes.

### Chapter 06 — Human authority + traceability

**Contains:** original sections 13–16.  
**KEEP:** Human Control Room, explainability, confidence, missing information, approve/override, system-agnostic integration, attribution chain, behavioural design.  
**PROMOTE:** this should be the most product-specific part of the page.

**Signature visual A:** redesigned Human Control Room screen.

First-read inside the control room:
1. what the system thinks;
2. why;
3. confidence / uncertainty;
4. suggested owner/action;
5. human decision.

**Signature visual B:** attribution chain.

`Inquiry → Qualification → Owner → Follow-up → Opportunity → Outcome → Revenue evidence`

**Signature visual C:** human behaviour gap.

Show that conversion feedback / recognition can close a missing-data loop that an API cannot.

### Chapter 07 — Outcomes, learning and capability proof

**Contains:** original sections 17–20.  
**KEEP:** demonstrated vs intended distinction, lessons learned, capability map, close.  
**REDESIGN:** capability map should not be a cloud of equal pills.

Group capabilities under four families:

1. **Transformation** — operating model, stakeholder alignment, change management.
2. **Revenue systems** — RevOps, attribution, CRM/MarTech, measurement.
3. **AI product** — human-in-the-loop, agentic workflow, signal modelling, governance.
4. **Delivery** — solution blueprinting, integration strategy, technical implementation, validation/remediation.

End with the existing core lesson: the important achievement was making an invisible commercial process visible, measurable and improvable; AI accelerated a system that had first been understood.

---

## 4. Proposed page wireframe

### 00 — Shared navigation

Two-row case-study navigation pattern already aligned across portfolio:

- row 1: `Mission Control Room · Case Study | Eliza Bingul` + EN / PL;
- row 2: chapter navigation, no heavy active pill;
- desktop: restrained underline / signal indicator;
- mobile: horizontal scroll with edge fade, visible first/last partial item as affordance.

### 01 — Hero / thesis

**Left 60%**
- case label;
- `From Noise to Measurable Revenue`;
- subtitle;
- 2–3 sentence thesis;
- compact metadata.

**Right 40%**
- signal/noise visual, not a fake dashboard;
- explicit marker: `AI enters later`.

Below fold: one thesis statement on full width.

### 02 — Chapter 1: Hidden signal

- editorial narrative left;
- large Noise → Signal visual right;
- human prototype as a thin process strip beneath.

### 03 — Chapter 2: Operating capability

- horizontal multi-year transformation timeline on desktop;
- vertically stepped editorial timeline on mobile;
- one canonical Before → Target flow beneath.

### 04 — Chapter 3: Measurement

- evidence-first composition;
- one prominent public-safe seven-figure evidence statement;
- supporting attribution evolution in compact rows, not cards.

### 05 — Chapter 4: Parallel layer

- full-width architecture diagram;
- core systems visually stable / neutral;
- Mission Control as distinct experimental intelligence plane;
- feedback / requirements loop back to core.

### 06 — Chapter 5: System blueprint

- one full-width system spine;
- sub-capabilities grouped beneath relevant stage;
- separate legend for Historical / Built / Next only where necessary.

### 07 — Chapter 6: Human Control Room

- dark product surface on a calmer editorial canvas;
- MCR decision screen large enough to be legible;
- reasoning + uncertainty + action hierarchy;
- human controls visibly dominant over automation status;
- attribution chain directly connected below.

### 08 — Chapter 7: Outcomes + capability proof

- demonstrated historical outcomes first;
- implemented capability second;
- intended future outcomes third;
- lessons learned in editorial numbered list;
- grouped capability map;
- closing statement + professional CTA.

---

## 5. Visual system direction

### Palette roles

Keep the existing family but reduce simultaneous use.

- **Paper:** main editorial canvas.
- **Ink:** primary text and authoritative system surfaces.
- **Signal lime:** surfaced value / human action / selected evidence. Use sparingly.
- **System blue:** process / system / technical structure.
- **Evidence teal:** validated / linked / outcome state.
- **Coral:** discrepancy / risk / unresolved signal only.

No decorative multi-colour gradients except the tiny existing progress indicator if retained.

### Radius hierarchy

Current implementation overuses large radii. New target:

- small controls: 8–12 px;
- evidence / annotation surfaces: 12–16 px;
- primary product surface: 18–20 px max;
- do not use 24–30 px by default.

### Typography roles

Do not default to changing the typeface until the current product/portfolio font setup is verified. Establish semantic roles first:

- Display / thesis;
- Chapter heading;
- Evidence number / proof;
- Body editorial;
- UI body;
- Technical annotation / label;
- Caption / provenance.

Minimum normal body target: ~16–18 px desktop, 16 px mobile. Avoid critical explanatory text below ~13–14 px.

### Spacing

Use a consistent 4/8-based scale. Major chapter separation should be materially larger than card/component gaps. The reader must feel chapter changes before reading labels.

### Containers

Default should be **open editorial layout**. A container must earn its border/background by serving one of these jobs:

- interactive/product surface;
- evidence callout;
- comparison state;
- system boundary;
- annotation requiring separation.

---

## 6. Responsive contract

### Desktop 1440

- max reading width remains controlled;
- signature visuals may extend wider than body copy;
- no more than 2 primary visual columns;
- Human Control Room remains fully legible without browser zoom.

### Tablet 768–1024

- chapters preserve visual relationships rather than immediately stacking everything;
- transformation / attribution flows may switch from horizontal to 2-column/stepped presentation;
- navigation becomes scrollable before content becomes compressed.

### Mobile 390

Mobile is a narrative redesign, not a desktop stack.

- Hero: thesis first, signal/noise visual second.
- Timeline: stepped vertical sequence with visible progression.
- Before → Target: two labelled states separated by a clear directional transition.
- System spine: numbered vertical stages; subordinate capabilities become concise lists.
- Human Control Room: first-read inference, evidence/confidence and decision controls stay visible; secondary history/detail moves below.
- Attribution chain: vertical spine with explicit lifecycle continuity.
- touch targets >= 44 px;
- no horizontal page overflow;
- navigation may scroll horizontally within its own container;
- key explanatory copy remains readable at 200% browser text scaling.

---

## 7. Component set for Figma

Create only reusable components that correspond to actual recurring narrative jobs.

1. `Case/Nav`
2. `Case/LanguageSwitch`
3. `Case/ChapterHeader`
4. `Case/EvidenceStatement`
5. `Case/Annotation`
6. `MCR/ProcessStep`
7. `MCR/SystemNode`
8. `MCR/DecisionSignal`
9. `MCR/StateComparison`
10. `MCR/StatusLegendItem`
11. `MCR/HumanAction`
12. `Case/CapabilityGroup`
13. `Case/CTA`

Do **not** create a generic `Card` component and then force every piece of content into it.

---

## 8. Figma file structure

Target file/pages:

- `00 Audit`
- `01 Foundations`
- `02 Components`
- `03 Desktop 1440`
- `04 Tablet 834`
- `05 Mobile 390`
- `06 Finish Gate`

`00 Audit` should preserve a screenshot/reference of the current implementation and place KEEP / REDESIGN / REMOVE observations beside it.

`01 Foundations` contains color roles, typography roles, spacing, radius and layout rules.

`06 Finish Gate` contains final desktop/mobile evidence and pass/hold findings.

---

## 9. Finish-gate criteria

The redesign remains **HOLD** until all are true:

1. First viewport clearly communicates transformation before product features.
2. AI is visibly positioned as accelerator, not starting point.
3. At least three major sections use a product-specific visual pattern rather than a generic card grid.
4. Seven-figure historical evidence is visually distinguishable from intended future benefit.
5. Parallel-layer diagram makes `not a CRM replacement / not uncontrolled shadow CRM` understandable without reading long copy.
6. Human Control Room makes human authority visually obvious.
7. Attribution continuity is understandable from inquiry to outcome.
8. Desktop 1440, tablet 834 and mobile 390 are individually designed and checked.
9. No horizontal page overflow at 390 px.
10. Interactive targets meet >= 44 px on mobile.
11. Normal text meets WCAG AA contrast target.
12. 200% text scaling does not destroy the narrative hierarchy.
13. EN and PL both fit without clipped labels or broken layouts.
14. No placeholder/generic dashboard content remains.
15. Final implementation matches accepted Figma design materially, not approximately.

---

## 10. Execution order

1. Freeze this audit as the design contract.
2. Capture/reference current MCR in Figma Audit page.
3. Build Foundations.
4. Build navigation + chapter header + evidence + process primitives.
5. Design Hero + Chapters 1–2 only.
6. Review direction before designing the rest.
7. Complete Desktop.
8. Derive intentionally redesigned Tablet and Mobile.
9. Run Finish Gate.
10. Only after PASS: implement on `mcr-figma-makeover` branch.
11. Regression test EN/PL, anchors, responsive layouts and overflow.
12. Merge only after visual and implementation parity review.
13. One controlled Vercel deployment and production parity check.
