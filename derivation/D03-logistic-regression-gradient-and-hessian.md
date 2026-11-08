---
tags:
  - derivation
row: D03
---
# D03 · Logistic regression: gradient and Hessian

Row and **Derive:** statement: [README.md](../README.md#week-3--days-15-21--part-a-linear-models-knn-naive-bayes-k-means). Related code: S2.03, S7.06.

## The target

**Intuition:** The gradient has the same shape as in linear regression, error times input. The Hessian shows the loss curves most where the model is least certain (`p` near 0.5).

**Step people usually fake:** `σ′ = σ(1−σ)` cancelling cleanly in the chain rule. Also the convexity proof, which shows `vᵀHv = Σ p(1−p)(xᵀv)² ≥ 0`.

**Check:** One feature with `x = 1`, `w = 0`, `y = 1` gives `p = 0.5`, gradient `−0.5`, Hessian `0.25`.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
