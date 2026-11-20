# Agent Skills: installation, discovery and research contracts

Five portable [Agent Skills](https://agentskills.io) are mirrored to meet repository-specific workflows and tool discovery conventions.

| Platform | Project skill directory | Note |
|---|---|---|
| Claude Code | `.claude/skills/<skill>/SKILL.md` | Referenced by root `CLAUDE.md` |
| Generic requested layout | `.agent/skills/<skill>/SKILL.md` | Explicit repository convention; discovery varies by agent |
| Agent Skills compatible / plural layout | `.agents/skills/<skill>/SKILL.md` | Extra compatibility path |
| Pi coding agent | `.pi/skills/<skill>/SKILL.md` | Project-local skill format |
| OpenCode | `.opencode/skills/<skill>/SKILL.md` | Project-local skill format |

Each skill has the required portable YAML frontmatter (`name`, `description`) and a detailed workflow. Some clients may discover multiple compatible directories; maintain identical definitions and avoid loading duplicates.

## Available skills
- **llm-paper-deep-review** — Use when asked to read, explain, critique or deeply review an LLM or LLM infrastructure paper, including mathematics, algorithms, experimental evidence and source-code analysis.
- **llm-stage-lab** — Use when planning, implementing or reviewing one of the eight LLM curriculum stages and its task checklists, paper readings, starter code, tests and experimental deliverables.
- **llm-experiment-reproduce** — Use when reproducing numerical claims from an LLM research paper, implementing benchmark baselines, comparing results or diagnosing failed reproduction experiments.
- **llm-infra-benchmark** — Use when benchmarking GPU attention, KV Cache, vLLM/SGLang inference serving, speculative decoding, prefill/decode scheduling, distributed MoE or memory/throughput optimization.
- **llm-knowledge-curator** — Use when adding or updating LLM research wiki topics, ten-dimensional paper notes, cross-links, knowledge.jsonl entries, glossary, or knowledge validation and taxonomy.

## Example tasks
- “Deep-read FlashAttention and fill all ten evidence dimensions” → `llm-paper-deep-review`.
- “Implement the Stage 02 cached decoder exercise” → `llm-stage-lab`.
- “Reproduce Grokking test accuracy under multiple seeds” → `llm-experiment-reproduce`.
- “Measure vLLM TTFT/TPOT with and without prefix caching” → `llm-infra-benchmark`.
- “Index a newly added arXiv paper and update knowledge.jsonl” → `llm-knowledge-curator`.

## Quality and security
- Skills only describe a workflow. They do **not** grant permission to download software, alter external services or run GPU jobs.
- Consult `AGENTS.md` and stage tasks; keep generated artifacts under the tracked folder contract.
- The source of truth for paper metadata remains TSV manifests; the JSONL index is generated.
- The repository's structural validator checks frontmatter, naming and cross-directory parity.

External docs: [Claude skills](https://code.claude.com/docs/en/skills) · [Pi skills](https://docs.pi.dev/latest/skills) · [OpenCode skills](https://opencode.ai/docs/skills) · [Agent Skills specification](https://agentskills.io).
