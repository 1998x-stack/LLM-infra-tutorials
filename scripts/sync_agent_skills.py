#!/usr/bin/env python3
"""Keep five cross-agent skill mirrors in sync with agent_skills/*.

Stdlib-only; no network, no dependency installs, no executing skill code.
Run with --check in CI, without arguments to write mirrors.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "agent_skills"
DESTINATIONS = (".claude", ".agent", ".agents", ".pi", ".opencode")
NAMES = (
    "llm-paper-deep-review",
    "llm-stage-lab",
    "llm-experiment-reproduce",
    "llm-infra-benchmark",
    "llm-knowledge-curator",
)
ALLOWED_FILES = {"SKILL.md"}
ALLOWED_FOLDERS = {"references", "assets"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def canonical_files(name: str) -> dict[Path, bytes]:
    base = SOURCE / name
    if not (base / "SKILL.md").is_file():
        raise ValueError(f"Missing canonical SKILL.md for {name}")
    out: dict[Path, bytes] = {}
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(base)
        if rel.as_posix() != "SKILL.md" and (rel.parts[0] not in ALLOWED_FOLDERS):
            raise ValueError(f"Unexpected skill file {path.relative_to(ROOT)}")
        if path.suffix not in (".md", ".json", ".yaml", ".yml", ".txt"):
            raise ValueError(f"Unreviewed asset extension {path.relative_to(ROOT)}")
        out[rel] = path.read_bytes()
    return out


def inspect_frontmatter(name: str, content: bytes) -> list[str]:
    text = content.decode("utf-8")
    errors: list[str] = []
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return [f"{name}: missing YAML frontmatter"]
    block = text.split("\n---\n", 1)[0][4:]
    match = re.search(r"(?m)^name:\s*(\S+)\s*$", block)
    if not match or match.group(1) != name or not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{name}: invalid or mismatched name")
    desc = re.search(r"(?m)^description:\s*(.+)$", block)
    if not desc:
        errors.append(f"{name}: description missing")
    else:
        value = desc.group(1).strip().strip('"').strip("'")
        if len(value) < 50 or len(value) > 1024:
            errors.append(f"{name}: description length must be 50..1024 characters")
        if "Use " not in value and "use " not in value:
            errors.append(f"{name}: description needs use-case trigger wording")
    # Check structural richness without assuming specific English section names.
    if len(re.findall(r"(?m)^## .+$", text)) < 3:
        errors.append(f"{name}: expected at least three substantive Markdown sections")
    return errors


def verify_local_references(name: str, source: dict[Path, bytes]) -> list[str]:
    text = source[Path("SKILL.md")].decode("utf-8")
    issues: list[str] = []
    for relative in re.findall(r"\]\((references/[^)#?]+|assets/[^)#?]+)\)", text):
        if Path(relative) not in source:
            issues.append(f"{name}: missing linked supporting file {relative}")
    for folder in ALLOWED_FOLDERS:
        if not any(p.parts[0] == folder for p in source):
            issues.append(f"{name}: missing {folder}/ supporting material")
    return issues


def sync(check: bool) -> list[str]:
    problems: list[str] = []
    for name in NAMES:
        if not (SOURCE / name).is_dir():
            problems.append(f"Missing canonical skill {name}")
            continue
        source = canonical_files(name)
        problems += inspect_frontmatter(name, source[Path("SKILL.md")])
        problems += verify_local_references(name, source)
        for client in DESTINATIONS:
            dest = ROOT / client / "skills" / name
            for relative, expected in source.items():
                target = dest / relative
                if check:
                    if not target.is_file():
                        problems.append(f"Missing mirror {target.relative_to(ROOT)}")
                    elif target.read_bytes() != expected:
                        problems.append(f"Outdated mirror {target.relative_to(ROOT)}")
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if not target.is_file() or target.read_bytes() != expected:
                        target.write_bytes(expected)
                        print(f"SYNC {target.relative_to(ROOT)}")
            if dest.exists():
                for existing in dest.rglob("*"):
                    if existing.is_file() and existing.relative_to(dest) not in source:
                        problems.append(f"Unexpected mirror file (manual review needed): {existing.relative_to(ROOT)}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check all mirrors, without editing files")
    args = parser.parse_args()
    failures = sync(args.check)
    for problem in failures:
        print("ERROR:", problem, file=sys.stderr)
    if failures:
        return 1
    print(
        f"OK: {len(NAMES)} canonical skills × {len(DESTINATIONS)} mirrored clients; "
        f"mode={'check' if args.check else 'sync'}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

