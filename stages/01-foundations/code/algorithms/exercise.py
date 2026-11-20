"""Stage 01: CPU-only numerically stable probability primitives.

Finite vector inputs represent one token's vocabulary logits. This is
transparent standard-library reference code, not a production tensor kernel.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
import random
import sys


def _check(logits):
    if not isinstance(logits, (tuple, list)) or not logits:
        raise ValueError("expected a nonempty vector")
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in logits):
        raise ValueError("all logits must be finite numbers")


def logsumexp(logits):
    """Stable log(sum(exp(logit_i))) without overflow for finite logits."""
    _check(logits)
    center = max(logits)
    return center + math.log(math.fsum(math.exp(x - center) for x in logits))


def softmax(logits):
    """Stable row-normalized probability distribution."""
    _check(logits)
    center = max(logits)
    unnorm = [math.exp(x - center) for x in logits]
    denominator = math.fsum(unnorm)
    return [x / denominator for x in unnorm]


def cross_entropy(logits, target):
    """One-token negative log-likelihood, target is a vocabulary index."""
    _check(logits)
    if isinstance(target, bool) or not isinstance(target, int) or not 0 <= target < len(logits):
        raise ValueError("target must be an in-range integer")
    # Compute using shifted scores to avoid catastrophic cancellation when
    # logits have large shared offsets. This is stable for both tails.
    center = max(logits)
    return math.log(math.fsum(math.exp(x - center) for x in logits)) - (logits[target] - center)


def cross_entropy_gradient(logits, target):
    """Exact gradient of one-token CE wrt logits: softmax - one_hot."""
    probabilities = softmax(logits)
    if isinstance(target, bool) or not isinstance(target, int) or not 0 <= target < len(logits):
        raise ValueError("target must be an in-range integer")
    return [p - (1.0 if i == target else 0.0) for i, p in enumerate(probabilities)]


def run_exercise(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--cases", type=int, default=100)
    args = parser.parse_args(argv)
    if args.cases < 1:
        parser.error("--cases must be positive")
    rng = random.Random(args.seed)
    worst_absolute_error = 0.0
    worst_relative_error = 0.0
    for _ in range(args.cases):
        logits = [rng.uniform(-6, 6) for _ in range(rng.randrange(2, 33))]
        answer = logsumexp(logits)
        reference = math.log(math.fsum(math.exp(x) for x in logits))
        err = abs(answer - reference)
        worst_absolute_error = max(worst_absolute_error, err)
        worst_relative_error = max(worst_relative_error, err / max(1.0, abs(reference)))
        if abs(math.fsum(softmax(logits)) - 1) > 1e-12:
            raise AssertionError("normalization invariant failed")
    if worst_relative_error > 1e-6:
        raise AssertionError(f"reference numerical mismatch {worst_relative_error}")
    report = {
        "stage": "01-foundations/stable-probabilities",
        "seed": args.seed, "cases": args.cases,
        "dtype": "Python float / IEEE754 binary64", "python": sys.version.split()[0],
        "platform": platform.platform(), "reference": "direct exp/log only at bounded logits [-6,6]",
        "max_absolute_error": worst_absolute_error,
        "max_relative_error": worst_relative_error,
        "required_relative_tolerance": 1e-6,
        "limitations": "synthetic CPU scalar vectors; not GPU, training or model accuracy reproduction"
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    run_exercise()
