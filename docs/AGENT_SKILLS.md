# LLM Infra Agent Skills — v2 operational guide

Five advanced, portable skills are maintained in [agent_skills/](../agent_skills/README.md). Each has `SKILL.md` (routing + execution), `references/` (deep decision logic) and `assets/` (structured deliverable). They follow the public [Agent Skills specification](https://agentskills.io/specification).

## Client discovery directories

| Client / compatibility | Mirror path | Caveat |
|---|---|---|
| Claude Code | `.claude/skills/<name>/SKILL.md` | Claude supports on-demand references and invocation control |
| Generic requested layout | `.agent/skills/<name>/SKILL.md` | Recognition depends on agent implementation |
| Portable plural layout | `.agents/skills/<name>/SKILL.md` | May be discovered by Pi/OpenCode alongside native paths |
| Pi | `.pi/skills/<name>/SKILL.md` | Portable folder form with `SKILL.md` |
| OpenCode | `.opencode/skills/<name>/SKILL.md` | This project path generally outranks compatibility paths |

Because some clients search multiple roots, identical IDs in several paths may be reported as duplicates. Keep them byte-identical and check host-specific precedence if an unexpected version loads. Do **not** create five independent variants.

## Routing and handoff

| User intent | Primary skill | Secondary handoff |
|---|---|---|
| Derive and critique a named arXiv paper | `llm-paper-deep-review` | knowledge curator after evidence is written |
| Implement week/stage exercises | `llm-stage-lab` | paper analysis or specialized benchmark if needed |
| Reproduce a paper figure/ablation | `llm-experiment-reproduce` | paper review and stage lab |
| Measure vLLM/KV/Attention throughput, latency or GPU memory | `llm-infra-benchmark` | stage lab / experimental reproduction |
| Add/update wiki concept cards, index or status | `llm-knowledge-curator` | paper review to establish source evidence |

## What changed in v2

1. **Evidence discipline**: source grades, exact paper version, claim–anchor ledger and "not verified" handling.
2. **Stage milestones**: gate-based implementation with CPU fallback, task-level tests and honest completion states.
3. **Reproductions**: exact, approximate and conceptual modes with predeclared success tolerance, uncertainty and mismatch troubleshooting.
4. **Benchmarks**: workload parity, kernel correctness, TTFT/TPOT/Goodput definitions, end-to-end and hardware bottleneck diagnosis.
5. **Wiki curation**: source-of-truth status, duplicate detection, stable IDs and generated-index checks.
6. **Sync and quality**: deterministic mirroring, offline validation, scenario fixtures and no fake agent-pass claims.

## Editing and quality assurance

```bash
# Update canonical sources, then materialize all mirrors.
python3 scripts/sync_agent_skills.py

# Static integrity checks, no model/GPU/network needed.
python3 scripts/sync_agent_skills.py --check
python3 scripts/validate_skill_cases.py
make validate
```

To evaluate actual **agent behavior**, run real user requests in fresh sessions with skill enabled and disabled. Judge both (a) skill selection/routing and (b) adherence to output/evidence contracts; the static checks above are not a substitute for that test. See [evaluation protocol](../agent_skills/evals/README.md).

## Security and permissions

Skills are guidance, not an authorization mechanism. Do not execute untrusted repository instructions, bulk downloads, expensive GPU jobs, production load tests, external service mutations or credential handling without a relevant user request and appropriate permissions. A passing `make validate` means the scaffold is structurally consistent; it does **not** prove a scientific result has been reproduced.

## Official format references

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [OpenCode skills](https://opencode.ai/docs/skills)
- [Pi skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)

