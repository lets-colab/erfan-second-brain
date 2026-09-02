# Erfan Second Brain — Context Engineering & World Model v1

## Why this upgrade exists
The repository already has strong canonical-source, governance, skill-contract and evaluation foundations. The next bottleneck is not storing more memory; it is compiling the **right context, at the right freshness, for the right task**, then preserving state across long-running execution.

## New operating model
`Founder → World Model → Context Engine → Model/Skill → Runtime → Observation → Evaluation → Learning → World Model`

The World Model distinguishes **knowledge, live state, intent, capability, constraints, evidence, decisions and outcomes**. The Context Engine creates task-specific context packs instead of dumping the entire brain into a model context window.

## New contracts
- `context-engine/context-policy.yaml` — selection, freshness, conflict and security policy.
- `context-engine/context-pack-schema.yaml` — portable task context contract.
- `memory/temporal-claim-schema.yaml` — validity windows and supersession.
- `world-model/schema.yaml` — evidence-backed entities and temporal relationships.
- `task-memory/checkpoint-schema.yaml` — resumable long-horizon state.
- `integrations/mcp-brain-interface.yaml` — model-agnostic MCP surface.
- `learning/learning-loop.yaml` — outcome-to-regression learning contract.
- `routing/cost-governor.yaml` — capability/risk/cost-aware routing.

## What this does NOT claim
These contracts do not mean an MCP server, autonomous runtime, temporal database or live Notion/Drive synchronization is already deployed. They define the canonical interfaces so implementation can be added without changing the architecture.

## Production gate
A design contract is not production proof. Promotion requires executable acceptance tests, fresh runtime evidence, security review and human owner signoff. Until then, these additions are **active design contracts**, not a claim of autonomous production operation.

## Upgrade doctrine
1. Context before model.
2. State before memory dump.
3. Evidence before confidence.
4. Freshness before convenience.
5. Least privilege before autonomy.
6. Evaluation before promotion.
7. Learning only from observed outcomes.
8. Keep the founder world model provider-agnostic so models and memory vendors remain replaceable.
