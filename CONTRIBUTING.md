# Contributing

We welcome reproducible implementations, paper reviews, experiment protocols and LLM infrastructure measurements.

## Development contract

1. Choose a task in `stages/<stage>/tasks/TASKS.md`.
2. Match the implementation to `code/<category>/`; do not mix measurement harnesses with code under test.
3. Start with a readable reference baseline, then add correctness tests and only then optimize.
4. For measured results document commit, device, driver, framework, model, data, precision, seeds, warmup, input/output sizes, repetitions and full commands.
5. Keep every experimental claim falsifiable; mark unimplemented or unverified work **TODO**.
6. Link original papers. Do not commit PDFs, pretrained weights, datasets, access tokens or proprietary material.
7. Run `make validate` before opening a PR.

Follow [Code Categories](docs/CODE_CATEGORY.md), [Research Protocol](docs/REPRODUCIBILITY.md) and [Knowledge Schema](wiki/SCHEMA.md).

## Research note requirement

A paper review must complete all ten dimensions: **Problem, Observation, Hypothesis, Algorithm, Experiment, Evidence, Limitations, Implementation, Systems, Extension**. Do not claim independent replication until code and measurements exist.

## File naming

- Paper slug and wiki entry: `lower-kebab-case`.
- Python module: `lower_snake_case.py`.
- Reproduction report: `YYYYMMDD-experiment-topic.md`.
- Prefer concise, independent commits; include scope and reproducibility in the PR description.
