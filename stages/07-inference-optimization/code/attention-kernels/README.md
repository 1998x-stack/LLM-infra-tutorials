# attention-kernels

**Stage:** 07 · Inference Optimization & Serving

## Implemented: CPU educational baseline

`exercise.py` now contains two dependency-free, single-head scaled dot-product attention operators:

- `reference_attention(Q, K, V, causal=False)`: row-wise stable softmax baseline.
- `online_attention(Q, K, V, block_size=8, causal=False)`: block streaming recurrence using running row maximum, denominator and weighted numerator.

Inputs are finite rectangular Python matrices, `Q:[Nq,d]`, `K:[Nk,d]`,
`V:[Nk,dv]`; output is `[Nq,dv]`. Causal masking supports a suffix
of the key sequence where `Nk >= Nq`. Wrong shapes, nonfinite values and
invalid tile sizes raise `ValueError`. Computation is float64-like Python
arithmetic, no dropout or padding mask.

### Validation and measured protocol

```bash
python3 -m unittest tests.test_stage07_online_attention -v
python3 stages/07-inference-optimization/code/attention-kernels/exercise.py \
  --seq 32 --dim 16 --value-dim 16 --block-size 8 \
  --seed 7 --warmup 3 --repeats 7 --causal
```

The JSON CLI report records Python/platform, shapes, random seed, warmups,
repetitions, exact correctness tolerance and per-variant wall-clock latency.
The benchmark **must not** be used to claim GPU performance: Python overhead
dominates and no CUDA timing, cache traffic or kernel fusion is measured.

`tests/test_stage07_online_attention.py` checks multiple shapes, causal
suffix semantics, prefix invariance, numerical stability and negative inputs.

## Still TODO

- Triton/CUDA fused attention implementation and accuracy at mixed precision.
- Hardware-specific HBM IO, GPU occupancy, warm-up and profiler measurements.
- Full FlashAttention performance reproduction with paper-matched workloads.
- Multi-head/batched attention, dropout and padding masks.

This stage remains **partially implemented**, not a finished Stage 07 lab.
