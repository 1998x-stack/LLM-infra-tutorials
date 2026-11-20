# LLM Infra Tutorials — 16 周论文到工程的研究路线

> **Read the paper · Reproduce the algorithm · Measure the system.**

这是一个面向 LLM 算法与基础设施的可复现学习仓库。覆盖八阶段、42 篇核心论文：数学与语言模型、Transformer、预训练、后训练、可解释性、推理强化学习、推理优化和分布式系统。

**状态：** 已建设文档体系、任务与实验模板、PDF 下载工具、机器可读知识库与多 Agent Skills。阶段代码为教学脚手架，尚未声称论文结果已复现。

| 阶段 | 周次 | 目标 |
|---|---|---|
| [01 Foundations](stages/01-foundations/README.md) | 1 | 概率、梯度、N-gram、语言模型 |
| [02 Transformer](stages/02-transformer-architecture/README.md) | 2–3 | Decoder GPT、RoPE、GQA |
| [03 Pretraining](stages/03-pretraining-scaling/README.md) | 4–5 | Scaling Law、数据、训练实验 |
| [04 Post-training](stages/04-post-training-alignment/README.md) | 6 | SFT、LoRA、DPO |
| [05 Interpretability](stages/05-mechanistic-interpretability/README.md) | 7–8 | Grokking、World Model、SAE |
| [06 Reasoning RL](stages/06-reasoning-rl/README.md) | 9–10 | CoT、搜索、GRPO |
| [07 Serving](stages/07-inference-optimization/README.md) | 11–13 | KV Cache、FlashAttention、vLLM |
| [08 Distributed](stages/08-distributed-frontiers/README.md) | 14–16 | ZeRO、TP/PP/DP、MoE |

## 快速开始

```bash
git clone https://github.com/1998x-stack/LLM-infra-tutorials.git
cd LLM-infra-tutorials
make validate
bash stages/07-inference-optimization/papers/core/download.sh --list
bash stages/07-inference-optimization/papers/core/download.sh
bash scripts/download_papers.sh --all --dry-run
```

所有核心论文 manifest 在各阶段的 `papers/core/manifest.tsv`；下载 PDF 进入 `papers/core/pdfs/`，不会提交到 Git。

## 仓库结构

- `stages/*/tasks/`：可执行任务、交付物和验收标准。
- `stages/*/papers/core/`：论文清单与 PDF 下载脚本。
- `stages/*/code/`：按职责组织的代码分类。
- `stages/*/experiments/`：实验协议与配置。
- `stages/*/results/`：评估报告与局限。
- `wiki/`：论文精读、知识卡片、知识关系与 JSONL 索引。
- `.claude/skills`、`.agent/skills`、`.pi/skills`、`.opencode/skills`：复用型研究工作流。

每篇论文使用 10 维精读法：Problem、Observation、Hypothesis、Algorithm、Experiment、Evidence、Limitations、Implementation、Systems、Extension。

[English README](README.md) · [学习路线](docs/CURRICULUM.md) · [代码规范](docs/CODE_CATEGORY.md) · [Wiki](wiki/README.md) · [Skills](docs/AGENT_SKILLS.md)
