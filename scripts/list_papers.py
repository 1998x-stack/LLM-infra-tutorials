#!/usr/bin/env python3
"""Print offline catalog of core papers."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
stages = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))["stages"]
for stage in stages:
    print(f"\n{stage['id']} — {stage['title']}")
    path = ROOT / "stages" / stage["id"] / "papers/core/manifest.tsv"
    with path.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            print(f"  {row['arxiv_id']:>12}  {row['title']}")
