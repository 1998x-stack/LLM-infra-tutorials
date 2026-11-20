# Stage lab playbook: implementation and acceptance

## Dependency map

| Stage | Reference exercise | Correctness evidence | Measured outcome |
|---|---|---|---|
| 01 Foundations | stable logsumexp, N-gram, AdamW | finite differences and negative split-leakage tests | loss/perplexity |
| 02 Transformer | masked Attention, RoPE/GQA, incremental decode | future-token independence and full-vs-cache logits | correctness first; VRAM |
| 03 Pretraining | data/tokenizer, NTP loop, scaling | split integrity, loss parity and seed control | validation loss vs FLOPs |
| 04 Post-training | SFT mask, LoRA merge, DPO objective | gradient sign and merge equivalence | quality/memory |
| 05 Interpretability | Grokking, probes, SAE | random controls, independent probe splits, ablation | accuracy and explanatory limits |
| 06 Reasoning RL | CoT/Best-of-N, verifiers, GRPO | answer parser, zero-variance group, reward leakage | success per compute budget |
| 07 Inference | kernel, cache, batching, serving | numerical identity and cache state tests | TTFT, TPOT, goodput, VRAM |
| 08 Distributed | parallel memory model, MoE router | tensor partition/dispatch invariants | collective communication, load balance |

## File-level task decomposition

For every milestone, declare:
- Target `code/<category>/<module>.py`: public API, input/output shapes, optional dependencies and error behavior.
- `tests/test_<module>.py`: reference oracle, edge cases and tolerance.
- `experiments/configs/<run>.yaml`: model/data/device/dtype/batch/seed.
- `results/<run>.md`: actual observations, baseline, limitations, commands and environment.

Avoid introducing hidden network calls in imports or tests. Use synthetic data for initial correctness checks.

## Gate 2: minimal correctness matrix

| Class | Mandatory check |
|---|---|
| Shapes | varying batch, heads, sequence length including 1 |
| Types | float32/float64 on CPU; BF16/FP16 only when supported |
| Masks/causality | future token edits cannot change prior logits |
| Optimization | loss decreases on tiny synthetic task; expected update sign |
| Reproducibility | seed set where relevant, no train/validation leakage |
| Errors | invalid shapes/dtypes give explicit error or documented constraints |

## Gate 3: experiment contract

1. Define the baseline and *one* independent variable.
2. Pin all remaining factors; for nondeterministic GPU tests record seeds and uncertainty.
3. Validate reference outputs on identical inputs before benchmarking.
4. Capture exact commands and run IDs. Do not silently adapt parameters after viewing results without recording it.
5. Record negative results. An improvement in accuracy with a 4× cost increase is a tradeoff, not a free gain.

## Checkboxes and completion

- A task may be **done** only with code, passing relevant tests, actual reproduction/benchmark evidence, and a truthful report.
- **partial** means some acceptance criteria passed; list missing checks.
- **blocked** means a specific external dependency is absent; include a CPU fallback if safe.
- **not started** is the correct status for a placeholder.

Pass repository structural checks separately from task-level correctness: `make validate` is necessary for repository hygiene, not sufficient for finishing a stage.

## Handoff routing

- Paper questions that require source re-reading → paper skill.
- Claims involving replication/figures → experiment reproduction skill.
- Kernel/serving comparison → Infra benchmark skill.
- Updating wiki crosslinks/schema → knowledge curator.

