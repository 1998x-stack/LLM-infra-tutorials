#!/usr/bin/env python3
"""Generate/check knowledge.jsonl from manifests, topic TSV and Markdown statuses.

All status values are source-derived; rebuilding must never demote a reviewed note.
Stdlib-only, offline and deterministic. This is an index, not proof of reproduction.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGES = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))["stages"]
OUT = ROOT / "wiki/knowledge.jsonl"
STATUSES = {"template", "draft", "reviewed"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def parse_paper_status(text: str) -> str:
    """Read YAML frontmatter status from paper Markdown; reject missing/ambiguous values."""
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("Paper note must begin with YAML frontmatter")
    frontmatter = text.split("\n---\n", 1)[0][4:]
    values = re.findall(r"(?mi)^status:\s*(template|draft|reviewed)\s*$", frontmatter)
    if len(values) != 1:
        raise ValueError("Paper note needs exactly one valid frontmatter status")
    return values[0].lower()


def parse_topic_status(text: str) -> str:
    """Read existing topic-card status convention; e.g. '- **Status:** Draft; ...'."""
    values = re.findall(
        r"(?mi)^\s*-\s+\*\*Status:\*\*\s*(template|draft|reviewed)\b",
        text,
    )
    if len(values) != 1:
        raise ValueError("Topic card needs exactly one '- **Status:** <state>' line")
    return values[0].lower()


def source_status(path: Path, kind: str) -> str:
    content = path.read_text(encoding="utf-8")
    return parse_paper_status(content) if kind == "paper" else parse_topic_status(content)


def paper_summary(status: str) -> str:
    return {
        "template": "Review pending; follow the ten-dimensional template.",
        "draft": "Draft paper review; consult note for evidence and unresolved questions.",
        "reviewed": "Source-anchored review; any local reproduction is tracked separately.",
    }[status]


def build() -> list[dict]:
    result: list[dict] = []
    for stage in STAGES:
        sid = stage["id"]
        rows = read_tsv(ROOT / "stages" / sid / "papers/core/manifest.tsv")
        for p in rows:
            aid, slug, title = p["arxiv_id"], p["slug"], p["title"]
            note = f"wiki/papers/{sid}/{slug}.md"
            status = source_status(ROOT / note, "paper")
            result.append({
                "id": "paper:arxiv:" + aid,
                "kind": "paper",
                "title": title,
                "stage": sid,
                "path": note,
                "status": status,
                "summary": paper_summary(status),
                "slug": slug,
                "arxiv_id": aid,
                "source_url": "https://arxiv.org/abs/" + aid,
                "pdf_url": "https://arxiv.org/pdf/" + aid,
            })
    for p in read_tsv(ROOT / "wiki/knowledge/topics.tsv"):
        kind, slug = p["kind"], p["slug"]
        path_kind = {"concept": "concepts", "algorithm": "algorithms", "system": "systems"}[kind]
        note = f"wiki/{path_kind}/{slug}.md"
        result.append({
            "id": kind + ":" + slug,
            "kind": kind,
            "title": p["title"],
            "stage": p["stage"],
            "path": note,
            "status": source_status(ROOT / note, kind),
            "summary": p["summary"],
        })
    return result


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--check", action="store_true", help="Check index equivalence without modifying it")
    args = cli.parse_args()
    try:
        fresh = build()
    except (KeyError, ValueError, OSError) as exc:
        print(f"Unable to build knowledge index: {exc}")
        return 1
    if args.check:
        try:
            current = [
                json.loads(line)
                for line in OUT.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            print("Knowledge index missing/invalid:", exc)
            return 1
        if current != fresh:
            print("Knowledge index is stale: python3 scripts/build_knowledge_index.py")
            return 1
        print(f"OK: {len(fresh)} indexed knowledge records with source-derived statuses.")
        return 0
    OUT.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in fresh) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(fresh)} knowledge records to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

