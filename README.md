---
created: 2026-07-19
updated: 2026-07-19
type: resource
status: active
tags: [second-brain, portability, governance]
---

# Erfan Second Brain

This is Erfan Uddin's user-controlled, Obsidian-ready personal knowledge base.
It is designed to be portable across Codex, Claude, other AI tools, MemPalace,
Graphify, and private Git version control.

## Purpose

- Preserve verified knowledge, decisions, projects, preferences, and corrections.
- Help an AI personal assistant retrieve context without pretending to be Erfan.
- Separate source facts, Erfan's stated views, and AI inferences.
- Measure knowledge readiness and expose important blind spots.

## Safety boundary

Never store passwords, one-time codes, recovery codes, secret keys, identity-document
images, full payment credentials, private authentication links, or raw private chats.
Account access is not authority to communicate, publish, spend, or make commitments.

## Main notes

- [Personal assistant mission](projects/personal-second-brain.md)
- [Knowledge readiness](areas/knowledge-readiness.md)
- [Operating charter](areas/operating-charter.md)
- [Digital presenter profile](areas/digital-presenter-profile.md)
- [Source inventory](notes/source-inventory.md)
- [Knowledge change log](reviews/knowledge-change-log.md)

## Update rule

Every durable addition must record its source, date, confidence, and whether it is a
verified fact, user-stated position, or inference. Each addition must update the
knowledge-readiness assessment when it materially changes assistant capability.


## Session bootstrap

Cloud Claude Code sessions run in a throwaway container, so MemPalace and
Graphify have to be reinstalled each time. Rather than re-deriving context in
tokens, run:

```bash
bash bootstrap.sh
```

It installs both tools, registers MemPalace as a user-scope MCP server,
installs the Graphify skill, and mines this repo into the palace. Idempotent —
re-run it after any restart. `--no-mine` skips the mining step.

Then `mempalace wake-up` gives ~800 tokens of session context instead of
re-reading the repository.
