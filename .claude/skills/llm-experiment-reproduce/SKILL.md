---
name: llm-experiment-reproduce
description: "Use when reproducing numerical claims from an LLM research paper, implementing benchmark baselines, comparing results or diagnosing failed reproduction experiments."
---

# Reproduce a controlled research experiment

## When to use
Use for requests to reproduce a named figure, baseline, ablation, accuracy curve, training procedure or interpretability intervention.

## Protocol
1. Write a falsifiable hypothesis and locate the *exact* paper version, section, figure and original reported metric.
2. Identify the authors' method and code commit, plus differences from this repository's baseline.
3. Specify dataset, tokenizer, model, seed(s), precision, hardware, software versions, optimizer, compute budget and evaluation criteria.
4. Implement correctness tests before running expensive training or benchmarking. Include at least one negative/edge case.
5. Establish a matched baseline and change one principal independent variable at a time. Record all confounders.
6. Run warmup and repetitions as appropriate; for stochastic tasks use multiple seeds and report dispersion or confidence intervals.
7. Store compact configurations in `experiments/`, report in `results/`, and large traces/checkpoints outside Git.
8. Label outcomes `reproduced`, `partial`, `not reproduced`, or `blocked` using evidence. No invented success.
9. If a claim cannot be reproduced due to unavailable resources, document the blocker and supply a truthful partial analysis, not fabricated measurements.

## Report contract
Follow `docs/EXPERIMENT_TEMPLATE.md` and `docs/REPRODUCIBILITY.md`. Include: command, git SHA, baselines, environment, measured values, uncertainty, error bars if feasible, correctness criteria and failure modes.

## Special considerations
- For circuits/SAE: probe decodability is not proof of causal use. Add random-direction and ablation controls.
- For kernel comparisons: compare same tensor shapes and dtype; synchronize GPU timing.
- For RL: identify reward leakage, reference-policy staleness and rollout version.

Run `make validate` before committing.

## Repository-relative paths
All paths above are relative to the repository root; from this file the root is `../../..`. Do not create or modify external files without explicit permission.
