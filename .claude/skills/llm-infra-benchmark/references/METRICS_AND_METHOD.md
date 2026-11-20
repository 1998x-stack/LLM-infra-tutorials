# LLM Infra performance metrics and test method

## 1. Precise metrics (write measurement boundaries)

Let request `i` arrive at time `a_i`, first output token at `f_i`, final token completion at `c_i`, output token count `n_i`.

- **TTFT_i** = `f_i - a_i`. Note queueing and network inclusion in the test setup.
- **E2E_i** = `c_i - a_i`.
- **Mean TPOT_i** = `(c_i - f_i) / max(n_i - 1, 1)` for multi-token streaming responses; mark single-token requests separately rather than dividing by 1 and treating it as comparable.
- **ITL** = inter-output-token gaps; report p50/p95 over requests or tokens and describe weighting.
- **Output token throughput** = sum of output tokens / wall-clock measured interval.
- **Request throughput** = completed requests / wall-clock interval.
- **Goodput** = completed requests satisfying stated TTFT/TPOT/E2E SLO / interval. State whether quality threshold is also included.
- **Cache efficiency** = eligible/reused prefetched tokens or KV blocks / eligible total (define denominator precisely).
- **Peak VRAM** = max allocated and max reserved (separate backend/runtime instrumentation).
- **Speedup** = baseline time / treatment time for matched quality and workload; do not compare kernel-only to server end-to-end.

Percentiles need request count and methodology; report dropped/failed/OOM/timeouts as outcomes rather than silently excluding them.

## 2. Minimum workload matrix

| Workload | Input tokens | Output tokens | Concurrency | Prefix/cache | Dominant question |
|---|---:|---:|---:|---|---|
| Short chat | 128–512 | 32–128 | 1, 8, 32 | mostly cold | queue/TTFT |
| Long prefill | 8k–32k | 32–128 | low/mid | mixed | prefill kernel/IO |
| Long reasoning | 1k–4k | 2k–8k | mixed | warm/cold | KV/Decode/TPOT |
| Shared-prefix | fixed common prefix | varying | 8, 32 | high overlap | prefix reuse/eviction |
| Mixed arrivals | synthetic empirical distribution | varying | varied | mixed | scheduler fairness/goodput |

These are **illustrative** sizes; adjust to model context support, hardware and user-supplied traffic. Do not force 32k requests on unsupported devices.

## 3. Kernel correctness suite

- Non-contiguous/contiguous tensors, varying seq lengths (1, boundary block sizes), different head dimensions and GQA ratios.
- Causal/non-causal attention mask semantics and padding.
- Float32 baseline before BF16/FP16/FP8; use dtype-aware absolute/relative error and downstream loss checks.
- For backward kernels compare gradients, not only forward output.
- Ensure timing code synchronizes GPU and does not include data allocation if the baseline excludes it.

## 4. KV/prefix/speculative checklist

- KV bytes: `2 × layers × sequences × context × kv_heads × head_dim × bytes_per_element`, plus page/table/allocator overhead.
- Compare cached versus uncached logits on identical prefixes; test cache hits, misses, eviction, COW branches and block fragmentation.
- Speculative decoding: target distribution acceptance/rejection plus residual sampling; acceptance rate and token generation cost belong in the speedup estimate.
- Multi-GPU: measure KV transfer/network and synchronization—not just standalone GPU FLOPs.

## 5. Repeatability and fairness

1. Pin model/config and workload generator seeds; test cold and warm separately.
2. Warmup enough to stabilize compilation/graphs and caches; disclose warmup policy.
3. Use repetitions, not one best run; report p50/p95 and confidence when feasible.
4. Record clocks, thermal throttling, power cap, competing jobs and network load.
5. Avoid reusing throughput/speedup claims when batch, precision, or quality changes without disclosure.
6. When no device is present, return `benchmark plan + NOT MEASURED`.

## 6. Bottleneck diagnosis

| Observation | Plausible cause | Inspect |
|---|---|---|
| High TTFT, normal TPOT | queueing, prefill contention | scheduler log, prefill time |
| Normal TTFT, poor TPOT | KV read bandwidth, small-batch launch costs | memory throughput, per-step profile |
| Low GPU compute utilization | CPU orchestration, kernel launch, underbatching | timeline and SM occupancy |
| High peak VRAM | KV fragmentation, long sessions, duplicate prefixes | allocator and blocks |
| Mixed-load goodput regression | prefill/decode interference | per-class SLO, chunking |
| Multi-GPU latency rise | collectives, interconnect contention, load imbalance | AllReduce/AllToAll, network traces |

Every conclusion needs supporting measurements rather than only this hypothesis table.

