---
name: drx-prelive-simulator
description: Pre-live a proposed business, product, campaign, operating model, investment, or strategic decision across time before committing resources. Use when Erfan asks to imagine the future, simulate what happens, pressure-test a path, compare strategic futures, or determine how an idea could evolve from experiment to durable company. Produces evidence-aware scenarios, decision branches, failure points, leading indicators, pivot triggers, and a final go/modify/kill recommendation without presenting simulation as prediction.
status: active
owner: drx-ai-os
version: 1.0.0
---

# DR.X Pre-Live Simulator

Simulate living through the decision before committing to it. The purpose is not storytelling; it is to expose hidden dependencies, likely behavior, failure modes, option value, and the sequence by which an idea either compounds or dies.

## Core integrity rule

A pre-live simulation is a structured hypothesis, never a forecast presented as fact.

Label material claims as one of:

- `OBSERVED` — grounded in verified current evidence.
- `BASE-RATE` — supported by external or historical reference classes.
- `ASSUMPTION` — necessary but unverified premise.
- `SIMULATION` — modeled consequence within the scenario.
- `UNKNOWN` — information that could materially change the outcome.

Never assign a precise success probability unless a defensible calibrated model exists.

## Before simulating

1. Define the exact decision being tested.
2. Define success in measurable terms.
3. Identify current state, resources, constraints, team, capital, dependencies, and deadlines.
4. Retrieve relevant verified context with `$drx-memory-retriever` when personal, project, financial, or prior-decision context matters.
5. If the subject has accumulated multiple architectures or reversals, run `$drx-architecture-convergence` first and bind the simulation to the current canonical architecture.
6. For material high-impact decisions, use `$drx-decision-council` after the simulation to independently challenge the result.
7. Separate what is known today from what the simulation invents in order to explore the future.

## Canonical-path binding

A simulation must not invent a new product architecture merely because a future scenario makes a different design sound attractive.

Before the simulation starts, record:

- current `PRODUCT_SOUL`;
- current `CORE_ARCHITECTURE`;
- current `SIGNATURE_MECHANICS`;
- current `V0_BUILD`;
- current `DEFERRED` and `KILLED` decisions.

During the simulation, new ideas are labeled as `REINFORCES`, `CLARIFIES`, `EXTENDS`, `CONTRADICTS`, or `REPLACES`.

Only `CONTRADICTS` or `REPLACES` may reopen the canonical path, and only when the simulation reveals a concrete failure or a materially stronger mechanism. Otherwise preserve the locked architecture.

## 2036-in-2026 mode

Use this mode when Erfan asks for reasoning as if a far more capable future AI were available **now**, while the company, market, money, team, data, and technical reality remain in 2026.

This is a capability-lens simulation, not time travel.

Assume the reasoning system is much stronger at:

- long-horizon consistency;
- temporal memory and event reconstruction;
- contradiction detection;
- causal uncertainty modeling;
- multi-agent orchestration;
- counterfactual simulation;
- dynamic interface reasoning;
- resource allocation;
- learning from forecast error;
- maintaining one coherent world model across years.

Do **not** assume unknown 2036 products, laws, prices, market sizes, model capabilities, or competitor actions as facts.

Run two realities simultaneously:

### Intelligence reality
Ask: `If a much stronger reasoning system were advising us today, what would it notice, preserve, reject, or sequence differently?`

### 2026 execution reality
Ask: `What can the actual 2026 team build, afford, integrate, validate, and trust right now?`

The answer must reconcile the two. Future-level insight may change priorities, schemas, evidence collection, and decision rules; it may not justify building impossible future technology today.

## Simulation horizons

Use the smallest useful set of horizons. Default for a new company or product:

- `T+7 days` — behavior and execution friction.
- `T+30 days` — first proof or disproof.
- `T+90 days` — retention, repeated use, economics, organizational strain.
- `T+12 months` — product/company shape if the mechanism works.
- `T+24–36 months` — only when strategic evolution materially matters.
- `T+5–10 years` — only for compounding assets, platform evolution, organizational learning, or irreversible architecture decisions.

Do not narrate every month, day, or hour unless an event actually changes state. Compress uneventful time and expand decision-relevant moments.

## Required scenario set

Always simulate at least three paths:

### 1. Base case
The most plausible sequence if the team behaves reasonably and no extraordinary external shock occurs.

### 2. Failure / near-death case
Assume the idea is weaker than expected. Identify exactly where adoption, economics, product complexity, data quality, trust, distribution, team capacity, or competition breaks the model.

### 3. Breakout case
Assume the core mechanism genuinely works. Trace the minimum sequence that converts local usefulness into repeatable external demand and then into a defensible business.

Add a fourth `NO-BUILD / ALTERNATIVE` scenario when the opportunity cost is material.

## Pre-live workflow

1. **Enter the system.** Speak from the operating perspective of the founder/team at the starting point. Do not romanticize.
2. **Run actual behavior.** Ask what people will open, ignore, update, forget, resist, pay for, or route around.
3. **Advance only on evidence.** A feature does not become valuable because it exists; show the event that demonstrates value.
4. **Inject friction.** Add realistic blockers such as delayed approvals, dirty data, cash pressure, founder distraction, low adoption, failed acquisition, or incumbent response.
5. **Branch decisions.** At every material blocker, identify alternative actions and their tradeoffs.
6. **Track capital and capacity.** Ask what the path consumes in money, founder attention, engineering, support, trust, and time.
7. **Track learning.** Record assumption -> decision -> action -> observed result -> learning.
8. **Watch for pull.** Distinguish founder enthusiasm from user pull. Strong signals include voluntary repeated use, workflows moving into the product, users referring to product-native concepts, willingness to pay, expansion requests, and distress when removed.
9. **Find the irreversible moment.** Identify when the project becomes expensive to reverse, and require stronger evidence before that point.
10. **Run contradiction checks.** Compare future lessons against the canonical architecture; do not silently mutate it.
11. **End with decision.** Return `GO`, `MODIFY`, `PILOT ONLY`, `DEFER`, or `KILL` and state exactly what evidence would reverse the decision.

## Branch and history model

When the subject has an outcome graph or operating graph, simulate it as a time-aware graph rather than a static plan.

Each material node or edge should be able to preserve:

- creation time;
- owner;
- original assumption;
- expected outcome;
- confidence at the time;
- cost / capital committed;
- blockers encountered;
- alternative routes considered;
- decision chosen and why;
- actual result;
- financial or strategic effect when measurable;
- evidence source;
- retrospective lesson.

This enables historical playback: `what did we believe then? -> what did we choose? -> what actually happened? -> what did we learn?`

Do not rewrite history using current knowledge. Preserve the information state that existed at the time of the decision.

## Temporal operating model

For company-intelligence products, reason across three linked states:

- `PAST / REPLAY` — reconstruct the information state, decisions, actions, and outcomes without hindsight contamination.
- `PRESENT / ORIENT` — determine current truth, blockers, resources, and next-best action.
- `FUTURE / PRE-LIVE` — simulate alternative routes with explicit assumptions and uncertainty.

These should share one underlying event ledger and time-aware graph. The model must distinguish recorded history from counterfactual history.

## Financial discipline

For money-related simulations:

- distinguish cash, committed spend, revenue, pipeline, expected value, and hypothetical upside;
- use base/upside/downside ranges where appropriate;
- expose assumptions behind conversion rates or economic impact;
- never imply task completion guarantees revenue;
- when data is insufficient, say `not yet estimable` rather than manufacture precision.

## Human / agent resource simulation

When capacity is part of the problem, compare:

`FOUNDER -> EXISTING TEAM -> AUTOMATION -> AI AGENT -> INTERN -> FREELANCER -> HIRE`

Evaluate required judgment, repetition, confidentiality, error cost, supervision burden, speed, cost, and reversibility. Do not recommend employment termination or consequential personnel decisions solely from model output.

## Output contract

A strong pre-live result contains:

1. **Decision being simulated**
2. **Canonical architecture being preserved**
3. **What is known vs assumed**
4. **Base-case journey** with key moments only
5. **Near-death / failure journey**
6. **Breakout journey**
7. **Critical branch points** and alternatives
8. **What becomes the real product/business** if the idea works
9. **What we should deliberately not build**
10. **Leading indicators to watch**
11. **Kill / pivot triggers**
12. **Architecture deltas revealed by the simulation**
13. **Final recommendation** with confidence
14. **Evidence that would change the recommendation**

In `2036-in-2026` mode, also include:

15. **What future-level reasoning notices that 2026 reasoning missed**
16. **What to change today without assuming future technology exists**

For founder-facing outputs, write vividly enough that the user can mentally experience the future, but keep every simulated consequence clearly distinguishable from verified reality.

## Quality gates

Before publishing, verify:

- The simulation contains at least one credible failure path.
- The breakout case requires concrete user behavior, not wishful adoption.
- The reasoning includes opportunity cost.
- No simulated metric is presented as observed fact.
- Capital and founder attention are treated as scarce resources.
- Incumbents and substitutes are considered where relevant.
- The first experiment is smaller than the long-term vision.
- The recommendation states what would falsify it.
- Any historical replay preserves the original information state and avoids hindsight bias.
- The canonical architecture did not drift silently during the simulation.
- Future-AI capabilities were used as reasoning lenses, not invented future facts.
- The output ends with one coherent path, not a menu of incompatible product directions.

## Learning rule

After a real-world experiment reaches a meaningful checkpoint, compare the simulated path against reality:

- what happened as expected;
- what surprised us;
- which assumption failed;
- which branch was actually chosen;
- what should change in this skill or future simulations;
- whether any locked architecture decision now has enough evidence to reopen.

Record durable corrections in the Second Brain learning / review ledger when appropriate. A pre-live skill that never learns from forecast error is incomplete.
