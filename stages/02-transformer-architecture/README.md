# Stage 02 · Transformer Architecture

**Weeks:** 2–3 · **Core papers:** 5 · **Status:** scaffold (not a completed reproduction)

> Build and verify a modern decoder-only GPT with position encoding and KV-cached decode.

## Learning objectives
- Derive causal attention matrix shapes and complexity.
- Implement Transformer blocks, RoPE and GQA with explicit shape contracts.
- Compare full-context and incremental decoding numerically.

## Prerequisites
Complete Stage 01 or document equivalent proficiency.

## Milestones
1. **Decoder-only model:** Implement masked attention, FFN, normalization, residual stream and LM head.
   - **Acceptance:** Run deterministic forward/backprop and verify future tokens are masked.
2. **RoPE/GQA extensions:** Implement rotary Q/K transformation and grouped KV heads.
   - **Acceptance:** Shape and memory calculation match implementation.
3. **Cached generation:** Implement a prefill/decode interface with KV reuse.
   - **Acceptance:** Cached and uncached evaluation logits agree within documented dtype tolerance.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | `1706.03762` | `transformer` |
| [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | `2005.14165` | `gpt3` |
| [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) | `2104.09864` | `roformer` |
| [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) | `2305.13245` | `gqa` |
| [Mistral 7B](https://arxiv.org/abs/2310.06825) | `2310.06825` | `mistral7b` |

**Download from any current directory:**
```bash
bash stages/02-transformer-architecture/papers/core/download.sh --list
bash stages/02-transformer-architecture/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`attention`](code/attention/README.md) | Causal MHA, RoPE and GQA operators. |
| [`model`](code/model/README.md) | GPT embeddings, RMSNorm/LayerNorm, FFN and residual blocks. |
| [`decoding`](code/decoding/README.md) | Greedy/sampling generation, stop criteria and KV-cached decode. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
