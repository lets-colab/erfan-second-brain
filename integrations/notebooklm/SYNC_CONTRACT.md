# NotebookLM ↔ DR.X Retrieval Sync Contract

Purpose: make NotebookLM's grounded answers usable by every approved agent through a durable source of truth, without treating a browser-automated session as canonical and without any agent depending on a live login it does not have.

## Epistemic class (read this before using any NotebookLM output)

Under `AGENTS.md` rule 4, memory and retrieval systems are **retrieval assistance only** unless explicitly designated authoritative. NotebookLM is **not** designated authoritative here, and this contract does not designate it.

A NotebookLM answer is an **external claim** produced by a model over sources the user uploaded. It is not a verified fact, and it is not a user-stated position. Two consequences bind every agent:

- A claim sourced from NotebookLM is recorded as an external claim with its citations, never promoted to verified fact merely because NotebookLM stated it confidently.
- Where NotebookLM cites an underlying document, the **document** is the evidence. Cite it. Copying a NotebookLM paraphrase into a repository note without its citation launders a weak recollection into a stronger one, which rule 5 forbids.

NotebookLM's value here is retrieval and synthesis across a corpus that is too large to read directly. That is a real capability. It is not an evidence upgrade.

## Why a sync contract rather than a live attachment

NotebookLM has no official public API. Every available MCP server drives a real authenticated browser session (Playwright or Patchright) against the NotebookLM web app. Three consequences follow, and they are the reason this integration is shaped like `integrations/claude-design/` rather than a normal connector:

1. **Authentication is interactive and desktop-bound.** It requires a real Google sign-in in a visible browser. It cannot be completed in a headless or remote agent session, so no remote agent can bootstrap this integration on its own.
2. **The session is not durable.** Cookies expire, and Google may require re-verification at any time. An agent that depends on a live NotebookLM session has an unreliable dependency.
3. **The transport is unofficial.** A NotebookLM UI change can break the automation without notice. Nothing load-bearing should sit behind it.

So the durable artifact is a **committed snapshot in this repository**, produced on a machine where the session is authenticated. Agents without NotebookLM access read the snapshot. The live MCP is a producer of snapshots, never a dependency of readers.

```text
NotebookLM notebook (founder.colab@gmail.com)
        ↓  authenticated desktop session only
Claude Code + notebooklm MCP
        ↓  verified snapshot with citations
GitHub repository (this contract)
        ↓
ChatGPT / Codex / Claude / other approved agents
```

## Account boundary

NotebookLM runs under `founder.colab@gmail.com`. Google Drive runs under `360cybertroopers@gmail.com`. These are **deliberately separate**, and an agent must not assume a document reachable in one is reachable in the other.

When a NotebookLM source originates from a Drive file on the other account, record the source's title and the account it belongs to. Do not assume Drive-connector access implies access to a NotebookLM source, or the reverse.

## Snapshot location

Write snapshots under:

`integrations/notebooklm/snapshots/<notebook-slug>/`

Recommended files:

- `manifest.json` — notebook id, title, share URL, source inventory, sync timestamp, account, and per-artifact classification.
- `SOURCES.md` — the notebook's source list: title, type, origin, and whether the underlying document is retrievable from this repository or from Drive.
- `QUESTIONS.md` — questions asked, verbatim answers, and the citations NotebookLM returned for each.
- `SYNTHESIS.md` — durable conclusions, each labeled with its epistemic class and citation.

## Mandatory provenance

Every snapshot records:

- the notebook identifier and share URL;
- the Google account the notebook belongs to;
- the sync timestamp and the tool version used;
- for every recorded claim, the NotebookLM citation and, where known, the underlying source document;
- classification per artifact: verbatim answer, interpreted summary, or human-authored conclusion;
- questions that returned no citation, which are recorded as unsupported and must not be reused as evidence.

## Never committed

Consistent with `AGENTS.md` rule 6:

- no Google credentials, cookies, session tokens, or `storage_state` files;
- no authenticated NotebookLM URLs containing session parameters;
- no raw source documents whose licensing or privacy status is unresolved;
- no personal data pulled in incidentally because it was reachable, per rule 24.

The MCP server persists its browser session in a local profile directory outside this repository. That directory is never copied here, and `.gitignore` must keep any local session artifact out.

## Staleness

A snapshot is bound to the notebook contents at sync time. Adding a source to the notebook invalidates every prior synthesis that depended on the old corpus, in the same way rule 16 invalidates verification evidence after a material change.

Record `captured_at` in the manifest. A snapshot older than its notebook's last source change is `stale`, and the DR.X Console renders that state rather than presenting the numbers as current.

## Acceptance

This integration is **not** proven by a successful `setup_auth` call, a registered MCP server, or a snapshot directory existing. Per rule 15, the final-state proof chain is:

1. the MCP server is registered and `get_health` reports `authenticated: true`;
2. `list_notebooks` returns the expected notebook under the expected account;
3. `ask_question` returns an answer **with citations**;
4. a snapshot exists in this repository carrying those citations;
5. an agent with no NotebookLM access reconstructs the same conclusion from the snapshot alone.

Step 5 is the one that matters. Until it holds, this integration is `not verified`.
