# Knowledge JSONL contract

`wiki/knowledge.jsonl` is a **generated index**, not an editable record store. It is generated from:

1. Core paper identity/title in `stages/<stage>/papers/core/manifest.tsv`.
2. Topic identity/title/summary in `wiki/knowledge/topics.tsv`.
3. **Source-derived review status** from each paper note's YAML frontmatter or topic card's `- **Status:** Draft` line.

Run `python3 scripts/build_knowledge_index.py` after changing a source status; `--check` fails if the index is stale. The index generator must never reset `reviewed` back to `template`.

## Record types

Required fields for all rows: `id`, `kind`, `title`, `stage`, `path`, `status`, `summary`.

Paper records add `slug`, `arxiv_id`, `source_url` and `pdf_url`. Topic records are `concept`, `algorithm` or `system`.

## Status lifecycle

| Status | Meaning | Authority |
|---|---|---|
| `template` | metadata + structured TODO only | source Markdown |
| `draft` | some authored analysis, still incomplete | source Markdown |
| `reviewed` | materially complete with anchored evidence + limitations | source Markdown, human/agent evidence review |

**Reviewed does not mean locally reproduced.** Reproduction evidence is tracked separately under stage experiments/results.

## Quality gates

- IDs are stable and unique; arXiv IDs and stage manifests match.
- Article paths must exist and contain all ten dimensions.
- Reviewed claims cite exact paper sections/figures or reproducible local experiment logs.
- No fabricated metrics, unsupported causal generalization or phantom code references.
- JSONL must match `scripts/build_knowledge_index.py --check`.
- Topic-card and paper-note statuses are strictly parsed; ambiguous/missing states cause validation failure.

## Example record

```json
{"id":"paper:arxiv:2205.14135","kind":"paper","title":"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness","stage":"07-inference-optimization","path":"wiki/papers/07-inference-optimization/flashattention.md","status":"template","summary":"Review pending; follow the ten-dimensional template.","slug":"flashattention","arxiv_id":"2205.14135","source_url":"https://arxiv.org/abs/2205.14135","pdf_url":"https://arxiv.org/pdf/2205.14135"}
```

The JSON field schema is at `wiki/knowledge/schema.json`. For migrations and safe editorial changes follow [Knowledge Curator](../agent_skills/llm-knowledge-curator/SKILL.md).

