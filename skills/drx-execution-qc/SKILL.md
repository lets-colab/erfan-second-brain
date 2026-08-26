---
name: drx-execution-qc
description: Mandatory final execution and quality-control gate for material DR.X work. Use before claiming a task, artifact, integration, system, report, presentation, workflow, or repository change is complete. Convert user requirements into acceptance criteria, verify evidence and live state, inspect output quality, identify missing or duplicated work, and return PASS, PARTIAL, BLOCKED, NEEDS_APPROVAL, or FAIL without overstating completion.
status: active
owner: drx-ai-os
version: 1.1.0
---

# DR.X Execution QC

## Objective

Prevent the most expensive class of AI failure: producing plausible work, overlooking requirements, and then claiming completion without proof.

This skill is the final gate after reasoning or execution. It does not replace domain skills; it verifies that their promised outcome was actually achieved.

## Input contract

Required:
- project namespace;
- original user request or authoritative requirement set;
- claimed deliverable/outcome;
- evidence of work performed;
- output/artifact/state to inspect;
- protected-action or approval constraints when relevant.

If the original requirement set cannot be recovered, mark the audit `BLOCKED` or `PARTIAL`; never invent missing acceptance criteria.

## Required sources

Retrieve in this order:
1. current user request and explicit corrections — authoritative;
2. canonical project requirements/brand/system files — authoritative;
3. actual produced artifact, repository diff, dashboard state, or tool result — authoritative execution evidence;
4. relevant skill contract and acceptance tests — authoritative process evidence;
5. supporting external references only when required by the task.

Never use a summary as stronger evidence than the underlying source when the source is available.

## Allowed tools

Use only tools needed to inspect the actual result. Typical examples:
- GitHub for repository state and diffs;
- Files/container for generated artifacts;
- connected source tools for actual operational state;
- browser/web only when current external verification is material.

Do not perform unrelated writes during QC.

## Workflow

### 1. Reconstruct the requirement matrix

Atomize the request into testable requirements. For every item record:
- requirement;
- source;
- priority: critical / important / optional;
- evidence required to pass;
- current evidence;
- state: PASS / FAIL / UNKNOWN / NOT_APPLICABLE.

Include later user corrections. A later correction supersedes the conflicting earlier requirement but does not erase unrelated earlier requirements.

### 2. Test definition of done

A task is not `DONE` because files exist, code was written, a setting was changed, or a tool call succeeded.

For technical or operational systems, completion requires the applicable proof chain:
1. intended change exists;
2. configuration/installation is valid;
3. live status or health check succeeds;
4. real connection or execution succeeds;
5. expected output/result is observed;
6. relevant dashboard/state reflects it;
7. critical regression/acceptance checks pass.

If any required proof is missing, use `NOT VERIFIED`, `PARTIAL`, or `BLOCKED` rather than `DONE`.

### 3. Enforce fresh final-state verification

Completion evidence must describe the current final state, not an earlier state that existed before the last relevant change.

Rules:
- any material change invalidates earlier verification evidence affected by that change;
- after the last material change, rerun every check necessary to prove the claimed outcome;
- when possible, bind verification to a final-state reference such as commit SHA, artifact hash/version, deployment ID, timestamped runtime state, or connector result;
- an old passing test, build, screenshot, health check, or delegated-agent report cannot prove a newer state;
- a delegated agent saying `done` or `tests pass` is supporting information only until the actual final artifact/state and relevant test output are inspected independently;
- if a final-state reference cannot be established, state the limitation and lower the verdict rather than laundering stale evidence into completion.

A repair performed during QC invalidates the affected checks. Rerun them before assigning `PASS`.

### 4. Completeness sweep

Check specifically for:
- omitted requirements;
- duplicated sections or features;
- requirements diluted into generic language;
- unresolved placeholders;
- broken or missing links/references;
- stale information;
- scope accidentally expanded beyond the request;
- critical dependencies left implicit;
- mismatched terminology or naming;
- unfinished handoffs.

### 5. Accuracy and provenance sweep

For every material claim verify that it is:
- supported by retrievable evidence;
- clearly labeled inference;
- clearly labeled assumption/forecast;
- or explicitly unknown.

Never allow confidence of wording to exceed evidence strength.

### 6. Artifact-specific QC

When an artifact exists, inspect the artifact itself rather than only its source text or generation code.

For documents/slides/designs/interfaces check as applicable:
- hierarchy;
- readability;
- spacing/alignment;
- overflow/cropping;
- duplicated content;
- visual consistency;
- brand compliance;
- interaction/navigation clarity;
- mobile/responsive behavior when relevant;
- links, embeds, forms, QR codes, or interactive elements;
- whether the result matches the requested audience and sophistication level.

For code/systems check as applicable:
- tests;
- build/runtime status;
- logs/errors;
- security boundaries;
- reversibility;
- configuration drift;
- actual end-to-end behavior.

### 7. Adversarial review

Ask:
- What would make the user reject this despite it looking polished?
- What did the previous attempt miss?
- What assumption am I using because it is convenient rather than proven?
- Where could a tool success be mistaken for outcome success?
- What would an expert reviewer identify in under 60 seconds?
- What is the single largest remaining failure risk?

### 8. Repair before reporting

If a failed requirement can be safely and reversibly repaired within the current task and authority, repair it and rerun the failed checks.

Do not merely describe a fix when the user asked for execution and the fix can be completed now.

### 9. Final verdict

Allowed final states:
- `PASS` — every critical requirement has direct fresh evidence from the current final state and all material acceptance checks clear.
- `PARTIAL` — useful work is complete but one or more material requirements remain unverified or incomplete.
- `BLOCKED` — completion depends on unavailable evidence, access, or external dependency.
- `NEEDS_APPROVAL` — the next required step crosses a protected boundary.
- `FAIL` — a critical acceptance criterion is demonstrably not met.

Never translate `PARTIAL`, `BLOCKED`, or `FAIL` into language implying completion.

## Output contract

Return, proportionate to task size:
1. verdict;
2. requirement coverage summary;
3. verified evidence;
4. final-state reference and verification freshness;
5. failures/gaps;
6. repairs performed;
7. remaining risk;
8. exact next action if not PASS.

For user-facing responses, keep this concise unless a detailed audit was requested.

## Evidence requirements

A completion claim must point to direct evidence from the final state, not merely evidence that an attempt occurred.

Examples:
- repository commit/final-state ref + file contents + fresh test result;
- live URL + current rendered inspection + interaction result;
- installed service + current health check + successful end-to-end invocation;
- report artifact/version + inspected pages + requirement matrix;
- connector state + successful current read/write result when authorized.

## QA gate

PASS only if all applicable critical checks are true:
- original requirements reconstructed;
- later corrections incorporated;
- no critical requirement missing;
- direct final-state evidence exists;
- affected evidence was regenerated after the last material change;
- final-state reference is recorded when technically available;
- completion wording matches verification level;
- no unsupported material claims;
- no protected action occurred without authority;
- artifact/system itself was inspected when inspectable;
- delegated results were independently checked when they materially support completion;
- the largest identified risk is below the task's acceptance threshold or explicitly accepted by the user.

## Learning loop

When QC catches a material failure:
1. identify the root cause, not only the symptom;
2. classify it: retrieval, requirement capture, reasoning, execution, tooling, verification, design, communication, governance, or other explicit class;
3. record the skill and skill version involved when available;
4. record repair count, user correction, regression result, and final evidence in the observability/evaluation layer when applicable;
5. update the relevant skill/checklist or canonical lesson when durable;
6. record what evidence would have prevented the error earlier;
7. reuse the new check on future similar work.

Repeated failure of the same class is a system defect and must trigger a skill/process update rather than another one-off correction.

## Escalation

Escalate when:
- authoritative requirements conflict;
- irreversible action is required;
- evidence cannot be obtained;
- domain-specific licensed review is necessary;
- the output remains below threshold after safe repair attempts.
