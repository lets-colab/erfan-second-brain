# NotebookLM MCP — setup

Run this on a **desktop or laptop with a visible browser**. It cannot be completed in a remote, headless, or CI session: the login step opens a real Chrome window and requires a human to sign in. A phone can complete the two-factor prompt but cannot perform the setup.

Account: `founder.colab@gmail.com`. See the account boundary in [`SYNC_CONTRACT.md`](SYNC_CONTRACT.md).

## 1. Register the server

User scope, so it is available in every project rather than one:

```bash
claude mcp add --scope user notebooklm -- npx notebooklm-mcp@latest
claude mcp list        # expect: notebooklm
```

On a headless Linux host, run the Claude session under a virtual display so the login window has somewhere to open:

```bash
xvfb-run -a claude
```

## 2. Authenticate once

In a Claude session:

1. Call `get_health`. If it reports `authenticated: false`, continue.
2. Call `setup_auth`. A browser window opens.
3. Sign in as `founder.colab@gmail.com`.
4. Call `get_health` again and confirm `authenticated: true`.

The session persists in a local browser profile outside this repository. **Never copy that profile, its cookies, or any `storage_state` file into git.**

## 3. Register a notebook

`add_notebook` takes a NotebookLM **share URL**, which you supply; the tool cannot discover notebooks on its own.

In NotebookLM: open the notebook, use Share, copy the link.

```text
add_notebook  <share-url>
select_notebook  <id from the previous result>
ask_question  "<your question>"
```

`ask_question` returns a `session_id`. Pass it back on follow-up questions so NotebookLM keeps conversational context; its retrieval sharpens across a session.

## 4. Verify before claiming this works

Registration is not completion, per `AGENTS.md` rule 15. The check that matters:

```text
get_health        -> authenticated: true
list_notebooks    -> the expected notebook, under the expected account
ask_question      -> an answer that carries citations
```

An answer with **no citations** is ungrounded model output, not a NotebookLM retrieval. Record it as unsupported or discard it; do not file it as a finding.

## 5. Produce a durable snapshot

A live session is useful only to the machine holding it. To make the result usable by every other agent, run the prompt in [`CLAUDE_CODE_SYNC_PROMPT.md`](CLAUDE_CODE_SYNC_PROMPT.md) and commit the snapshot.

## Troubleshooting

| Symptom | Cause | Action |
|---|---|---|
| `authenticated: false` after signing in | Cookies did not persist, or a different Chrome profile was used | Re-run `setup_auth`; confirm the window is the one the tool opened |
| Session works, then stops days later | Google expired the session | Re-run `setup_auth`. Expected and not a defect |
| Tools absent from the session | Server not registered at user scope, or the session predates registration | `claude mcp list`, then restart the session |
| Timeouts or selector errors | NotebookLM UI changed under the automation | Update the server; if it persists, treat the integration as `blocked` and say so rather than working around it |
| Nothing works in a remote session | Expected | This integration is desktop-only by construction. See the contract |

## Scope limit

This is a **read and retrieve** integration. Do not automate bulk source ingestion into NotebookLM from an agent: rule 24 forbids ingesting a source merely because it is reachable. Sources are added deliberately, by a human, with their provenance known.
