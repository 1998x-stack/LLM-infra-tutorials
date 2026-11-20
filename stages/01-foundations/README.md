# Stage 01 · Mathematics, Autograd & Language Modeling

**Weeks:** 1 · **Core papers:** 3 · **Status:** scaffold (not a completed reproduction)

> Master NTP loss and numerical optimization with CPU-verifiable baselines.

## Learning objectives
- Derive entropy, KL, cross-entropy and optimizer updates.
- Implement a deterministic N-gram baseline and finite-difference gradient checks.
- Explain validation leakage, reproducibility and loss/perplexity.

## Prerequisites
Python 3.10+, introductory probability, linear algebra, calculus.

## Milestones
1. **Stable probability operators:** Implement logsumexp and token cross-entropy and test against a reference.
   - **Acceptance:** max relative error ≤ 1e-6 on float64 synthetic inputs; tests documented.
2. **N-gram model:** Implement an N-gram baseline with smoothing and document-level train/validation split.
   - **Acceptance:** Outperform uniform baseline on synthetic structured data, without split leakage.
3. **Training loop:** Train a tiny model with reproducible optimizer settings.
   - **Acceptance:** Record seed, optimizer, loss curve and CPU/GPU environment.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | `1412.6980` | `adam` |
| [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101) | `1711.05101` | `adamw` |
| [Layer Normalization](https://arxiv.org/abs/1607.06450) | `1607.06450` | `layer-norm` |

**Download from any current directory:**
```bash
bash stages/01-foundations/papers/core/download.sh --list
bash stages/01-foundations/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`algorithms`](code/algorithms/README.md) | Stable softmax, logsumexp and cross-entropy with numerical tests. |
| [`autograd`](code/autograd/README.md) | Finite-difference gradient checks and SGD/AdamW update exercises. |
| [`language-modeling`](code/language-modeling/README.md) | Unigram/bigram conditional prediction, smoothing and evaluation. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
