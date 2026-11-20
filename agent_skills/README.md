# Canonical, portable LLM Infra skills

The five skills in this directory are the **single source of truth**. The same `SKILL.md`, `references/` and `assets/` are copied into five client-specific locations by a deterministic offline sync tool.

| Skill | Scope | Supporting docs |
|---|---|---|
| [llm-paper-deep-review](llm-paper-deep-review/SKILL.md) | source-anchored ten-dimensional reading | evidence protocol and note template |
| [llm-stage-lab](llm-stage-lab/SKILL.md) | milestone delivery and stage DoD | lab gate matrix and handoff |
| [llm-experiment-reproduce](llm-experiment-reproduce/SKILL.md) | exact/approximate/conceptual reproduction | replication protocol and report |
| [llm-infra-benchmark](llm-infra-benchmark/SKILL.md) | correctness-first GPU/serving benchmarking | metric definitions and report |
| [llm-knowledge-curator](llm-knowledge-curator/SKILL.md) | wiki taxonomy, provenance and index | integrity policy and change report |

## How to edit

1. Edit `agent_skills/<name>/SKILL.md` and its `references/` or `assets/`.
2. Run `python3 scripts/sync_agent_skills.py`.
3. Run `python3 scripts/sync_agent_skills.py --check`, `make validate` and inspect diffs.
4. Evaluate triggers and workflow outputs in fresh agent sessions using [evaluation cases](evals/README.md).

Do **not** edit mirrored files directly; they will be overwritten during sync.

## Discoverability and progressive disclosure

The frontmatter description is short and task-specific so agents load only relevant skills. Each `SKILL.md` contains the minimal execution contract. Specialized math, metrics, edge cases and templates reside in supporting files, loaded only when relevant. This follows the public [Agent Skills format](https://agentskills.io/specification).

Mirrors: `.claude/skills`, `.agent/skills`, `.agents/skills`, `.pi/skills`, `.opencode/skills`. Some agents can discover multiple mirror roots, but identical IDs/content prevent semantic divergence. The host chooses precedence; no skill claims permission to execute external actions.

