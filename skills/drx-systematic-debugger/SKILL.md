---
name: drx-systematic-debugger
description: Diagnose technical or operational failures by reproducing the symptom, tracing evidence to the failing boundary, testing one causal hypothesis at a time, repairing the root cause, and proving the repair with fresh final-state verification. Use when code, integrations, automations, deployments, workflows, data flows, or tools are broken, inconsistent, regressed, or producing unexpected results.
status: active
owner: drx-ai-os
version: 1.0.0
---

# DR.X Systematic Debugger

## Objective

Prevent patch-driven debugging. Find the most defensible root cause before making a material repair, then verify the repair against the actual failure and relevant regressions.

This skill handles failure diagnosis. It does not replace architecture judgment, domain expertise, or the mandatory final gate in `drx-execution-qc`.

## Input contract

Required:
- project namespace;
- observed symptom or failure;
- expected behavior;
- latest known working state when available;
- relevant logs, errors, inputs, outputs, diffs, or runtime state;
- authority and rollback constraints.

If the failure cannot be reproduced or observed, classify it as `INTERMITTENT` or `NOT_REPRODUCED`; do not invent a root cause.

## Required sources

Retrieve in this order:
1. current failure evidence — authoritative observation;
2. canonical code/configuration/workflow state — authoritative implementation state;
3. recent relevant changes — causal candidates, not proof;
4. logs, traces, test output, runtime state, or connector responses — execution evidence;
5. known-good reference behavior or prior working version when available;
6. external primary documentation only when the failure depends on current platform behavior.

## Allowed tools

Use only tools necessary to inspect and test the failing system. Prefer read-only inspection first. Use write tools only after a causal hypothesis is explicit and the repair is reversible or approved.

## Core rules

- Do not treat temporal correlation as causation.
- Do not stack speculative fixes.
- Change one causal variable at a time when practical.
- A workaround is not a root-cause fix unless explicitly accepted as the intended solution.
- Containment is allowed before root cause only when needed to prevent harm, data loss, security exposure, or compounding failure. Mark containment separately from repair.
- Delegated-agent confidence is not evidence. Inspect the actual state and outputs.
- After three materially different failed repair hypotheses, stop patching and escalate to architecture/system-boundary review before a fourth repair attempt.

## Workflow

### 1. Define the failure precisely

Record:
- expected behavior;
- observed behavior;
- first known occurrence;
- frequency: deterministic / intermittent / unknown;
- affected scope;
- severity;
- last known working state;
- recent changes that could plausibly affect the path.

### 2. Reproduce before repairing

Attempt the smallest faithful reproduction.

Capture:
- exact input;
- environment/state;
- command, action, or request;
- full relevant error/output;
- whether the failure repeats.

If reproduction is unsafe, destructive, expensive, or unavailable, use the strongest non-destructive evidence and state the limitation.

### 3. Trace the failing path

Follow the data/control path from input to expected output. At each material boundary record:
- input received;
- transformation performed;
- output emitted;
- expected invariant;
- actual invariant;
- evidence source.

Identify the earliest boundary where observed state diverges from expected state. Prefer the earliest defensible divergence over the most visible downstream symptom.

### 4. Compare against a working reference

When available, inspect a known-good implementation, prior version, test, configuration, or environment. List material differences rather than assuming the largest-looking difference is causal.

### 5. Form one causal hypothesis

State:
`Because <evidence>, I predict <specific cause> produces <specific failure>. If true, <minimal test> should change <observable result>.`

A hypothesis must be falsifiable. If the test result does not support it, discard or revise it instead of layering another fix on top.

### 6. Run the minimum discriminating test

Prefer the smallest test that separates competing causes. Avoid unrelated refactors, cleanup, dependency upgrades, or feature changes during diagnosis.

Record result as:
- `SUPPORTED`;
- `REFUTED`;
- `INCONCLUSIVE`.

### 7. Repair one root cause

When evidence supports a cause:
- make the smallest durable repair;
- preserve rollback path;
- avoid opportunistic refactors;
- add or update a regression test/check when practical;
- record exactly what causal mechanism the repair addresses.

### 8. Verify the repair

Run, in order when applicable:
1. original reproduction — must no longer fail;
2. direct unit/component check;
3. relevant integration/end-to-end check;
4. critical regression checks;
5. live/health/state inspection.

Then pass the result through `drx-execution-qc`. Any material change after verification invalidates affected verification evidence and requires fresh verification.

### 9. Learn from the incident

Record:
- failure class;
- root cause;
- detection gap;
- repair count;
- regression added;
- what evidence would have exposed the issue earlier;
- whether a skill, test, architecture rule, monitoring rule, or documentation contract should change.

Repeated failures of the same causal class are a system defect, not isolated incidents.

## Output contract

Return:
1. `FAILURE` — exact observed vs expected behavior;
2. `REPRODUCTION` — reproduced / intermittent / not reproduced;
3. `EVIDENCE` — strongest observations and failing boundary;
4. `ROOT-CAUSE HYPOTHESIS` — supported/refuted/inconclusive;
5. `REPAIR` — exact change or no-change decision;
6. `VERIFICATION` — fresh checks and results;
7. `REGRESSION RISK`;
8. `VERDICT` — PASS / PARTIAL / BLOCKED / NEEDS_APPROVAL / FAIL;
9. `LEARNING` — durable prevention rule when applicable.

## QA gate

PASS only when all applicable critical checks clear:
- the failure was reproduced or the evidence limitation is explicit;
- the earliest defensible failing boundary was identified;
- a falsifiable causal hypothesis was tested;
- the repair addresses the supported cause rather than only the visible symptom;
- the original reproduction passes after repair;
- relevant regression checks pass;
- verification evidence is fresh against the final state;
- no protected action occurred without authority.

## Escalation

Escalate when:
- three materially different repair hypotheses fail;
- the suspected cause is architectural rather than local;
- repair requires irreversible or protected action;
- evidence is insufficient to distinguish causes;
- the incident creates security, legal, financial, or data-integrity risk;
- the correct specialist/tool is unavailable.

For architectural escalation, use `drx-architecture-convergence` before continuing repair attempts.

## Method note

This DR.X-native contract incorporates general scientific and root-cause debugging practices, including patterns reviewed from the MIT-licensed Superpowers debugging workflow, while preserving the Erfan Second Brain's provenance, authority, routing, and completion-verification rules.
