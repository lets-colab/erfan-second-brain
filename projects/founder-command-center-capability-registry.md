---
created: 2026-08-17
updated: 2026-08-17
type: capability-registry
status: active
tags: [founder-command-center, tools, integrations, skills, sync, architecture]
---

# Founder Command Center — Capability, Skill & Tool Registry

## Purpose

Keep one canonical map of what the Founder Command Center can do now, what can be integrated next, what should be architected now but exposed later, and what should not enter V0.

This registry prevents feature drift and separates product vision from verified implementation capability.

## Decision states

- `CORE_NOW` — required for the LastBench V0 operating loop.
- `CONNECTED_NOW` — already verified through an accessible connector or existing system in the current workflow.
- `ARCHITECT_NOW_UI_LATER` — data model or permissions should anticipate it now; full UI later.
- `NEXT_INTEGRATION` — high-value integration after the V0 loop works.
- `DEFERRED` — useful, but not required to validate the product thesis.
- `KILLED_FOR_V0` — deliberately excluded because it increases complexity or adoption friction without proving the core value.

# 1. PRODUCT SOUL — LOCKED

The Founder Command Center is not another task manager or chat application.

Its job is to answer, in one glance:

1. What is our mission?
2. What is the current goal?
3. Are we on track?
4. What must each person do next?
5. What is blocking progress?
6. What is our financial state and runway?
7. What changed in meetings/decisions?
8. Why does this work matter?

# 2. CORE V0 FEATURES

## Mission Control — CORE_NOW

- North-star goal always visible.
- 30-day and 90-day targets.
- Visual progress bar.
- Founder-specific progress.
- Company execution score.
- Current bottleneck.
- Three Must-Win tasks per founder.
- Daily and weekly operating rhythm.

## Goal -> Work graph — CORE_NOW

Every meaningful task must link to at least one goal, milestone, blocker, customer/revenue outcome, or operational requirement.

The system must show why a task matters, not merely that it exists.

## Founder task engine — CORE_NOW

Each task record should support:

- owner;
- due date;
- priority;
- status;
- goal link;
- dependency;
- evidence of completion;
- expected outcome;
- points/XP category;
- blocker;
- actual result.

## Gamified execution — CORE_NOW

Reward categories:

- Outcome XP.
- Collaboration XP.
- Reliability XP.
- Learning XP.
- Impact XP.

Do not reward raw task volume as the main score.

## Why We Started — CORE_NOW

Persistent mission and emotional motivation card containing:

- founder-defined purpose;
- community/customer beneficiary;
- long-term change the company wants to create;
- evidence of impact when permission allows.

## Community mission — CORE_NOW

At least one real community-impact action per operating cycle, with evidence and owner.

# 3. MEETING + COMPANY MEMORY

## Fireflies meeting ingestion — CONNECTED_NOW / CORE_NOW

The current workflow has already used Fireflies meeting retrieval to obtain meeting summaries and action items.

Target behavior:

Meeting -> transcript/summary -> decisions -> promises -> tasks -> owners -> deadlines -> goal/revenue links.

Every meeting should create structured company memory rather than a dead transcript.

## Meeting decision ledger — CORE_NOW

Every material decision should store:

- decision;
- date;
- meeting/source;
- decision maker(s);
- rationale;
- assumptions;
- expected result;
- revisit trigger;
- later outcome.

## Calendar event linking — NEXT_INTEGRATION

Google Calendar connector exists in the current broader ChatGPT tool environment, but the Founder Command Center workflow has not yet validated an end-to-end calendar sync.

Target behavior:

Calendar event -> meeting prep card -> meeting record -> actions -> follow-up.

## Scheduler / booking layer — ARCHITECT_NOW_UI_LATER

Support external scheduling identifiers and booking links in the data model.

Potential providers:

- Calendly;
- Google Calendar appointment schedules;
- Microsoft scheduling equivalents;
- eventual native scheduler.

Do not build a native scheduling product in V0.

# 4. COMMUNICATION

## Communication strategy — LOCKED

Integrate existing channels rather than forcing founders to abandon them.

Founder Command Center becomes the operating brain over communication, not another mandatory chat network.

## Gmail / email — NEXT_INTEGRATION

Gmail is available in the current ChatGPT tool environment. Use for explicit, permissioned operating workflows such as:

- important founder/customer thread retrieval;
- turning explicit commitments into tasks;
- meeting follow-up drafts/actions;
- opportunity and risk detection.

Do not silently ingest all email.

## Slack — NEXT_INTEGRATION WHEN CONNECTOR/API IS AVAILABLE

Desired capabilities:

- ingest selected channels;
- detect commitments and blockers;
- create task candidates;
- push concise daily/weekly operating briefs;
- preserve message provenance.

## Microsoft Teams — NEXT_INTEGRATION WHEN CONNECTOR/API IS AVAILABLE

Same operating pattern as Slack; avoid separate product logic when a common communication-event adapter can serve both.

## Google Chat — DEFERRED

Use the same communication adapter architecture if real user demand appears.

## WhatsApp Business — ARCHITECT_NOW_UI_LATER

High-value for founder-led businesses but higher privacy/consent/identity risk.

Required before general use:

- explicit account and thread scope;
- sender/principal identity separation;
- permission boundaries;
- audit log;
- no silent personal-chat ingestion;
- clear human approval gates for money, promises, sensitive topics, or commitments.

# 5. FINANCE COMMAND CENTER

## Capital dashboard — CORE_NOW

Show:

- starting capital;
- spent to date;
- remaining capital;
- committed future costs;
- revenue collected;
- cash position;
- monthly burn;
- runway.

## Budget vs actual — CORE_NOW

Every material spend category should show budget, actual, variance, owner, and purpose.

## Scenario projection — CORE_NOW with manual/verified inputs

Never claim that completing a task guarantees money.

Use models such as:

`Expected Revenue = Qualified Opportunities x Observed Conversion Probability x Expected Net Revenue`

Show base, upside and downside cases.

## Accounting/bank automation — DEFERRED

Do not connect banking or move money in V0.

Architecture should allow later read-only finance connectors, but spending and payment execution remain explicit human checkpoints.

# 6. ROADMAP + STRATEGY

## Visual roadmap — CORE_NOW

One line of sight:

Today -> 30 days -> 90 days -> 1 year -> long-term mission.

Every milestone shows:

- owner;
- completion percentage;
- dependency;
- confidence;
- evidence;
- current risk.

## Scenario and detour logic — ARCHITECT_NOW_UI_LATER

The system should eventually show alternate paths when a milestone becomes blocked or assumptions fail, without silently rewriting the main strategy.

# 7. AI CHIEF-OF-STAFF CAPABILITIES

## Daily operating brief — CORE_NOW

Generate a concise founder-specific brief:

- one goal;
- three Must-Wins;
- overdue commitment;
- highest-value opportunity;
- blocker;
- money/risk alert;
- one mission/impact reminder.

## Meeting-to-action extraction — CORE_NOW

AI proposes structured tasks, decisions, owners and deadlines from meeting records.

Human confirmation should be required where ownership, financial commitment, external promise or interpretation is uncertain.

## Blocker detection — CORE_NOW

Detect:

- overdue dependencies;
- unowned action items;
- conflicting deadlines;
- repeated objections;
- stalled opportunities;
- commitments mentioned but not captured.

## Next-best-action — ARCHITECT_NOW_UI_LATER

Rank recommendations by expected effect on the current bottleneck, not generic productivity scoring.

## Decision memory — CORE_NOW

Retrieve why a decision was made and whether the expected result occurred.

## Company-state explanation — CORE_NOW

The OS should be able to answer in plain language:

- Are we on track?
- What changed today?
- Where are we losing time/money?
- What should happen next?
- What needs founder attention?

# 8. VERIFIED EXISTING DR.X SKILLS TO REUSE

## drx-architecture-convergence

Use to maintain one canonical product architecture and prevent feature drift.

Founder OS application:

- lock product soul;
- separate V0 from later capabilities;
- classify new requests;
- prevent accidental expansion into an all-in-one suite.

## drx-memory-retriever

Use as a pattern for context retrieval and provenance-aware company memory.

Founder OS application:

- retrieve meetings;
- decisions;
- prior commitments;
- project context;
- relevant operating history.

## drx-decision-council

Use for high-consequence decisions and adversarial review.

Founder OS application:

- investment decisions;
- strategic pivots;
- high-cost launches;
- major partnership terms;
- high-risk assumptions.

## drx-contextual-communicator

Use as a pattern for channel-aware, context-aware communication.

Founder OS application:

- meeting follow-ups;
- partner communication;
- founder messages;
- communication summaries;
- channel-specific tone/context.

## drx-prelive-simulator

Use before releasing major workflows or automations.

Founder OS application:

- simulate a week of founder use;
- test failure states;
- test task overload;
- test bad financial data;
- test missing meeting context;
- test false AI recommendations.

## drx-fable2036-reasoner

Use as an advanced reasoning lens, not as a factual future capability claim.

Founder OS application:

- long-horizon roadmap consistency;
- counterfactual testing;
- contradiction detection;
- decision consequence analysis.

# 9. NEW PRODUCT SKILL

Install and maintain `founder-command-center-operator` as the execution skill for this product concept.

Its responsibilities:

- reconstruct company state;
- generate one-glance founder brief;
- connect goals, tasks, meetings, money and decisions;
- classify blockers;
- calculate evidence-based progress;
- enforce three-Must-Win focus;
- preserve provenance;
- escalate uncertain money/promises/ownership decisions;
- keep mission and community impact visible.

# 10. TOOL / CONNECTOR STATUS

## Verified in current workflow

- GitHub — canonical project/skill storage and change history.
- Google Drive — approved document discovery and context retrieval.
- Fireflies — meeting summary/action-item retrieval used in the Founder OS workflow.

## Available in broader connected tool environment; validate before relying on production sync

- Google Calendar.
- Gmail.
- Notion.
- Google Drive/Docs/Sheets.
- GitHub.
- Microsoft Outlook email.

Availability does not mean the Founder Command Center has completed an end-to-end integration.

## Planned external integrations

- Slack.
- Microsoft Teams.
- Google Chat.
- WhatsApp Business.
- Calendly or equivalent scheduler.
- future finance/accounting read connectors.

# 11. V0 BUILD BOUNDARY — LOCKED

Build only enough to answer:

> Does a founder team make better, faster, more aligned decisions when goals, meetings, tasks, money, decisions and mission are compressed into one operating view?

V0 includes:

- Mission Control dashboard.
- founder tasks / three Must-Wins.
- goal and roadmap view.
- meeting/action/decision capture.
- capital + runway snapshot.
- revenue pipeline snapshot.
- points/XP tied to meaningful outcomes.
- blockers.
- daily brief.
- weekly review.
- why-we-started + impact mission.

# 12. ARCHITECT NOW / UI LATER

- calendar event entities;
- communication event entities;
- external scheduling link/provider IDs;
- permission and audit model;
- scenario records;
- structured financial connectors;
- multi-business/workspace support;
- people + AI agent identities;
- source/provenance fields;
- decision-to-outcome history.

# 13. DEFERRED

- native chat replacement;
- native video meetings;
- full accounting software;
- payroll;
- banking/payment execution;
- complex enterprise resource planning;
- public marketplace;
- broad employee surveillance/analytics;
- deep customization marketplace.

# 14. KILLED FOR V0

- forcing migration away from Slack/Teams/WhatsApp;
- points based primarily on task quantity;
- fake task-to-revenue certainty;
- auto-sending external commitments without explicit authority;
- full-company data ingestion by default;
- building every integration before LastBench proves daily usage.

# 15. SYNC RULE

Whenever a new Founder Command Center feature, skill, connector or automation is proposed:

1. retrieve this registry;
2. classify the change;
3. identify the user problem;
4. check whether an existing mechanism already solves it;
5. assign a decision state;
6. update the canonical registry only when the change is accepted;
7. preserve rejected/deferred ideas and reopen triggers;
8. do not silently treat tool availability as a finished product integration.
