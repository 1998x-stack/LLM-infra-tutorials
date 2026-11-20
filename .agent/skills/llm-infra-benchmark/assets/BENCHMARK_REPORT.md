# LLM Infra benchmark report

**Hypothesis / baseline:** TODO  
**Workload type:** kernel | cache | serving | distributed  
**Reproduction state:** not-run | measured | partial | blocked

## Environment
GPU(s), VRAM, interconnect, driver, runtime, framework/serving SHA, power/clock, model/tokenizer, dtype, quantization.

## Traffic and correctness contract
Prompt/output token length distribution, arrival rate, batch/concurrency, cache condition, SLO. Oracle, tolerance, edge cases and failure counts.

## Commands
```bash
# TODO: benchmark invocation
```

## Performance results
| Metric (units) | Baseline | Treatment | Sample count | Note |
|---|---:|---:|---:|---|
| TTFT p50/p95 (ms) | NOT MEASURED | NOT MEASURED | 0 | |
| TPOT p50/p95 (ms) | NOT MEASURED | NOT MEASURED | 0 | |
| E2E p50/p95 (ms) | NOT MEASURED | NOT MEASURED | 0 | |
| Output tok/s | NOT MEASURED | NOT MEASURED | 0 | |
| SLO goodput (req/s) | NOT MEASURED | NOT MEASURED | 0 | |
| Peak allocated/reserved VRAM | NOT MEASURED | NOT MEASURED | 0 | |

## Profiler evidence
Kernel time, HBM traffic, occupancy, queueing, transfer and network data. Reference trace/run IDs but keep large traces out of Git.

## Correctness, regressions and limits
List matching output checks, failure cases, long-tail latency and tradeoffs.

## Conclusion / next experiment
Only claim measured improvements with a matched workload and clear speedup definition.

