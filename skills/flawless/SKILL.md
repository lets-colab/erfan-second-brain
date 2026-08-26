---
name: flawless
description: >
  Run work to Dr.X's highest standard — the full ingest, design, verification and
  reporting discipline, as enforced steps rather than intentions. Use when the task
  is high-stakes, when a supplied file (PDF, deck, image, archive) is the source of
  truth, when the output is something a human will look at, or when the user invokes
  /flawless, "ultra mode", "god mode", or asks for flawless / trend-setting /
  perfect work.
status: active
owner: drx-ai-os
version: 1.0.0
---

# Flawless

This is a discipline, not a capability unlock. It does not change the model or
raise a limit. What it does is force the checks whose absence has actually
produced failures — each gate below exists because something real was missed.

Run every gate that applies. Say which ones you ran.

## Gate A — Ingest. Before building anything from a supplied file.

Never build from a partial reading of a source.

1. **Enumerate every stream.** Not just the obvious one.
   - PDF → text layer **and embedded images** and metadata and page count.
     `pypdf`: iterate `page.images` on every page (needs `pillow`); `extract_text()`
     alone is not a reading of the file.
   - Office docs → text, embedded media, speaker notes, comments, tracked changes.
   - Images → view them. Never infer content from a filename.
   - Archives and repos → list the tree before opening any single file.
2. **State the inventory out loud** before using it: "N pages, N images, N assets".
   Zero is a finding worth saying, not silence.
3. **Look at every asset found.** An extracted image gets viewed, not counted.
4. **Extract the design, not only the words.** Sample the brand colours. Note the
   typography, layout and logo. That is the raw material for anything visual.

An asset present in the source and absent from the output is a defect that needs a
stated reason.

> This gate exists because a CV was parsed for its text layer while the candidate's
> photograph sat embedded in the same file, unnoticed, through an entire build.

## Gate B — Design. For anything a human looks at.

The bar is a strong product team, not "tidy".

**Required:** depth and layering — real shadow, elevation, considered surfaces;
type with genuine weight and scale contrast; a palette derived from the subject's
own identity where one exists; purposeful motion; data visualisation that is
designed rather than defaulted.

**Banned unless asked for:** flat grey with hairline rules; all-monospace body
text; austerity mistaken for restraint; and the AI-default looks — cream with a
serif and terracotta, near-black with acid green, a purple-blue gradient hero,
Inter or Space Grotesk as the safe pick, emoji as section markers, everything
centred.

**Use the subject's real material.** Their photo, their brand colour, their logo.
Never a placeholder for something that was provided.

Both themes designed; tokens on bare `:root`; `body` background painted explicitly.

## Gate C — Verify. Before presenting.

1. **Look at the rendered output.** Open the file, read the document, view the
   image. Passing tests is not evidence the output is good.
2. **Hunt the defect that has not surfaced.** Adversarial input, empty input,
   malformed input, the path the happy case never touches.
3. **Check every number** against the thing that produced it. Arithmetic in a
   summary must reconcile.
4. **No claim without a check.** If you say it works, you ran it. If you say it is
   clean, you scanned it.

When the work is large or subtle, get a second pair of eyes: an independent review
pass with a different lens (correctness, spec compliance, security, the end
reader's judgement). Fix what it finds; say what held up.

## Gate D — Report.

- A real rating with the reasoning behind it. Never overstate completeness.
- Name what is genuinely blocking, and who has to act on it.
- Separate "engineered and verified" from "written but unproven".
- Correct an error in one sentence and move on. No ruminating, no repeated apology.
- Say plainly when further AI spend has low marginal value next to a cheap human
  action.

## Gate E — Cost.

Before a long autonomous run, state what it will produce and roughly what it will
cost. Prefer the cheap decisive step to the expensive thorough one when both
resolve the same uncertainty. Do not polish something whose real blocker is
elsewhere.

## What this is not

It does not make the model smarter, faster or unmetered, and it does not unlock a
hidden mode. Anything promising that is selling something. What it buys is the
elimination of a specific class of failure: the one where the work was capable and
the checking was not.
