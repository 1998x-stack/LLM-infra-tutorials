---
name: llm-infra-benchmark
description: "Use when benchmarking GPU attention, KV Cache, vLLM/SGLang inference serving, speculative decoding, prefill/decode scheduling, distributed MoE or memory/throughput optimization."
---

# Benchmark LLM infrastructure rigorously

## Activation
Use for requests involving speedups, GPU kernels, batching, KV memory, cache hit rates, prefill/decode, vLLM/SGLang, GPU profiling, throughput, latency or goodput.

## Establish the workload
1. Name the exact baseline and proposed implementation (commit/revision), model revision, GPU and interconnect topology.
2. Record input distribution: prompt tokens, output tokens, concurrency, batch size, cold/warm cache, prefix sharing, decoding policy and dtype.
3. Separate **prefill**, **decode**, and any verifier or network transfer overhead. Do not aggregate incompatible workloads into one unqualified number.

## Correctness before timing
- Compare reference and optimized logits/outputs at explicit tolerances.
- For speculative decoding verify target distribution preservation under the chosen sampler.
- For KV cache and paging verify allocation, eviction, prefix sharing and tensor shape/state invariants.
- For GPU kernels validate boundary conditions, masks, dimensions, precision and numerical stability.

## Benchmark method
1. Warm up, synchronize GPU timing or use CUDA events and repeat under a fixed environment.
2. Report p50/p95 TTFT, TPOT, request throughput, output-token throughput, goodput under specified SLO, peak allocated/reserved VRAM and cache hit rate.
3. Profile resource bottlenecks: HBM, compute occupancy, kernel launch overhead, collective communication and CPU scheduler.
4. Present at least one quality/cost or performance/memory tradeoff, not just best-case speedup.
5. Describe measurement tool, repetitions and outlier handling; never claim speedups without a matched baseline.

## Files
Place benchmark runners in `stages/07-inference-optimization/code/benchmarks/`, configs in `experiments/` and compact reports in `results/`. Distributed-system benchmarks may live under Stage 08.

## Output
A reproducible command and machine-readable result summary, a small comparison table, a bottleneck diagnosis and unverified assumptions. Use `docs/REPRODUCIBILITY.md`.

## Repository-relative paths
All paths above are relative to the repository root; from this file the root is `../../..`. Do not create or modify external files without explicit permission.
