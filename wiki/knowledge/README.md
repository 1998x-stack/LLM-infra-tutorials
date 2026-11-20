# Knowledge data sources

`wiki/knowledge/topics.tsv` is the canonical editable catalog of non-paper topics. The 42 paper records are derived directly from stage `papers/core/manifest.tsv` files.

To regenerate the complete machine-readable knowledge index:
```bash
python3 scripts/build_knowledge_index.py
python3 scripts/build_knowledge_index.py --check
python3 scripts/validate_repo.py
```

**Format:** `kind<TAB>slug<TAB>title<TAB>stage<TAB>summary`. Valid kinds are `concept`, `algorithm`, and `system`.

New topic workflow: add a TSV entry, create `wiki/<kind>s/<slug>.md`, rebuild, validate and update related paper review.

All paper rows begin at `status=template` until a human or agent produces supported reviews. The index is for discovery, not a performance evidence database.
