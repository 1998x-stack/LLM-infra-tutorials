# Core paper reviews

The 42 core papers each have a ten-dimension review file under their stage folder: `wiki/papers/<stage>/<slug>.md`.

**These are structured review templates, not fabricated analyses.** Complete citations, calculations, ablation descriptions and source-code checks before changing `status` to reviewed.

## Paper review quality checklist
- **Problem:** What prior method, assumption, task, or resource constraint is inadequate? Specify the baseline, its failure mode and where the paper establishes it.
- **Observation:** What qualitative/quantitative phenomenon motivated the method? State the experimental setting and separate observation from inference.
- **Hypothesis:** What precise causal or engineering mechanism do the authors propose? What result would falsify it?
- **Algorithm:** Give inputs, outputs, assumptions, pseudocode, objective, tensor shapes, numerical stability, complexity and invariant checks.
- **Experiment:** Specify datasets, models, GPUs, seeds, baselines, controls, ablations, evaluation metrics and exact figure/table references.
- **Evidence:** Record measured values with table/figure/page, uncertainty, whether original paper or reproduced locally, and strength of support.
- **Limitations:** List external validity, scaling assumptions, failure cases, untested ablations and differences from other evidence.
- **Implementation:** Provide official upstream link/commit if verified, relevant functions, tensor layouts, data structures, CLI and reproduction tests.
- **Systems:** Quantify compute/FLOPs, memory, HBM traffic, communication, latency, throughput, GPU occupancy and serving implications where applicable.
- **Extension:** Propose one falsifiable improvement or ablation, control variables, metrics, expected tradeoffs and stopping rule.

See [full review template](../templates/PAPER_REVIEW_TEMPLATE.md).
