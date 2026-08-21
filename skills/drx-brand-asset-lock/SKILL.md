---
name: drx-brand-asset-lock
description: Mandatory integrity gate for branded DR.X artifacts. Use whenever a deliverable contains an approved logo, wordmark, brand mark, QR code, identity asset, approved real-person portrait, or other protected visual. Prevents generative reconstruction, logo drift, portrait/identity drift, fake QR codes, audience-mixing, and final-render brand regressions.
status: active
owner: drx-ai-os
version: 1.0.1
---

# DR.X Brand Asset Lock

## Objective

Prevent a polished artifact from failing because a canonical brand or identity asset was approximated, regenerated, distorted, recolored, substituted, or mixed with the wrong campaign/message.

## Trigger

Use this skill for any poster, social creative, presentation, document, website, badge, card, signage, ad, invitation, recognition post, mockup, or generated image that contains a DR.X project brand or identity asset.

## Prime rule — canonical assets are immutable

An approved logo, wordmark, mark, favicon, symbol, QR code, signature, badge, approved real-person portrait/photo, or other identity asset is a protected source asset.

Never:
- redraw it;
- regenerate it with an image model;
- trace or reconstruct it from a screenshot;
- approximate it from memory;
- substitute a visually similar mark or portrait;
- retype the wordmark as ordinary text;
- alter proportions, geometry, spacing, colors, line count, icon details, or internal relationships;
- alter a real person's face/identity when the brief requires their actual supplied photograph;
- let a generative model render a QR code that is supposed to function.

Allowed transformations are limited to deterministic placement operations explicitly compatible with the source: proportional scaling, translation, non-destructive cropping, background masking/removal when it preserves identity, cropping of surrounding transparent canvas when safe, and approved light/dark variant selection. The protected source itself must remain faithful.

## Canonical source resolution

Before execution, resolve the protected asset in this order:
1. the exact asset the user supplied or explicitly approved in the current task;
2. the latest explicitly approved canonical asset in the persistent file library;
3. the canonical project source in Drive/GitHub/brand repository;
4. if none can be retrieved, stop and ask for the source asset rather than reconstructing it.

A poster, screenshot, mockup, social post, or previous AI generation is not a canonical logo or portrait source when the original asset exists.

## Two-layer production architecture

For branded visuals, separate production into two layers.

### Generative layer
May generate:
- backgrounds;
- environments;
- decorative imagery;
- non-critical illustrative elements;
- fictional people only when the brief calls for them.

An approved real person's supplied portrait is not part of the generative layer unless the user explicitly asks for stylization/transformation and identity drift is acceptable.

### Deterministic protected layer
Must place with non-generative tooling:
- canonical logo/wordmark;
- exact brand marks;
- approved real-person portraits when likeness accuracy matters;
- critical names and dates when text accuracy matters;
- phone/email/address details;
- legal or financial claims;
- functional QR codes;
- registration URLs/codes.

Do not ask an image model to recreate these elements inside the image. If composition changes are needed, redesign the surrounding layout around the protected assets.

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
- approved portrait remains the same person's supplied photograph when likeness accuracy is required;
- no facial reconstruction or generative identity drift;
- no missing internal details;
- no added details;
- aspect ratio unchanged;
- logo not stretched, skewed, traced, blurred, or reinterpreted;
- clear space is acceptable;
- campaign message matches the artifact's intended audience;
- names/dates/contact information match authoritative inputs;
- QR decodes to the intended destination if present.

For protected assets, visual similarity is not a PASS criterion. The source asset must have been deterministically placed or non-destructively processed.

## Repeated-failure escalation

If the same brand/identity-asset failure occurs twice, treat it as a process defect, not another design revision.

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
- PASS — canonical assets were retrieved, placed deterministically, final render inspected, and all critical checks pass;
- PARTIAL — layout/content is useful but a protected source or functional verification is missing;
- FAIL — a protected asset was regenerated, substituted, distorted, identity-drifted, mixed with the wrong campaign, or QR/contact details are unverified.
