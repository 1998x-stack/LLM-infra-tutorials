# Low-Rank Adapter Update

- **Kind:** algorithm
- **Curriculum:** [04-post-training-alignment](../../stages/04-post-training-alignment/README.md)
- **Status:** Draft; educational model, not evidence of full reproduction.

## Definition
Train low-rank factors rather than full frozen weights.

## Mathematical mechanism or operating principle
Freeze W; learn low-rank A,B with W'=W+BA (rank<=r). Test merge numerically at a stated dtype.

## Algorithm sketch / invariants
1. Identify inputs, outputs, state and correctness criteria.
2. Implement a transparent reference baseline.
3. Change one factor at a time and record controlled evidence.

## Complexity and system implications
TODO: Quantify FLOPs, memory bytes, communication, latency, numerical stability and scaling conditions where meaningful.

## Evidence and limitations
This card is a research scaffold. Link paper sections and actual measurements before asserting speedups or causal explanations.

## Reproduction and tests
TODO: Link stage code, experiment configs, correctness checks and result report.

## Related knowledge
Browse neighboring [core papers](../papers/README.md) and add specific cross-links supported by the underlying method.

## Falsifiable extension
TODO: Propose one controlled ablation with a baseline, metric, resource budget and failure criterion.
