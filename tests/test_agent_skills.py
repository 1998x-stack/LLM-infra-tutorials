"""Offline static skill tests; no model invocation, GPU or network."""
from __future__ import annotations

import importlib.util
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class SkillIntegrityTests(unittest.TestCase):
    def test_canonical_and_mirrors_are_identical(self):
        sync = load_script("sync_agent_skills")
        self.assertEqual([], sync.sync(check=True))

    def test_routing_cases_are_well_formed(self):
        cases = load_script("validate_skill_cases")
        self.assertEqual([], cases.validate())

    def test_wiki_paper_status_parser_preserves_reviewed(self):
        builder = load_script("build_knowledge_index")
        self.assertEqual(
            "reviewed",
            builder.parse_paper_status("---\nstatus: reviewed\nid: foo\n---\n# Note\n"),
        )
        self.assertEqual(
            "template",
            builder.parse_paper_status("---\nstatus: template\n---\nTODO"),
        )

    def test_wiki_topic_status_parser_preserves_reviewed(self):
        builder = load_script("build_knowledge_index")
        self.assertEqual(
            "reviewed",
            builder.parse_topic_status("# Card\n- **Status:** Reviewed; validated"),
        )
        self.assertEqual(
            "draft",
            builder.parse_topic_status("# Card\n- **Status:** Draft; educational placeholder"),
        )

    def test_wiki_parser_rejects_ambiguous_status(self):
        builder = load_script("build_knowledge_index")
        with self.assertRaises(ValueError):
            builder.parse_paper_status("---\nstatus: draft\nstatus: reviewed\n---\n")
        with self.assertRaises(ValueError):
            builder.parse_topic_status("# no status here")

    def test_index_matches_paper_and_card_source_status(self):
        builder = load_script("build_knowledge_index")
        self.assertEqual(72, len(builder.build()))
        cmd = ["python3", str(ROOT / "scripts/build_knowledge_index.py"), "--check"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

