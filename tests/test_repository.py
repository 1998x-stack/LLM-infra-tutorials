"""Offline smoke and structural tests (Python standard library only)."""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class RepoTests(unittest.TestCase):
    def test_structure_and_wiki(self):
        spec = importlib.util.spec_from_file_location("validate_repo", ROOT / "scripts/validate_repo.py")
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual([], module.validate())

    def test_index_is_current(self):
        subprocess.run(
            ["python3", str(ROOT / "scripts/build_knowledge_index.py"), "--check"],
            check=True, capture_output=True, text=True,
        )
        recs = [json.loads(s) for s in (ROOT / "wiki/knowledge.jsonl").read_text().splitlines()]
        self.assertEqual(len(recs), 72)
        self.assertEqual(sum(r["kind"] == "paper" for r in recs), 42)

    def test_all_papers_dry_run(self):
        result = subprocess.run(
            ["bash", str(ROOT / "scripts/download_papers.sh"), "--all", "--dry-run"],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout.count("[DRY RUN]"), 42)

    def test_stage_wrapper_lists_papers(self):
        result = subprocess.run(
            ["bash", str(ROOT / "stages/07-inference-optimization/papers/core/download.sh"), "--list"],
            capture_output=True, text=True, check=True,
        )
        self.assertIn("FlashAttention", result.stdout)
        self.assertIn("arxiv.org/pdf/2205.14135", result.stdout)

    def test_unknown_stage_fails(self):
        result = subprocess.run(
            ["bash", str(ROOT / "scripts/download_papers.sh"), "--stage", "99", "--list"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)

    def test_mocked_pdf_download_cache_and_invalid_pdf(self):
        """Exercise the actual downloader without touching arXiv or project directories."""
        with tempfile.TemporaryDirectory(prefix="llm-infra-pdf-test-") as tmp:
            base = Path(tmp)
            (base / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/download_papers.sh", base / "scripts/download_papers.sh")
            core = base / "stages/01-test/papers/core"
            core.mkdir(parents=True)
            (core / "manifest.tsv").write_text(
                "slug\tarxiv_id\ttitle\nfake-paper\t2205.14135\tTest Paper\n", encoding="utf-8"
            )
            bin_dir = base / "bin"
            bin_dir.mkdir()
            curl = bin_dir / "curl"
            curl.write_text(
                '#!/usr/bin/env bash\n'
                'out=""\n'
                'while [ "$#" -gt 0 ]; do\n'
                '  if [ "$1" = "-o" ]; then shift; out="$1"; fi\n'
                '  shift\n'
                'done\n'
                "printf '%s\\n' '%PDF-1.4' 'mock offline content' > \"$out\"\n",
                encoding="utf-8",
            )
            curl.chmod(0o755)
            env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ.get("PATH", ""))
            cmd = ["bash", str(base / "scripts/download_papers.sh"), "--stage", "01"]
            result = subprocess.run(cmd, env=env, check=True, capture_output=True, text=True)
            self.assertIn("[OK]", result.stdout)
            pdf = core / "pdfs/fake-paper--2205.14135.pdf"
            self.assertTrue(pdf.read_bytes().startswith(b"%PDF-"))
            second = subprocess.run(cmd, env=env, check=True, capture_output=True, text=True)
            self.assertIn("[SKIP]", second.stdout)
            pdf.write_text("<html>not a pdf</html>", encoding="utf-8")
            third = subprocess.run(cmd, env=env, check=True, capture_output=True, text=True)
            self.assertIn("[OK]", third.stdout)
            self.assertTrue(pdf.read_bytes().startswith(b"%PDF-"))


if __name__ == "__main__":
    unittest.main()
