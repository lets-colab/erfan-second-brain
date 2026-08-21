---
created: 2026-08-21
updated: 2026-08-21
type: decision
status: active
project: Last Bench
owner: drx-ai-os
---

# Last Bench Canonical Brand Asset Lock — 2026-08-21

## Current authoritative state — VERIFIED BY DIRECT USER APPROVAL

On 21 August 2026, Erfan/Dr.X directly supplied and explicitly approved the exact Last Bench logo reference shown in the current conversation and said to lock it as the logo.

The canonical approved source is now:
- Conversation source file: `16544.jpg`
- Conversation file id: `file_0000000007c4821187d7369b250cea6d`
- SHA-256: `49c59068654d9067608f681bd96744cd3ea532d54ade2742238530ede028af86`
- Persistent Library copy: `/LAST BENCH/LOCKED ASSETS/LastBench_Canonical_Logo_UserApproved_2026-08-21.jpg`
- Persistent Library file id: `file_000000006f14820793a9d13057b1e475`
- Persistent Library library_file_id: `libfile_f18a5bec16fc819198b8648e8ac19f71`

The directly approved supporting guideline/reference board is:
- Conversation source file: `16545.png`
- Conversation file id: `file_00000000272c8207bb5a1205d3f19517`
- SHA-256: `54f2ad2132db4cdb4ec2f2fadc277899187d5ab3403b84f1386b783555acc213`
- Persistent Library copy: `/LAST BENCH/LOCKED ASSETS/LastBench_Canonical_Logo_Guideline_UserApproved_2026-08-21.png`
- Persistent Library file id: `file_0000000014f88211b70497b12bac58d5`
- Persistent Library library_file_id: `libfile_3a8d7ba101ac8191834bf0a82178a999`

This direct current user approval supersedes the earlier temporary `UNKNOWN / NEEDS USER CONFIRMATION` state and any prior AI-generated or inferred logo lock.

## Canonical logo identity

The approved logo is the exact supplied artwork showing:
- stacked `LAST` over `BENCH` wordmark;
- green bench symbol;
- green rising arrow integrated from the bench;
- tagline `CREATING A LASTING BENCHMARK` beneath.

The exact source pixels are authoritative. Visual similarity is not sufficient.

## Revoked prior inferred assets

The following remain revoked as canonical sources unless explicitly re-approved by Erfan/Dr.X:
- `master-logo-light.png`
- `master-logo-dark.png`
- `last-bench-logo-lambda-light.png`
- `last-bench-logo-lambda-dark.png`

Any AI-generated manifest, guideline, lock file, filename, caption, metadata, or prior assistant statement that previously claimed those assets were approved is insufficient authority and remains superseded.

## Production rule — HARD LOCK

For every Last Bench artifact containing the logo:

`VERIFIED USER-APPROVED SOURCE -> DETERMINISTIC PLACEMENT -> FINAL SOURCE COMPARISON`

Never regenerate, redraw, trace, reinterpret, reconstruct, retype, or visually approximate the confirmed logo with an image model.

If a generative image tool would touch the logo layer, do not use that tool for the final composite. Generate only non-protected background material if needed, then place the exact approved logo afterward using deterministic compositing.

## Real-person portrait rule — HARD LOCK

For recognition posts, the exact supplied real-person portrait must also be treated as a protected asset whenever likeness accuracy matters.

Allowed:
- proportional scaling;
- cropping;
- deterministic masking/background removal;
- non-destructive color/contrast adjustment.

Not allowed unless the user explicitly asks for stylization:
- changing the face;
- changing hair/beard/facial structure;
- inventing a different pose;
- changing clothing by generation;
- recreating the person from a poster/reference;
- using an AI-generated lookalike.

If the exact original portrait cannot be tied to a user-supplied source, stop and request the exact photo instead of guessing.

## Incident diagnosis

The repeated failure was a production-path failure, not a memory failure alone.

The assistant correctly retrieved or was shown a protected logo/photo, but then routed the entire final poster through image generation. The generator re-rendered both the logo and the person's face, causing drift even though the intended assets had been 'locked'.

Therefore 'locked in memory' is not enough. The final production toolchain must also preserve the asset deterministically.

## Campaign isolation for 24 August

Keep these assets distinct unless Erfan explicitly merges them:

1. **Partner recognition post** — recognition, credibility and social proof for a named education consultant/partner.
2. **Partner invitation/recruitment post** — recruit relevant education consultants/agents.
3. **Friends & family amplification post** — close contacts share personalized creatives and invite their networks to visit/register by 24 August if interested in working with Malaysia as a consultant or learning AI skills.
4. **Student/application post** — student/parent acquisition and application support.

## Mandatory acceptance test before handoff

A Last Bench branded artifact is not ready until:
- exact user-approved logo source is retrieved;
- exact logo hash/provenance matches this decision;
- logo is placed deterministically, never generated;
- exact original real-person portrait is retrieved if likeness accuracy matters;
- no facial reconstruction or AI identity drift occurred;
- final render is compared to the approved logo source and original portrait after the last edit;
- names, titles, event date/day, address and contacts are checked;
- campaign purpose/audience is not mixed with another asset;
- any QR decodes from the final exported artifact to the approved destination.

## Escalation rule

Any future Last Bench logo drift or real-person identity drift is a **process regression**. Stop the generative final-render path immediately and return to deterministic compositing with the protected sources.