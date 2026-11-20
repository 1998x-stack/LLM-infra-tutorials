# GRPO Rollout and Advantage

- **Kind:** algorithm
- **Curriculum:** [06-reasoning-rl](../../stages/06-reasoning-rl/README.md)
- **Status:** Draft; educational model, not evidence of full reproduction.

## Definition
Group sampling, relative reward normalization and clipped objective.

## Mathematical mechanism or operating principle
For each prompt sample G trajectories, compute rewards r_i, then normalized group advantage A_i=(r_i-mean(r))/(std(r)+eps). Handle groups with zero reward variance.

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
