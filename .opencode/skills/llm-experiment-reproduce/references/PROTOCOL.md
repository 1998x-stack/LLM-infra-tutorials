# Paper experiment reproduction playbook

## 1. Three levels of reproduction

| Level | Contract | Allowed claim |
|---|---|---|
| Exact | pinned paper version + author code/data/hardware/split with documented environment | matched target under exact declared conditions |
| Approximate | architecture/data/hardware substitutions explicitly controlled | partial/approximate reproduction, **not** identical result |
| Conceptual | synthetic toy problem tests mechanism/invariant | mechanism demonstration, **not** paper metric reproduced |

Paper version drift, hardware differences, dataset leakages and optimizer revisions must be recorded.

## 2. Pre-registration worksheet

- Claim: what exactly will be tested (paper figure/table)?
- Hypothesis and null explanation:
- Baseline and treatment:
- Independent variable(s):
- Fixed controls:
- Metric with definition and expected direction:
- Acceptance tolerance specified **before** seeing local results:
- Number of seeds/runs and maximum compute/data budget:
- Stop condition and fallback if resources unavailable:

## 3. Setup checklist

| Area | Inspect |
|---|---|
| Data | origin, license, checksum/version, deduplication, train/val/test boundaries |
| Tokenization | tokenizer revision, special tokens, packed sequence and label shift |
| Model | architecture, weights/checkpoint, initialization, number of parameters |
| Training | optimizer, LR scheduler, weight decay, gradient accumulation, clipping, number of tokens/steps |
| Evaluation | parser, sampling temp/top-p, prompt format, masking, calibration and metric code |
| Hardware | CPU/GPU type, VRAM, compute capability, interconnect, precision, determinism constraints |
| Evidence | exact commands/logs, elapsed time, code revision, failures, figures |

## 4. Correctness and experimental statistics

- Assert the reference outcome before optimizing. For floating point, choose tolerance based on numerical method and dtype, not arbitrarily tight.
- Stochastic studies: run multiple seeds when possible; report spread with sample size. Do not claim statistical significance from a single favorable seed.
- For classification, define the unit of sampling and whether bootstrap resampling is valid.
- Track cost and time. A local trial using 1/1000th the paper compute is often a **conceptual test**, not full reproduction.

## 5. Domain-specific traps

**Grokking:** data split, prime modulus, weight decay, model width, optimizer, seeds, training steps; report training-vs-test curves and inspect circuits rather than only accuracy.

**World model/probes:** distinguish probe decoding from causal model use; include random-direction interventions and multiple probe-capacity controls.

**SAE:** log sparsity, reconstruction fidelity, dead features, downstream loss recovery and steering effect vs perturbation control.

**Reasoning RL:** prompt/test contamination; answer checker and reward hack risks; policy/reference/rollout version; group rewards with zero variance; KL estimator and length normalization.

**Test-time search:** hold model/decoding conditions constant; report total generation + verifier tokens, not just the number of branches.

## 6. Mismatch diagnosis tree

1. **Numerically wrong baseline?** Check equations, dtype, masks, label shift, gradient sign and objective implementation.
2. **Correct on synthetic, wrong on real data?** Check data preprocessing, train/eval split, tokenizer and prompt.
3. **Same setup, different quality?** Check learning rate schedule, seed, precision, evaluation parser, checkpoint/version.
4. **Same quality, different speed?** Hardware architecture, software/kernel version, batch, warmup and synchronization.
5. **Data/code inaccessible?** Status `blocked`. Do not invent missing settings.

## 7. Output discipline

Separate columns: `paper-reported`, `local-measured`, `estimated`, `not verified`. If any are unknown, write `N/A`. Preserve negative results and any deviations from the original method.

