# Stage 03 · Pretraining & Scaling

**Weeks:** 4–5 · **Core papers:** 5 · **Status:** scaffold (not a completed reproduction)

> Run controlled NTP training and analyze the model–data–compute tradeoff.

## Learning objectives
- Build auditable train/eval splits and token statistics.
- Train multiple small models under controlled conditions.
- Fit a small scaling trend without claiming universal scaling laws.

## Prerequisites
Complete Stage 02 or document equivalent proficiency.

## Milestones
1. **Data quality:** Prepare corpus statistics, document-level split and deduplication check.
   - **Acceptance:** No train/validation contamination in synthetic tests.
2. **Mini pretraining:** Train two model sizes at two token budgets with stable seeds.
   - **Acceptance:** Publish validation loss curves, commands and environment.
3. **Scaling study:** Estimate FLOPs with caveats and fit a basic power-law surrogate.
   - **Acceptance:** Include residuals, uncertainty and train-vs-serving cost discussion.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | `2001.08361` | `kaplan-scaling` |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | `2203.15556` | `chinchilla` |
| [The Pile: An 800GB Dataset of Diverse Text for Language Modeling](https://arxiv.org/abs/2101.00027) | `2101.00027` | `pile` |
| [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) | `2406.17557` | `fineweb` |
| [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) | `2407.21783` | `llama3` |

**Download from any current directory:**
```bash
bash stages/03-pretraining-scaling/papers/core/download.sh --list
bash stages/03-pretraining-scaling/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`data`](code/data/README.md) | Preprocessing, quality filtering, tokenizer and data cards. |
| [`pretraining`](code/pretraining/README.md) | NTP training, evaluation, checkpoints and profiling. |
| [`scaling`](code/scaling/README.md) | Compute/FLOP models and measured loss curves. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
