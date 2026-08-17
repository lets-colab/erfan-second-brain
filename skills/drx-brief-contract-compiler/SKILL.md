---
name: drx-brief-contract-compiler
description: Compile a long or evolving user brief into a non-lossy execution contract before designing or editing. Use when requirements span multiple turns, references, examples, corrections, or deliverables. Prevents recency bias, omitted requirements, and accidental reinterpretation.
---

# DR.X Brief Contract Compiler

## Purpose
Turn the user's request history into one executable acceptance contract before any build begins.

## Required passes
1. Recover the original ask and every later correction.
2. Separate `MUST_HAVE`, `SHOULD_HAVE`, `REFERENCE_ONLY`, `DO_NOT_DO`, and `UNKNOWN`.
3. Preserve original intent even when later implementation language changes.
4. Record named benchmarks separately from requirements.
5. Flag contradictions instead of silently choosing one interpretation.

## Output contract
Create an internal matrix with:
- user intent;
- required deliverable;
- required information architecture;
- required data/metrics;
- required visual/interaction behavior;
- required proof/evidence;
- prohibited outcomes;
- acceptance test.

## Non-loss rule
No material requirement may disappear because:
- it was stated early in the conversation;
- a later request focused on one subproblem;
- a benchmark introduced new terminology;
- the current tool makes another structure easier.

## Recency-bias gate
Before execution ask:
- What did the user ask before the latest correction?
- What requirements are older than the current visual problem?
- Did the latest feedback narrow the task, or merely expose one defect?

## Acceptance gate
Do not start a major rewrite until every `MUST_HAVE` has a planned location in the artifact.

## Season KL example
For a client growth wiki, the contract may simultaneously require:
- executive one-glance status;
- departmental report of what was built and why;
- live CRM/pipeline controls;
- campaign/outreach diagnostics;
- visual proof of shipped website experiences;
- current vs previous period context;
- detailed evidence behind drill-downs.

Treat these as concurrent requirements, not alternatives.
