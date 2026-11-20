# LLM Infra Tutorials — Agent instructions

This repository is a research curriculum with executable scaffolding, not a finished benchmark suite. Preserve truthful implementation status.

## Read before editing
- `README.md`, `docs/CODE_CATEGORY.md`, `docs/REPRODUCIBILITY.md`.
- `curriculum.json` and target stage's `tasks/TASKS.md`.
- `wiki/SCHEMA.md`, `wiki/templates/PAPER_REVIEW_TEMPLATE.md`.

## Reusable skills
The portable skill set is available at `.agent/skills/` and `.agents/skills/`, mirrored for `.claude/skills/`, `.pi/skills/` and `.opencode/skills/`. Choose the relevant `SKILL.md` rather than relying on generic instructions:
- `llm-paper-deep-review`: review a paper via ten evidence dimensions.
- `llm-stage-lab`: implement a curriculum task.
- `llm-experiment-reproduce`: reproduce a claim with controlled experiments.
- `llm-infra-benchmark`: characterize GPU/serving behavior.
- `llm-knowledge-curator`: maintain wiki and JSONL index.

## Non-negotiable policies
1. Do not fabricate citations, measured speedups, model qualities or reproduced results.
2. Keep full paper PDFs, model weights, datasets, keys and profiler dumps out of Git.
3. Reproduce a baseline with correctness tests before proposing optimization.
4. Keep `wiki/knowledge.jsonl` in sync by running `scripts/build_knowledge_index.py`.
5. Use `python3 scripts/validate_repo.py` and offline unit tests before commits.
6. Network downloads, GPU-costly experiments and external changes require user intent/appropriate permissions.
7. Distinguish paper-author evidence from local experiments and hypotheses.
