# Stage 07 · Inference Optimization & Serving

**Weeks:** 11–13 · **Core papers:** 8 · **Status:** scaffold (not a completed reproduction)

> Implement correctness-first kernels, cache analysis and reproducible online serving benchmarks.

## Learning objectives
- Explain online softmax and IO-aware tiled attention.
- Compute GQA/MLA KV footprint and understand block allocation.
- Measure TTFT, TPOT, goodput, peak memory and cache hit rate.

## Prerequisites
Complete Stage 06 or document equivalent proficiency.

## Milestones
1. **Attention kernel lab:** Compare reference attention and tiled/online-softmax baseline on controlled sizes.
   - **Acceptance:** Check numerical tolerance before profiling speed.
2. **Cache and speculative decode:** Estimate KV memory; study block allocation, shared prefixes and draft verification.
   - **Acceptance:** Report cache footprint, hit rate and sampling correctness.
3. **Serving benchmark:** Measure short input, long prefill, long decode and shared-prefix workloads.
   - **Acceptance:** Document TTFT, TPOT, goodput, peak memory, hardware and warmup.

## Core papers
| Paper | arXiv | Slug |
|---|---|---|
| [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) | `2205.14135` | `flashattention` |
| [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691) | `2307.08691` | `flashattention2` |
| [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | `2309.06180` | `pagedattention` |
| [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) | `2211.17192` | `speculative-decoding` |
| [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) | `2312.07104` | `sglang` |
| [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670) | `2401.09670` | `distserve` |
| [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310) | `2403.02310` | `sarathi-serve` |
| [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://arxiv.org/abs/2407.08608) | `2407.08608` | `flashattention3` |

**Download from any current directory:**
```bash
bash stages/07-inference-optimization/papers/core/download.sh --list
bash stages/07-inference-optimization/papers/core/download.sh
```

## Code categories
| Directory | Purpose |
|---|---|
| [`attention-kernels`](code/attention-kernels/README.md) | Reference attention, tiling, online softmax and Triton kernels. |
| [`kv-cache`](code/kv-cache/README.md) | KV layout, page/block allocation and memory estimators. |
| [`serving`](code/serving/README.md) | Continuous batching, prefix sharing and prefill/decode scheduling. |
| [`benchmarks`](code/benchmarks/README.md) | Workload generators, correctness, latency and throughput measurement. |

## Research workflow
Read [stage tasks](tasks/TASKS.md) → annotate papers using [ten-dimensional template](../../wiki/templates/PAPER_REVIEW_TEMPLATE.md) → implement → test → report.
Save experiment configs under `experiments/`, honest observations under `results/` and polished paper notes under `wiki/papers/`.

## Definition of done
- [ ] Core paper notes have evidence and limitations, not only summaries.
- [ ] All milestone acceptance tests executed or clearly marked blocked.
- [ ] Reference implementation and numerical checks exist.
- [ ] Experiment configs, seeds, environment and baseline are recorded.
- [ ] Final report separates the paper's claim, observed data and interpretation.
