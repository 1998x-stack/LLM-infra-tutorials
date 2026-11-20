# LLM Infrastructure Research Wiki

This wiki is an **evidence-aware, machine-indexed research notebook** for the 16-week curriculum. It is not a scraped paper abstract collection or a claim that all methods have been reproduced.

## Navigation
- [Knowledge index](knowledge.jsonl): newline-delimited JSON records (papers + concepts + algorithms + systems).
- [Schema and validation](SCHEMA.md): field semantics, status lifecycle, quality gates.
- [Knowledge records](knowledge/README.md): canonical topic metadata in `topics.tsv`.
- [Paper reviews](papers/README.md): 42 core paper files organized by stage.
- [Concepts](concepts/README.md), [Algorithms](algorithms/README.md), [Systems](systems/README.md): topic cards.
- [Ten-dimension paper template](templates/PAPER_REVIEW_TEMPLATE.md): Problem through Extension.
- [Experiment note](templates/EXPERIMENT_NOTE_TEMPLATE.md) and [Concept card](templates/CONCEPT_CARD_TEMPLATE.md).

## Workflow
1. Choose a core paper from a stage's `papers/core/manifest.tsv`.
2. Fill its `wiki/papers/<stage>/<slug>.md` using all ten dimensions, citing paper sections/figures and verified source code.
3. Distinguish author observations, our reproduction, inference and open hypotheses. Never fabricate a measurement.
4. Add or update relevant topic cards. A topic may be covered by multiple papers.
5. Rebuild the JSONL index with `python3 scripts/build_knowledge_index.py`.
6. Run `python3 scripts/validate_repo.py` and `python3 -m unittest discover -s tests -v`.

## Data model
All entry IDs are stable (`paper:arxiv:<id>`, `concept:<slug>`, `algorithm:<slug>`, `system:<slug>`).
`status=template` means metadata and prompts only; `draft` means authored but not reviewed; `reviewed` requires sources and evidence.
Paper URLs refer to original arXiv sources; downloading PDFs is separately controlled by stage scripts.
Do not embed copyrighted paper text, unverified metrics, or unsupported causal claims.
