---
tags:
  - derivation
row: D08
---
# D08 · Adam's bias correction

Row and **Derive:** statement: [README.md](../README.md#week-6--days-36-42--part-b-pytorch-workflow-optimizers-convolution-debugging). Related code: S3.09.

## The target

**Intuition:** Starting the running average at zero drags early estimates toward zero. The correction removes that drag.

**Step people usually fake:** Unrolling the recursion into a geometric sum, and stating the assumption that the gradients are stationary.

**Check:** At `t = 1`, the corrected estimate should equal `g₁` exactly.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
