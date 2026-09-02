---
name: DR.X Console
description: >-
  Evidence instrument. A light-first operator console whose semantic color
  vocabulary encodes proof status rather than progress. Amber is the resting
  state because the system is mostly unproven, and the interface says so.
created: 2026-09-02
updated: 2026-09-02
type: resource
status: active
tags: [design-system, console, tokens, drx-ai-os]
---

# DR.X Console design system

Source of truth for tokens is `console/tokens.css`. This document is the portable
export and the reasoning behind it. If a value changes there, update both.

## The governing idea

Every other decision follows from one: **proof status is the semantic axis**, the
way severity is the axis in a log viewer or diff state is the axis in a code review.
Not "healthy vs. unhealthy." Not "complete vs. incomplete." Proven vs. not.

This matters because the repository is in a state most dashboards render
dishonestly: comprehensively built, barely verified. Every contract file exists.
Verification passes. And `production_certified` is `false` with zero acceptance
tests executed. A conventional dashboard reads file presence and paints green.

So the color system is inverted from the norm. Green is rare and hard to earn.
Amber is the resting state of an honest system that has not yet been measured, and
because most of this OS is unmeasured, **the console is mostly amber**. That is the
design working, not the design warning.

## Register and reflex rejection

Register is **product**: the console serves a task, so earned familiarity wins over
distinctiveness. Density, standard affordances, and a single type family are correct.

Two reflexes were rejected before composing anything.

- **First-order.** "AI OS console" plus "Jarvis" resolves to cyan-on-black with
  glowing rings and animated telemetry. It is the single most saturated answer in
  the category and it is decoration pretending to be instrumentation.
- **Second-order.** Rejecting that lands on terminal-native: green phosphor,
  monospace body, ASCII rules. Equally reflexive, reached for precisely because the
  first was avoided.

The third path is **laboratory instrument**: light ground, ink-on-paper legibility,
a status vocabulary borrowed from assay reporting where the null result prints at
full weight. Light-first is itself the anti-reflex choice. This is a record, not a
cockpit.

## Color

Strategy: **Restrained**, the product-register floor. Neutrals carry the surface,
one accent family carries state. Status color is the only saturation on screen and
it is never decorative.

Neutrals are tinted 0.003 to 0.012 chroma toward the brand hue (68°), not toward
generic warmth. The body background is pure white, `oklch(1 0 0)`, with no hidden
warmth. Warmth lives in the status colors, not the surface.

### Light theme (default)

| Token | OKLCH | Hex | Contrast vs. surface | Role |
|---|---|---|---:|---|
| `--bg` | `oklch(1 0 0)` | `#ffffff` | — | Page ground |
| `--surface` | `oklch(0.985 0.003 68)` | `#fbfaf8` | — | Panels |
| `--surface-2` | `oklch(0.963 0.005 68)` | `#f5f2ef` | — | Rail, toolbar, table header |
| `--line` | `oklch(0.90 0.006 68)` | `#e4dedb` | — | Hairlines |
| `--line-strong` | `oklch(0.82 0.008 68)` | `#cbc3bd` | — | Emphasis borders |
| `--ink` | `oklch(0.20 0.012 68)` | `#1a1510` | 17.35 | Body and data |
| `--ink-2` | `oklch(0.44 0.012 68)` | `#57514c` | 7.45 | Labels |
| `--ink-3` | `oklch(0.52 0.010 68)` | `#6d6863` | 5.28 | Captions, provenance |

### Status vocabulary

Five states, exhaustive. Every value in the console resolves to exactly one.

| State | Light OKLCH | Hex | Ratio | Dark OKLCH | Hex | Ratio | Meaning |
|---|---|---|---:|---|---|---:|---|
| `proven` | `oklch(0.46 0.10 168)` | `#00694d` | 6.41 | `oklch(0.76 0.11 168)` | `#61c8a4` | 8.67 | Executed, evidence recorded, current |
| `partial` | `oklch(0.55 0.13 95)` | `#8a6f00` | 4.62 | `oklch(0.82 0.13 95)` | `#dec358` | 10.19 | Some evidence, incomplete coverage |
| `unproven` | `oklch(0.54 0.15 68)` | `#a55900` | 4.99 | `oklch(0.80 0.14 68)` | `#f8ab4f` | 9.25 | Defined but never executed. **Brand primary.** |
| `failed` | `oklch(0.51 0.19 27)` | `#ba1e20` | 6.07 | `oklch(0.70 0.16 27)` | `#f27166` | 6.19 | Executed and did not pass |
| `stale` | `oklch(0.52 0.02 68)` | `#71675d` | 5.29 | `oklch(0.68 0.02 68)` | `#a1968b` | 6.14 | Evidence exists but predates a material change |

All ratios measured against `--surface` in their own theme. Every pairing clears
4.5:1 for small text; none rely on the 3:1 large-text allowance.

`stale` is deliberately the only near-neutral. It is the one state meaning "this
reading is no longer bound to the current final state," and desaturation is the
honest signal for a number you should not trust.

### Rules

- `proven` never appears for a file that merely exists. It requires recorded evidence.
- `unproven` is never gray, never lowered in weight, never sorted last.
- No aggregate reads better than its worst material input.
- Status is never carried by hue alone. Each state pairs its color with a text label
  and a distinct marker shape.

### Dark theme

Ground is `oklch(0.17 0.008 68)`, a warm ink near-black rather than pure black or a
cool blue-gray. Pure black plus saturated accent is the HUD reflex; blue-gray is the
SaaS-dark reflex. Status hues hold their identity and lift in lightness to clear
contrast on the darker ground.

Three theme states are supported: `:root` carries the full light palette,
`@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`
redefines tokens, and `:root[data-theme="dark"]` repeats them so an explicit toggle
wins in both directions.

## Typography

One sans for the interface, one mono for data. This is a contrast-axis pairing, not
two similar sans-serifs, and mono here is functional: identifiers, versions, commit
refs, and YAML keys are data whose character alignment carries meaning.

- **Interface:** Inter, then `system-ui` stack.
- **Data:** IBM Plex Mono, then `ui-monospace, SFMono-Regular, Menlo, monospace`.

Fixed rem scale at a 1.15 ratio, not fluid. Users view at consistent DPI and a
clamp-scaled heading in a dense panel looks worse, not better.

| Step | Size | Use |
|---|---|---|
| `--t-xs` | 0.75rem | Provenance lines, table meta |
| `--t-sm` | 0.8125rem | Labels, status text, dense rows |
| `--t-base` | 0.9375rem | Body, table cells |
| `--t-md` | 1.0625rem | Panel titles |
| `--t-lg` | 1.375rem | Section headings |
| `--t-xl` | 1.75rem | Page title |
| `--t-readout` | 2.5rem | The readiness figure, once per page |

No display faces in labels, buttons, or data. Prose caps at 68ch; tables run dense.

## Layout

Fixed left rail plus a scrolling content column. The rail collapses to a horizontal
bar under 900px. Responsiveness is structural: columns collapse and tables gain
horizontal scroll containers. Type does not fluidly resize.

Spacing is a 4px base scale (`4 8 12 16 24 32 48 64`) with varied rhythm between
sections rather than uniform stacking.

Panels are bordered regions with a header row, not cards. There are no nested cards
and no identical repeating card grids. Where the data is tabular it is rendered as a
table, because a table is the correct affordance for scannable rows of like values.

## Motion

150 to 220ms, `ease-out-quart`. Motion conveys state only: hover feedback, theme
transition, focus. There is no page-load choreography, no counter animation, no
decorative pulse. A value that is not changing does not move.

Every transition is disabled under `prefers-reduced-motion: reduce`.

The single exception is a slow `stale` indicator fade, which encodes an actual
property of the data (age) rather than drawing attention for its own sake, and it
is also suppressed under reduced motion.

## Component states

Every interactive element ships default, hover, focus-visible, active, and disabled.
Focus is a 2px outline at 2px offset in the brand amber, never removed.

Empty states name the file that would populate them, so an empty panel teaches the
data model rather than saying "nothing here."

## Bans specific to this surface

On top of the shared absolute bans:

- No ring gauges, radial progress, or percentage dials.
- No "All systems operational" banner or any aggregate health verdict not derived
  from the worst material input.
- No progress bars for work that was never started.
- No sparklines or trend indicators without a real recorded series.
- No checkmark for existence. Checkmarks require evidence.
- No count of passing tests presented without the count of unexecuted ones.
