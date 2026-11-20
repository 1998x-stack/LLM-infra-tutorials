---
name: llm-stage-lab
description: "Plan, implement, audit, or complete a numbered stage (01–08) of the LLM-infra 16-week curriculum. Use for stage tasks, code-category work, reference implementations, acceptance criteria, checkpoints, test cases, or stage progress; delegate deep paper reading, reproduction, benchmark and wiki maintenance to their specialized skills."
compatibility: "Repository project skill. Python 3.10+ is sufficient for offline validation; GPU/data/model dependencies vary by stage."
metadata:
  version: "2.0.0"
  category: "engineering"
---

# Execute one LLM learning stage

**Outcome:** a minimal **working, tested, and evidenced** stage deliverable; never confuse existing TODO scaffolding with completed implementation.

## Route and prerequisites

- **Use:** "start Stage 02", "week 7 plan", "implement the KV-cache lab", "audit Stage 05 progress", "finish a stage task".
- **Other skills:** paper-only explanation → `llm-paper-deep-review`; exact figure reproduction → `llm-experiment-reproduce`; serving performance study → `llm-infra-benchmark`; wiki/index repair → `llm-knowledge-curator`.
- Resolve the stage from `curriculum.json`, then inspect `stages/<stage>/README.md`, `tasks/TASKS.md`, `code/` and `tests/` **before editing**. Read `docs/CODE_CATEGORY.md` and `docs/REPRODUCIBILITY.md`.
- Do not assume a stage is incomplete solely because a checkbox remains unchecked; inspect files and tests before updating state.

## Execution gates

**Gate 0 — Scope:** Select one concrete milestone and write down its desired behavior, input/output contract, prerequisites, hardware/data availability and accepted cost. If no GPU is available, implement and test a CPU baseline and label performance work blocked.

**Gate 1 — Plan:** Map the milestone to the allowed code category and enumerate **source file → test → experiment config → report**. Derive the minimal reference algorithm from the assigned paper, not solely its README.

**Gate 2 — Correctness:** Write or repair the reference implementation. Test shapes, mask/sequence boundaries, numerical stability, deterministic seeds and negative cases. Do not replace `NotImplementedError` with a fake pass or an untested stub.

**Gate 3 — Controlled experiment:** Create a matched baseline, exact command and settings. Keep model/data versions, precision and batch/sequence lengths fixed where the hypothesis requires it.

**Gate 4 — Evidence and review:** Record observations under `results/`; update task checkboxes only when acceptance criteria are actually met, and link checks plus command/log path. If blocked, include a precise blocker and the next smallest safe action.

## Deliverables

- Runnable reference implementation in `stages/<stage>/code/<category>/`, with an intentionally explicit CLI or function API.
- Tests in stage `tests/`, config in `experiments/`, compact report in `results/`.
- Task status **done / partial / blocked / not started**, with evidence paths and remaining failures.
- A short next-step decision based on acceptance results, not hypothetical completion.

Read [lab playbook](references/PLAYBOOK.md) for stage-specific traps, task decomposition and evidence gates; use [handoff template](assets/STAGE_HANDOFF.md) for the final report.

## Stop and safety criteria

- Do not automatically download untrusted dependencies/models/datasets, run expensive GPU clusters, deploy services or commit secrets.
- Preserve existing working code and stage scope; avoid unrelated refactors.
- Never mark a stage complete using only passing scaffolding/structure tests.
- Run `make validate` (or the available equivalent) after changes; state skipped GPU tests and missing data explicitly.

