# algorithms

**Stage:** 01 · Mathematics, Autograd & Language Modeling

## Implemented: stable CPU probability primitives

`exercise.py` provides dependency-free reference implementations of
`logsumexp(logits)`, `softmax(logits)`, `cross_entropy(logits,target)`
and `cross_entropy_gradient(logits,target)` for one finite vocabulary logit
vector (Python `float`, binary64).

- Reject empty, ragged, nonfinite, nonnumeric input and out-of-range targets.
- Use max-shifting and compensated `math.fsum` for numerical stability.
- Verify normalization, finite extreme-logit outputs and analytic gradients.
- Check the Stage 01 `1e-6` relative-error contract against direct
  `exp/log` on a **bounded** synthetic input range; never use the unstable
  reference to validate extreme logits.

### Reproduce

```bash
python3 -m unittest tests.test_stage01_probabilities -v
python3 stages/01-foundations/code/algorithms/exercise.py --seed 7 --cases 100
```

The CLI outputs exact Python/platform, seed, case count, scalar precision,
maximum observed errors, comparison domain and known limitations.

**Status:** Stable probability-operator CPU baseline implemented and unit-tested.
This does **not** complete Stage 01: N-gram modeling, optimizer training
curves, core-paper reviews and controlled full-stage experiments remain TODO.
