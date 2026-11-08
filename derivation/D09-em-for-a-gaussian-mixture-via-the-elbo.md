---
tags:
  - derivation
row: D09
---
# D09 · EM for a Gaussian mixture, via the ELBO

Row and **Derive:** statement: [README.md](../README.md#week-14--days-91-96--part-b-iterative-fitting-and-representations). Related code: S7.07.

## The target

**Intuition:** EM repeatedly builds a lower bound that touches the true likelihood at the current parameters, then maximizes it. The likelihood can never go down.

**Step people usually fake:** Introducing `q(z)` and applying Jensen. The fact that the gap is exactly a KL divergence is what justifies the E-step choice. The Lagrange multiplier for the mixing weights summing to 1 is also commonly skipped.

**Check:** Your S7.07 log-likelihood must never decrease between iterations. That is the check on your algebra.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
