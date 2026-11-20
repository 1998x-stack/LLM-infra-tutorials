# Evidence-first paper analysis protocol

Read this reference when a paper contains nontrivial equations, empirical performance comparisons, causal interpretation, or a requested code-level trace. The ten dimensions align with `wiki/templates/PAPER_REVIEW_TEMPLATE.md`.

## A. Source and provenance hierarchy

| Source | Can substantiate | Cannot automatically substantiate |
|---|---|---|
| Exact primary paper/version | Author methods, stated equations, reported results | Your local reproduction or current upstream code state |
| Paper appendix/supplement | Experimental specifics and proofs | Unreported real-world generalization |
| Verified author repository and pinned commit | What the inspected implementation does | That experiments in the paper used this exact version |
| Local code + logs with environment | Reproduced output in stated conditions | Universal speedups or correctness outside tests |
| Secondary article/discussion | Useful context or critique | Exact paper figures/equations without cross-check |
| Your deduction/model | Testable interpretation and cost estimate | Experimental fact without measurement |

Record source URL, exact version, section/page, table/figure identifier, code commit and retrieval date when applicable. If a supplied PDF is inaccessible, explicitly say so.

## B. Ten-dimension analysis rubric

| Dimension | Technical questions | Minimum evidence |
|---|---|---|
| Problem | Task objective? Prior limitation? Operational constraint? | Author's problem statement and strongest baseline |
| Observation | What measured/observed effect motivates work? | Figure/table/data setting |
| Hypothesis | Which mechanism or causal explanation? | Stated proposal + alternative explanations |
| Algorithm | Objective, update rule, shapes, states, pseudocode? | Equation number and worked trace |
| Experiment | Dataset splits, model, precision, seeds, hardware, ablations? | Method/appendix details; missing data noted |
| Evidence | Which outcomes match claimed contribution? | Reported numerical values with source location |
| Limitations | Failure cases, non-stationarity, conditions, confounders? | Explicit and inferred caveats labeled separately |
| Implementation | Repo URL, revision, file/function, kernels/structures? | Verified code path or `not verified` |
| Systems | Complexity, peak memory, bandwidth, communication, latency? | Units + shape/hardware assumptions |
| Extension | Smallest falsifiable next experiment? | Baseline, independent variable, budget and outcome rule |

## C. Equation verification

1. Write the original definition and all variables with units/dimensions.
2. Identify assumptions: independence, precision, fixed sequence length, architecture and sampling distribution.
3. Track a synthetic shape through each stage; flag broadcasting/axis ambiguities.
4. Derive each step, noting algebraic equivalence vs approximation vs empirical fit.
5. Check edge conditions (zeros, epsilon, masks, sequence boundaries and conditioning).
6. Give computational complexity in the appropriate variables—not `O(1)` merely because network depth is fixed.

If a derivation cannot be established from inspected source, label it `independent explanation`, not "paper proves".

## D. Evidence ledger example

| Claim ID | Claim | Origin | Supporting anchor | Evidence grade | Uncertainty |
|---|---|---|---|---|---|
| C-01 | Variant reduces kernel HBM traffic for given shapes | Author | ``3, Fig. 2 | Reported analytical/empirical | GPU-dependent |
| C-02 | Local optimized kernel is faster | Local | run ID, profiler trace | Not run yet | Must not claim speedup |

Evidence grade vocabulary: `theorem/derivation`, `paper experiment`, `local experiment`, `interpretation`, `unverified`.

## E. Conflict and contradiction handling

- Compare methods and data/metrics before comparing absolute numbers.
- Check dataset versions, token counts, dtypes, hardware and baseline revisions.
- Do not "resolve" contradictions by rewriting author claims; preserve both and state what additional experiment separates them.
- Distinguish statistical significance, practical effect size, correctness and reproducibility.

## F. Output decision

- `verified review`: source inspected, key claims anchored, ten dimensions substantively complete.
- `partial review`: important sections, appendix or code unavailable; include precisely what was not read.
- `reading notes`: idea summary only; never promote knowledge status to `reviewed` solely on this basis.

