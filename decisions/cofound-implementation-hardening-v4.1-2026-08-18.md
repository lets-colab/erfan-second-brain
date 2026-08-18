---
created: 2026-08-18
updated: 2026-08-18
type: implementation-decision
status: locked
version: v4.1
classification: implementation-hardening; does-not-redesign-v4
extends: decisions/founder-intelligence-canonical-lock-2026-08-17.md
related:
  - projects/founder-command-center-capability-registry.md
  - skills/founder-command-center-operator/SKILL.md
  - evaluations/cofound-v0-acceptance.yaml
---

# CO.FOUND — v4.1 Implementation Hardening

## Purpose

This decision hardens the locked v4 product architecture for implementation. It does **not** add a new product mode, change the product soul, reopen naming, or create a new feature family.

The v4 architecture remains authoritative for product behavior. This file is authoritative for the invisible trust, learning, observability, and measurement substrate required to implement it safely.

## Build authority

For new CO.FOUND implementation work, retrieve in this order:

1. `decisions/founder-intelligence-canonical-lock-2026-08-17.md` — product architecture and experiment;
2. this file — implementation-hardening contracts;
3. `projects/founder-command-center-capability-registry.md` — current capability state;
4. `skills/founder-command-center-operator/SKILL.md` — operating behavior;
5. `evaluations/cofound-v0-acceptance.yaml` — acceptance gates.

Older Founder Command Center documents remain historical context only when they conflict with the sources above.

# 1. AUTHORITY CONTRACT — CORE FOUNDATION NOW

CO.FOUND may combine multiple company spaces and sensitive operating sources. Every read, recommendation, mutation, and execution must be evaluated against identity and authority.

Minimum authorization model:

`Actor -> Role -> Company Space -> Data Scope -> Action Scope`

AI action modes:

- `READ` — may retrieve authorized context;
- `PROPOSE` — may suggest a change/action but not commit it;
- `EXECUTE` — may perform only an explicitly authorized reversible action within a narrow charter.

Protected actions require explicit current approval unless a narrower approved authority already exists:
- spending or moving money;
- contracts or material commitments;
- publishing sensitive information;
- security/account changes;
- destructive actions;
- material external promises;
- hiring/firing or equivalent consequential people decisions.

Cross-space retrieval is denied by default. A user who can see LastBench data must not automatically see Co.Lab, Class A, or private Erfan context.

# 2. TRUTH ARBITRATION CONTRACT — CORE FOUNDATION NOW

Every material state should carry one truth status:

- `VERIFIED` — supported by an authoritative fresh source or explicit human confirmation;
- `PROVISIONAL` — plausible but not yet confirmed;
- `STALE` — previously credible but outside its freshness window;
- `CONFLICTED` — credible sources disagree;
- `SIMULATED` — future/counterfactual only;
- `UNKNOWN` — insufficient evidence.

When sources disagree, CO.FOUND must not silently choose. Resolve in this order where applicable:

1. declared authoritative source for that field/domain;
2. effective event timestamp, not merely ingestion time;
3. corroborating independent evidence;
4. explicit authorized human confirmation.

If conflict remains, preserve all material claims and surface `CONFLICTED / NEEDS CONFIRMATION`.

A later summary or AI inference never outranks an authoritative primary source merely because it is newer.

# 3. RECOMMENDATION LEDGER — CORE FOUNDATION NOW

CO.FOUND must learn from its own advice, not only from founder decisions.

Add a durable `Recommendation` concept with at least:
- recommendation ID;
- company space;
- timestamp;
- triggering question/event;
- recommended route/action;
- alternatives considered;
- source evidence;
- assumptions;
- confidence at the time;
- expected outcome;
- reversibility/risk;
- founder decision: accepted / modified / rejected / deferred;
- founder reason when captured;
- chosen action/route;
- actual result;
- evaluation: helpful / neutral / harmful / unresolved;
- learning/update note.

Core learning loop:

`Evidence -> Recommendation -> Founder Decision -> Action -> Actual Result -> Evaluate Advice -> Update Guidance`

Do not auto-train opaque models from this data in V0. First preserve high-fidelity labeled history so later learning is inspectable.

# 4. CONNECTOR HEALTH + OBSERVABILITY CONTRACT — CORE FOUNDATION NOW

Correction-first capture fails if connectors silently stop syncing.

Every source/connector should expose or record where technically possible:
- connection status;
- last successful sync/read;
- last attempted sync/read;
- freshness SLA/expected cadence;
- current freshness state;
- coverage/scope of the connection;
- last error;
- permission/access state;
- source identifier;
- ingestion/event timestamp distinction.

When a critical connector is stale or failed, dependent conclusions must be downgraded and ROOM/MAP/ASK must surface the degraded evidence state.

Every material proposed or confirmed state change should be reconstructable:
- actor/agent;
- source/evidence;
- prior value/state;
- proposed/new value/state;
- timestamp;
- confirmation/approval;
- final status;
- rollback/reversal pointer when technically possible.

# 5. METRIC CONTRACT — CORE FOUNDATION NOW

A destination or outcome metric is not valid merely because a number exists.

For each material metric preserve where applicable:
- metric name;
- operational definition;
- formula/method;
- unit;
- baseline;
- target;
- target timeframe;
- source(s);
- owner;
- update cadence;
- current actual;
- freshness;
- truth status;
- confidence/quality note.

If the formula or source is not defensible, show the qualitative state instead of a fake precision score.

# 6. ATTENTION ROUTER — CORE FOUNDATION NOW

CO.FOUND must decide not only what matters, but **when and where it deserves founder attention**.

Classify each meaningful event by:
- urgency;
- deadline proximity;
- reversibility;
- financial/strategic impact;
- risk of waiting;
- whether another owner can resolve it;
- founder-specific responsibility;
- evidence confidence.

Allowed delivery states:
- `NO_INTERRUPT` — store only;
- `FOCUS` — appears in personal next actions;
- `SINCE_YOU_LEFT` — catch-up item;
- `DIGEST` — daily/weekly summary;
- `URGENT_FOUNDER_ALERT` — rare interrupt for genuinely time-sensitive material risk/decision.

Default to the least interruptive state that preserves decision quality.

# 7. COMPANY BOOTSTRAP CONTRACT — CORE FOUNDATION NOW, LIGHTWEIGHT V0

CO.FOUND needs a trustworthy first company model without turning onboarding into manual data-entry labor.

Initial bootstrap flow:

1. choose company/venture space;
2. define authorized founders/users/roles;
3. connect only approved sources;
4. identify/propose current destination/objective;
5. identify/propose <=3 primary routes;
6. identify current founder actions, blockers, and unresolved decisions;
7. identify real money fields that have authoritative sources;
8. propose a first company model with provenance/truth status;
9. founders confirm/correct;
10. record the initial baseline timestamp.

The system should say `UNKNOWN` rather than forcing users to fill every possible field.

# 8. PILOT TELEMETRY CONTRACT — CORE FOUNDATION NOW

The 30-day LastBench experiment must produce evidence, not impressions.

Instrument at minimum:
- time to answer destination/state/blocker/next-action questions;
- founder disagreement/conflict rate on company state;
- time to retrieve rationale for a material decision;
- number of meaningful commitments lost/missed;
- number of Detour recommendations shown;
- Detour accepted/modified/rejected counts;
- recommendation helpful/neutral/harmful/unresolved outcomes;
- number of manual corrections required;
- admin minutes spent maintaining/correcting CO.FOUND;
- connector stale/error incidents;
- voluntary ROOM/FOCUS return behavior;
- MAP use at real decision moments;
- capability-gap flows started/completed/applied;
- weekly founder-review use;
- removal test: whether founders materially miss the system.

Telemetry must not become employee surveillance. Measure system usefulness and operating outcomes, not human worth or minute-by-minute productivity.

# 9. V0 IMPLEMENTATION DELTA — NO PRODUCT REDESIGN

The visible v4 V0 remains unchanged:
- ROOM;
- MAP / Visual Action Branches;
- FOCUS;
- one real blocker + Detour;
- real sourced money;
- Decision -> Outcome Memory;
- provenance/freshness/confidence;
- meaningful state change;
- ASK;
- Meeting Mode;
- Since You Left;
- correction-first updates;
- basic Replay;
- one learning-through-work flow;
- basic Pre-Live.

The implementation must additionally support the invisible foundations above sufficiently to prevent false trust and to measure the experiment.

# 10. SPEC-FREEZE RULE

When older Founder Command Center material conflicts with v4/v4.1:
- v4/v4.1 wins;
- preserve old material as history;
- do not silently merge killed concepts back into the build.

Specifically:
- XP/points are experimental, not required V0 architecture;
- no company execution score without a defensible metric contract;
- Detour is core to V0A, not later;
- ROOM/MAP/FOCUS/ASK are the primary cognitive modes;
- CO.FOUND is the environment; Founder Intelligence is the brain;
- LastBench is the first company-space, not the umbrella product.

# 11. IMPLEMENTATION ORDER

1. spec freeze and stale-skill repair;
2. authority + truth-status primitives;
3. company bootstrap + real LastBench baseline;
4. V0A ROOM/MAP/FOCUS/Detour;
5. recommendation ledger + decision/outcome memory;
6. connector health + correction/audit trail;
7. attention routing;
8. V0B Meeting/ASK/Since You Left/Replay/Learning/Pre-Live;
9. pilot telemetry;
10. execution-QC against `evaluations/cofound-v0-acceptance.yaml`.

# 12. DEFINITION OF READY-TO-BUILD

CO.FOUND is `READY_TO_BUILD_V0` only when:
- current build authority is unambiguous;
- stale operator/registry instructions are repaired;
- authority and truth contracts are defined;
- the Recommendation Ledger contract exists;
- connector health/audit expectations exist;
- metric contract exists;
- V0 telemetry/acceptance gates exist.

This readiness state does not mean the product itself is implemented or verified.
