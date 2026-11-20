#!/usr/bin/env python3
"""Strict offline repository integrity checks (Python stdlib only)."""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARXIV = re.compile(r"^[0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
DIMENSIONS = ("Problem", "Observation", "Hypothesis", "Algorithm", "Experiment",
              "Evidence", "Limitations", "Implementation", "Systems", "Extension")
KINDS = {"paper", "concept", "algorithm", "system"}
PLATFORMS = (".claude", ".agent", ".agents", ".pi", ".opencode")
SKILLS = ("llm-paper-deep-review", "llm-stage-lab", "llm-experiment-reproduce",
          "llm-infra-benchmark", "llm-knowledge-curator")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def validate() -> list[str]:
    errors: list[str] = []
    curriculum_file = ROOT / "curriculum.json"
    if not curriculum_file.is_file():
        return ["Missing curriculum.json"]
    stages = json.loads(curriculum_file.read_text(encoding="utf-8"))["stages"]
    if len(stages) != 8:
        errors.append(f"Expected 8 stages, found {len(stages)}")

    total = 0
    known_paper_ids: set[str] = set()
    known_note_paths: set[str] = set()
    stage_ids = {stage["id"] for stage in stages}
    for stage in stages:
        sid = stage["id"]
        base = ROOT / "stages" / sid
        expected = (
            "README.md", "tasks/TASKS.md",
            "papers/core/README.md", "papers/core/manifest.tsv",
            "papers/core/download.sh", "papers/core/pdfs/.gitkeep",
            "papers/optional/README.md", "experiments/README.md",
            "experiments/configs/example.yaml", "tests/README.md",
            "notes/README.md", "results/README.md",
        )
        for name in expected:
            if not (base / name).is_file():
                errors.append(f"{sid}: missing {name}")
        for category in stage["categories"]:
            if not SLUG.fullmatch(category):
                errors.append(f"{sid}: bad category {category}")
            for name in ("README.md", "exercise.py"):
                if not (base / "code" / category / name).is_file():
                    errors.append(f"{sid}: missing code/{category}/{name}")

        manifest = base / "papers/core/manifest.tsv"
        if not manifest.is_file():
            continue
        rows = read_tsv(manifest)
        with manifest.open(encoding="utf-8", newline="") as fh:
            head = fh.readline().rstrip("\r\n")
        if head != "slug\tarxiv_id\ttitle":
            errors.append(f"{sid}: invalid manifest header")
        if len(rows) != stage["coreCount"]:
            errors.append(f"{sid}: expected {stage['coreCount']} papers, found {len(rows)}")
        seen_slugs: set[str] = set()
        total += len(rows)
        for p in rows:
            slug, aid, title = ((p.get(k) or "").strip() for k in ("slug", "arxiv_id", "title"))
            if not SLUG.fullmatch(slug) or slug in seen_slugs:
                errors.append(f"{sid}: invalid or duplicate paper slug {slug!r}")
            seen_slugs.add(slug)
            if not ARXIV.fullmatch(aid) or aid in known_paper_ids:
                errors.append(f"{sid}: invalid or duplicate arXiv ID {aid!r}")
            known_paper_ids.add(aid)
            if not title:
                errors.append(f"{sid}: blank title for {aid}")
            rel = f"wiki/papers/{sid}/{slug}.md"
            known_note_paths.add(rel)
            file = ROOT / rel
            if not file.is_file():
                errors.append(f"{sid}: missing paper review {rel}")
                continue
            body = file.read_text(encoding="utf-8")
            if f"paper:arxiv:{aid}" not in body:
                errors.append(f"{rel}: wrong paper identifier")
            if f"https://arxiv.org/abs/{aid}" not in body:
                errors.append(f"{rel}: missing canonical link")
            for i, label in enumerate(DIMENSIONS, 1):
                if f"## {i}. {label}" not in body:
                    errors.append(f"{rel}: missing review dimension {label}")

    if total != 42:
        errors.append(f"Expected 42 core papers, found {total}")

    index = ROOT / "wiki/knowledge.jsonl"
    if not index.is_file():
        errors.append("Missing wiki/knowledge.jsonl")
    else:
        rows = []
        for n, line in enumerate(index.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                errors.append(f"knowledge.jsonl:{n}: blank line")
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"knowledge.jsonl:{n}: invalid JSON: {exc}")
                continue
            rows.append(row)
        if len(rows) != 72:
            errors.append(f"Expected 72 knowledge records, found {len(rows)}")
        ids: set[str] = set()
        index_papers: set[str] = set()
        for row in rows:
            rid = row.get("id")
            if not isinstance(rid, str) or rid in ids:
                errors.append(f"Duplicate or missing record ID: {rid!r}")
            ids.add(rid)
            kind, stage, path = row.get("kind"), row.get("stage"), row.get("path")
            if kind not in KINDS or stage not in stage_ids:
                errors.append(f"Invalid kind/stage: {rid!r}")
            if not isinstance(path, str) or not path.startswith("wiki/") or ".." in Path(path).parts:
                errors.append(f"Invalid path: {rid!r} -> {path!r}")
            elif not (ROOT / path).is_file():
                errors.append(f"Missing knowledge card: {path}")
            if row.get("status") not in ("template", "draft", "reviewed"):
                errors.append(f"Invalid record status: {rid!r}")
            if kind == "paper":
                aid = row.get("arxiv_id", "")
                if aid not in known_paper_ids or row.get("source_url") != f"https://arxiv.org/abs/{aid}":
                    errors.append(f"Paper index/manifest mismatch: {rid!r}")
                index_papers.add(aid)
                if path not in known_note_paths:
                    errors.append(f"Paper path mismatch: {rid!r}")
        if index_papers != known_paper_ids:
            errors.append("Knowledge paper index does not match core manifests")

    spec = importlib.util.spec_from_file_location("knowledge_builder", ROOT / "scripts/build_knowledge_index.py")
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if index.is_file():
            try:
                current = [json.loads(s) for s in index.read_text(encoding="utf-8").splitlines() if s.strip()]
                if current != module.build():
                    errors.append("Knowledge index is stale; run scripts/build_knowledge_index.py")
            except (ValueError, KeyError, OSError) as exc:
                errors.append(f"Unable to compare generated knowledge index: {exc}")

    for skill in SKILLS:
        canonical = None
        for platform in PLATFORMS:
            path = ROOT / platform / "skills" / skill / "SKILL.md"
            if not path.is_file():
                errors.append(f"Missing skill: {path.relative_to(ROOT)}")
                continue
            content = path.read_text(encoding="utf-8")
            if not content.startswith("---\n") or "\n---\n" not in content[4:]:
                errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            if f"name: {skill}\n" not in content:
                errors.append(f"{path.relative_to(ROOT)}: skill name mismatch")
            if not re.search(r'^description:\s*".{20,}"\s*$', content, flags=re.M):
                errors.append(f"{path.relative_to(ROOT)}: missing meaningful description")
            if canonical is None:
                canonical = content
            elif content != canonical:
                errors.append(f"Skill mirrors differ: {skill} / {platform}")

    for name in ("README.md", "README.zh-CN.md", "AGENTS.md", "CLAUDE.md",
                 "docs/CODE_CATEGORY.md", "docs/PAPER_POLICY.md",
                 "docs/REPRODUCIBILITY.md", "docs/AGENT_SKILLS.md",
                 "wiki/SCHEMA.md", "wiki/templates/PAPER_REVIEW_TEMPLATE.md",
                 "scripts/download_papers.sh", "scripts/build_knowledge_index.py"):
        if not (ROOT / name).is_file():
            errors.append(f"Missing top-level file: {name}")

    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        for problem in errors:
            print("ERROR:", problem, file=sys.stderr)
        raise SystemExit(1)
    print("OK: 8 stages, 42 core papers, 72 knowledge records, 25 mirrored skills, task/code scaffolds.")
