---
created: 2026-08-21
updated: 2026-08-21
type: decision
status: active
project: Last Bench
owner: drx-ai-os
---

# Last Bench Brand Asset Authority Correction — 2026-08-21

## Current authoritative state

The Last Bench canonical logo is **NOT CURRENTLY VERIFIED in the repository/library by provenance alone**.

Erfan/Dr.X explicitly corrected the prior AI claim on 21 August 2026: he did **not** approve the files previously labeled `master-logo-light.png` / `master-logo-dark.png` as the official Last Bench logo.

Therefore the following files are **REVOKED AS CANONICAL SOURCES** unless Erfan explicitly re-approves them in a later interaction:
- `master-logo-light.png`
- `master-logo-dark.png`
- `last-bench-logo-lambda-light.png`
- `last-bench-logo-lambda-dark.png`

Any AI-generated manifest, guideline, lock file, filename, caption, metadata, or prior assistant statement that claims these assets were approved by Dr.X is insufficient authority and is superseded by the user's direct correction.

## Incident diagnosis

The failure was not merely a bad logo rendering. It was an **authority/provenance failure**.

The assistant searched the persistent Library, found files with authoritative-looking names such as `master-logo-*`, and found AI-generated metadata/lock files asserting that they were approved. It then elevated those derived artifacts to canonical status without finding direct user approval tied to the exact pixels.

This created a false chain:

`AI-GENERATED ASSET/MANIFEST -> AUTHORITATIVE-SOUNDING FILENAME -> ASSUMED USER APPROVAL -> FALSE CANONICAL LOCK`

That chain is invalid.

## Root cause

Failure class: **retrieval + provenance laundering + verification**.

1. Filename semantics (`master`, `official`, `locked`) were mistaken for approval evidence.
2. Model-generated Library assets and model-generated brand-lock metadata were treated as though they were user-authored sources.
3. A prior AI statement claiming user approval was reused as evidence for later work.
4. The exact source image was not traced back to a user-uploaded/explicitly approved asset.
5. Direct current user correction was not available until now; once given, it supersedes all inferred approval.

## Permanent Last Bench logo authority rule

A Last Bench logo may be called canonical only if at least one of these is true:

1. Erfan/Dr.X explicitly uploads the exact logo asset and states that it is the official/current/correct logo; or
2. Erfan/Dr.X explicitly identifies an existing exact file/image as the official/current/correct logo; or
3. a repository/Drive source has retrievable provenance showing it originated from such direct user approval, with no later user correction superseding it.

The following are **never sufficient by themselves**:
- a filename containing `official`, `master`, `final`, or `locked`;
- AI-generated Library metadata;
- an AI-generated brand guideline or manifest;
- a previous assistant's claim that the user approved something;
- a logo appearing in an AI-generated poster/mockup;
- visual similarity to another Last Bench asset.

If approval provenance cannot be established, the correct state is:

`CANONICAL LOGO = UNKNOWN / NEEDS USER CONFIRMATION`

Do not guess.

## Production rule after confirmation

Once Erfan identifies the correct source asset, branded work must use:

`VERIFIED USER-APPROVED SOURCE -> DETERMINISTIC PLACEMENT -> FINAL PIXEL/SOURCE COMPARISON`

Never regenerate, redraw, trace, reinterpret, or reconstruct the confirmed logo with an image model.

## Real-person portrait rule

Supplied real-person portraits used for recognition posts are also protected assets when likeness accuracy is required. They may be cropped, masked, background-removed, or color-adjusted non-destructively, but the person's face must not be reconstructed by generation unless Erfan explicitly requests a stylized transformation.

## Campaign isolation for 24 August

Keep these assets distinct unless Erfan explicitly merges them:

1. **Partner recognition post** — recognition, credibility and social proof for a named education consultant/partner.
2. **Partner invitation/recruitment post** — recruit relevant education consultants/agents.
3. **Friends & family amplification post** — close contacts share personalized creatives and invite their networks to visit/register by 24 August if interested in working with Malaysia as a consultant or learning AI skills.
4. **Student/application post** — student/parent acquisition and application support.

## Mandatory acceptance test before handoff

A Last Bench branded artifact is not ready until:
- logo approval provenance is verified;
- exact approved source asset is retrieved;
- logo is placed deterministically, never generated;
- supplied real-person portrait is preserved when likeness accuracy is required;
- final render is compared to the approved source after the last edit;
- names, titles, event date/day, address and contacts are checked;
- campaign purpose/audience is not mixed with another asset;
- any QR decodes from the final exported artifact to the approved destination.

## Escalation rule

Any future use of a Last Bench logo whose exact user approval cannot be proven is a **process regression**. Stop before rendering and request/resolve the authoritative source instead of inferring one.