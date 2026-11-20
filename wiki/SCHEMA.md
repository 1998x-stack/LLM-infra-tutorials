# Knowledge JSONL contract

`wiki/knowledge.jsonl` is generated from stage paper manifests and `wiki/knowledge/topics.tsv`. Do not hand-edit generated rows.

## Record types
Common required fields: `id`, `kind`, `title`, `stage`, `path`, `status`, `summary`.

**paper** records additionally have `arxiv_id`, `source_url`, `pdf_url`, and `slug`.
**concept**, **algorithm** and **system** records use human-curated descriptions in `topics.tsv`.

## Status lifecycle
- `template`: metadata and a structured TODO note, **not read or validated**.
- `draft`: at least one substantive analysis exists; may still contain TODO items.
- `reviewed`: ten dimensions completed with evidence, limitations and reproducibility references.

## Quality gates
- Unique IDs, valid arXiv IDs and safe relative paths.
- Paper arXiv ID/title must match stage `manifest.tsv` exactly.
- No dangling topic paths or duplicated article slugs.
- JSONL must match source manifests (`scripts/build_knowledge_index.py --check`).
- A reviewed claim requires traceable support from paper section/table/figure or local reproducible experiment.

## Example
```json
{"id":"paper:arxiv:2205.14135","kind":"paper","title":"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness","stage":"07-inference-optimization","path":"wiki/papers/07-inference-optimization/flashattention.md","status":"template","summary":"Review pending; follow the ten-dimensional template.","slug":"flashattention","arxiv_id":"2205.14135","source_url":"https://arxiv.org/abs/2205.14135","pdf_url":"https://arxiv.org/pdf/2205.14135"}
```

Schema specification lives at `wiki/knowledge/schema.json`. See `wiki/knowledge/README.md` for source-of-truth editing.
