---
name: llm-stage-lab
description: "Use when planning, implementing or reviewing one of the eight LLM curriculum stages and its task checklists, paper readings, starter code, tests and experimental deliverables."
---

# Execute a curriculum stage

## When to use
Use for requests such as "start week 7", "implement stage 02", "finish the inference optimization exercises" or "audit progress of stage tasks".

## Inputs
Determine the exact stage ID from `curriculum.json`. Read:
- `stages/<stage>/README.md`
- `stages/<stage>/tasks/TASKS.md`
- `stages/<stage>/papers/core/manifest.tsv`
- `docs/CODE_CATEGORY.md` and `docs/REPRODUCIBILITY.md`.

## Workflow
1. Convert milestones into specific file-level changes. Preserve the stage's code-category ownership.
2. Identify prerequisites, device availability, datasets and a minimum CPU-checkable baseline. Avoid requesting GPU hardware just to validate repository structure.
3. Read/annotate relevant papers before implementing algorithms. Use `llm-paper-deep-review` when the task calls for deep analysis.
4. Implement transparent reference logic first; replace `NotImplementedError` in relevant `code/<category>/exercise.py` only when the implementation has tests.
5. Create negative/numerical edge-case tests in `tests/`; write experiment configuration under `experiments/`.
6. For optional GPU optimization, define correctness tolerances and use explicit profiler instrumentation.
7. Record *actual* results, commands, environment, seeds, caveats and failed attempts under `results/`; do not invent completion.
8. Update `tasks/TASKS.md` checkboxes only for completed, verified work and link evidence paths.

## Completion criteria
The milestone has a tested reference, a reproducible experiment, a measured report, and a clear limitation statement. Run `make validate`.

## Non-goals
Do not download large models or private datasets automatically, mix experiments with core implementation code, or mark a stage complete because the scaffolding exists.

## Repository-relative paths
All paths above are relative to the repository root; from this file the root is `../../..`. Do not create or modify external files without explicit permission.
