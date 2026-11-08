---
tags:
  - derivation
row: D02
---
# D02 · Least squares as maximum likelihood

Row and **Derive:** statement: [README.md](../README.md#week-3--days-15-21--part-a-linear-models-knn-naive-bayes-k-means). Related code: S2.01, S1.15.

## The target

**Intuition:** Gaussian noise means large errors are penalized quadratically. Maximizing likelihood and minimizing squared error are the same problem.

**Step people usually fake:** Differentiating a quadratic form with respect to a vector, and dropping terms that do not depend on `w`. Also state when `XᵀX` is invertible.

**Check:** Points `(1, 2), (2, 3), (3, 5)` give slope 1.5 and intercept about 0.333. Your general formula should reproduce that.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
