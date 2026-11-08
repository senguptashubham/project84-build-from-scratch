---
tags:
  - derivation
row: D06
---
# D06 · PCA from maximum variance

Row and **Derive:** statement: [README.md](../README.md#week-4--days-22-28--part-b-trees-boosting-pca-and-imbalanced-data). Related code: S2.10.

## The target

**Intuition:** The first principal component is the direction in which the data spreads out most. The eigenvalue is exactly the variance along it.

**Step people usually fake:** Why the unit-norm constraint is needed at all (without it the problem is unbounded). Also why the data must be centered first, and where the `n − 1` factor comes from.

**Check:** Points on the line `y = x` should give a first component along `(1, 1)/√2` and zero variance on the second.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
