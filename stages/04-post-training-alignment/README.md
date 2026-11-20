# Stage 04 · SFT, PEFT & Preference Optimization

**Weeks:** 6 · **Core papers:** 4 · **Status:** scaffold (not a completed reproduction)

> Compare SFT, LoRA/QLoRA and DPO on a fixed held-out instruction set.

## Learning objectives
- Distinguish pretrained, supervised and preference-tuned policies.
- Compute trainable parameter and optimizer memory footprints.
- Test LoRA merge and DPO preference loss on synthetic cases.

## Prerequisites
Complete Stage 03 or document equivalent proficiency.

## Milestones
1. **SFT baseline:** Build instruction masking and evaluate against frozen baseline.
   - **Acceptance:** No answer leakage and baseline metric recorded.
2. **LoRA vs full tune:** Implement adapter path and compare trainable parameters/memory.
   - **Acceptance:** Verify merge equivalence within expected precision tolerance.
3. **DPO study:** Implement preference objective with frozen reference policy.
   - **Acceptance:** Gradient sign sanity check and held-out comparison.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | `2203.02155` | `instructgpt` |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | `2106.09685` | `lora` |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | `2305.14314` | `qlora` |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | `2305.18290` | `dpo` |

**Download from any current directory:**
```bash
bash stages/04-post-training-alignment/papers/core/download.sh --list
bash stages/04-post-training-alignment/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`sft`](code/sft/README.md) | Instruction-response packing and supervised tuning. |
| [`peft`](code/peft/README.md) | Low-rank adapters, memory estimates and quantization controls. |
| [`preference`](code/preference/README.md) | Chosen/rejected data and DPO objective. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
