# Knowledge data sources and status preservation

`wiki/knowledge/topics.tsv` is the canonical metadata table for non-paper topics. The 42 core papers are derived from stage-specific `papers/core/manifest.tsv` files.

**Status sources:**
- Paper review `wiki/papers/<stage>/<slug>.md`: YAML frontmatter `status: template|draft|reviewed`.
- Concept/algorithm/system card: `- **Status:** Draft` (or Template/Reviewed).
- The generated `wiki/knowledge.jsonl` mirrors these statuses. Regeneration **must not** overwrite `reviewed` progress.

```bash
python3 scripts/build_knowledge_index.py
python3 scripts/build_knowledge_index.py --check
python3 scripts/validate_repo.py
```

Topic TSV columns: `kind<TAB>slug<TAB>title<TAB>stage<TAB>summary`. Types are `concept`, `algorithm` and `system`. Add a source row and the corresponding `wiki/<kind>s/<slug>.md` before rebuilding.

Index entries are discovery records, not an assurance of verified model quality or paper experiment reproduction. The [integrity playbook](../../agent_skills/llm-knowledge-curator/references/INTEGRITY.md) explains ID stability, evidence and status transitions.

