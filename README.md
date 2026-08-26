---
created: 2026-07-19
updated: 2026-08-21
type: resource
status: active
tags: [second-brain, drx-ai-os, cofound, portability, governance]
---

# Erfan Second Brain

Erfan Second Brain is the user-controlled knowledge, decision, skill, evaluation, and technical-governance layer for the DR.X AI OS and the evolving CO.FOUND operating-intelligence environment.

It is designed to remain portable across ChatGPT, Claude, Codex, OpenClaw, Obsidian, MemPalace, Graphify, and other approved tools without making any single model or memory service the source of truth.

## What this repository owns

GitHub is authoritative here for:
- DR.X skills and agent instructions;
- AI OS architecture and routing contracts;
- technical governance and approval boundaries;
- evaluation, skill-fitness, and acceptance-test definitions/evidence;
- versioned technical decisions;
- durable knowledge structures that must be reviewable and provenance-aware.

It is **not** the canonical store for every operational or source artifact.

Canonical ownership across the wider OS:
- **GitHub** — code, skills, configuration, architecture, technical decisions;
- **Notion** — structured operations, owners, deadlines, CRM, live project state and dashboards;
- **Google Drive** — documents, evidence, source files, reports, creative assets and archives;
- **memory layers** — retrieval assistance only unless a specific source is explicitly designated authoritative.

See [`architecture/DRX-AI-OS.md`](architecture/DRX-AI-OS.md).

## CO.FOUND continuity and recovery

For substantive CO.FOUND work, do not reconstruct the product only from the latest screen idea or an old Founder Command Center file.

Retrieve in this order when history/rationale matters:
1. [`projects/cofound-evolution-ledger.md`](projects/cofound-evolution-ledger.md) — canonical historical evolution: what changed, why, what was killed/restored/deferred, and how the reasoning system evolved;
2. [`decisions/founder-intelligence-canonical-lock-2026-08-17.md`](decisions/founder-intelligence-canonical-lock-2026-08-17.md) — current v4 product architecture;
3. [`decisions/cofound-implementation-hardening-v4.1-2026-08-18.md`](decisions/cofound-implementation-hardening-v4.1-2026-08-18.md) — implementation trust/learning substrate;
4. [`projects/founder-command-center-capability-registry.md`](projects/founder-command-center-capability-registry.md) — current capability states;
5. [`skills/founder-command-center-operator/SKILL.md`](skills/founder-command-center-operator/SKILL.md) — active CO.FOUND Operator v2.0.0 at the legacy folder path;
6. [`evaluations/cofound-v0-acceptance.yaml`](evaluations/cofound-v0-acceptance.yaml) — behavioral acceptance gates.

The historical Founder Command Center file is retained only as a superseded pointer; its original body remains available in Git history for reconstruction.

## Core purpose

- Preserve verified knowledge, decisions, projects, preferences, corrections and lessons.
- Give AI systems reliable context without pretending to literally be Erfan.
- Separate source facts, user-stated positions, external claims, inferences, simulations and unknowns.
- Reduce context loss and repeated decisions across AI tools.
- Turn repeatable judgment into explicit skills with evidence and QA contracts.
- Turn execution outcomes, failures, repairs, regressions, and user corrections into measurable learning evidence.
- Preserve product evolution so later AI systems understand not only **what** was decided but **why** it changed.
- Measure readiness honestly and expose important blind spots.

## Production discipline

A file, prompt, install attempt, config change, or successful tool call is not proof that a system is operational.

Material work should use:
- [`skills/_template/SKILL.md`](skills/_template/SKILL.md) for production skill contracts;
- [`skills/drx-fable-godlevel-execution/SKILL.md`](skills/drx-fable-godlevel-execution/SKILL.md) for material client deliverables where brief integrity, delivery order, executive readability, and submission readiness matter;
- [`skills/drx-brand-asset-lock/SKILL.md`](skills/drx-brand-asset-lock/SKILL.md) for branded artifacts containing protected logos, portraits, QR codes, or identity assets;
- [`skills/drx-systematic-debugger/SKILL.md`](skills/drx-systematic-debugger/SKILL.md) for root-cause diagnosis before material repair;
- [`skills/drx-execution-qc/SKILL.md`](skills/drx-execution-qc/SKILL.md) as the mandatory final completion gate using fresh final-state evidence;
- [`evaluations/acceptance-tests.yaml`](evaluations/acceptance-tests.yaml) for AI OS release gates;
- [`evaluations/acceptance-evidence.yaml`](evaluations/acceptance-evidence.yaml) for executed acceptance evidence and explicit `not_run` state;
- [`evaluations/skill-fitness.yaml`](evaluations/skill-fitness.yaml) for measured skill-version performance and regressions;
- [`evaluations/cofound-v0-acceptance.yaml`](evaluations/cofound-v0-acceptance.yaml) for CO.FOUND V0 gates;
- [`governance/authority-matrix.yaml`](governance/authority-matrix.yaml) for protected-action boundaries;
- [`observability/event-schema.yaml`](observability/event-schema.yaml) for reconstructable execution and learning evidence;
- [`routing/task-router.yaml`](routing/task-router.yaml) for default agent/source/process routing.

The `10.5/10` label is an internal quality target. Production status requires executed evidence and acceptance tests; it is never inferred from design sophistication, prompt length, installed skills, or repository commits alone.

## Verification state

The repository contains a strong verification framework, but the wider DR.X AI OS is **not production-certified** until `evaluations/acceptance-evidence.yaml` shows all critical tests passed and human owner signoff exists.

A specialist skill is not considered proven merely because it is active. Register it in `evaluations/skill-fitness.yaml`, benchmark it on representative tasks, record regressions, and use fresh final-state evidence.

## Learning loop

The intended DR.X improvement loop is:

`execute -> inspect -> fresh verification -> record outcome -> classify failure/correction -> evaluate skill version -> repair skill/process only when evidence warrants -> regression test`

For CO.FOUND product evolution, preserve an additional historical loop:

`previous state -> new evidence/correction -> change classification -> new state -> result -> durable lesson`

A longer prompt is not automatically a better skill. Skill changes should be promoted only when representative evidence shows improved or preserved quality without hidden critical regression.

## Current skill layer

Active skills on `main` include:
- DR.X memory retrieval;
- contextual communication;
- decision council;
- architecture convergence;
- pre-live simulation;
- Fable-2036 reasoning;
- Fable God-Level Execution for material client deliverables;
- systematic root-cause debugging;
- DR.X representation;
- CO.FOUND operation (active content at legacy `skills/founder-command-center-operator/` path);
- Brand Asset Lock for protected branded artifacts;
- DR.X execution/completion QC as the mandatory final gate.

Skills are reusable operating contracts, not claims that every connector or runtime is live or that every skill has passed repeatability benchmarks.

## Main knowledge notes

- [Personal assistant mission](projects/personal-second-brain.md)
- [CO.FOUND continuity memory](projects/cofound.md)
- [CO.FOUND evolution ledger](projects/cofound-evolution-ledger.md)
- [CO.FOUND v4 product lock](decisions/founder-intelligence-canonical-lock-2026-08-17.md)
- [CO.FOUND v4.1 implementation hardening](decisions/cofound-implementation-hardening-v4.1-2026-08-18.md)
- [Historical Founder Command Center pointer](projects/founder-command-center-os.md)
- [Last Bench canonical brand asset lock](decisions/last-bench-brand-asset-lock-2026-08-21.md)
- [Knowledge readiness](areas/knowledge-readiness.md)
- [Operating charter](areas/operating-charter.md)
- [Digital presenter profile](areas/digital-presenter-profile.md)
- [Source inventory](notes/source-inventory.md)
- [Knowledge change log](reviews/knowledge-change-log.md)

## Safety boundary

Never store passwords, one-time codes, recovery codes, secret keys, identity-document images, full payment credentials, private authentication links, or unapproved raw private chats.

Account or connector access is not authority to communicate, publish, spend, change security, or make commitments. Follow the authority matrix and the task-specific operating charter.

## Update rule

Every durable knowledge addition must record its source, date, confidence, and classification where material. Preserve history rather than silently rewriting it. User corrections override inferred patterns.

For material CO.FOUND evolution, update `projects/cofound-evolution-ledger.md` instead of replacing the previous reasoning with only the latest conclusion.

After a meaningful durable knowledge or capability change:
1. update `reviews/knowledge-change-log.md`;
2. reassess `areas/knowledge-readiness.md`;
3. update routing/fitness registries when a material specialist skill is added or changed;
4. state clearly whether the change improved design readiness, operational verification, or both.

## Session bootstrap

Cloud Claude Code sessions run in a throwaway container, so MemPalace and
Graphify have to be reinstalled each time. Rather than re-deriving context in
tokens, run:

```bash
bash bootstrap.sh
```

It installs both tools, registers MemPalace as a user-scope MCP server,
installs the Graphify skill, and mines this repo into the palace. Idempotent —
re-run it after any restart. `--no-mine` skips the mining step.

Then `mempalace wake-up` gives ~800 tokens of session context instead of
re-reading the repository.
