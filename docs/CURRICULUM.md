# 16-week curriculum

Read [README](../README.md) for the overview. Each stage defines acceptance criteria and a core paper manifest.

| Stage | Weeks | Core papers | Deliverable |
|---|---:|---:|---|
| [01 Foundations](../stages/01-foundations/README.md) | 1 | 3 | Reference loss and N-gram |
| [02 Transformer](../stages/02-transformer-architecture/README.md) | 2–3 | 5 | Mini decoder GPT |
| [03 Pretraining](../stages/03-pretraining-scaling/README.md) | 4–5 | 5 | Scaling and loss study |
| [04 Post-training](../stages/04-post-training-alignment/README.md) | 6 | 4 | SFT/PEFT/DPO comparison |
| [05 Interpretability](../stages/05-mechanistic-interpretability/README.md) | 7–8 | 5 | Mechanism/probe reproduction |
| [06 Reasoning RL](../stages/06-reasoning-rl/README.md) | 9–10 | 6 | Quality–compute frontier |
| [07 Inference](../stages/07-inference-optimization/README.md) | 11–13 | 8 | Serving benchmark |
| [08 Distributed](../stages/08-distributed-frontiers/README.md) | 14–16 | 6 | Parallel/MoE analysis |

Each stage requires three layers of evidence:
- **Correctness:** numerical and behavioral tests against a known reference.
- **Reproducibility:** pinned settings, deterministic seeds when possible, and commands.
- **Performance or quality:** baseline, measurement methodology, limitations.

**Knowledge loop:** read → ten-dimensional paper note → linked knowledge cards → implement → evaluate → update the knowledge index.

Follow [Research Protocol](REPRODUCIBILITY.md).
