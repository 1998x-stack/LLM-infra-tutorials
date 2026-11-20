---
name: llm-experiment-reproduce
description: "Reproduce or diagnose a specific LLM paper experiment, figure, ablation, training curve, probing intervention, model-quality result, or numerical claim. Use for controlled baseline comparisons, confidence intervals, reproducibility protocols, and failure analysis; use the Infra skill for primary serving/GPU performance benchmarking."
compatibility: "Python 3.10+ for offline validation; experiments may require explicitly provisioned GPU, datasets and pinned package versions."
metadata:
  version: "2.0.0"
  category: "research-execution"
---

# Reproduce an LLM research result

**Outcome:** an auditable result on specified hardware/data—not a confident restatement of paper numbers. A paper's result is **reported**, not **locally reproduced**, until executed here.

## When to invoke and delegate

- **Invoke:** "reproduce Figure 3", "check Grokking transition", "run ablation", "why won't this experiment match?", "evaluate SAE reconstruction" or "recreate a reasoning accuracy curve".
- **Route:** paper analysis before implementation → `llm-paper-deep-review`; stage task ownership → `llm-stage-lab`; GPU kernel/serving throughput/SLO study → `llm-infra-benchmark`; indexing evidence → `llm-knowledge-curator`.

## Reproduction protocol

**0. Identify exact target.** Pin paper ID/version, figure/table, claim, metric direction and baseline. Locate input files and upstream code commit. If exact source unavailable, do not reverse-engineer imagined settings.

**1. Pre-register a minimal test.** State falsifiable hypothesis, acceptance metric/tolerance, null explanation and compute budget. Decide `exact` (same code/data/hardware), `approximate` (documented substitutions), or `conceptual` reproduction before running.

**2. Audit the environment.** Record repository SHA, Python/torch/CUDA/driver, GPU/VRAM, model and tokenizer revisions, dataset split/hash, dtype, optimizer, seeds and sampling settings. Preserve original evaluation protocol.

**3. Implement/check baseline.** Test reference calculations, shape contracts, leaks/contamination, reward parser, data pipeline and small synthetic edge cases before expensive jobs.

**4. Run controlled comparisons.** Change one independent variable when possible, keep matched baselines, log training and validation separately, repeat across seeds when feasible and capture failure runs. Avoid test-set tuning.

**5. Analyze uncertainty.** Report actual mean/median, dispersion, confidence intervals where justified, correctness criteria and sample sizes. Highlight non-comparable hardware, missing seeds or dataset revisions; avoid copying paper metrics into local-result columns.

**6. Diagnose mismatch.** Follow [experiment playbook](references/PROTOCOL.md): data → preprocessing → training objective → model/code → optimizer → metric → hardware/nondeterminism. Distinguish `not reproduced` from `not tested`.

**7. Write artifacts.** Store small configs in `stages/<stage>/experiments/`, source code and tests in matching category, report under `results/`, and a summarized evidence pointer in Wiki only if requested.

## Result states

- `reproduced`: stated target met within declared tolerance and protocol.
- `partial`: subset reproduced, with precise divergence.
- `not-reproduced`: executable protocol completed but target failed.
- `blocked`: resource/source/runtime requirement prevented a valid test.
- `not-run`: design exists, no execution occurred.

Use [report template](assets/REPRODUCTION_REPORT.md). Always list commands executed and commands **not run**.

## Stop and safety gates

- Never fabricate training logs, model weights, benchmark timings, theorem checks or "authors' code works" statements.
- No large download, unbounded training, paid GPU allocation or external service mutation without user authorization and budget.
- If a run cannot finish within available resources, save a partial controlled result and label remaining work blocked.
- Validate offline repository integrity with `make validate` if code/docs were edited; task-level tests must also run.

