---
tags:
  - derivation
row: D10
---
# D10 · Cross-entropy, KL divergence and negative log-likelihood

Row and **Derive:** statement: [README.md](../README.md#week-2--days-8-14--part-b-preprocessing-leakage-and-statistics). Related code: S2.03, S1.15.

## The target

**Intuition:** Three phrases used interchangeably for training a classifier are one idea: make the model's distribution match the data's.

**Step people usually fake:** Which direction of KL training uses, `KL(p ‖ q)` and not `KL(q ‖ p)`, and the step replacing the true distribution with the empirical one.

**Check:** With `p = (0.5, 0.5)` and `q = (0.9, 0.1)`, cross-entropy is about 1.204 nats, `H(p)` is about 0.693, and `KL(p ‖ q)` is about 0.511. Confirm `1.204 − 0.693 ≈ 0.511`, then compute the KL directly from its definition.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
