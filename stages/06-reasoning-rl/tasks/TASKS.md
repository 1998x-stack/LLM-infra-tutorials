# Stage 06 · Task Specification

Mission: Evaluate test-time search and a small verifiable-reward policy optimization loop.

## Tasks
### 1. Reasoning quality

**Task:** Run direct, CoT and self-consistency on a held-out verified set.

**Definition of done:** Report Accuracy/Token/Latency with consistent answer extraction.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 2. Budget-aware search

**Task:** Implement candidate selection with a verifier and multiple budgets.

**Definition of done:** Report accuracy–compute curve with complete compute accounting.

- [ ] Read relevant core paper sections, write notes in `wiki/papers`.
- [ ] Define an explicit baseline and one falsifiable prediction.
- [ ] Implement in the appropriate code category with shape/type contracts.
- [ ] Add correctness/negative tests and run a controlled experiment.
- [ ] Record exact command, software versions, dataset/model source and seed.
- [ ] Report observations, uncertainties, failure modes and next steps.

### 3. Group relative RL

**Task:** Implement synthetic GRPO advantage and small online rollout loop.

**Definition of done:** Check zero-variance groups and policy/reference version integrity.

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
