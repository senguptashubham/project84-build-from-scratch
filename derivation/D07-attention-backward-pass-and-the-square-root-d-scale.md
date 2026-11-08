---
tags:
  - derivation
row: D07
---
# D07 · Attention backward pass and the square-root-d scale

Row and **Derive:** statement: [README.md](../README.md#week-7--days-43-49--part-a-attention-blocks-and-a-character-gpt). Related code: S4.01.

## The target

**Intuition:** Attention is a softmax-weighted average, so its backward pass is the softmax Jacobian applied row by row, plus matrix transposes. The scale keeps the scores at a stable size so the softmax does not saturate.

**Step people usually fake:** The row-wise softmax Jacobian and getting the transposes and shapes right. For the scale: if the entries of `q` and `k` are independent with zero mean and unit variance, `q·k` has variance `d`, so dividing by `√d` returns it to variance 1.

**Check:** Compare all three gradients against PyTorch autograd on small random tensors.

## Derivation

*Photo of your paper, or a clean retyped version. Done on paper first, with the 25-minute cap.*

## The faked step

*One sentence on the step in the entry's "Step people usually fake" and why it is true. If you cannot write it, the derivation is not done.*

## Numeric check

*The small check from the entry, a few lines of NumPy, and what it showed.*

## Card

*Four lines: the statement, the key steps, the faked step, and the one-sentence interview version.*
