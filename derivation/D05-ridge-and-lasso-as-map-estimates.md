---
tags:
  - derivation
row: D05
---
# D05 · Ridge and lasso as MAP estimates

Row and **Derive:** statement: [README.md](../README.md#week-3--days-15-21--part-a-linear-models-knn-naive-bayes-k-means). Related code: S2.01, S7.05, S1.15.

## The target

**Intuition:** A prior says what weights you believe before seeing data. A Laplace prior has a sharp peak at zero, which is why lasso sets weights exactly to zero.

**Step people usually fake:** Taking the negative log of the prior and tracking the scaling. Also why the kink of `|w|` at zero produces exact zeros while `w²` does not.

**Check:** With `XᵀX = I`, take the lasso objective `½‖y − Xw‖² + λ‖w‖₁` and the ridge objective `‖y − Xw‖² + λ‖w‖²` (the one whose solution is `(XᵀX + λI)⁻¹Xᵀy`). Lasso should reduce to soft-thresholding the least-squares coefficients at λ, and ridge to dividing them by `1 + λ`. For example, coefficients `(1.5, −0.3, 0.8)` with `λ = 0.5` give lasso `(1.0, 0, 0.3)` and ridge `(1.0, −0.2, 0.533)`. Finish the lasso check against your code at S7.05.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
