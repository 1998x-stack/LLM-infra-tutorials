# Stage 01 · Task Specification

Mission: Master NTP loss and numerical optimization with CPU-verifiable baselines.

## Tasks
### 1. Stable probability operators

**Task:** Implement logsumexp and token cross-entropy and test against a reference.

**Definition of done:** max relative error ≤ 1e-6 on float64 synthetic inputs; tests documented.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 2. N-gram model

**Task:** Implement an N-gram baseline with smoothing and document-level train/validation split.

**Definition of done:** Outperform uniform baseline on synthetic structured data, without split leakage.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 3. Training loop

**Task:** Train a tiny model with reproducible optimizer settings.

**Definition of done:** Record seed, optimizer, loss curve and CPU/GPU environment.

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
