# Knowledge integrity and status protocol

## 1. Data lineage (one direction)

`stages/*/papers/core/manifest.tsv` + `wiki/knowledge/topics.tsv` + Markdown evidence/status
→ `scripts/build_knowledge_index.py`
→ `wiki/knowledge.jsonl`

**Never** edit the JSONL manually. Changing source TSVs without regenerating JSONL is a validation failure.

## 2. Identity decisions

- Paper ID = `paper:arxiv:<arxiv-id>`. An arXiv version suffix may be used where pinned.
- Topic IDs = `concept:<slug>`, `algorithm:<slug>`, `system:<slug>`.
- Slugs use lowercase kebab-case; IDs do not encode directory paths.
- Use stable IDs even if a title spelling changes. If an ID must change, migrate all links and record the reason.
- Before creating a new card, search exact ID, title aliases and related concepts.
- Do not merge a broad concept with a concrete algorithm if they have different evidence/invariants.

## 3. Status policy

| Status | Meaning | Evidence requirement |
|---|---|---|
| template | structured metadata and prompts only | No experimental claim |
| draft | real authorship exists but incomplete | explicit uncertainties and citations where present |
| reviewed | ten dimensions substantively covered | each material claim anchored; limitations and verification status included |

**Status is source-derived**. The builder should read paper frontmatter and topic card status rather than resetting records to template/draft.

A paper's `reviewed` flag does not mean its empirical results were reproduced locally. Reproduction is a separate state tracked in report artifacts.

## 4. Topic card minimum schema

- Definition and mathematical/operational model.
- Related source papers with canonical URLs and limitations.
- Algorithm, inputs/outputs and complexity where relevant.
- Implementation location and test state (if any).
- Systems implications with correct units and assumptions.
- At least one falsifiable extension or open question.

## 5. Editorial quality controls

- Citation anchors point to exact paper sections, table or figure and, for local results, experiment command/run ID.
- Imported paper text: short quotations only with attribution; avoid copying large copyrighted passages.
- Unknown evidence → `NOT VERIFIED`. Different source perspectives remain separate rather than silently reconciled.
- Link only to actual files; use relative paths that work from the current document.
- Do not claim benchmark performance from an unexecuted implementation or stage TODO.

## 6. Drift diagnosis

1. `python3 scripts/build_knowledge_index.py --check` fails → inspect paper status/frontmatter and topic TSV/card state; regenerate.
2. Duplicate paper IDs → check stages for reuse and versions.
3. Missing card paths → create the file or remove the unsupported topic row.
4. Broken cross-links → update Markdown links in the correct source (avoid edits to generated JSONL).
5. Invalid reviewed state → return to draft until evidence is sufficient; preserve critique and review history in Markdown.

## 7. Safe changes

Small, scoped metadata edits are preferred. For bulk migrations: checkpoint original IDs, generate a mapping table, update all references, run validation, inspect diffs and avoid deleting old IDs without explicit user approval.

