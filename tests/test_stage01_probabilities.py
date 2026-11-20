"""Stage 01: deterministic correctness and failure-mode checks."""
import importlib.util
import math
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "stages/01-foundations/code/algorithms/exercise.py"
spec = importlib.util.spec_from_file_location("stage01_probabilities", FILE)
probs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probs)


class TestStableProbabilityPrimitives(unittest.TestCase):
    def test_against_float64_bounded_reference(self):
        rng = random.Random(11)
        for width in (2, 3, 7, 32, 127):
            for _ in range(25):
                logits = [rng.uniform(-5, 5) for _ in range(width)]
                naive = math.log(math.fsum(math.exp(x) for x in logits))
                stable = probs.logsumexp(logits)
                relative = abs(stable - naive) / max(1.0, abs(naive))
                self.assertLessEqual(relative, 1e-6)
                self.assertAlmostEqual(math.fsum(probs.softmax(logits)), 1.0, places=12)
                target = rng.randrange(width)
                expected_ce = naive - logits[target]
                self.assertAlmostEqual(probs.cross_entropy(logits, target), expected_ce, places=11)

    def test_extreme_logits_stay_finite(self):
        for logits, target in [
            ([1000.0, 1001.0, 999.0], 2),
            ([-1000.0, -1001.0, -999.0], 1),
            ([1e6, 1e6-1, 1e6-2], 2),
            ([-1e6, -1e6+1], 0),
        ]:
            self.assertTrue(math.isfinite(probs.logsumexp(logits)))
            values = probs.softmax(logits)
            self.assertTrue(all(math.isfinite(x) for x in values))
            self.assertAlmostEqual(math.fsum(values), 1.0, places=12)
            self.assertTrue(math.isfinite(probs.cross_entropy(logits, target)))

    def test_analytic_cross_entropy_gradient(self):
        logits = [1.3, -0.7, 0.2, 3.1]
        target = 2
        expected = probs.cross_entropy_gradient(logits, target)
        eps = 1e-5
        for i in range(len(logits)):
            pos, neg = logits.copy(), logits.copy()
            pos[i] += eps
            neg[i] -= eps
            numerical = (probs.cross_entropy(pos, target) -
                         probs.cross_entropy(neg, target)) / (2 * eps)
            self.assertAlmostEqual(expected[i], numerical, places=8)
        self.assertAlmostEqual(math.fsum(expected), 0.0, places=12)

    def test_invalid_vector_and_target(self):
        for logits in ([], [math.inf], [math.nan, 1.0], [[1], [2]], [1.0, "bad"]):
            with self.assertRaises(ValueError):
                probs.logsumexp(logits)
            with self.assertRaises(ValueError):
                probs.softmax(logits)
        for target in (-1, 2, True, 0.0):
            with self.assertRaises(ValueError):
                probs.cross_entropy([0.0, 1.0], target)
            with self.assertRaises(ValueError):
                probs.cross_entropy_gradient([0.0, 1.0], target)

    def test_seeded_executable_report(self):
        from contextlib import redirect_stdout
        from io import StringIO
        with redirect_stdout(StringIO()):
            report = probs.run_exercise(["--seed", "23", "--cases", "15"])
        self.assertEqual(report["seed"], 23)
        self.assertEqual(report["cases"], 15)
        self.assertLessEqual(report["max_relative_error"], report["required_relative_tolerance"])
        self.assertIn("synthetic CPU", report["limitations"])


if __name__ == "__main__":
    unittest.main()
