# Stage 05 · Mechanistic Interpretability

**Weeks:** 7–8 · **Core papers:** 5 · **Status:** scaffold (not a completed reproduction)

> Study internal mechanisms with controlled probes, circuits and SAE experiments.

## Learning objectives
- Observe Grokking and inspect Fourier-related internal structure.
- Separate state decodability from causal reliance.
- Measure SAE fidelity, sparsity and intervention effects.

## Prerequisites
Complete Stage 04 or document equivalent proficiency.

## Milestones
1. **Grokking:** Train modular addition and vary weight decay/training split.
   - **Acceptance:** Report train/test curves across seeds and Fourier diagnostics.
2. **World state:** Train an Othello-style probe and perform controlled interventions.
   - **Acceptance:** Contrast probe accuracy with randomized control and causality.
3. **SAE:** Train an SAE on frozen hidden activations.
   - **Acceptance:** Report L0, reconstruction, dead-feature fraction and downstream loss.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) | `2201.02177` | `grokking` |
| [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217) | `2301.05217` | `grokking-progress` |
| [Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task](https://arxiv.org/abs/2210.13382) | `2210.13382` | `othello` |
| [Emergent Linear Representations in World Models of Self-Supervised Sequence Models](https://arxiv.org/abs/2309.00941) | `2309.00941` | `world-linear` |
| [Scaling and Evaluating Sparse Autoencoders](https://arxiv.org/abs/2406.04093) | `2406.04093` | `sae-scaling` |

**Download from any current directory:**
```bash
bash stages/05-mechanistic-interpretability/papers/core/download.sh --list
bash stages/05-mechanistic-interpretability/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`grokking`](code/grokking/README.md) | Modular arithmetic models and Fourier circuit diagnostics. |
| [`probes`](code/probes/README.md) | Linear/nonlinear probing, controls and causal activation interventions. |
| [`sae`](code/sae/README.md) | Sparse autoencoder features, reconstruction and steering. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
