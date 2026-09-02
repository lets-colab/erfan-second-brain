---
created: 2026-09-02
updated: 2026-09-02
type: resource
status: active
tags: [design, console, drx-ai-os, product-context]
---

# Product

## Register

product

## Surface

The DR.X Console: a live operator surface for this repository. It renders the
real, current state of the AI OS from the repository's own contract files. It is
an instrument, not a landing page and not a report.

## Users

One primary user: Erfan, operating the DR.X AI OS. He opens the console to answer
a single question that the rest of this repository exists to make answerable:

> Is this system actually verified, or does it only look built?

Secondary readers are agents and collaborators who need the same answer without
reading eleven YAML files by hand.

## Product Purpose

`AGENTS.md` rule 3 governs this repository: *confidence of wording may not exceed
evidence strength.* Rule 15 refuses to accept setup evidence as completion. Rule 17
requires the words `not verified`, `partial`, `blocked`, `needs approval`, or
`failed` when final-state evidence is incomplete. Rule 20 forbids calling the OS
production-ready merely because architecture files and skills exist.

The console is the visual enforcement of those rules. Its purpose is to make the
gap between **what exists** and **what is proven** impossible to miss or overstate.

Success is measured one way: a person who glances at this console for five seconds
arrives at a reading of system health no more confident than the evidence supports.

## The core design problem

Dashboards inflate. The default grammar of the form rewards green checkmarks,
rising numbers, and completion percentages, because those read as progress. This
repository's constitution forbids exactly that grammar.

The current honest state is:

- overall knowledge readiness **3.5 / 10.5**, governed by the lowest material dimension
- **0 of 11** acceptance tests executed
- `production_certified: false`, `human_owner_signoff: false`
- most production skills at `benchmark_status: not_run`
- Graphify output stale relative to the repository it describes

A conventional dashboard would render this as a wall of green, because every file
is present and the verification script passes. The console must render it as what
it is: a well-built system that has not yet been proven, which is a different and
more useful thing to know.

## Brand Personality

Instrument, ledger, witness. The console has the manner of laboratory apparatus:
it reports the reading, including the null result, at the same weight as any other.
It does not congratulate, warn theatrically, or editorialize.

Three words: **exacting, candid, unhurried**.

## Anti-references

The console must not become the thing its own repository would fail in review.

- **The Iron Man HUD.** Cyan on black, glowing rings, radial sweeps, scanline
  overlays, floating hexagons, animated telemetry that measures nothing. "Jarvis"
  names a relationship with a system, not a visual style, and this is the first
  reflex to reject.
- **The terminal-native escape hatch.** Green phosphor, full-monospace body text,
  ASCII borders. This is the second reflex, reached for precisely because the first
  was rejected, and it is equally generic.
- **Health-score theater.** A large percentage, a ring gauge, a green "All systems
  operational" banner. Any single number that flattens eleven unexecuted tests into
  one reassuring figure violates rule 20.
- **Completion framing.** Progress bars implying inevitability, checkmarks for
  existence rather than evidence, "X of Y complete" where Y was never attempted.
- **Decorative telemetry.** Sparklines with no series behind them, counters that
  animate for drama, live-looking motion on static values.

## Design Principles

1. **Evidence over existence.** A file existing is not a passing state. Presence and
   proof are separate axes and must be separately visible.
2. **The null result is a first-class reading.** `not_run` is displayed with the same
   typographic weight and color commitment as `verified`. It is never gray, never
   collapsed, never sorted to the bottom to make the view look better.
3. **The instrument does not flatter.** No aggregate number that reads better than
   its worst input. Where the repository governs by lowest material dimension, the
   console shows that dimension, not the mean.
4. **Every value is traceable.** Each figure names the file it came from. Nothing on
   screen is authored by the console itself.
5. **Density is respect.** This user reads YAML for a living. Show the real rows.
   Do not paginate, summarize, or hide behind progressive disclosure what fits.

## Liveness

The console holds no data of its own. `scripts/build_console_state.py` reads the
repository's contract files and emits the state the console renders. Regenerating
is the only way its contents change, and CI regenerates on every push to `main`.
A stale console is therefore visible as a stale timestamp rather than as
confidently wrong numbers.

## Accessibility

WCAG 2.1 AA, verified rather than assumed, consistent with the repository's
existing evidence standard.

- Contrast checked numerically for every ink and status color on both themes.
- Status is never carried by color alone. Every state carries a text label, and the
  status marker differs in shape as well as hue.
- Full keyboard operation with visible focus. Semantic HTML first.
- `prefers-reduced-motion` honored on every transition.
