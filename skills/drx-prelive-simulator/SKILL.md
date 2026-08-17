---
name: drx-prelive-simulator
description: Pre-live a proposed business, product, campaign, operating model, investment, or strategic decision across time before committing resources. Use when Erfan asks to imagine the future, simulate what happens, pressure-test a path, compare strategic futures, or determine how an idea could evolve from experiment to durable company. Produces evidence-aware scenarios, decision branches, failure points, leading indicators, pivot triggers, and a final go/modify/kill recommendation without presenting simulation as prediction.
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
5. For material high-impact decisions, use `$drx-decision-council` after the simulation to independently challenge the result.
6. Separate what is known today from what the simulation invents in order to explore the future.

## Simulation horizons

Use the smallest useful set of horizons. Default for a new company or product:

- `T+7 days` — behavior and execution friction.
- `T+30 days` — first proof or disproof.
- `T+90 days` — retention, repeated use, economics, organizational strain.
- `T+12 months` — product/company shape if the mechanism works.
- `T+24–36 months` — only when strategic evolution materially matters.

Do not narrate every month. Jump to decision-relevant moments.

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
10. **End with decision.** Return `GO`, `MODIFY`, `PILOT ONLY`, `DEFER`, or `KILL` and state exactly what evidence would reverse the decision.

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
2. **What is known vs assumed**
3. **Base-case journey** with key moments only
4. **Near-death / failure journey**
5. **Breakout journey**
6. **Critical branch points** and alternatives
7. **What becomes the real product/business** if the idea works
8. **What we should deliberately not build**
9. **Leading indicators to watch**
10. **Kill / pivot triggers**
11. **Final recommendation** with confidence
12. **Evidence that would change the recommendation**

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

## Learning rule

After a real-world experiment reaches a meaningful checkpoint, compare the simulated path against reality:

- what happened as expected;
- what surprised us;
- which assumption failed;
- which branch was actually chosen;
- what should change in this skill or future simulations.

Record durable corrections in the Second Brain learning / review ledger when appropriate. A pre-live skill that never learns from forecast error is incomplete.
