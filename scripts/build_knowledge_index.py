#!/usr/bin/env python3
"""Generate/check wiki/knowledge.jsonl from stage manifests and knowledge/topics.tsv.

The index is a discovery artifact, NOT proof that paper templates have been reviewed.
Stdlib-only, no network, no GPU. Format is intentionally deterministic.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGES = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))["stages"]
OUT = ROOT / "wiki/knowledge.jsonl"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def build() -> list[dict]:
    result: list[dict] = []
    for stage in STAGES:
        sid = stage["id"]
        rows = read_tsv(ROOT / "stages" / sid / "papers/core/manifest.tsv")
        for p in rows:
            aid, slug, title = p["arxiv_id"], p["slug"], p["title"]
            result.append({
                "id": "paper:arxiv:" + aid,
                "kind": "paper",
                "title": title,
                "stage": sid,
                "path": f"wiki/papers/{sid}/{slug}.md",
                "status": "template",
                "summary": "Review pending; follow the ten-dimensional template.",
                "slug": slug,
                "arxiv_id": aid,
                "source_url": "https://arxiv.org/abs/" + aid,
                "pdf_url": "https://arxiv.org/pdf/" + aid,
            })
    for p in read_tsv(ROOT / "wiki/knowledge/topics.tsv"):
        kind, slug = p["kind"], p["slug"]
        path_kind = {"concept": "concepts", "algorithm": "algorithms", "system": "systems"}[kind]
        result.append({
            "id": kind + ":" + slug,
            "kind": kind,
            "title": p["title"],
            "stage": p["stage"],
            "path": f"wiki/{path_kind}/{slug}.md",
            "status": "draft",
            "summary": p["summary"],
        })
    return result


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--check", action="store_true", help="Check index equivalence without modifying it")
    args = cli.parse_args()
    fresh = build()
    if args.check:
        try:
            current = [json.loads(line) for line in OUT.read_text(encoding="utf-8").splitlines() if line.strip()]
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            print("Knowledge index missing/invalid:", exc)
            return 1
        if current != fresh:
            print("Knowledge index is stale: python3 scripts/build_knowledge_index.py")
            return 1
        print(f"OK: {len(fresh)} indexed knowledge records.")
        return 0
    OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in fresh) + "\n", encoding="utf-8")
    print(f"Wrote {len(fresh)} knowledge records to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
