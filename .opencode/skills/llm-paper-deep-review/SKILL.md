---
name: llm-paper-deep-review
description: "Use when asked to read, explain, critique or deeply review an LLM or LLM infrastructure paper, including mathematics, algorithms, experimental evidence and source-code analysis."
---

# Deep review of an LLM paper

## When to use
Use for a named paper, arXiv link, stage paper TODO, algorithm-paper comparison, or a request for a rigorous research review. Do **not** use to fabricate an experiment or to claim replication from paper figures.

## Inputs
Identify the exact paper title, arXiv ID/version, local stage, any supplied PDF and the target review path `wiki/papers/<stage>/<slug>.md`. Consult the stage's `papers/core/manifest.tsv`. If the paper is not available locally, use the supplied link or obtain permission for network access.

## Procedure
1. Read the abstract, method, main equations, experiment protocol, figure captions and limitations; cross-check the appendix when present.
2. Complete every heading in `wiki/templates/PAPER_REVIEW_TEMPLATE.md`: **Problem, Observation, Hypothesis, Algorithm, Experiment, Evidence, Limitations, Implementation, Systems, Extension**.
3. Under **Algorithm**, define inputs, outputs, dimensions, mathematical objective, pseudocode, algorithm invariants and computational complexity.
4. Under **Experiment**, identify baselines, hardware, model, datasets, metrics, seeds and ablations; do not present a paper's results as your own measurements.
5. Under **Evidence**, cite exact paper sections, tables/figures or reproducible local logs. Mark uncited/uncertain findings as `TODO: verify`.
6. Under **Implementation**, distinguish author-provided code from a tutorial implementation and identify the verified code revision.
7. Under **Systems**, discuss FLOPs, HBM traffic, VRAM/KV memory, communication, concurrency and serving latency only where applicable.
8. Under **Extension**, propose one falsifiable ablation with control variables, budget and expected tradeoff.
9. Update topic cards if a new supported relationship is discovered. Rebuild the index only after editing source manifests or `wiki/knowledge/topics.tsv`.

## Deliverables
Updated paper review, paper-to-code links, one concise evidence/limitations table, and any related topic-card references.

## Quality gate
No unsupported causal conclusions, no invented benchmark values or citations, no mixing paper measurements with locally measured ones. Run `python3 scripts/build_knowledge_index.py --check` and `python3 scripts/validate_repo.py`.

## Repository-relative paths
All paths above are relative to the repository root; from this file the root is `../../..`. Do not create or modify external files without explicit permission.
