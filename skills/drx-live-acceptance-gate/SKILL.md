---
name: drx-live-acceptance-gate
description: Prevent false completion claims after editing live systems. Use after Notion, GitHub, dashboards, documents, automations, or other connected artifacts are changed. Requires re-fetching the actual live artifact, checking against the brief contract, and logging unresolved defects before calling work done.
---

# DR.X Live Acceptance Gate

## Prime rule
`WRITE SUCCESS != TASK COMPLETE`

A tool returning success proves only that a mutation was accepted. It does not prove the final artifact is coherent, visually correct, current, non-duplicated, or aligned with the user's brief.

## Mandatory post-edit loop
After every material build:
1. Re-fetch the actual live artifact.
2. Compare it against the compiled brief contract.
3. Inspect ordering, labels, duplicate sections, stale views, filters, broken/deleted blocks, and contradictory claims.
4. Re-check key metrics against authoritative sources where applicable.
5. Run the one-glance/dashboard audit if client-facing.
6. Run a regression sweep against the reference benchmark and previous accepted state.
7. List unresolved defects internally.
8. Only then assign `PASS`, `PASS_WITH_LIMITS`, or `FAIL`.

## Completion language
Use `done`, `fixed`, `live`, `ready`, or `submission-ready` only when the acceptance gate passes.
If not verified, say `changed but not yet accepted` or `not verified`.

## Regression sweep
Explicitly check:
- requirement dropped during rewrite;
- stale historical metric shown as current;
- client jargon returned;
- duplicate front door created;
- live view filters still point to previous period;
- proof/evidence became more prominent than decision content;
- child page/database accidentally deleted or orphaned;
- new visual element exists but sits in the wrong hierarchy;
- user's latest correction was implemented while an earlier requirement regressed.

## Two-pass rule
For high-stakes client deliverables:
- Pass 1: builder verifies implementation.
- Pass 2: adversarial reviewer tries to reject it.

A 10.5/10 claim requires both passes plus no unresolved P0/P1 defect.
