# Stage 03 · Task Specification

Mission: Run controlled NTP training and analyze the model–data–compute tradeoff.

## Tasks
### 1. Data quality

**Task:** Prepare corpus statistics, document-level split and deduplication check.

**Definition of done:** No train/validation contamination in synthetic tests.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 2. Mini pretraining

**Task:** Train two model sizes at two token budgets with stable seeds.

**Definition of done:** Publish validation loss curves, commands and environment.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 3. Scaling study

**Task:** Estimate FLOPs with caveats and fit a basic power-law surrogate.

**Definition of done:** Include residuals, uncertainty and train-vs-serving cost discussion.

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
