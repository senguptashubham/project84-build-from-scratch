---
tags:
  - derivation
row: D04
---
# D04 · Bias-variance decomposition

Row and **Derive:** statement: [README.md](../README.md#week-3--days-15-21--part-a-linear-models-knn-naive-bayes-k-means). Related code: S2.04, S7.03.

## The target

**Intuition:** Error has three sources: being wrong on average (bias), being unstable across training sets (variance), and irreducible noise.

**Step people usually fake:** Adding and subtracting `E[f̂]`, then showing the cross terms vanish. They vanish because `ε` is independent of `f̂` and because `E[f̂ − E f̂] = 0`.

**Check:** Take the estimator `c·x̄` for the mean `μ` of `n` samples. Compute its bias and variance from your formulas, then confirm them by simulation.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
