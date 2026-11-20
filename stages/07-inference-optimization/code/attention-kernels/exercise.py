"""Stage 07: correctness-first, CPU-only scaled dot-product attention lab.

Reference and tiled online-softmax variants operate on lists of float rows.
This is an educational numerical baseline, NOT a CUDA/Triton implementation or
a reproduction of the FlashAttention GPU speedups. No external dependencies.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
import random
import statistics
import sys
from time import perf_counter


def _matrix(name: str, values: list[list[float]]) -> tuple[int, int]:
    if not values or not isinstance(values, (tuple, list)):
        raise ValueError(f"{name}: expected a nonempty matrix")
    if not isinstance(values[0], (tuple, list)) or not values[0]:
        raise ValueError(f"{name}: expected nonempty rows")
    width = len(values[0])
    for row in values:
        if not isinstance(row, (tuple, list)) or len(row) != width:
            raise ValueError(f"{name}: ragged rows")
        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in row):
            raise ValueError(f"{name}: nonfinite or nonnumeric element")
    return len(values), width


def _shape(q: list[list[float]], k: list[list[float]],
           v: list[list[float]], causal: bool) -> tuple[int, int, int, int]:
    nq, d = _matrix("query", q)
    nk, dk = _matrix("key", k)
    nv, dv = _matrix("value", v)
    if d != dk or nk != nv:
        raise ValueError("Q/K dimension or K/V sequence length mismatch")
    if causal and nk < nq:
        raise ValueError("causal suffix attention requires key length >= query length")
    return nq, nk, d, dv


def _allowed(i: int, j: int, nq: int, nk: int, causal: bool) -> bool:
    # For suffix decode, query i corresponds to absolute position nk-nq+i.
    return not causal or j <= nk - nq + i


def reference_attention(q: list[list[float]], k: list[list[float]],
                        v: list[list[float]], *, causal: bool = False
                        ) -> list[list[float]]:
    """Stable row-wise softmax(Q K^T / sqrt(d)) V, without NumPy.

    Q:[Nq,d], K:[Nk,d], V:[Nk,dv]; outputs [Nq,dv].
    No dropout, padding mask, positional bias, or batch/head dimension.
    """
    nq, nk, d, dv = _shape(q, k, v, causal)
    scale = math.sqrt(d)
    result = []
    for i in range(nq):
        scores = [
            math.fsum(q[i][t] * k[j][t] for t in range(d)) / scale
            if _allowed(i, j, nq, nk, causal) else -math.inf
            for j in range(nk)
        ]
        high = max(scores)
        weights = [math.exp(score - high) if score != -math.inf else 0.0
                   for score in scores]
        den = math.fsum(weights)
        result.append([math.fsum(weights[j] * v[j][t] for j in range(nk)) / den
                       for t in range(dv)])
    return result


def online_attention(q: list[list[float]], k: list[list[float]],
                     v: list[list[float]], *, block_size: int = 8,
                     causal: bool = False) -> list[list[float]]:
    """Streaming block-wise exact attention via the online-softmax recurrence.

    Holds O(dv + block_size) temporary values per query row, rather than
    an explicit QK^T matrix. This pedagogical Python implementation is not a
    GPU IO benchmark and can be slower than the dense reference.
    """
    nq, nk, d, dv = _shape(q, k, v, causal)
    if not isinstance(block_size, int) or isinstance(block_size, bool) or block_size < 1:
        raise ValueError("block_size must be a positive integer")
    scale = math.sqrt(d)
    result = []
    for i in range(nq):
        high = -math.inf
        denominator = 0.0
        numerator = [0.0] * dv
        for start in range(0, nk, block_size):
            js = [j for j in range(start, min(nk, start + block_size))
                  if _allowed(i, j, nq, nk, causal)]
            if not js:
                continue
            scores = [math.fsum(q[i][t] * k[j][t] for t in range(d)) / scale
                      for j in js]
            new_high = max(high, max(scores))
            carry = math.exp(high - new_high) if high != -math.inf else 0.0
            exp_scores = [math.exp(score - new_high) for score in scores]
            denominator = carry * denominator + math.fsum(exp_scores)
            numerator = [
                carry * numerator[t] + math.fsum(exp_scores[b] * v[j][t]
                                                for b, j in enumerate(js))
                for t in range(dv)
            ]
            high = new_high
        result.append([x / denominator for x in numerator])
    return result


def run_exercise(argv: list[str] | None = None) -> dict:
    """Measure deterministic CPU-only toy input; never assert a speedup."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seq", type=int, default=32)
    parser.add_argument("--dim", type=int, default=16)
    parser.add_argument("--value-dim", type=int, default=16)
    parser.add_argument("--block-size", type=int, default=8)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--repeats", type=int, default=10)
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--causal", action="store_true")
    args = parser.parse_args(argv)
    if min(args.seq, args.dim, args.value_dim, args.block_size,
           args.repeats) <= 0 or args.warmup < 0:
        parser.error("shapes, block size and repeats must be positive; warmup >= 0")
    rng = random.Random(args.seed)
    q = [[rng.uniform(-1, 1) for _ in range(args.dim)] for _ in range(args.seq)]
    k = [[rng.uniform(-1, 1) for _ in range(args.dim)] for _ in range(args.seq)]
    v = [[rng.uniform(-1, 1) for _ in range(args.value_dim)] for _ in range(args.seq)]
    implementations = {
        "dense_reference": lambda: reference_attention(q, k, v, causal=args.causal),
        "tiled_online": lambda: online_attention(
            q, k, v, block_size=args.block_size, causal=args.causal),
    }
    reference = implementations["dense_reference"]()
    candidate = implementations["tiled_online"]()
    error = max(abs(a-b) for x, y in zip(reference, candidate)
                for a, b in zip(x, y))
    if error > 1e-10:
        raise AssertionError(f"numerical mismatch: {error}")
    timings = {}
    for name, fn in implementations.items():
        for _ in range(args.warmup):
            fn()
        samples = []
        for _ in range(args.repeats):
            start = perf_counter()
            fn()
            samples.append((perf_counter() - start) * 1000.0)
        timings[name] = {"median_ms": statistics.median(samples),
                         "min_ms": min(samples), "max_ms": max(samples)}
    report = {"method": "single-threaded Python list CPU toy, wall-clock perf_counter",
              "python": sys.version.split()[0], "platform": platform.platform(),
              "seed": args.seed, "nq": args.seq, "nk": args.seq,
              "d": args.dim, "dv": args.value_dim, "block_size": args.block_size,
              "causal": args.causal, "warmup": args.warmup,
              "repeats": args.repeats, "max_abs_error": error,
              "tolerance": 1e-10, "timings": timings,
              "limitations": "not a GPU benchmark; no prefill/decode concurrency, CUDA kernel or memory profiling"}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    run_exercise()
