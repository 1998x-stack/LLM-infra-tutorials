#!/usr/bin/env python3
"""Validate skill routing eval fixtures; this does NOT run a model."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "agent_skills/evals/cases.jsonl"
SKILLS = {
    "llm-paper-deep-review", "llm-stage-lab", "llm-experiment-reproduce",
    "llm-infra-benchmark", "llm-knowledge-curator",
}


def validate() -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    prompts: set[str] = set()
    counts: Counter[str | None] = Counter()
    for i, line in enumerate(PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            errors.append(f"Empty line at {i}")
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"Line {i}: invalid JSON: {exc}")
            continue
        needed = {"id", "prompt", "expected_skill", "must_include", "must_avoid"}
        if set(row) != needed:
            errors.append(f"Line {i}: wrong fields")
            continue
        if row["id"] in ids or row["prompt"] in prompts:
            errors.append(f"Line {i}: repeated ID or prompt")
        ids.add(row["id"])
        prompts.add(row["prompt"])
        skill = row["expected_skill"]
        if skill is not None and skill not in SKILLS:
            errors.append(f"Line {i}: invalid skill {skill!r}")
        counts[skill] += 1
        if not isinstance(row["prompt"], str) or len(row["prompt"]) < (10 if skill is not None else 2):
            errors.append(f"Line {i}: prompt too short")
        for field in ("must_include", "must_avoid"):
            if not isinstance(row[field], list) or any(not isinstance(s, str) for s in row[field]):
                errors.append(f"Line {i}: {field} must be list[str]")
        if skill is not None and (not row["must_include"] or not row["must_avoid"]):
            errors.append(f"Line {i}: positive case needs both assertions")
    for skill in SKILLS:
        if counts[skill] < 4:
            errors.append(f"Too few cases for {skill}: {counts[skill]}")
    if counts[None] < 3:
        errors.append("Need at least three negative no-skill prompts")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print("ERROR:", problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("OK: skill eval fixture structure validated; agent behavior NOT executed.")

