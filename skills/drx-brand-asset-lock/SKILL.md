---
name: drx-brand-asset-lock
description: Mandatory integrity gate for branded DR.X artifacts. Use whenever a deliverable contains an approved logo, wordmark, brand mark, QR code, identity asset, or other protected visual. Prevents generative reconstruction, logo drift, fake QR codes, audience-mixing, and final-render brand regressions.
status: active
owner: drx-ai-os
version: 1.0.0
---

# DR.X Brand Asset Lock

## Objective

Prevent a polished artifact from failing because a canonical brand asset was approximated, regenerated, distorted, recolored, substituted, or mixed with the wrong campaign/message.

## Trigger

Use this skill for any poster, social creative, presentation, document, website, badge, card, signage, ad, invitation, recognition post, mockup, or generated image that contains a DR.X project brand asset.

## Prime rule — canonical assets are immutable

An approved logo, wordmark, mark, favicon, symbol, QR code, signature, badge, or other identity asset is a protected source asset.

Never:
- redraw it;
- regenerate it with an image model;
- trace or reconstruct it from a screenshot;
- approximate it from memory;
- substitute a visually similar mark;
- retype the wordmark as ordinary text;
- alter proportions, geometry, spacing, colors, line count, icon details, or internal relationships;
- let a generative model render a QR code that is supposed to function.

Allowed transformations are limited to deterministic placement operations explicitly compatible with the brand source: proportional scaling, translation, cropping of surrounding transparent canvas when safe, and approved light/dark variant selection. The internal asset itself must remain unchanged.

## Canonical source resolution

Before execution, resolve the protected asset in this order:
1. the exact asset the user supplied or explicitly approved in the current task;
2. the latest explicitly approved canonical asset in the persistent file library;
3. the canonical project source in Drive/GitHub/brand repository;
4. if none can be retrieved, stop and ask for the source asset rather than reconstructing it.

A poster, screenshot, mockup, social post, or previous AI generation is not a canonical logo source when the original asset exists.

## Two-layer production architecture

For branded visuals, separate production into two layers.

### Generative layer
May generate:
- backgrounds;
- people;
- environments;
- decorative imagery;
- non-critical illustrative elements.

### Deterministic protected layer
Must place with non-generative tooling:
- canonical logo/wordmark;
- exact brand marks;
- critical names and dates when text accuracy matters;
- phone/email/address details;
- legal or financial claims;
- functional QR codes;
- registration URLs/codes.

Do not ask an image model to recreate these elements inside the image. If composition changes are needed, redesign the surrounding layout around the protected asset.

## Campaign-separation gate

Before rendering, name the artifact and its single primary job.

Examples:
- partner recognition post;
- partner invitation;
- friends-and-family amplification post;
- student application post;
- event information poster.

Do not merge copy or CTAs from another campaign unless the brief explicitly requires it. A partner recognition post should not silently inherit a friends-and-family AI-skills CTA; a student poster should not inherit partner-commercial language.

## QR integrity gate

A QR code is functional infrastructure, not decoration.

If a QR is present:
1. destination must be known and approved;
2. generate the QR deterministically from that destination;
3. place it as an exact asset;
4. decode/test the final rendered QR from the final file;
5. if the destination is unknown or decoding fails, remove the QR or mark the artifact NOT READY.

Never use an image-model-generated QR as a functional code.

## Final-render acceptance test

Before handoff, inspect the actual final artifact and compare it against the canonical source.

Critical checks:
- correct light/dark logo variant;
- exact mark geometry preserved;
- exact wordmark shape preserved;
- no missing internal details;
- no added details;
- aspect ratio unchanged;
- logo not stretched, skewed, traced, blurred, or reinterpreted;
- clear space is acceptable;
- campaign message matches the artifact's intended audience;
- names/dates/contact information match authoritative inputs;
- QR decodes to the intended destination if present.

For protected assets, visual similarity is not a PASS criterion. The source asset must have been deterministically placed.

## Repeated-failure escalation

If the same brand-asset failure occurs twice, treat it as a process defect, not another design revision.

Required response:
1. stop using the failing generation path for protected assets;
2. isolate the protected layer from image generation;
3. retrieve the canonical source again;
4. perform deterministic compositing/layout;
5. compare the final render against source;
6. record the durable lesson in the project decision/memory layer;
7. do not claim completion until the final artifact passes.

## Output state

Allowed states:
- PASS — canonical asset was retrieved, placed deterministically, final render inspected, and all critical checks pass;
- PARTIAL — layout/content is useful but a protected source or functional verification is missing;
- FAIL — the asset was regenerated, substituted, distorted, mixed with the wrong campaign, or QR/contact details are unverified.
