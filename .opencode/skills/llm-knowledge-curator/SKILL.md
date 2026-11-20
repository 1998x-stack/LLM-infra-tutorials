---
name: llm-knowledge-curator
description: "Use when adding or updating LLM research wiki topics, ten-dimensional paper notes, cross-links, knowledge.jsonl entries, glossary, or knowledge validation and taxonomy."
---

# Curate the LLM Infra knowledge base

## When to use
Use to index a new paper, link an algorithm to papers, refine concepts/systems, reconcile duplicate topic names, or answer "where does this concept belong?"

## Source of truth
- Core paper metadata: `stages/<stage>/papers/core/manifest.tsv`
- Topic metadata: `wiki/knowledge/topics.tsv`
- Human-readable paper reviews: `wiki/papers/<stage>/<slug>.md`
- Topic cards: `wiki/concepts/`, `wiki/algorithms/`, `wiki/systems/`
- Generated index: `wiki/knowledge.jsonl`
- Contract: `wiki/SCHEMA.md`

## Procedure
1. Search existing IDs and titles before adding new entries. Prefer stable slugs; never silently repoint an existing ID.
2. For papers, verify arXiv ID, title and version against the actual source. Keep the stage manifest canonical.
3. Use `wiki/templates/PAPER_REVIEW_TEMPLATE.md` and complete its ten evidence dimensions. Do not mark a template as reviewed without source anchors.
4. For non-paper concepts, add one TSV row and create its matching topic-card Markdown file.
5. Maintain explicit related-paper links and avoid duplicating large passages from copyrighted sources.
6. Rebuild the JSONL index with `python3 scripts/build_knowledge_index.py`; inspect changed records and run `--check`.
7. Run `python3 scripts/validate_repo.py` and resolve IDs, paths, manifest drifts and format errors.

## Status policy
`template` = scaffold only, `draft` = authored but not fully verified, `reviewed` = cited/evidence-backed analysis. Do not use JSONL presence to imply paper mastery or experimental reproduction.

## Output
Changed source Markdown/TSV, regenerated index, validation command and short summary of added/updated relations and open uncertainty.

## Repository-relative paths
All paths above are relative to the repository root; from this file the root is `../../..`. Do not create or modify external files without explicit permission.
