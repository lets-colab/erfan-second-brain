---
created: 2026-08-18
updated: 2026-08-18
type: canonical-evolution-ledger
status: active
coverage: substantial
classification: historical-continuity + decision-rationale + product-evolution
canonical_product: decisions/founder-intelligence-canonical-lock-2026-08-17.md
implementation_hardening: decisions/cofound-implementation-hardening-v4.1-2026-08-18.md
related:
  - projects/cofound.md
  - reviews/cofound-final-convergence-audit-2026-08-18.md
  - reviews/cofound-ultramax-reaudit-2026-08-17.md
---

# CO.FOUND — Evolution Ledger

## Purpose

This is the canonical historical source for **how CO.FOUND evolved**.

Future ChatGPT, Claude, Codex, OpenClaw, or other approved AI systems should use this ledger to understand:
- where the idea began;
- what changed;
- why it changed;
- which ideas were killed, restored, reframed, or deferred;
- which mistakes created durable reasoning rules;
- which concepts are original human intent versus later mechanisms;
- which conclusions are still hypotheses rather than proven facts.

This file is not the current build specification. For current product behavior use the v4 product lock; for implementation substrate use v4.1.

Coverage is `SUBSTANTIAL`, not a claim that every sentence from every historical chat is independently retrievable.

## Evidence classes used in this ledger

- `DIRECT_USER_STATEMENT` — visible/retrieved user instruction or correction.
- `PRIMARY_PROJECT_SOURCE` — uploaded/canonical project file or repository decision.
- `EXTERNAL_MARKET_EVIDENCE` — current external research used to pressure-test the idea.
- `DERIVED_INFERENCE` — interpretation made from the above.
- `SIMULATION` — hypothetical future/test scenario.
- `UNVERIFIED_RECOLLECTION` — remembered historical detail not independently re-retrieved.

A later summary does not upgrade weak evidence into stronger historical fact.

# EVOLUTION 0 — THE HUMAN ORIGIN

**State:** original intent / retained permanently.

**Source class:** DIRECT_USER_STATEMENT + PRIMARY_PROJECT_SOURCE.

The concept began as an operating system for **Erfan, Sayem, and Fahim**.

The initial problem was not “build SaaS.” It was:
- three founders carrying too much company context in their heads;
- scattered work across meetings, chat, calendar, documents, tasks, money, and memory;
- commitments disappearing;
- founders not always knowing what matters next;
- difficulty seeing whether work is actually moving the company toward the goal;
- desire for an emotionally motivating shared operating environment rather than another administrative system.

Original intent included:
- shared company truth;
- North Star / destination;
- personal next actions;
- blockers;
- meetings and commitments;
- real money;
- motivation/game feel;
- Why We Started / community meaning;
- learning when someone does not yet know how to do important work.

**Durable lesson:** preserve the human problem even when the technical architecture changes.

# EVOLUTION 1 — FOUNDER COMMAND CENTER / MISSION CONTROL

**State:** evolved; name/model superseded but many needs survive.

The first product form was a Founder Command Center / OS with:
- one-glance company state;
- North Star;
- roadmap;
- founder tasks;
- blockers;
- calendar/scheduler;
- meeting intelligence;
- communication integrations;
- finance/capital visibility;
- scenario projections;
- gamification;
- Why We Started / impact;
- AI chief-of-staff style briefing.

The conceptual value was high, but the first visual language drifted toward a dashboard with many cards.

**Why it changed:** cards describe data; founders need answers and next moves.

# EVOLUTION 2 — FAKE METRICS CREATED THE TRUST LAW

**State:** failure -> permanent rule.

Early prototype material used illustrative-looking progress, money, runway, blocker, completion, and streak values as though they were live.

This became a major trust failure.

Permanent rule created:

> `source -> method/calculation -> timestamp/freshness -> owner -> confidence/status`

If evidence is not connected or defensible, CO.FOUND must say `UNKNOWN`, `STALE`, `CONFLICTED`, or otherwise expose uncertainty rather than display fake precision.

**Durable lesson:** interface confidence must never exceed evidence confidence.

# EVOLUTION 3 — DASHBOARD CARDS -> FOUNDER QUESTIONS

**State:** retained.

The information architecture shifted from “what modules should be on the dashboard?” to “what must a founder understand or decide?”

Core questions became:
1. Where are we going?
2. What is happening / are we moving?
3. What do I need to do?
4. What is blocking us?
5. Are we financially safe?
6. What happened while I was away?
7. Why are we doing this?

This change eventually produced ROOM, FOCUS, Since You Left, Meeting Mode, and ASK.

**Durable lesson:** design around founder decisions, not software modules.

# EVOLUTION 4 — MONEY: TASK VALUE -> OUTCOME CONSEQUENCE

**State:** corrected and retained.

Early thinking risked connecting task completion too directly to revenue.

It evolved to:

`Action -> Milestone -> Objective -> Business Metric -> Financial Outcome`

Truth distinction:
- cash/spent/committed/available/revenue collected = facts when sourced;
- pipeline/expected contribution/scenario/runway assumptions = models;
- task completion never guarantees money;
- precise probability requires defensible calibration.

**Durable lesson:** money consequences need causal humility.

# EVOLUTION 5 — ROADMAP -> OUTCOME / DECISION GRAPH

**State:** evolved into MAP and Visual Action Branches.

The static roadmap began connecting:
- goals;
- drivers;
- tasks/actions;
- blockers/dependencies;
- decisions;
- outcomes;
- money.

This introduced the intuition that company work should be seen as a connected model rather than a list.

**Problem discovered:** a generic graph can become visually complex and falsely imply causality.

# EVOLUTION 6 — OUTCOME GRAPH -> VISUAL ACTION BRANCHES

**State:** signature mechanic / retained.

The graph concept became more founder-native:

`Destination -> primary routes -> dependencies -> actions -> outcomes`

Instead of exposing a spiderweb, the interface follows progressive disclosure:

> `1 destination -> <=3 primary routes -> depth`

Each important action should answer:

> **Toward what outcome?**

**Durable lesson:** MAP is navigation, not graph visualization for its own sake.

# EVOLUTION 7 — BLOCKER -> DETOUR / RECALCULATE

**State:** signature mechanic / retained.

A blocker originally appeared as a red problem to solve.

The concept evolved into the law:

> **Blocked does not mean stopped.**

When a route is blocked, CO.FOUND should preserve the destination and identify alternative executable paths.

Comparison dimensions can include:
- evidence;
- time;
- cost;
- capacity;
- dependency;
- risk;
- relevant historical result.

The strongest mental model became Google-Maps-like navigation:

`YOU ARE HERE -> DESTINATION -> ROUTES -> BLOCKER -> DETOUR -> RECALCULATE`

This is a mental model, not a plan to clone Google visual identity.

Human experience:

> **This route is blocked. The destination may not be. Recalculating.**

# EVOLUTION 8 — THE ROOM / MY VIEW -> ROOM / MAP / FOCUS / ASK

**State:** locked primary cognitive model.

Earlier concepts included:
- THE ROOM / Unified Room;
- MY VIEW;
- Board/Founder Meeting mode;
- Founder AI.

They converged into four primary human modes:

## ROOM
Shared orientation: the place founders meet the company.

## MAP
Navigation: see destination, routes, blockers, alternatives, consequences, and history.

## FOCUS
Personal action: max-three high-leverage items, why they matter, what they unlock.

## ASK
Natural-language access/control over approved company context.

**Durable lesson:** these are cognitive modes, not conventional product modules.

# EVOLUTION 9 — BOARD MODE -> CONTEXTUAL MEETING MODE

**State:** restored and clarified.

The original concept had a dedicated founder/board meeting experience.

Later architecture accidentally hid too much of this inside generic meeting ingestion.

Final interpretation:
- Meeting Mode survives;
- it is a contextual state of ROOM, not a fifth permanent top-level mode.

Before:
- meaningful changes;
- blockers;
- money changes;
- unresolved decisions;
- previous commitments.

During:
- decision;
- rationale;
- owner;
- action;
- deadline/dependency.

After:

`Meeting -> Decision -> Action -> Owner -> Result -> Memory -> Next Meeting`

**Durable lesson:** meetings should modify the company model, not die as transcripts.

# EVOLUTION 10 — CATCH-UP -> SINCE YOU LEFT

**State:** retained.

The product gained a catch-up behavior so a founder returning after time away does not reconstruct the company manually.

Meaningful changes include:
- important completion;
- blocker added/removed;
- decision;
- money event;
- material meeting;
- important customer/lead change;
- approval needed.

End with the one founder action/decision that matters most.

**Durable lesson:** compress change; do not create another activity feed.

# EVOLUTION 11 — LEARNING BECOMES PART OF WORK

**State:** original user intent restored as locked core principle.

The user clarified that a central early idea was: if the founders/team do not know how to do important work, the system should help them build the skill while doing the work.

The principle was temporarily over-deferred during minimalism audits and later restored.

Core loop:

`Real Mission -> Capability Gap -> Learn/Guidance -> Practice -> Apply -> Result -> Skill Evidence -> Person + Company Progress`

Class A may contribute:
- learning material;
- frameworks;
- mentors;
- exercises/interventions.

But the Learning Engine belongs to CO.FOUND itself.

**Durable lesson:** the company improves and the people improve at the same time.

# EVOLUTION 12 — GAMIFICATION -> MEANINGFUL MOMENTUM

**State:** reframed, retained.

Original intent included making execution game-like, rewarding, motivating, and supportive for founders/users who struggle with long unstructured work and attention.

Earlier implementations explored XP, points, streaks, and leaderboards.

Pressure testing killed performative gamification as the primary mechanism.

Final principle:

> **Reality changing is the reward.**

Reward meaningful states:
- route activation;
- blocker removal;
- dependency unlock;
- milestone achievement;
- capability growth;
- customer/impact result;
- team recovery/momentum.

XP/points/streaks/levels remain experimental only when tied to real behavior and shown to help.

Killed:
- activity farming;
- toxic leaderboards;
- employee ranking;
- shame loops;
- compulsive dark patterns;
- medical claims that CO.FOUND treats ADHD.

**Durable lesson:** design for low cognitive load, short missions, immediate feedback, visible progress, and neuroinclusive motivational support without pretending to be medical treatment.

# EVOLUTION 13 — PEOPLE / AGENTS / CAPACITY

**State:** architect-now / richer UI later.

The system expanded beyond founder tasks into execution-resource choices:

`FOUNDER -> EXISTING TEAM -> AUTOMATION -> AI AGENT -> INTERN -> FREELANCER -> HIRE`

Purpose:
- choose the right execution configuration for work;
- surface capacity conflicts;
- eventually coordinate human + AI resources.

Killed boundaries:
- employee productivity ranking;
- surveillance;
- autonomous firing/hiring.

**Durable lesson:** optimize work configuration, not human worth.

# EVOLUTION 14 — HISTORY -> DECISION -> OUTCOME MEMORY / REPLAY

**State:** signature long-term mechanism / retained.

Historical memory evolved from generic activity history into preserving what the company actually knew and believed at the time.

Material decision record:
- information available then;
- unknowns;
- assumptions;
- alternatives;
- chosen route;
- rationale;
- expected result;
- confidence at the time;
- owner;
- money/resources committed;
- actual result;
- lesson.

Permanent rule:

> **Never rewrite historical belief with hindsight.**

Replay asks:
- What did we know then?
- Why did we choose this?
- What happened?
- What did we learn?
- Have we seen a similar situation before?

# EVOLUTION 15 — SCENARIOS -> PRE-LIVE

**State:** retained.

Future planning evolved into Pre-Live:
- explore alternate routes before commitment;
- expose assumptions;
- show reversibility/failure modes;
- never present simulation as historical fact;
- never invent precise probability.

Temporal model:

`PAST / REPLAY -> PRESENT / ROOM+MAP -> FUTURE / PRE-LIVE`

**Durable lesson:** simulation supports judgment; it is not prophecy.

# EVOLUTION 16 — MANUAL COMPANY MODEL -> CORRECTION-FIRST CAPTURE

**State:** strategic requirement / retained.

A major simulated failure emerged: if founders must manually maintain the company model, CO.FOUND becomes another job.

The capture philosophy became:

`External Source -> Evidence -> Proposed State Change -> Human Confirm/Correct -> Company Model`

Key rule:

> **Correction > data entry.**

A logically brilliant recommendation based on stale data is a product failure.

# EVOLUTION 17 — GRAPH RELATIONSHIPS GET EPISTEMIC TYPES

**State:** locked trust principle.

The system must not visually imply causality when it only knows association or strategic intent.

Relationship concepts include equivalents of:
- `REQUIRES` — real operational dependency;
- `CONTRIBUTES_TO` — strategic hypothesis;
- `OBSERVED_WITH` — association;
- `FOLLOWED_BY_RESULT` — historical sequence/result;
- `SIMULATED` — future/counterfactual.

**Durable lesson:** a beautiful graph must not lie.

# EVOLUTION 18 — SINGLE COMPANY -> MULTI-COMPANY ENVIRONMENT

**State:** hierarchy locked; richer portfolio UI later.

The product stopped being defined as “the LastBench OS.”

Correct hierarchy became:

1. **CO.FOUND** — operating intelligence environment.
2. **Founder Intelligence** — reasoning/navigation/memory brain.
3. **ROOM / MAP / FOCUS / ASK** — primary human modes.
4. **Meeting Mode / Detour / Since You Left / Replay / Pre-Live / Learning / Momentum** — contextual mechanics.
5. **LastBench / Co.Lab / Class A / future ventures** — company/venture spaces inside CO.FOUND.

Important correction:

> CO.FOUND does **not** sit under Co.Lab in runtime/product hierarchy.

Co.Lab can still be an origin/implementation/distribution partner while also being a resident company-space.

# EVOLUTION 19 — BRAND / NAMING PATH

**State:** internal working name locked for continuity; public/legal brand intentionally unresolved.

### Founder Command Center
Early functional name; reflected control-room origin.

### Founder Intelligence
Became the strongest name for the intelligence/brain layer rather than the full environment.

### CO.FOUND
Current working environment name.

Semantic territory includes:
- co-found / build together;
- founder;
- found/discover;
- establish/foundation;
- `CO.` as company/collective/together.

### Hierarchy correction
An earlier assistant incorrectly framed `CO.FOUND by Co.Lab` as if CO.FOUND sat under Co.Lab. User corrected this; current hierarchy places Co.Lab inside CO.FOUND as a company-space.

### CO.MPASS
Later naming candidate based on navigation / compass semantics.

### CO.ORDINATE
Later candidate based on the double meaning of coordinating work and geographic coordinates.

### Foundry
Historical status: `UNVERIFIED_RECOLLECTION` as the earlier remembered double-meaning name. A prior assistant incorrectly claimed it had recovered a primary quote; the provenance-hardened audit retracted that claim.

Public brand remains unresolved because name/category crowding requires separate legal/domain/trademark research.

**Durable lesson:** a brand rename must not trigger an architecture redesign.

# EVOLUTION 20 — MARKET PRESSURE TEST KILLS FALSE UNIQUENESS

**State:** retained market reality.

Current-market research showed that broad mechanisms such as:
- AI chief of staff;
- work/outcome graphs;
- scenario planning;
- human + agent coordination;
- strategy/work/people/funds links;
- meeting intelligence;
- skill inference;
- agents/search/knowledge workspaces

are already being productized by established and emerging platforms.

Therefore CO.FOUND may not claim that those primitives alone are its moat.

Differentiation hypothesis became the combined behavior created by:
1. founder-native cognitive compression;
2. company navigation / Visual Action Branches;
3. Detour / Recalculate;
4. correction-first truth;
5. Decision -> Outcome Memory;
6. learning through live work;
7. meaningful Momentum;
8. Past -> Present -> Future on one model;
9. company-specific learned guidance.

None is a proven moat today.

# EVOLUTION 21 — SIMPLICITY BECOMES TWO COMPLEMENTARY LAWS

**State:** locked.

Two principles emerged at different stages and were later reconciled.

### Comprehension
`3 seconds -> 1 minute -> depth`

### MAP disclosure
`1 destination -> <=3 primary routes -> depth`

Attention rule:

> **Never show 50 things when the founder only needs the next 3.**

**Durable lesson:** cognitive simplicity and graph disclosure are different dimensions and both matter.

# EVOLUTION 22 — DR.X REASONING FAILURE: INTELLIGENCE WITHOUT CONVERGENCE

**State:** meta-learning; produced permanent reasoning skills.

Repeated assistant behavior became a problem:

`new insight -> new architecture -> new insight -> new architecture`

The assistant often generated improvements but failed to preserve one converged product.

This led to explicit architecture states and change classes.

Change classes:
- REINFORCES;
- CLARIFIES;
- EXTENDS;
- CONTRADICTS;
- REPLACES.

Architecture states:
- LOCKED;
- PROVISIONAL;
- ARCHITECT_NOW_UI_LATER;
- DEFERRED;
- KILLED;
- REOPENED.

**Durable lesson:** intelligence without convergence creates product drift.

# EVOLUTION 23 — ARCHITECTURE CONVERGENCE SKILL

**State:** active reusable reasoning capability.

`drx-architecture-convergence` was created to:
- preserve one canonical model;
- stop silent replacement;
- preserve deferred/killed ideas with reopen triggers;
- separate V0 from long-term vision;
- establish stopping rules.

The current stopping rule is:

> after final convergence for the LastBench experiment, architecture changes should come from real behavior/data/material external evidence rather than more ideation.

# EVOLUTION 24 — PRE-LIVE SIMULATOR

**State:** active reusable reasoning capability.

`drx-prelive-simulator` was upgraded to bind simulations to canonical architecture and explicitly distinguish:
- base path;
- failure / near-death path;
- breakout path;
- no-build / existing-tools path;
- service-only path.

Simulations are treated as tests of assumptions, not evidence that the future will occur.

# EVOLUTION 25 — FABLE-2036 / ULTRA-MAX REASONING

**State:** active reasoning protocol; not a literal future model claim.

The user repeatedly requested a Fable-5 / future-2036-style high-intelligence audit mode.

The resulting `drx-fable2036-reasoner` evolved to include:
- reconstruct full evolution before redesign;
- requirement coverage;
- contradiction sweep;
- belief destruction;
- missingness audit;
- seduction audit;
- overbuild audit;
- underbuild audit;
- provenance audit;
- history-fidelity audit;
- convergence before simulation;
- no-build/service alternatives;
- irreversible-moment analysis;
- kill/pivot criteria.

**Durable lesson:** the skill is a reasoning protocol, not evidence of superhuman/future model capability.

# EVOLUTION 26 — PROVENANCE CONFABULATION FAILURE

**State:** assistant failure -> permanent memory hygiene rule.

A prior assistant claimed it had “recovered” the exact earlier Foundry double-meaning wording even though accessible retrieval did not support that claim.

The error then risked being copied into durable memory.

This exposed:
- provenance confabulation;
- tool-result mismatch;
- memory laundering;
- historical backfill;
- audit-completeness overclaim.

Repairs added:
- `FULL / SUBSTANTIAL / PARTIAL` source-coverage grading;
- absolute quotation/recovery rule;
- evidence-class separation;
- memory-write provenance gate;
- tool output outranks narrative expectation;
- later summaries do not become primary evidence.

**Durable lesson:** a learning system that stores plausible mistakes as facts becomes more confidently wrong over time.

# EVOLUTION 27 — FINAL v4 CONVERGENCE

**State:** current locked product architecture.

The final convergence restored the original emotional operating experience without undoing later intelligence/trust improvements.

Product soul:

> **Make the company visible to the people trying to build it.**

Complementary promise:

> **Build the company. Build yourself. Find the next path forward.**

Human outcomes:
- clarity;
- direction;
- agency;
- resilience;
- learning;
- momentum;
- memory;
- meaning.

Core operating loop:

`SEE -> UNDERSTAND -> CHOOSE -> ACT -> LEARN -> RECALCULATE`

v4 locked:
- CO.FOUND environment;
- Founder Intelligence brain;
- ROOM / MAP / FOCUS / ASK;
- Meeting Mode;
- Visual Action Branches;
- Detour;
- Since You Left;
- real money truth;
- Decision -> Outcome Memory / Replay;
- Pre-Live;
- learning through work;
- Momentum;
- epistemic relationships;
- correction-first capture;
- LastBench V0 experiment;
- service-assisted external validation before expensive SaaS.

# EVOLUTION 28 — EXPERT GAP AUDIT: THE PRODUCT IS THERE, THE TRUST SUBSTRATE IS NOT

**State:** produced v4.1 hardening; no product redesign.

After v4 was locked, an expert audit found the strongest remaining gaps were invisible foundations rather than new user-facing features.

Missing/under-specified foundations:
1. identity + permissions + action authority;
2. truth arbitration when real sources disagree;
3. learning from CO.FOUND's own recommendations;
4. connector health, audit trail, rollback;
5. metric contract;
6. attention routing / interruption policy;
7. company bootstrap / first model construction;
8. pilot telemetry.

The conclusion was:

> **We are no longer missing the product. We are missing the trust-and-learning substrate that makes the product safe enough to believe and smart enough to improve.**

# EVOLUTION 29 — v4.1 IMPLEMENTATION HARDENING

**State:** current locked implementation substrate.

v4.1 added eight contracts without changing the product modes or soul.

## Authority
`Actor -> Role -> Company Space -> Data Scope -> Action Scope`

AI modes:
- READ;
- PROPOSE;
- narrowly authorized EXECUTE.

Cross-space access denied by default.

## Truth arbitration
Truth states:
- VERIFIED;
- PROVISIONAL;
- STALE;
- CONFLICTED;
- SIMULATED;
- UNKNOWN.

Source conflict resolution:
`authoritative source -> effective timestamp -> corroboration -> authorized human confirmation`.

## Recommendation Ledger
CO.FOUND must remember its own advice:

`Evidence -> Recommendation -> Founder Decision -> Action -> Actual Result -> Evaluate Advice -> Update Guidance`

This is the substrate for inspectable company-specific learned guidance.

## Connector health / observability
Track source health/freshness/scope/errors and preserve material change audit history.

## Metric contract
Every material metric requires definition/method/source/freshness/owner/target-baseline where applicable.

## Attention Router
Meaningful events route to:
- NO_INTERRUPT;
- FOCUS;
- SINCE_YOU_LEFT;
- DIGEST;
- URGENT_FOUNDER_ALERT.

## Company bootstrap
Propose a first model from approved sources and ask founders to confirm/correct rather than forcing exhaustive manual entry.

## Pilot telemetry
Measure whether CO.FOUND actually improves orientation, decision retrieval, commitment capture, Detour value, recommendation quality, learning, maintenance burden, return behavior, and founder-review use.

# EVOLUTION 30 — SPEC-FREEZE / STALE INSTRUCTION REPAIR

**State:** executed.

An implementation audit found active older repository instructions still told agents to:
- use old Mission Control language;
- calculate five XP categories;
- treat some later-core concepts differently.

This created a serious AI-build risk: Codex/Claude could retrieve stale instructions and rebuild ideas already killed or reframed.

Repairs:
- active operator upgraded to CO.FOUND Operator v2.0.0;
- active capability registry synchronized to v4.1;
- original Founder Command Center project file marked historical/superseded with old blob preserved in Git history;
- V0 acceptance suite added;
- build authority explicitly ordered.

**Durable lesson:** architecture lock is meaningless if active implementation prompts still contain stale architecture.

# EVOLUTION 31 — V0 SUCCESS LOGIC BECOMES COMPARATIVE, NOT AESTHETIC

**State:** locked experiment logic.

CO.FOUND must not be judged against imagination or visual beauty.

Baseline comparison should use the current operating workflow (meetings/chat/docs/tasks/AI/manual memory) and ask the same questions:
- Where are we going?
- What is blocked?
- What should I do next?
- What changed?
- What money is actually available/committed?
- Why did we make decision X?
- What alternate route is executable?
- Can the system help when someone lacks the capability to execute a mission?

Evidence should include:
- time-to-orient;
- decision-rationale retrieval;
- founder agreement/contradictions;
- missed commitments;
- Detour decision changes;
- recommendation outcomes;
- correction/admin burden;
- connector freshness incidents;
- capability learned/applied;
- voluntary return behavior;
- weekly founder review use;
- removal test.

**Durable lesson:** pretty prototype != product value.

# EVOLUTION 32 — COMMERCIAL PATH CONVERGES

**State:** strategy locked, outcome unproven.

The strongest low-risk path became:

`LastBench dogfood -> baseline comparison -> 30-day behavioral proof -> service-assisted external pilots -> reduce Co.Lab human support -> recurring paid retention -> productize repeated patterns -> only then broad SaaS`

Key distinction:
- internal usefulness != external usefulness;
- external usefulness != willingness to pay;
- willingness to pay != retention;
- retention != venture-scale defensibility.

If software does not outperform existing tools + methodology, the best mechanisms can remain a valuable internal/Co.Lab operating-intelligence method instead of forcing a SaaS thesis.

# CURRENT LOCKED PRODUCT ESSENCE

## Product soul

> **Make the company visible to the people trying to build it.**

## Product promise

> **Build the company. Build yourself. Find the next path forward.**

## Master loop

`SEE -> UNDERSTAND -> CHOOSE -> ACT -> LEARN -> RECALCULATE`

## Primary modes
- ROOM;
- MAP;
- FOCUS;
- ASK.

## Signature/supporting mechanics
- Visual Action Branches;
- Detour / Recalculate;
- Meeting Mode;
- Since You Left;
- Decision -> Outcome Memory;
- Replay;
- Pre-Live;
- Learning through live work;
- Momentum;
- Recommendation Ledger;
- correction-first capture;
- truth arbitration;
- Attention Router.

## Company spaces
- LastBench — first live pilot;
- Co.Lab;
- Class A;
- future ventures.

# RETAIN / DEFER / KILL MEMORY

## Retain/core
- three-founder origin;
- radical clarity;
- ROOM/MAP/FOCUS/ASK;
- Meeting Mode;
- real money truth;
- Visual Action Branches;
- Blocked != stopped / Detour;
- Since You Left;
- Why We Started / impact;
- learning through real work;
- meaningful Momentum;
- Decision -> Outcome Memory;
- Replay / Pre-Live;
- correction-first capture;
- provenance/truth states;
- Recommendation Ledger;
- multi-company architecture;
- Founder Intelligence as brain;
- CO.FOUND as environment.

## Architect now / UI later
- richer multi-company portfolio intelligence;
- people/roles/ownership/capacity;
- AI agents/automation as execution resources;
- richer capability graph;
- capital allocation across spaces;
- permissions/privacy UX;
- reusable business-model templates;
- data portability/retention controls;
- mobile-first approval/FOCUS/ASK patterns.

## Deferred
- full Capacity Intelligence UI;
- full Class A curriculum platform;
- rich skill trees/certification;
- advanced calibrated forecasting;
- advanced road-not-taken analysis;
- full scenario optimizer;
- external multi-company tenancy/admin;
- cross-company benchmarking;
- native communications/docs/accounting unless integrations repeatedly fail.

## Killed unless real evidence reopens
- fake metrics;
- unsupported probability scores;
- task = guaranteed revenue;
- giant 20-tab primary dashboard;
- generic Slack/Notion/task-manager clone;
- native video-meeting product without repeated need;
- employee surveillance/productivity rankings;
- toxic leaderboards;
- meaningless XP farming;
- autonomous consequential hiring/firing/spending/contracts;
- all-in-one collaboration positioning;
- graph/event-sourcing backend cathedral before behavioral proof;
- claims that common market mechanisms are uniquely invented here.

# REASONING EVOLUTION — HOW THE AI WORKING METHOD CHANGED

Earlier pattern:

`Generate -> Critique -> Redesign`

Intermediate pattern:

`Retrieve -> Challenge -> Converge -> Simulate`

Current target pattern:

`Retrieve -> Grade Evidence -> Diagnose Prior Reasoning -> Reconstruct History -> Separate Original from Later -> Classify -> Falsify -> Compare Alternatives -> Check Provenance -> Check Irreversible Risk -> Preserve Deferred Value -> Converge -> Simulate -> Baseline Against Reality -> Execute -> Fresh QC -> Learn -> Repair Memory`

Active reusable skills supporting this include:
- `drx-memory-retriever`;
- `drx-contextual-communicator`;
- `drx-decision-council`;
- `drx-representative`;
- `drx-prelive-simulator`;
- `drx-architecture-convergence`;
- `drx-fable2036-reasoner`;
- `drx-systematic-debugger`;
- `drx-execution-qc`;
- active CO.FOUND Operator at legacy path `skills/founder-command-center-operator/SKILL.md`.

These are durable procedures and contracts. They are not a claim that the underlying model weights self-modified during the conversation.

# FUTURE-AI RECOVERY RULE

Before material CO.FOUND work:

1. retrieve this evolution ledger if history/why/architecture rationale matters;
2. retrieve v4 for current product behavior;
3. retrieve v4.1 for implementation substrate;
4. retrieve the active capability registry/operator/acceptance gates for execution;
5. do not infer current architecture from old Founder Command Center documents;
6. do not erase rejected/deferred ideas from history;
7. do not resurrect them without evidence;
8. when a new insight appears, classify it as REINFORCES / CLARIFIES / EXTENDS / CONTRADICTS / REPLACES;
9. architecture changes after the current lock require real LastBench behavior, real data, or material external evidence.

# FINAL CONTINUITY SENTENCE

> **CO.FOUND evolved from a three-founder command center into a founder-native company navigation, learning, memory, and decision environment by repeatedly removing fake certainty, reducing cognitive load, turning blockers into routes, turning work into learning, turning decisions into reusable memory, and turning AI advice into evidence that can itself be evaluated and improved.**
