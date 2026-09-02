# Claude Code prompt — sync a NotebookLM notebook into the shared DR.X source of truth

Use this from Claude Code on a machine where the `notebooklm` MCP is registered and authenticated. See [`MCP_SETUP.md`](MCP_SETUP.md).

---

Synchronize the approved NotebookLM notebook into the DR.X shared retrieval mirror.

Requirements:

1. Use the connected `notebooklm` MCP. Call `get_health` first. If it reports `authenticated: false`, run `setup_auth` and let the user sign in. Never inspect, copy, or commit credential files, cookies, or session state.
2. Call `list_notebooks` and identify the exact notebook by id. Do not guess an id, and do not proceed if more than one notebook plausibly matches. Ask which.
3. Inventory the notebook's sources before asking anything. Record each source's title, type, and origin. Where a source originates from Google Drive, note that Drive is on a different account (`360cybertroopers@gmail.com`) than NotebookLM (`founder.colab@gmail.com`), and do not assume it is retrievable from this repository.
4. Ask the questions the task requires. Reuse the returned `session_id` across follow-ups so retrieval stays in context.
5. **Record citations for every answer.** An answer without citations is ungrounded model output: mark it `unsupported` and do not promote it to a finding. This is the single most important step in this prompt.
6. Write a durable snapshot under `integrations/notebooklm/snapshots/<notebook-slug>/` containing at minimum:
   - `manifest.json` — notebook id, share URL, account, source inventory, `captured_at`, tool version, and per-artifact classification;
   - `SOURCES.md` — the source list with origin and retrievability;
   - `QUESTIONS.md` — each question, the verbatim answer, and its citations;
   - `SYNTHESIS.md` — durable conclusions, each labeled `verified fact`, `external claim`, `inference`, or `unknown`.
7. Preserve verbatim answers where they matter. Label every interpretation as interpretation. Never smooth a hedged answer into a confident one: confidence of wording may not exceed evidence strength.
8. Do not invent citations, source titles, or notebook metadata. A gap is recorded as a gap.
9. Where a NotebookLM conclusion conflicts with a canonical file in this repository, record the conflict in `SYNTHESIS.md` rather than silently resolving it. GitHub is authoritative for what this repository owns; NotebookLM is not.
10. Do not bulk-ingest sources into the notebook as part of a sync. Retrieval only.
11. Refresh the console state so the new snapshot is reflected:
    `python3 scripts/build_console_state.py`
12. Commit with message: `notebooklm-sync: <notebook name>`
13. Report the commit SHA, snapshot path, notebook id, questions asked, answers lacking citations, unresolved gaps, and any conflicts with canonical repository files.

Goal: an agent with no NotebookLM access must be able to reconstruct the same grounded conclusions from GitHub alone, with provenance intact, without depending on a live browser session or on cross-vendor chat history.

---

## What this prompt deliberately does not do

- It does not designate NotebookLM authoritative. Under `AGENTS.md` rule 4 it stays retrieval assistance.
- It does not upgrade a NotebookLM answer to verified fact. The cited underlying document is the evidence.
- It does not treat a completed sync as proof the integration works. That requires the acceptance chain in [`SYNC_CONTRACT.md`](SYNC_CONTRACT.md), whose final step is another agent reconstructing the conclusion from the snapshot alone.
