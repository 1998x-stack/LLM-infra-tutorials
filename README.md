# LLM Infra Tutorials

> **Read the paper. Reproduce the algorithm. Measure the system.**  
> A 16-week, research-to-engineering curriculum for language models, reasoning, GPU kernels, and large-scale LLM infrastructure.

[简体中文](README.zh-CN.md) · [Curriculum](docs/CURRICULUM.md) · [Code taxonomy](docs/CODE_CATEGORY.md) · [Paper policy](docs/PAPER_POLICY.md) · [Contributing](CONTRIBUTING.md)

## What this repository is

**LLM Infra Tutorials** is a reproducible learning laboratory. Each stage connects **core research papers** to **executable implementations**, **controlled experiments**, and **measurable acceptance criteria**. The curriculum starts with the mathematics of language modeling and ends with inference scheduling, distributed training, and mixture-of-experts systems.

> **Repository status:** Educational scaffold. Stage tasks, paper manifests, downloaders and starter implementations are provided; advanced labs are marked `TODO` until implemented and validated. No benchmark results are claimed.

## The 16-week roadmap

| Stage | Weeks | Focus | Core papers | Deliverable |
|---|---:|---|---:|---|
| [01 · Foundations](stages/01-foundations/README.md) | 1 | Math, autograd, N-grams, optimization | 3 | Loss + language-modeling basics |
| [02 · Transformer Architecture](stages/02-transformer-architecture/README.md) | 2–3 | Decoder-only GPT, RoPE, GQA, KV Cache | 5 | Mini GPT |
| [03 · Pretraining & Scaling](stages/03-pretraining-scaling/README.md) | 4–5 | Data, NTP, scaling laws, profiling | 5 | Mini pretraining study |
| [04 · Post-training & Alignment](stages/04-post-training-alignment/README.md) | 6 | SFT, LoRA, QLoRA, DPO | 4 | Comparison of fine-tuning methods |
| [05 · Mechanistic Interpretability](stages/05-mechanistic-interpretability/README.md) | 7–8 | Grokking, probes, causal intervention, SAE | 5 | Mechanism reproduction |
| [06 · Reasoning & RL](stages/06-reasoning-rl/README.md) | 9–10 | CoT, search, test-time compute, GRPO | 6 | Accuracy–compute evaluation |
| [07 · Inference Optimization](stages/07-inference-optimization/README.md) | 11–13 | FlashAttention, PagedAttention, batching, serving | 8 | Serving benchmark suite |
| [08 · Distributed Frontiers](stages/08-distributed-frontiers/README.md) | 14–16 | ZeRO, TP/PP/DP, MoE, MLA | 6 | Distributed/MoE study |

**42 core papers** in total. Full checklists, reproducibility contracts, and optional readings live in each stage.

## Quick start

```bash
git clone https://github.com/1998x-stack/LLM-infra-tutorials.git
cd LLM-infra-tutorials

# Structural checks: Python 3.10+, no GPU required.
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v

# Inspect a stage's papers without downloading.
bash stages/07-inference-optimization/papers/core/download.sh --list

# Download only this stage's core PDFs (curl or wget required).
bash stages/07-inference-optimization/papers/core/download.sh

# Alternative: run from repository root.
bash scripts/download_papers.sh --stage 07-inference-optimization
bash scripts/download_papers.sh --all --dry-run
```

Optional ML dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[ml,dev]"
```

Install a CUDA-compatible PyTorch build following [official instructions](https://pytorch.org/get-started/locally/) when running GPU exercises.

## Stage layout

```text
stages/NN-topic/
├── README.md                     # goals, prerequisites, milestones, DoD
├── tasks/TASKS.md                # actionable checklist and acceptance tests
├── papers/
│   ├── core/
│   │   ├── manifest.tsv          # slug / arxiv ID / title
│   │   ├── download.sh           # one-command PDF downloader
│   │   └── pdfs/                 # downloaded PDFs (git-ignored)
│   └── optional/README.md
├── code/<category>/              # topic-specific implementations
├── experiments/                  # configurations and experiment protocol
├── tests/                        # expected checks for this stage
├── notes/                        # paper-reading notes
└── results/                      # measurements, tables, limitations
```

## Code categories

See [CODE_CATEGORY.md](docs/CODE_CATEGORY.md) for the repository-wide contracts. The stage's `code/` directory groups work by *technical responsibility*, rather than by paper author or library:

- **Algorithms:** mathematical reference implementations and minimal operators.
- **Models & training:** architecture, data, optimization, post-training.
- **Interpretability & reasoning:** probes, circuits, search, reward optimization.
- **Systems:** GPU kernels, memory management, scheduling, distributed execution.
- **Benchmarks:** validated performance and quality measurements, separated from implementation.

Prefer transparent baseline code before optimized kernels. Every claimed improvement should include the baseline, hardware/software environment, measurement method, and a correctness test.

## Paper management

Each stage has `papers/core/manifest.tsv` and its own `download.sh`. Downloads are saved to `papers/core/pdfs/` and are **not committed**. The downloader supports:

```bash
bash scripts/download_papers.sh --stage 01           # stage number
bash scripts/download_papers.sh --stage 05-mechanistic-interpretability --list
bash scripts/download_papers.sh --all --dry-run
bash scripts/download_papers.sh --all
bash scripts/download_papers.sh --stage 07 --force
```

Only public arXiv PDF endpoints are used by the core manifests. The script checks the PDF signature, retries transient failures, and preserves successful files. Respect authors' licenses and arXiv rate limits. See [PAPER_POLICY.md](docs/PAPER_POLICY.md).

## Definition of done

A stage is complete only when you have (1) read and annotated the core papers, (2) implemented or reproduced the listed algorithms, (3) run correctness checks and a controlled experiment, (4) recorded hardware, seeds, datasets, metrics and limitations, and (5) updated the stage's task checklist honestly.

## Development and contribution

- Follow [Reproducibility](docs/REPRODUCIBILITY.md) and [Contributing](CONTRIBUTING.md).
- Run `make validate` before submitting changes.
- Do not check in model weights, datasets, downloaded PDFs, secrets, or large profiler traces.
- New work should live under the matching stage and code category. Propose cross-stage infrastructure in `scripts/` or `docs/`.
- Respect the original licenses of papers, datasets, models, and upstream source code. This repository does not relicense them.

## Navigation

[Curriculum](docs/CURRICULUM.md) · [Research workflow](docs/REPRODUCIBILITY.md) · [Paper index](docs/PAPER_INDEX.md) · [Code categories](docs/CODE_CATEGORY.md)

---

**Goal:** graduate from reading LLM papers to reproducing research results and explaining performance bottlenecks with measurements. Contributions are welcome; unimplemented work must remain explicitly labeled as a scaffold.
