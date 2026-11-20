# Stage 04 · Task Specification

Mission: Compare SFT, LoRA/QLoRA and DPO on a fixed held-out instruction set.

## Tasks
### 1. SFT baseline

**Task:** Build instruction masking and evaluate against frozen baseline.

**Definition of done:** No answer leakage and baseline metric recorded.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 2. LoRA vs full tune

**Task:** Implement adapter path and compare trainable parameters/memory.

**Definition of done:** Verify merge equivalence within expected precision tolerance.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 3. DPO study

**Task:** Implement preference objective with frozen reference policy.

**Definition of done:** Gradient sign sanity check and held-out comparison.

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
