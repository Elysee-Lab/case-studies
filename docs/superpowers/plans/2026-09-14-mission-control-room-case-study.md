# Mission Control Room Case Study Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a public, bilingual, single-file portfolio case study for Mission Control Room and prepare it for an independent Vercel project at `b2b-lead-qualification-engine-case-study-eliza-bingul.vercel.app`.

**Architecture:** A single static HTML file under `mission-control-room/index.html`, with embedded CSS and minimal client-side JavaScript only for language switching and sticky navigation state. No external runtime data fetches, no loaders, no server functions, and no dependency on the DietoLab deployment.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, GitHub, Vercel static hosting.

**Spec:** `docs/superpowers/specs/2026-09-14-mission-control-room-case-study-design.md`

## Global Constraints

- Public-safe content only; do not expose real endpoints, secrets, credentials, raw lead data, internal IDs, private scoring thresholds, full prompts, or confidential security topology.
- English is the default language; Polish is available through an EN/PL switch.
- One self-contained `index.html`; no build step and no runtime network dependency required to render the page.
- Distinguish demonstrated historical outcomes, implemented product capability, and planned/future capability.
- Keep the enterprise context public-safe: Salesforce and Salesforce Marketing Cloud may be named; internal implementation details and client records may not.
- Preserve the approved hero: `From Noise to Measurable Revenue` / `Building a B2B Inquiry-to-Revenue Operating System`.

---

### Task 1: Build the public-safe narrative and page structure

**Files:**
- Create: `mission-control-room/index.html`

**Produces:** A complete semantic HTML document with all approved narrative sections in English and Polish.

- [ ] Write hero, executive context, transformation timeline, product capability map, architecture, integration model, attribution, behavioural design, outcomes, learnings, capability map and closing CTA.
- [ ] Use only public-safe abstractions for internal systems and synthetic examples where examples are needed.
- [ ] Label claims by type: historical evidence, implemented capability, future/roadmap.
- [ ] Include the historical path from manual lead qualification and Power BI measurement through regional operating capability, change management, attribution and Mission Control.

### Task 2: Implement responsive portfolio UI

**Files:**
- Modify: `mission-control-room/index.html`

**Produces:** Responsive enterprise-AI portfolio design with sticky navigation and readable typography.

- [ ] Add embedded CSS using a dark navy/teal control-room palette with high-contrast cards and diagrams.
- [ ] Add sticky navigation that wraps on wide screens and becomes horizontal-scroll navigation on smaller screens.
- [ ] Use a 16px minimum body text, 18px+ long-form text and responsive headings.
- [ ] Add abstract flow diagrams in HTML/CSS only; do not embed screenshots with production data.
- [ ] Add EN/PL switch with English active by default.

### Task 3: Add lightweight interaction with no rendering dependency

**Files:**
- Modify: `mission-control-room/index.html`

**Produces:** Language switching and active-section navigation while preserving full content in the static document.

- [ ] Add vanilla JS for EN/PL toggling only.
- [ ] Add IntersectionObserver for active navigation highlighting.
- [ ] Ensure failure or blocking of JavaScript does not prevent English content from rendering.

### Task 4: Public-safety and content QA

**Files:**
- Test: `mission-control-room/index.html`

**Produces:** A deployable file with no confidential implementation material.

- [ ] Scan for real Supabase URLs, API keys, authentication strings, email addresses from the original employer environment, Salesforce record IDs, internal hostnames, and exact proprietary scoring rules.
- [ ] Scan for language that implies planned capabilities are already in production.
- [ ] Parse HTML and verify unique IDs and valid language sections.
- [ ] Verify responsive CSS contains desktop, tablet and mobile rules.
- [ ] Verify the page contains no runtime `fetch()` calls and no external JS/CSS dependency required for rendering.

### Task 5: Commit source-of-truth files to GitHub

**Files:**
- Create: `mission-control-room/index.html`
- Create: `docs/superpowers/plans/2026-09-14-mission-control-room-case-study.md`

**Produces:** A GitHub-backed deployable subdirectory for a dedicated Vercel project.

- [ ] Commit the implementation plan.
- [ ] Commit the final static HTML.
- [ ] Verify the files are present on `main` after explicit user instruction to deploy this case study.

### Task 6: Vercel deployment and verification

**Produces:** Public production URL at `https://b2b-lead-qualification-engine-case-study-eliza-bingul.vercel.app/`.

- [ ] Create/import a separate Vercel project named `b2b-lead-qualification-engine-case-study-eliza-bingul` with repository `Elysee-Lab/case-studies` and root directory `mission-control-room`.
- [ ] Use Framework Preset `Other`, no build command, no output directory.
- [ ] Deploy production from `main`.
- [ ] Verify the canonical URL returns HTTP 200 and the hero text is `From Noise to Measurable Revenue`.
- [ ] Verify anonymous access in a fresh browser session.
