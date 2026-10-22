# Ten On-Paper Derivations

A standalone tracker for the ten derivations worth doing by hand alongside Project 84. Each one is related to something you implement, so your code gives you a real numeric check on your algebra. Tick a derivation here when it is done; `README.md` shows where it falls in the sequence and copies the tick when you refresh it.

This file gives you the target, the intuition, the step people usually fake, and a way to check yourself. It does not give the derivations. Working them out is the point.

## Why these ten

Each one meets three tests:

1. It comes up as a "derive this" or "why does this work" question.
2. It is related to a Project 84 item, so your own code can check the algebra.
3. It contains an algebraic step that is easy to wave through without understanding.

The number ten is a judgment, not a measured figure. Left out on purpose: SVM dual, RNN backpropagation through time, VAE ELBO, policy gradient, CNN backward. Add them later if a posting asks.

Budget about 1 to 1.5 hours each, 13.5 hours in total. These hours are not counted in `CODE_README.md`; `README.md` adds them to the weekly load.

## How to work each one

1. **Paper first.** Pen and paper. Photograph it, or retype a clean version, into the derivation's note file (the `Notes:` link on its row). Put photos next to it in `derivation/`. The note's `description:` field copies the entry's **Derive:** line; edit it here, then run `python master.py --sync-notes`.
2. **25-minute cap.** Stuck for 25 minutes? Take one hint, close it, then continue on your own.
3. **Name the faked step.** Write one sentence on the step in the "Step people usually fake" row and why it is true. If you cannot, the derivation is not done.
4. **Check numerically.** Use the small check in each entry. A few lines of NumPy are enough.
5. **Re-derive blind after 7 days.** Fresh paper, no notes, 15 minutes. If you miss it, repeat the next week. Each derivation has a second checkbox for this; the master tracks only the first.
6. **One card per derivation**, four lines: the statement, the key steps, the faked step, and the one-sentence interview version.

## At a glance

| ID | Derivation | Related code (Project 84) | Time |
| --- | --- | --- | --- |
| D01 | Softmax + cross-entropy gradient | S3.02 | 1 h |
| D02 | Least squares as maximum likelihood | S2.01, S1.15 | 1.5 h |
| D03 | Logistic regression: gradient and Hessian | S2.03, S7.06 | 1.5 h |
| D04 | Bias-variance decomposition | S2.04, S7.03 | 1.5 h |
| D05 | Ridge and lasso as MAP estimates | S2.01, S7.05, S1.15 | 1.5 h |
| D06 | PCA from maximum variance | S2.10 | 1.5 h |
| D07 | Attention backward pass and the square-root-d scale | S4.01 | 1.5 h |
| D08 | Adam's bias correction | S3.09 | 1 h |
| D09 | EM for a Gaussian mixture, via the ELBO | S7.07 | 1.5 h |
| D10 | Cross-entropy, KL divergence and negative log-likelihood | S2.03, S1.15 | 1 h |

The related code items are a static link, not a schedule: your own implementation is what checks the derivation. Derivation D02 needs the maximum likelihood section of your statistics reference first. The order to do things in lives in `README.md`.

---

## D01 · Softmax + cross-entropy gradient

- [ ] **D01 · Softmax + cross-entropy gradient.** `1 h` Derived on paper, faked step named, numeric check passed. Notes: [D01-softmax-cross-entropy-gradient](D01-softmax-cross-entropy-gradient.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S3.02. Do this one before S3.02: that item asks you to derive this gradient yourself.

**Derive:** For logits `z`, `p = softmax(z)` and a one-hot label `y`, the loss is `L = -Σ yₖ log pₖ`. Show that `∂L/∂z = p − y`.

**Intuition:** The gradient pushes down the logits of classes that got too much probability and pushes up the true class. It is exactly zero when `p = y`.

**Step people usually fake:** The softmax Jacobian, `∂pᵢ/∂zⱼ = pᵢ(δᵢⱼ − pⱼ)`. People jump to the clean answer without showing why the sum over classes collapses. It collapses because `Σ yₖ = 1`.

**Check:** Logits `(2, 1, 0)` with the true class 0 give `p ≈ (0.665, 0.245, 0.090)`, so the gradient is about `(−0.335, 0.245, 0.090)`. Compare against finite differences or PyTorch autograd.

## D02 · Least squares as maximum likelihood

- [ ] **D02 · Least squares as maximum likelihood.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D02-least-squares-as-maximum-likelihood](D02-least-squares-as-maximum-likelihood.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.01, S1.15.

**Derive:** Assume `y = Xw + ε` with `ε ~ N(0, σ²)`. Show that maximizing the likelihood over `w` is the same as minimizing `Σ(y − Xw)²`, then obtain the normal equations `XᵀXw = Xᵀy`. Also find the maximum likelihood estimate of `σ²`.

**Intuition:** Gaussian noise means large errors are penalized quadratically. Maximizing likelihood and minimizing squared error are the same problem.

**Step people usually fake:** Differentiating a quadratic form with respect to a vector, and dropping terms that do not depend on `w`. Also state when `XᵀX` is invertible.

**Check:** Points `(1, 2), (2, 3), (3, 5)` give slope 1.5 and intercept about 0.333. Your general formula should reproduce that.

## D03 · Logistic regression: gradient and Hessian

- [ ] **D03 · Logistic regression: gradient and Hessian.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D03-logistic-regression-gradient-and-hessian](D03-logistic-regression-gradient-and-hessian.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.03, S7.06.

**Derive:** With `p = σ(wᵀx)` and log-loss, show the gradient is `(p − y)x` per example. Then derive the Hessian `Σ p(1−p) x xᵀ = XᵀWX`, and show it is positive semi-definite, so the loss is convex.

**Intuition:** The gradient has the same shape as in linear regression, error times input. The Hessian shows the loss curves most where the model is least certain (`p` near 0.5).

**Step people usually fake:** `σ′ = σ(1−σ)` cancelling cleanly in the chain rule. Also the convexity proof, which shows `vᵀHv = Σ p(1−p)(xᵀv)² ≥ 0`.

**Check:** One feature with `x = 1`, `w = 0`, `y = 1` gives `p = 0.5`, gradient `−0.5`, Hessian `0.25`.

## D04 · Bias-variance decomposition

- [ ] **D04 · Bias-variance decomposition.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D04-bias-variance-decomposition](D04-bias-variance-decomposition.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.04, S7.03.

**Derive:** For `y = f(x) + ε` with `E[ε] = 0` and `Var(ε) = σ²`, show that the expected squared error of an estimator `f̂` at a point is `bias² + variance + σ²`.

**Intuition:** Error has three sources: being wrong on average (bias), being unstable across training sets (variance), and irreducible noise.

**Step people usually fake:** Adding and subtracting `E[f̂]`, then showing the cross terms vanish. They vanish because `ε` is independent of `f̂` and because `E[f̂ − E f̂] = 0`.

**Check:** Take the estimator `c·x̄` for the mean `μ` of `n` samples. Compute its bias and variance from your formulas, then confirm them by simulation.

## D05 · Ridge and lasso as MAP estimates

- [ ] **D05 · Ridge and lasso as MAP estimates.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D05-ridge-and-lasso-as-map-estimates](D05-ridge-and-lasso-as-map-estimates.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.01, S7.05, S1.15.

**Derive:** Show that a Gaussian prior on `w` gives ridge regression and a Laplace prior gives lasso, and find how `λ` relates to the noise and prior scales. Then show the ridge solution is `(XᵀX + λI)⁻¹Xᵀy` and how SVD shows each component being shrunk.

**Intuition:** A prior says what weights you believe before seeing data. A Laplace prior has a sharp peak at zero, which is why lasso sets weights exactly to zero.

**Step people usually fake:** Taking the negative log of the prior and tracking the scaling. Also why the kink of `|w|` at zero produces exact zeros while `w²` does not.

**Check:** With `XᵀX = I`, take the lasso objective `½‖y − Xw‖² + λ‖w‖₁` and the ridge objective `‖y − Xw‖² + λ‖w‖²` (the one whose solution is `(XᵀX + λI)⁻¹Xᵀy`). Lasso should reduce to soft-thresholding the least-squares coefficients at λ, and ridge to dividing them by `1 + λ`. For example, coefficients `(1.5, −0.3, 0.8)` with `λ = 0.5` give lasso `(1.0, 0, 0.3)` and ridge `(1.0, −0.2, 0.533)`. Finish the lasso check against your code at S7.05.

## D06 · PCA from maximum variance

- [ ] **D06 · PCA from maximum variance.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D06-pca-from-maximum-variance](D06-pca-from-maximum-variance.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.10.

**Derive:** For centered data with covariance `Σ`, maximize `wᵀΣw` subject to `‖w‖ = 1` using a Lagrange multiplier. Show the solution is the eigenvector with the largest eigenvalue, and link it to the SVD of the data matrix.

**Intuition:** The first principal component is the direction in which the data spreads out most. The eigenvalue is exactly the variance along it.

**Step people usually fake:** Why the unit-norm constraint is needed at all (without it the problem is unbounded). Also why the data must be centered first, and where the `n − 1` factor comes from.

**Check:** Points on the line `y = x` should give a first component along `(1, 1)/√2` and zero variance on the second.

## D07 · Attention backward pass and the square-root-d scale

- [ ] **D07 · Attention backward pass and the square-root-d scale.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D07-attention-backward-pass-and-the-square-root-d-scale](D07-attention-backward-pass-and-the-square-root-d-scale.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S4.01.

**Derive:** For `Y = softmax(QKᵀ/√d) V`, derive the gradients with respect to `V`, `Q` and `K`, including their shapes. Then show why the scale is `1/√d`.

**Intuition:** Attention is a softmax-weighted average, so its backward pass is the softmax Jacobian applied row by row, plus matrix transposes. The scale keeps the scores at a stable size so the softmax does not saturate.

**Step people usually fake:** The row-wise softmax Jacobian and getting the transposes and shapes right. For the scale: if the entries of `q` and `k` are independent with zero mean and unit variance, `q·k` has variance `d`, so dividing by `√d` returns it to variance 1.

**Check:** Compare all three gradients against PyTorch autograd on small random tensors.

## D08 · Adam's bias correction

- [ ] **D08 · Adam's bias correction.** `1 h` Derived on paper, faked step named, numeric check passed. Notes: [D08-adams-bias-correction](D08-adams-bias-correction.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S3.09.

**Derive:** With `m₀ = 0` and `mₜ = β mₜ₋₁ + (1 − β) gₜ`, show that if the gradient has a constant mean `μ`, then `E[mₜ] = (1 − βᵗ) μ`. That is why Adam divides by `1 − βᵗ`. Do the same for the second moment.

**Intuition:** Starting the running average at zero drags early estimates toward zero. The correction removes that drag.

**Step people usually fake:** Unrolling the recursion into a geometric sum, and stating the assumption that the gradients are stationary.

**Check:** At `t = 1`, the corrected estimate should equal `g₁` exactly.

## D09 · EM for a Gaussian mixture, via the ELBO

- [ ] **D09 · EM for a Gaussian mixture, via the ELBO.** `1.5 h` Derived on paper, faked step named, numeric check passed. Notes: [D09-em-for-a-gaussian-mixture-via-the-elbo](D09-em-for-a-gaussian-mixture-via-the-elbo.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S7.07.

**Derive:** For a latent variable `z`, show that `log p(x | θ) = ELBO(q, θ) + KL(q ‖ p(z | x, θ))` using Jensen's inequality. Show that setting `q` to the posterior (the responsibilities) closes the gap. Then derive the M-step updates for the means, covariances and mixing weights, using a Lagrange multiplier for the weights.

**Intuition:** EM repeatedly builds a lower bound that touches the true likelihood at the current parameters, then maximizes it. The likelihood can never go down.

**Step people usually fake:** Introducing `q(z)` and applying Jensen. The fact that the gap is exactly a KL divergence is what justifies the E-step choice. The Lagrange multiplier for the mixing weights summing to 1 is also commonly skipped.

**Check:** Your S7.07 log-likelihood must never decrease between iterations. That is the check on your algebra.

## D10 · Cross-entropy, KL divergence and negative log-likelihood

- [ ] **D10 · Cross-entropy, KL divergence and negative log-likelihood.** `1 h` Derived on paper, faked step named, numeric check passed. Notes: [D10-cross-entropy-kl-divergence-and-negative-log-likelihood](D10-cross-entropy-kl-divergence-and-negative-log-likelihood.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

**Related code:** S2.03, S1.15.

**Derive:** Show that `H(p, q) = H(p) + KL(p ‖ q)`. Show that minimizing cross-entropy over `q` is minimizing `KL(p ‖ q)`, and that when `p` is the empirical distribution of your data, cross-entropy is the average negative log-likelihood, so minimizing it is maximum likelihood. Show `KL ≥ 0` using Jensen.

**Intuition:** Three phrases used interchangeably for training a classifier are one idea: make the model's distribution match the data's.

**Step people usually fake:** Which direction of KL training uses, `KL(p ‖ q)` and not `KL(q ‖ p)`, and the step replacing the true distribution with the empirical one.

**Check:** With `p = (0.5, 0.5)` and `q = (0.9, 0.1)`, cross-entropy is about 1.204 nats, `H(p)` is about 0.693, and `KL(p ‖ q)` is about 0.511. Confirm `1.204 − 0.693 ≈ 0.511`, then compute the KL directly from its definition.

---

## Progress log

| ID | Derivation | First attempt | Needed a hint? | Faked step named? | Numeric check passed? | Blind re-derive (date, pass/fail) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | Softmax + cross-entropy gradient | | | | | |
| D02 | Least squares as MLE | | | | | |
| D03 | Logistic gradient and Hessian | | | | | |
| D04 | Bias-variance | | | | | |
| D05 | Ridge and lasso as MAP | | | | | |
| D06 | PCA | | | | | |
| D07 | Attention backward and √d | | | | | |
| D08 | Adam bias correction | | | | | |
| D09 | EM / ELBO | | | | | |
| D10 | Cross-entropy, KL, NLL | | | | | |
