# Stage 07 · Task Specification

Mission: Implement correctness-first kernels, cache analysis and reproducible online serving benchmarks.

## Tasks
### 1. Attention kernel lab

**Task:** Compare reference attention and tiled/online-softmax baseline on controlled sizes.

**Definition of done:** Check numerical tolerance before profiling speed.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 2. Cache and speculative decode

**Task:** Estimate KV memory; study block allocation, shared prefixes and draft verification.

**Definition of done:** Report cache footprint, hit rate and sampling correctness.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 3. Serving benchmark

**Task:** Measure short input, long prefill, long decode and shared-prefix workloads.

**Definition of done:** Document TTFT, TPOT, goodput, peak memory, hardware and warmup.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

## Paper review acceptance
For **each** core paper fill all ten dimensions: **Problem, Observation, Hypothesis, Algorithm, Experiment, Evidence, Limitations, Implementation, Systems, Extension**. Unknown facts must be marked `TODO / Not verified` rather than invented.

## Final artifact
- A short methods/results report under `results/` based on `docs/EXPERIMENT_TEMPLATE.md`.
- Updated task checklist with links to code/tests/runs.
- Updated knowledge index if new concepts or citations are added.
