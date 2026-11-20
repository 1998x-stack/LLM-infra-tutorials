# Stage 08 · Distributed Training & Frontier Architecture

**Weeks:** 14–16 · **Core papers:** 6 · **Status:** scaffold (not a completed reproduction)

> Reason about DP/TP/PP/EP memory, routing and collective communication tradeoffs.

## Learning objectives
- Quantify sharded optimizer, parameter and gradient memory.
- Explain TP collectives, PP bubbles and EP token dispatch.
- Implement and evaluate a small Top-K expert router.

## Prerequisites
Complete Stage 07 or document equivalent proficiency.

## Milestones
1. **Parallelism calculator:** Model DP/TP/PP/ZeRO states for a fixed transformer shape.
   - **Acceptance:** Compare memory and communication with explicit assumptions.
2. **MoE router:** Implement Top-K routing and inspect tokens-per-expert imbalance.
   - **Acceptance:** Test capacity and load-balancing behavior across seeds.
3. **Distributed case study:** Build a TP/PP/EP deployment analysis from an open architecture.
   - **Acceptance:** Report network volume, latency model, bottlenecks and limits.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) | `1909.08053` | `megatron-lm` |
| [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) | `1910.02054` | `zero` |
| [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) | `2104.04473` | `megatron-3d` |
| [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) | `2101.03961` | `switch` |
| [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) | `2405.04434` | `deepseek-v2` |
| [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | `2412.19437` | `deepseek-v3` |

**Download from any current directory:**
```bash
bash stages/08-distributed-frontiers/papers/core/download.sh --list
bash stages/08-distributed-frontiers/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`parallelism`](code/parallelism/README.md) | DP, TP, PP, ZeRO memory and communication modeling. |
| [`moe`](code/moe/README.md) | Expert routing, balancing, capacity and dispatch. |
| [`distributed-serving`](code/distributed-serving/README.md) | Distributed inference orchestration and topology analysis. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
