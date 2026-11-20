# Research and experiment protocol

Every result needs a claim, a reference, a baseline, a method, and a falsifiable evaluation.

## Required metadata

- Paper title, URL and version, plus upstream code revision if used.
- Dataset source, split, tokenizer and prompt template.
- Model identifier and revision, hyperparameters, precision and random seeds.
- Hardware, driver, CUDA/ROCm, framework and package versions.
- Exact command, timeout, repetitions, warmup and measurement tool.
- Correctness tolerances, outcome metrics, memory and latency details.
- Failure conditions, confounders and a limit on what the evidence supports.

## Standard report

```markdown
# Experiment: <title>
- Stage / task:
- Hypothesis / baseline:
- Paper and version:
- Git SHA / command:
- GPU, driver, CUDA, framework:
- Dataset / model / seed / precision:
- Warmup and sample count:
- Correctness criteria:
- Results (p50/p95/mean with repetitions):
- Error bars and anomalies:
- Reproduced / partial / blocked:
- Interpretation and limitations:
```

Serving reports should separate TTFT, TPOT, throughput and SLO-constrained goodput. GPU timing should use CUDA events or appropriate synchronization. A best-ever timing is not a benchmark.
