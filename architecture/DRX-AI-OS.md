# DR.X AI OS — Locked Architecture v1.0

Status: locked design target
Locked: 2026-08-10
Implementation branch: `build/drx-ai-os-v1`

## Objective

Build a founder operating system that reduces context loss, repeated decisions, tool fragmentation, and low-quality AI output while increasing execution speed, traceability, repeatability, and safe delegation.

This architecture is a design target, not a claim of guaranteed business success. The implementation earns production status only after passing the acceptance gates in `evaluations/acceptance-tests.yaml`.

## Core layers

### 1. Executive interface

**ChatGPT** is the executive command and decision interface.

Responsibilities:
- clarify goals and constraints;
- make or frame strategic decisions;
- route work to the correct execution engine;
- synthesize outputs;
- challenge weak assumptions;
- require evidence for material claims;
- surface decisions requiring human approval.

ChatGPT is not the low-level runtime orchestrator.

### 2. Runtime control plane

**OpenClaw Gateway** is the technical orchestrator.

Responsibilities:
- dispatch approved jobs;
- enforce tool and permission policy;
- connect specialist agents and local tools;
- preserve execution logs;
- isolate risky execution where possible;
- provide an auditable runtime boundary.

### 3. Specialist execution engines

- **Claude** — deep synthesis, long-document work, creative and strategic development.
- **Codex** — engineering, repository work, tests, refactors, deployment preparation.
- **Other agents** — admitted only when they replace a layer, reduce cost, materially improve capability, or solve a documented bottleneck.

### 4. Skill layer

Skills define repeatable operating intelligence.

Sources:
- curated official Google Skills where directly useful;
- selected engineering skill patterns;
- private DR.X skills stored in this repository.

Every production DR.X skill should define:
1. input contract;
2. required sources;
3. allowed tools;
4. workflow;
5. output contract;
6. evidence requirements;
7. QA checks;
8. pass/fail criteria;
9. escalation or approval rules.

### 5. Knowledge router and canonical truth

No single memory system is authoritative.

Canonical ownership:
- **GitHub** — code, agent instructions, skills, configuration, technical decisions.
- **Notion** — structured operations, project state, owners, deadlines, CRM and execution dashboards.
- **Google Drive** — documents, evidence, source files, reports, creative assets and archives.

The knowledge router retrieves from the authoritative source appropriate to the task. Derived summaries must preserve provenance.

### 6. Memory acceleration

**TencentDB Agent Memory** is a pilot/read-assist layer only.

Rules:
- memory may accelerate recall but must not override canonical sources;
- project and business namespaces must be isolated;
- memory writes require provenance metadata;
- cross-project retrieval is denied by default;
- promotion beyond pilot requires the isolation and provenance tests in the acceptance suite.

### 7. Governance and security

Principles:
- least privilege;
- read-only by default;
- secrets are never stored in this repository;
- external publishing, spending, security changes and destructive actions require approval unless a narrower approved charter exists;
- untrusted content is processed with restricted tools and minimal permissions;
- risky execution is sandboxed or performed in disposable clones/containers.

See `governance/authority-matrix.yaml`.

### 8. Observability

Material agent work must be reconstructable.

Log:
- request/task ID;
- project namespace;
- agent/model;
- skill invoked;
- sources read;
- tools/actions used;
- files/data changed;
- approvals requested and granted;
- result/status;
- failures;
- cost or usage where available.

See `observability/event-schema.yaml`.

### 9. Evaluation

Production work is measured against deterministic acceptance criteria, not subjective confidence.

Minimum gates:
- authoritative context survives handoffs;
- no cross-project memory contamination;
- sensitive writes cannot bypass approval;
- material outputs are traceable to evidence;
- repeated runs consistently clear QA thresholds;
- malicious instructions in untrusted content cannot expand permissions;
- failures can be reconstructed and reversible changes can be rolled back.

## Routing doctrine

Default task ownership:
- executive decision / synthesis -> ChatGPT;
- long-form synthesis / creative depth -> Claude;
- repository engineering -> Codex;
- runtime automation / local dispatch -> OpenClaw;
- canonical business state -> retrieve from Notion;
- canonical documents/evidence -> retrieve from Drive;
- canonical technical state -> retrieve from GitHub;
- memory -> assist retrieval only.

The router must choose the simplest capable path. Do not spawn multiple agents merely to create the appearance of sophistication.

## Admission rule for new tools

A new tool enters the core architecture only if it demonstrably does at least one of the following:
- replaces an existing layer with lower total complexity;
- materially reduces cost;
- materially improves reliability;
- creates a needed capability that does not already exist;
- solves a documented bottleneck with measurable impact.

Otherwise: reject, watch, or sandbox.

## Definition of 10.5/10

`10.5/10` is an internal quality target meaning the system has cleared its specified acceptance tests. It is not a guarantee of market position, income, productivity percentage, or business success.
