---
created: 2026-07-19
updated: 2026-08-17
type: resource
status: active
tags: [second-brain, drx-ai-os, cofound, portability, governance]
---

# Erfan Second Brain

Erfan Second Brain is the user-controlled knowledge, decision, skill, and technical-governance layer for the DR.X AI OS and the evolving CO.FOUND operating-intelligence environment.

It is designed to remain portable across ChatGPT, Claude, Codex, OpenClaw, Obsidian, MemPalace, Graphify, and other approved tools without making any single model or memory service the source of truth.

## What this repository owns

GitHub is authoritative here for:
- DR.X skills and agent instructions;
- AI OS architecture and routing contracts;
- technical governance and approval boundaries;
- evaluation and acceptance-test definitions;
- versioned technical decisions;
- durable knowledge structures that must be reviewable and provenance-aware.

It is **not** the canonical store for every operational or source artifact.

Canonical ownership across the wider OS:
- **GitHub** — code, skills, configuration, architecture, technical decisions;
- **Notion** — structured operations, owners, deadlines, CRM, live project state and dashboards;
- **Google Drive** — documents, evidence, source files, reports, creative assets and archives;
- **memory layers** — retrieval assistance only unless a specific source is explicitly designated authoritative.

See [`architecture/DRX-AI-OS.md`](architecture/DRX-AI-OS.md).

## Core purpose

- Preserve verified knowledge, decisions, projects, preferences, corrections and lessons.
- Give AI systems reliable context without pretending to literally be Erfan.
- Separate source facts, user-stated positions, external claims, inferences, simulations and unknowns.
- Reduce context loss and repeated decisions across AI tools.
- Turn repeatable judgment into explicit skills with evidence and QA contracts.
- Measure readiness honestly and expose important blind spots.

## Production discipline

A file, prompt, install attempt, config change, or successful tool call is not proof that a system is operational.

Material work should use:
- [`skills/_template/SKILL.md`](skills/_template/SKILL.md) for production skill contracts;
- [`skills/drx-execution-qc/SKILL.md`](skills/drx-execution-qc/SKILL.md) before claiming completion;
- [`evaluations/acceptance-tests.yaml`](evaluations/acceptance-tests.yaml) for AI OS release gates;
- [`governance/authority-matrix.yaml`](governance/authority-matrix.yaml) for protected-action boundaries;
- [`observability/event-schema.yaml`](observability/event-schema.yaml) for reconstructable execution;
- [`routing/task-router.yaml`](routing/task-router.yaml) for default agent/source routing.

The `10.5/10` label is an internal quality target. Production status requires evidence and acceptance tests; it is never inferred from design sophistication alone.

## Current skill layer

Active skills on `main` include:
- DR.X memory retrieval;
- contextual communication;
- decision council;
- architecture convergence;
- pre-live simulation;
- Fable-2036 reasoning;
- DR.X representation;
- Founder Command Center operation;
- DR.X execution/completion QC.

Skills are reusable operating contracts, not claims that every connector or runtime is live.

## Main knowledge notes

- [Personal assistant mission](projects/personal-second-brain.md)
- [CO.FOUND](projects/cofound.md)
- [Founder Command Center](projects/founder-command-center-os.md)
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

After a meaningful durable knowledge or capability change:
1. update `reviews/knowledge-change-log.md`;
2. reassess `areas/knowledge-readiness.md`;
3. state clearly whether the change improved design readiness, operational verification, or both.
