"""Deterministic CPU correctness tests for the Stage 07 attention laboratory."""
import importlib.util
import math
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = (ROOT / "stages/07-inference-optimization/code/attention-kernels/exercise.py")
spec = importlib.util.spec_from_file_location("stage07_attention", MODULE)
attention = importlib.util.module_from_spec(spec)
spec.loader.exec_module(attention)


class TestStage07OnlineAttention(unittest.TestCase):
    def test_block_sizes_shapes_causal_and_decode_suffix(self):
        rng = random.Random(11)
        for nq, nk, d, dv in [(1, 1, 1, 2), (3, 3, 4, 3), (2, 5, 7, 2), (8, 8, 4, 9)]:
            q = [[rng.uniform(-5, 5) for _ in range(d)] for _ in range(nq)]
            k = [[rng.uniform(-5, 5) for _ in range(d)] for _ in range(nk)]
            v = [[rng.uniform(-5, 5) for _ in range(dv)] for _ in range(nk)]
            for causal in (False, True):
                expected = attention.reference_attention(q, k, v, causal=causal)
                for block in (1, 2, 3, nk, nk + 1):
                    actual = attention.online_attention(q, k, v, block_size=block, causal=causal)
                    self.assertEqual(len(actual), nq)
                    self.assertEqual(len(actual[0]), dv)
                    for erow, arow in zip(expected, actual):
                        for e, a in zip(erow, arow):
                            self.assertAlmostEqual(e, a, places=11)

    def test_numerical_stability_extreme_logits(self):
        q = [[500.0, -500.0], [20.0, -20.0]]
        k = [[500.0, -500.0], [-500.0, 500.0], [100.0, -100.0]]
        v = [[1.0, 4.0], [-2.0, 3.0], [8.0, 7.0]]
        for causal in (False, True):
            dense = attention.reference_attention(q, k, v, causal=causal)
            online = attention.online_attention(q, k, v, block_size=1, causal=causal)
            self.assertTrue(all(math.isfinite(x) for row in online for x in row))
            for a, b in zip(dense, online):
                for x, y in zip(a, b):
                    self.assertAlmostEqual(x, y, places=10)

    def test_causal_prefix_invariance(self):
        rng = random.Random(17)
        q = [[rng.random() for _ in range(4)] for _ in range(5)]
        k = [[rng.random() for _ in range(4)] for _ in range(5)]
        v = [[rng.random() for _ in range(3)] for _ in range(5)]
        whole = attention.online_attention(q, k, v, causal=True, block_size=2)
        for n in range(1, 6):
            prefix = attention.online_attention(q[:n], k[:n], v[:n], causal=True)
            for a, b in zip(whole[:n], prefix):
                for x, y in zip(a, b):
                    self.assertAlmostEqual(x, y, places=12)

    def test_reject_invalid_input(self):
        valid_q = [[1.0, 0.0]]
        valid_k = [[0.0, 1.0]]
        valid_v = [[3.0]]
        bad_inputs = [
            ([], valid_k, valid_v),
            (valid_q, [[1.0]], valid_v),
            (valid_q, valid_k, []),
            ([[1.0, math.nan]], valid_k, valid_v),
            ([[1.0, 0.0], [1.0]], valid_k, valid_v),
        ]
        for q, k, v in bad_inputs:
            with self.subTest(q=q, k=k):
                with self.assertRaises(ValueError):
                    attention.reference_attention(q, k, v)
        for invalid in [0, -1, 2.1, True]:
            with self.assertRaises(ValueError):
                attention.online_attention(valid_q, valid_k, valid_v, block_size=invalid)
        with self.assertRaises(ValueError):
            attention.reference_attention([[1, 0], [0, 1]], valid_k, valid_v, causal=True)

    def test_executable_report_records_metadata_and_numerical_error(self):
        from contextlib import redirect_stdout
        from io import StringIO
        buffer = StringIO()
        with redirect_stdout(buffer):
            report = attention.run_exercise([
                "--seq", "5", "--dim", "3", "--value-dim", "2",
                "--seed", "13", "--block-size", "2",
                "--warmup", "1", "--repeats", "2", "--causal",
            ])
        self.assertLessEqual(report["max_abs_error"], report["tolerance"])
        self.assertEqual(report["seed"], 13)
        self.assertEqual(report["repeats"], 2)
        self.assertIn("dense_reference", report["timings"])
        self.assertIn("tiled_online", report["timings"])
        self.assertIn("not a GPU benchmark", report["limitations"])


if __name__ == "__main__":
    unittest.main()
