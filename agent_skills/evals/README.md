# Agent Skill behavioral evaluation protocol

The `cases.jsonl` corpus contains realistic positive, negative and boundary prompts. It is a **routing and behavioral rubric**, not a claim that real agent runs have already passed.

## Offline checks

```bash
python3 scripts/validate_skill_cases.py
python3 scripts/sync_agent_skills.py --check
```

The validator checks JSON structure, candidate IDs, prompt uniqueness and expected assertions. It does **not** call an LLM.

## Real evaluation with your agent

For each case:
1. Start a **fresh session** with the five skills installed and available. Submit only the case's `prompt`.
2. Record whether the agent loaded `expected_skill` (or none); for multi-step requests record the primary skill and secondary handoffs.
3. Audit actual output against `must_include` and `must_avoid` criteria. Check source evidence and command logs.
4. Repeat with the relevant skill disabled in a separate fresh session. Compare outcomes, not just trigger rates.
5. Score: **routing accuracy**, **output compliance**, **grounding correctness**, **safe failure handling**, **unnecessary tool/cost actions**.
6. Log environment, agent version, model, prompts, tool availability and repeat count. Report failures and false positives.

Suggested acceptance: ≥90% exact primary-skill routing on a representative prompt set, **zero invented measurements/citations**, and no unrequested expensive external actions. This is a **proposed target**, not measured quality.

## Example record

```json
{"id":"paper-flashattention","prompt":"Derive FlashAttention online-softmax and inspect its experimental evidence","expected_skill":"llm-paper-deep-review","must_include":["exact primary paper evidence","equation derivation"],"must_avoid":["fabricated local benchmark"]}
```

The fixtures are designed to detect **skill overlap** as well as missing behavior. They should be extended as the corpus matures.

