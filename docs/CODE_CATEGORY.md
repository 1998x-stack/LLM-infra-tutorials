# Code categories and architecture

Separate research reference implementations, test harnesses, and production-oriented optimizations. Each stage has its own `code/<category>/`.

| Stage | Categories | Ownership |
|---|---|---|
| 01 | `algorithms`, `autograd`, `language-modeling` | numerical math, gradients, N-grams |
| 02 | `attention`, `model`, `decoding` | Transformer operations and generation |
| 03 | `data`, `pretraining`, `scaling` | preprocessing, train loop, scaling study |
| 04 | `sft`, `peft`, `preference` | finetuning, adapters, preference optimization |
| 05 | `grokking`, `probes`, `sae` | circuits, representation decoders and sparse features |
| 06 | `prompting`, `search`, `rl` | CoT, candidate selection, reward optimization |
| 07 | `attention-kernels`, `kv-cache`, `serving`, `benchmarks` | compute kernels, cache, scheduling, evaluation |
| 08 | `parallelism`, `moe`, `distributed-serving` | DP/TP/PP/EP, experts and orchestration |

## Module contract

For each `code/<category>/`:
1. Record inputs, shapes, dtype, precision, state and output contract in README.
2. Write a minimal reference implementation before optimized code.
3. Add tests in the matching stage `tests/`.
4. Put experiment configurations in `experiments/` and measured reports in `results/`.
5. Avoid committing model weights and benchmark data dumps.

Prefer readable modules with explicit CLI entry points. Do not claim unimplemented scaffolds to be functioning code.
