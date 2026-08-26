---
name: replace-me
description: State exactly when this skill should run and what outcome it produces.
status: draft
owner: drx-ai-os
version: 0.1.0
---

# Skill Contract

## Objective

Define one repeatable outcome. Do not broaden the skill into an all-purpose agent.

## Input contract

Required:
- project namespace;
- goal;
- deadline or decision horizon when relevant;
- constraints;
- required output format.

Reject or escalate when a required input cannot be retrieved from an authoritative source.

## Required sources

List canonical sources in retrieval order. Mark whether each source is authoritative, supporting, or optional.

## Allowed tools

List only the tools required for this skill. Least privilege applies.

## Workflow

1. Retrieve authoritative context.
2. Validate scope and assumptions.
3. Execute the minimum sufficient workflow.
4. Preserve source provenance.
5. Run QA.
6. Return output, uncertainty, and next action.

## Output contract

Specify required structure, fields, artifact type, and level of detail.

## Evidence requirements

Every material factual claim must be one of:
- directly supported by a cited/retrievable source;
- explicitly labeled inference;
- explicitly labeled unknown or blocked.

## QA gate

Define measurable checks appropriate to this skill. Examples:
- all required sections present;
- no unsupported material claims;
- all calculations reproducible;
- no cross-project contamination;
- output matches requested format;
- protected actions were not executed without approval.

## Pass / fail

PASS only when every critical QA check clears.
FAIL when a critical check fails.
BLOCKED when required evidence or authority is unavailable.
NEEDS_APPROVAL when the next action crosses a protected boundary.

## Escalation

State exactly what requires human review, another specialist, or a different tool.
