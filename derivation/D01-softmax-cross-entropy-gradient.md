---
tags:
  - derivation
row: D01
---
# D01 · Softmax + cross-entropy gradient

Row and **Derive:** statement: [README.md](../README.md#week-5--days-29-35--part-a-neural-networks-from-scratch-in-numpy). Related code: S3.02. Do this one before S3.02: that item asks you to derive this gradient yourself.

## The target

**Intuition:** The gradient pushes down the logits of classes that got too much probability and pushes up the true class. It is exactly zero when `p = y`.

**Step people usually fake:** The softmax Jacobian, `∂pᵢ/∂zⱼ = pᵢ(δᵢⱼ − pⱼ)`. People jump to the clean answer without showing why the sum over classes collapses. It collapses because `Σ yₖ = 1`.

**Check:** Logits `(2, 1, 0)` with the true class 0 give `p ≈ (0.665, 0.245, 0.090)`, so the gradient is about `(−0.335, 0.245, 0.090)`. Compare against finite differences or PyTorch autograd.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
