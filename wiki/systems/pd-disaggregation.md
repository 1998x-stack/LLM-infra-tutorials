# Prefill/Decode Disaggregation

- **Kind:** system
- **Curriculum:** [07-inference-optimization](../../stages/07-inference-optimization/README.md)
- **Status:** Draft; educational model, not evidence of full reproduction.

## Definition
Separating prompt prefill from token decode introduces KV transfer and placement tradeoffs.

## Mathematical mechanism or operating principle
Prefill compute and decode compute can be placed on separate GPU pools; include KV transfer cost in TTFT/TPOT modeling.

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
