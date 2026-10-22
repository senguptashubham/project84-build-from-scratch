---
tags:
  - derivation
row: D01
description: For logits `z`, `p = softmax(z)` and a one-hot label `y`, the loss is `L = -Σ yₖ log pₖ`. Show that `∂L/∂z = p − y`.
---
# D01 · Softmax + cross-entropy gradient

Tracker: [DERIVATION_README.md](DERIVATION_README.md#d01--softmax--cross-entropy-gradient). Related code: S3.02. Do this one before S3.02: that item asks you to derive this gradient yourself.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
