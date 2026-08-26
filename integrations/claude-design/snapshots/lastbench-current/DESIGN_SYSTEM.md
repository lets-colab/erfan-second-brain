# Last Bench — Current Claude-Derived Design System Snapshot

Status: **production-derived snapshot**

This file is an interpreted cross-agent summary of the current `lets-colab/LastBenchBd` production design state. It is grounded in the canonical design-system files and in commits that explicitly document Claude Design imports. It is **not** a claim of a fresh authenticated export from Claude Design.

## Design thesis

Last Bench should feel like a real journey from Bangladesh to Malaysia rather than a conventional education-agency website.

The current production register is:

- cinematic
- sincere
- determined
- proud rather than pity-driven
- forward-moving
- emotionally dark when telling the journey
- light and calm when establishing trust
- green only when signaling progress or emphasis

Core visual law:

> **Dark for emotion. Warm white for trust. Green for progress.**

## Fixed brand system

- Brand Green: `#00C853`
- Green on dark: `#00E676`
- Charcoal: `#111111`
- Warm White: `#FAFAF8`
- Sage: `#E6F2E9`
- Gray: `#6B6F76`
- Soft Gray: `#A1A1AA`

Production typography currently has two contexts:

- Site display: **Anton**
- Site body: **Space Grotesk**
- App / formal brand display: **General Sans**
- App / formal brand body: **Sora**

Do not casually collapse these contexts into one font pairing. Preserve the current surface unless a deliberate redesign is approved.

## Voice grammar

The brand uses short declarative beats rather than long advertising copy.

Examples of the grammar:

- `From Last Bench. To The World.`
- `Your journey, our mission.`

One phrase may receive Brand Green emphasis; the rest remains neutral.

Avoid:

- generic education-agency reassurance
- stock-photo optimism
- trust-badge clutter
- WhatsApp-button spam
- SaaS bento-card language
- purple/blue startup gradients
- pity framing around "last bench" students
- invented outcomes, partnerships, scholarships or success rates

## Current motion / cinematic grammar

Claude-derived production work established a cinematic Malaysia Experience with:

- scroll-driven journey from Dhaka to Kuala Lumpur
- dark night-sky atmosphere
- Brand Green progress accents
- moving traffic light streams
- tropical haze
- aircraft warning beacons
- subtle camera sway/bank
- occasional lightning / weather atmosphere
- chapter-like scroll pacing
- orchestrated hero entrances
- reduced-motion handling
- mobile rendering budgets

The lesson is not to reproduce those effects everywhere. The reusable principle is:

> **Motion should express journey, place, progression or emotional transition.**

For founder experiences, motion must remain subordinate to the person and the story.

## Founder-section implication

`Meet the Founders` must live inside the Last Bench universe, not become three unrelated portfolio sites.

Shared environment:

- canonical Last Bench navigation and brand assets
- fixed brand colors
- consistent motion quality
- same accessibility/performance expectations
- same sincerity and anti-corporate tone

Founder chapters may introduce a controlled personal grammar, but they must return naturally to the Last Bench world.

For Sayem Ahmed specifically, the profile should use the existing cinematic language as connective tissue while creating a founder-specific narrative from:

`Limkokwing → entrepreneurship → hospitality → shipping / C.S Corporation → Last Bench`

Do **not** turn the shipping background into a literal nautical theme. Translate it into ideas of routes, systems, scale, responsibility and movement.

## Source hierarchy

1. Current explicit user instruction.
2. Canonical protected Last Bench brand assets.
3. Current approved production code.
4. Exact design-system tokens.
5. Claude-derived production design language.
6. This interpreted summary.

## Provenance

Primary source repository: `lets-colab/LastBenchBd`

Current production SHA at snapshot time:

`d493b752504c659e71725e801ad371768ca4c630`

Known Claude Design import/provenance commits:

- `8e38ef6f15eb86e3215d0bc8613d04cffc4dc65d`
- `5674cc174d20b388b52b41ec4a1cd0094b216fae`
- `a256b4012c3edc7a4731a1f11f776b718668de85`
