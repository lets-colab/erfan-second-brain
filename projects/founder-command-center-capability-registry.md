---
created: 2026-08-17
updated: 2026-08-18
type: capability-registry
status: active
version: v4.1
canonical_product: decisions/founder-intelligence-canonical-lock-2026-08-17.md
implementation_hardening: decisions/cofound-implementation-hardening-v4.1-2026-08-18.md
tags: [cofound, founder-intelligence, capabilities, integrations, v0, trust, learning]
---

# CO.FOUND — Capability, Skill & Tool Registry v4.1

> Legacy file path retained for continuity. This registry supersedes the older Founder Command Center capability states.

## Purpose

Keep one current map of what CO.FOUND requires now, what is verified/connected, what must be architected now but exposed later, what is deferred, and what is killed.

When this file conflicts with the v4 product lock or v4.1 hardening decision, the decisions win.

## Decision states

- `CORE_FOUNDATION_NOW` — invisible trust/learning/measurement infrastructure required before reliable V0.
- `V0A_CORE` — required to test orientation/navigation.
- `V0B_CORE` — required to test capture/learning/memory after V0A is usable.
- `CONNECTED_OR_REUSED` — existing verified capability/source pattern that can be reused, subject to live revalidation before production reliance.
- `ARCHITECT_NOW_UI_LATER` — preserve in contracts/data model; richer UI later.
- `NEXT_INTEGRATION` — high-value integration only after core loop works.
- `DEFERRED` — strategically retained but not needed for V0 proof.
- `EXPERIMENTAL` — may be tested but is not required architecture.
- `KILLED` — excluded unless material observed evidence reopens it.

# 1. PRODUCT SOUL — LOCKED

> **Make the company visible to the people trying to build it.**

Complementary promise:

> **Build the company. Build yourself. Find the next path forward.**

Primary cognitive modes:
- ROOM;
- MAP;
- FOCUS;
- ASK.

Contextual mechanics:
- Meeting Mode;
- Detour;
- Since You Left;
- Replay;
- Pre-Live;
- Learning / Capability;
- Momentum.

# 2. CORE FOUNDATION NOW

## Authority + permission model — CORE_FOUNDATION_NOW

Minimum contract:
`Actor -> Role -> Company Space -> Data Scope -> Action Scope`.

AI modes:
- READ;
- PROPOSE;
- explicitly authorized EXECUTE.

Cross-space access denied by default.

## Truth arbitration — CORE_FOUNDATION_NOW

Truth states:
- VERIFIED;
- PROVISIONAL;
- STALE;
- CONFLICTED;
- SIMULATED;
- UNKNOWN.

Credible source disagreement must surface as conflict unless resolved through authoritative source, effective event timestamp, corroboration, or authorized human confirmation.

## Recommendation Ledger — CORE_FOUNDATION_NOW

Record material CO.FOUND advice:
`evidence -> recommendation -> founder response -> action -> actual result -> evaluate advice -> learning`.

Minimum state includes evidence, assumptions, confidence, alternatives, expected result, accepted/modified/rejected/deferred, founder reason when captured, actual result, helpful/neutral/harmful/unresolved, and learning.

## Connector health + observability — CORE_FOUNDATION_NOW

Track where technically available:
- connection/access status;
- last successful read/sync;
- last attempted read/sync;
- freshness state/SLA;
- scope/coverage;
- latest error;
- permission state.

Material changes need an audit trail with actor, evidence, prior state, new/proposed state, timestamp, confirmation, and rollback pointer where possible.

## Metric contract — CORE_FOUNDATION_NOW

Material metrics should preserve:
- definition;
- method/formula;
- unit;
- baseline;
- target/timeframe;
- source;
- owner;
- current actual;
- update cadence/freshness;
- truth state/confidence.

## Attention Router — CORE_FOUNDATION_NOW

Route meaningful events to:
- NO_INTERRUPT;
- FOCUS;
- SINCE_YOU_LEFT;
- DIGEST;
- URGENT_FOUNDER_ALERT.

Default to the least interruptive state that preserves decision quality.

## Company bootstrap — CORE_FOUNDATION_NOW

For a new company-space:
- authorized users/roles;
- approved sources;
- proposed destination;
- <=3 primary routes;
- current actions/blockers/decisions;
- sourced money where available;
- provenance/truth status;
- founder confirmation/correction;
- baseline timestamp.

## Pilot telemetry — CORE_FOUNDATION_NOW

Measure system usefulness rather than employee productivity:
- time-to-orient;
- decision-rationale retrieval time;
- state disagreement;
- missed commitments;
- Detour outcomes;
- Recommendation Ledger outcomes;
- correction/admin burden;
- connector incidents;
- voluntary return behavior;
- MAP decision-moment use;
- capability-gap flow outcomes;
- weekly review use;
- removal test.

# 3. V0A — ORIENTATION / NAVIGATION

## ROOM — V0A_CORE

Show only:
- current destination/objective;
- evidence-based state;
- real sourced money;
- max three critical missions;
- one major blocker;
- one decision needing attention;
- meaningful change / Since You Left preview where available;
- subtle Why We Started / impact.

No unexplained execution/health score.

## MAP + Visual Action Branches — V0A_CORE

`1 destination -> <=3 primary routes -> depth`.

Connect action -> dependency/path -> driver -> outcome with provenance/truth state.

## Detour — V0A_CORE

At least one real blocker must support alternative executable routes compared on available evidence such as time, cost, capacity, dependency, risk, and history.

Detour is core V0A, not a later feature.

## FOCUS — V0A_CORE

Default max three high-leverage actions per founder/user with:
- why it matters;
- what it unlocks;
- blocker/dependency;
- evidence of completion where applicable;
- capability gap if relevant.

## Real money state — V0A_CORE

Facts only when sourced:
- invested/starting capital;
- spent;
- committed;
- available;
- revenue collected;
- actual expenses/budget values.

Models/scenarios must be visibly distinct.

## Decision -> Outcome Memory — V0A_CORE

Lightweight material decision record from day one.

## Provenance/freshness/truth status — V0A_CORE

Important state must expose source/freshness/status and conflict rather than fake certainty.

## Meaningful state change — V0A_CORE

Real progress visibly changes routes, blockers, dependencies, milestones, or capabilities.

# 4. V0B — CAPTURE / LEARNING / MEMORY

## ASK — V0B_CORE

Initial supported questions:
- What matters?
- What changed?
- What is blocked?
- What can we do instead?
- Why?
- What do I need to decide?
- What should I do next?

## Meeting Mode + ingestion — V0B_CORE

`meeting -> decision -> action -> owner -> result -> MAP/history -> next meeting`.

Ambiguous ownership/commitments must be flagged, not invented.

## Since You Left — V0B_CORE

Meaningful change only; end with the most important founder attention item.

## Correction-first updates — V0B_CORE

`source -> evidence -> proposed state -> authorized human confirm/correct -> model`.

## Basic Replay — V0B_CORE

Reconstruct captured historical state without hindsight overwrite.

## Learning through real work — V0B_CORE

At least one real flow:
`mission -> capability gap -> learn/guidance -> practice -> apply -> result -> skill evidence`.

Class A can contribute content; Learning Engine remains CO.FOUND platform capability.

## Basic Pre-Live — V0B_CORE

Explicit simulation with visible assumptions and no invented precise probability.

# 5. MOTIVATION / MOMENTUM

## Meaningful Momentum — V0A_CORE / V0B_CORE

Reward real change:
- route activation;
- blocker removal;
- dependency unlock;
- milestone achievement;
- capability growth;
- customer/impact outcome;
- team recovery/momentum.

## XP / points / streaks / levels — EXPERIMENTAL

Not required V0 architecture.

May be tested only if:
- tied to meaningful behavior/state;
- non-coercive;
- not used for employee ranking;
- shown to improve useful behavior rather than create activity farming.

# 6. SOURCE / INTEGRATION STRATEGY

Integrate before replacing.

## Reusable/previously demonstrated patterns — CONNECTED_OR_REUSED

- GitHub — canonical technical/project/skill storage and change history.
- Google Drive — approved document/evidence retrieval pattern.
- Fireflies — meeting retrieval has been used in prior Founder OS workflow.

These are not automatically production-grade CO.FOUND integrations. Revalidate connection scope, health, permissions, freshness, and end-to-end behavior before relying on them.

## High-value next integrations — NEXT_INTEGRATION

- Calendar/scheduling;
- task/project source;
- CRM/pipeline;
- selected email/communication sources;
- finance read sources.

## WhatsApp Business — ARCHITECT_NOW_UI_LATER / NEXT_INTEGRATION ONLY AFTER SCOPE SAFETY

Requires explicit account/thread scope, identity separation, permission boundaries, audit logs, no silent personal-chat ingestion, and approval gates for material commitments.

# 7. ARCHITECT NOW / UI LATER

- multiple company/venture spaces;
- shared people/roles/ownership/capacity;
- AI agents/automation as execution resources;
- richer capability graph;
- capital allocation across spaces;
- impact outcomes;
- richer historical/simulation state comparison;
- reusable business-model templates;
- mobile-first approval/FOCUS/ASK patterns;
- data export/portability and retention controls.

# 8. DEFERRED

- full Capacity Intelligence UI;
- full Class A curriculum/Skill Quest platform;
- rich skill trees/certification;
- advanced calibrated probability/forecasting;
- advanced road-not-taken analysis;
- full scenario optimizer;
- external multi-company tenancy/admin;
- cross-company benchmarking;
- native communications/docs/accounting unless integrations repeatedly fail.

# 9. KILLED

- fake metrics or unsupported success/probability scores;
- task = guaranteed revenue;
- giant 20-tab primary dashboard;
- generic Slack/Notion/task-manager clone;
- native video meeting product without repeated need;
- employee surveillance/productivity ranking;
- toxic leaderboards;
- meaningless XP farming;
- autonomous consequential hiring/firing/spending/contracts;
- all-in-one collaboration positioning;
- graph/event-sourcing backend cathedral before behavioral proof;
- claiming common market mechanisms are uniquely invented here.

# 10. ACTIVE SKILLS / PROCESS

## `skills/founder-command-center-operator/SKILL.md`

Legacy path; active content is now **CO.FOUND Operator v2.0.0** and must follow v4/v4.1.

## `drx-fable2036-reasoner`

Use for deep contradiction/history/counterfactual audits, not as evidence of future intelligence.

## `drx-architecture-convergence`

Use to classify any proposed product change and prevent architecture drift.

## `drx-memory-retriever`

Use provenance-aware retrieval patterns.

## `drx-decision-council`

Use for high-consequence adversarial review.

## `drx-prelive-simulator`

Use for evidence-aware simulations only after canonical reconstruction.

## `drx-execution-qc`

Mandatory final gate before completion claims.

# 11. ACCEPTANCE AUTHORITY

Use `evaluations/cofound-v0-acceptance.yaml` for CO.FOUND V0 acceptance.

Specification/code/tool setup is not operational completion. Behavioral requirements require live behavioral evidence.

# 12. SYNC RULE

For any new CO.FOUND feature, skill, connector, or automation:
1. retrieve v4 product lock;
2. retrieve v4.1 hardening decision;
3. retrieve this registry;
4. identify the user problem;
5. classify through architecture convergence;
6. assign a decision state;
7. update the canonical registry only when accepted;
8. preserve historical/rejected/deferred ideas;
9. never treat tool availability or generated files as completion.
