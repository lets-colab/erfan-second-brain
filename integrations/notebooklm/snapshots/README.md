# NotebookLM snapshots

Empty. No notebook has been synchronized yet.

This is the accurate state, not a gap to paper over: the integration contract exists, and the retrieval it describes is **`not verified`** until a snapshot lands here carrying real citations.

## To populate

On a desktop with the `notebooklm` MCP authenticated (see [`../MCP_SETUP.md`](../MCP_SETUP.md)), run the prompt in [`../CLAUDE_CODE_SYNC_PROMPT.md`](../CLAUDE_CODE_SYNC_PROMPT.md). Each sync writes one directory here:

```text
snapshots/<notebook-slug>/
  manifest.json    notebook id, share URL, account, sources, captured_at
  SOURCES.md       source inventory with origin and retrievability
  QUESTIONS.md     questions, verbatim answers, citations
  SYNTHESIS.md     conclusions, each labeled with its epistemic class
```

## Why this directory is tracked while empty

An agent reading this repository should be able to tell the difference between *the integration was never set up* and *the integration was set up and returned nothing*. An absent directory is ambiguous between the two. This file resolves it: the contract is defined, the sync has not run.

Per `AGENTS.md` rule 15, neither the contract's existence nor a registered MCP server counts as completion. The acceptance chain is in [`../SYNC_CONTRACT.md`](../SYNC_CONTRACT.md), and its final step is another agent reconstructing a grounded conclusion from a snapshot here, without NotebookLM access of its own.
