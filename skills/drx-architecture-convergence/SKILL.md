---
name: drx-architecture-convergence
description: Maintain one canonical product or system architecture while allowing new evidence to refine it without silent drift. Use when a long strategy discussion accumulates many ideas, audits, reversals, deferred features, simulations, or competing architectures and Erfan asks for the final path, re-audit, lock, or whether prior changes have caused confusion.
status: active
owner: drx-ai-os
version: 1.0.0
---

# DR.X Architecture Convergence

Prevent intelligent iteration from becoming architectural drift.

## Core principle

New insight must update a canonical model deliberately. It may not silently replace, duplicate, or blur an earlier decision.

## Canonical hierarchy

Always separate:

1. `PRODUCT_SOUL` — the irreducible user promise and governing principles.
2. `CORE_ARCHITECTURE` — durable system layers, entities, and relationships.
3. `SIGNATURE_MECHANICS` — interactions or behaviors that express the product's distinctive value.
4. `V0_BUILD` — the smallest current experiment.
5. `LATER_CAPABILITIES` — deliberately deferred but architecturally anticipated capabilities.
6. `KILLED` — rejected ideas with reason and explicit reopen trigger.

A change at a lower level must not silently rewrite a higher level.

## Decision states

Every material feature or architectural decision must have one status:

- `LOCKED` — current canonical direction; reopen only with new evidence or a contradiction.
- `PROVISIONAL` — plausible but still being tested.
- `ARCHITECT_NOW_UI_LATER` — schema/model support now, user interface later.
- `DEFERRED` — deliberately postponed; no current implementation work.
- `KILLED` — rejected for a recorded reason.
- `REOPENED` — prior decision is under review because new evidence met its reopen trigger.

Never use `later` to mean both important and unimportant. Record the exact state.

## Change classification

Before accepting any new idea, classify it as exactly one:

- `REINFORCES` — supports the canonical model; no architecture change.
- `CLARIFIES` — makes an existing concept more explicit; no architecture change.
- `EXTENDS` — adds a compatible capability without displacing the core.
- `CONTRADICTS` — conflicts with a locked decision and requires reopening it.
- `REPLACES` — intentionally supersedes a prior locked decision; must state what is replaced and why.

If the model cannot classify the change, do not integrate it yet.

## No-silent-replacement rule

Whenever an answer proposes a materially different architecture, it must include:

- previous canonical decision;
- new evidence or reasoning;
- exact delta;
- what remains unchanged;
- what is now deprecated;
- why the replacement is worth migration cost.

Without that record, keep the previous canonical decision.

## Convergence workflow

1. Retrieve the latest canonical project specification and relevant decisions.
2. Reconstruct the current architecture in one compact model before proposing changes.
3. Inventory all meaningful ideas from the discussion or source material.
4. Deduplicate synonyms and nested concepts.
5. Assign every item a decision state.
6. Identify contradictions between recent answers and the canonical model.
7. Restore any signature mechanic that was accidentally hidden by simplification.
8. Reject duplicate surfaces when a capability can be contextual rather than top-level.
9. Produce exactly one recommended path.
10. Record unresolved hypotheses separately from architecture.
11. Define what evidence is allowed to reopen locked decisions.

## Rejected-feature audit

When asked to re-audit rejected ideas, do not merely list them. For each rejected or deferred idea, answer:

- What original user problem was it trying to solve?
- Is that problem still real?
- Is another retained mechanism already solving it?
- Was the idea killed because it is bad, or merely because it is wrong for V0?
- Would omitting it create architectural debt later?
- What evidence would justify reopening it?

Then classify as `CORE_NOW`, `ARCHITECT_NOW_UI_LATER`, `DEFERRED`, or `KILLED`.

## Path lock

A final architecture is considered `BUILD-FINAL` when:

- the product soul is stable;
- signature mechanics are explicit;
- no material user problem is left without a mechanism;
- V0 is smaller than the full vision;
- deferred capabilities have clear boundaries;
- killed capabilities have recorded reasons;
- no two top-level surfaces solve the same job;
- new insight can be absorbed without redesigning the core data model;
- further conceptual change is less valuable than real-world evidence.

After `BUILD-FINAL`, default to experimentation, implementation, and evidence collection rather than new ideation.

## Contradiction check

Before publishing a major product verdict, compare it against the last locked architecture and explicitly flag:

- accidental removals;
- renamed concepts that only appear new;
- ideas previously killed but silently restored;
- V2 capabilities accidentally promoted into V0;
- signature mechanics accidentally demoted into infrastructure;
- product vision accidentally shrunk to match MVP scope;
- MVP accidentally expanded to match long-term vision.

## Output contract

Return:

1. `CANONICAL PRODUCT SOUL`
2. `CANONICAL ARCHITECTURE`
3. `SIGNATURE MECHANICS`
4. `V0 BUILD`
5. `ARCHITECT NOW / UI LATER`
6. `DEFERRED`
7. `KILLED + REOPEN TRIGGERS`
8. `CHANGES SINCE LAST LOCK`
9. `UNRESOLVED HYPOTHESES`
10. `ONE PATH FORWARD`

Do not produce multiple competing final architectures unless Erfan explicitly requests alternatives.

## Quality gate

Before declaring a final path, verify:

- exactly one canonical architecture exists;
- the answer distinguishes vision from V0;
- every important prior idea is accounted for;
- the user can tell what is locked versus still hypothetical;
- no new feature was added merely because it sounded sophisticated;
- no valuable feature was killed merely because it was not immediate;
- the architecture remains understandable in one diagram;
- the recommendation can survive a new idea without collapsing into another redesign.
