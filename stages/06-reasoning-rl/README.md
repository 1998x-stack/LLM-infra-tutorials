# Stage 06 · Reasoning, Search & Reinforcement Learning

**Weeks:** 9–10 · **Core papers:** 6 · **Status:** scaffold (not a completed reproduction)

> Evaluate test-time search and a small verifiable-reward policy optimization loop.

## Learning objectives
- Compare direct answer, CoT and self-consistency on matched tasks.
- Distinguish Pass@K, Majority@K and verifier-based best-of-N.
- Derive policy ratios, group advantage and KL regularization.

## Prerequisites
Complete Stage 05 or document equivalent proficiency.

## Milestones
1. **Reasoning quality:** Run direct, CoT and self-consistency on a held-out verified set.
   - **Acceptance:** Report Accuracy/Token/Latency with consistent answer extraction.
2. **Budget-aware search:** Implement candidate selection with a verifier and multiple budgets.
   - **Acceptance:** Report accuracy–compute curve with complete compute accounting.
3. **Group relative RL:** Implement synthetic GRPO advantage and small online rollout loop.
   - **Acceptance:** Check zero-variance groups and policy/reference version integrity.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | `2201.11903` | `cot` |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) | `2203.11171` | `self-consistency` |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | `2305.10601` | `tree-of-thoughts` |
| [Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) | `2408.03314` | `test-time-compute` |
| [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) | `2402.03300` | `deepseekmath` |
| [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | `2501.12948` | `deepseek-r1` |

**Download from any current directory:**
```bash
bash stages/06-reasoning-rl/papers/core/download.sh --list
bash stages/06-reasoning-rl/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`prompting`](code/prompting/README.md) | Direct/CoT prompts, answer extraction, token accounting. |
| [`search`](code/search/README.md) | Self-consistency, Best-of-N, tree exploration and verifiers. |
| [`rl`](code/rl/README.md) | Reward computation, GRPO and offline rollout analysis. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
