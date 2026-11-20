# Claude Code project context

Follow [AGENTS.md](AGENTS.md) and [Contributor Guide](CONTRIBUTING.md). Project skills are in `.claude/skills/*/SKILL.md` and are named `llm-paper-deep-review`, `llm-stage-lab`, `llm-experiment-reproduce`, `llm-infra-benchmark`, and `llm-knowledge-curator`.

Prioritize **correctness → reproducibility → optimization**, and never claim a scaffold or paper-template note is a completed reproduction.

- Curriculum: `curriculum.json`
- Task source: `stages/<stage>/tasks/TASKS.md`
- Core papers: `stages/<stage>/papers/core/manifest.tsv`
- Paper review: `wiki/templates/PAPER_REVIEW_TEMPLATE.md`
- Knowledge index: `wiki/knowledge.jsonl`
- Offline validation: `make validate`

Do not run bulk PDF downloads or expensive GPU jobs without a relevant explicit task.
