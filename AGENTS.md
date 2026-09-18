# Case Studies — Agent Instructions

## Repository purpose

This repository publishes and maintains case-study experiences and supporting assets, including the main index and individual case-study sections.

Treat published claims, metrics, screenshots, diagrams and project descriptions as evidence-bearing content, not generic marketing copy.

## Core invariants

- One task = one branch/worktree = one writer.
- Material work must not be performed autonomously on `main`.
- Reuse the existing case-study structure before creating new parallel layouts or frameworks.
- Do not invent metrics, outcomes, clients, technologies, dates, roles, screenshots or implementation facts.
- Preserve the distinction between verified facts, assumptions, hypotheses and illustrative material.
- Do not silently rewrite an existing case study's substantive claims while performing visual or responsive work.
- Keep unrelated case studies isolated; a change for one case study must not regress another.
- Provider access never expands policy permission.
- Missing or conflicting authority must fail closed.

## Evidence and content rule

Before changing substantive content:

1. identify the source of truth for the claim;
2. verify that the repository/project evidence supports it;
3. preserve qualifications and uncertainty;
4. do not convert an estimate, hypothesis or draft into a factual claim;
5. keep Polish/English variants semantically aligned when both exist.

If evidence is unavailable, mark the point as unverified or request the source instead of filling the gap.

## UI / implementation rule

Before meaningful layout, responsive or navigation changes:

- inspect the current implementation and affected case-study section;
- reuse existing CSS/components/patterns where practical;
- check desktop and mobile behavior;
- preserve working anchors, navigation and deployment assumptions;
- avoid unrelated redesigns;
- keep accessibility and readability intact.

For large single-file HTML changes, prefer bounded edits over broad rewrites.

## Deployment safety

Repository writes, merge and deployment are separate permissions.

Do not trigger production deployment, alter deployment configuration, or merge to `main` unless explicitly authorized for the current task.

Files used only as deployment triggers must not be changed accidentally as part of unrelated work.

## Provider-neutral governance

Codex, Copilot, ChatGPT, Lovable and future agents use the same repository rules.

Lovable write permission is DEFAULT DENY unless explicitly authorized for the current scoped task.

Report evidence, changed files, verification performed and any remaining uncertainty before requesting merge.
