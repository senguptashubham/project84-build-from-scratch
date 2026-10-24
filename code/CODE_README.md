# Build From Scratch: 84 Days

A 120-day, nine-sprint ladder for building ML and AI engineering code without an AI assistant - from NumPy fluency to transformers to a working retrieval-augmented generation (RAG) app, followed by a breadth extension. The project keeps its original name, Project 84, after its first 84 days: Sprints 1-6 (Days 1-84) are the core ladder, and Sprints 7-9 (Days 85-120) extend it. Each item is a problem statement: read it, open a blank file, solve it, test it, commit it.

## Why

AI assistants make it easy to ship code you couldn't write yourself. That's fine for getting work done, but interviews, debugging and research all depend on what you can build from a blank file. This plan rebuilds that ability one small, testable piece at a time. The items are drawn from what ML and AI engineering interviews commonly ask candidates to implement from scratch.

## Who it's for

Anyone comfortable with basic Python (functions, classes, list comprehensions) who has met the core ML ideas (loss functions, gradient descent, train/test splits) and wants to be able to write them without help. This plan tests implementation, not theory; if a concept is new to you, learn it first, then come back to the item.

## What this doesn't cover

Data structures and algorithms. Many companies, especially in India, still open ML interviews with a standard coding round, but it's a separate skill with good tracked resources already. If your target roles need it, work through a list like [NeetCode 150](https://neetcode.io/practice) alongside this plan, rather than squeezing it into the same hour.

## At a glance

| Sprint | Days | Theme | Items | Hours | Per day |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-14 | NumPy, data and statistics fluency | 16 | 40 | 2.9 |
| 2 | 15-28 | Classical ML by hand | 12 | 45.5 | 3.2 |
| 3 | 29-42 | Neural networks | 11 | 42 | 3.0 |
| 4 | 43-56 | Transformers | 13 | 43 | 3.1 |
| 5 | 57-70 | Retrieval, ranking and LLM engineering | 10 | 40.5 | 2.9 |
| 6 | 71-84 | Ship a RAG app from your own parts | 10 | 40.5 | 2.9 |
| 7 | 85-96 | Data, classical ML and representation breadth | 10 | 40 | 3.3 |
| 8 | 97-108 | Deep learning and transformer internals breadth | 11 | 39.5 | 3.3 |
| 9 | 109-120 | Retrieval, serving and alignment breadth, final exam | 10 | 38.5 | 3.2 |
| | 1-120 | **Total** | **103** | **369.5** | **3.1** |

**★** marks an item added to the original ladder after it was first published; it follows the same rules as every other item. Sprints 7-9 are entirely extension, so their items carry no stars. Hours are planning estimates from the size tags described below.

## Sizes and pacing

Every item carries a size tag: `S` is about 1.5 h, `M` about 3.5 h, `L` about 6 h. These are planning numbers, not promises. An `L` item is best done in two sessions, and its text ends with a *Break* note saying where to stop. The sprint totals above are the sums of these tags; the plan averages about 3 h a day, from 2.9 to 3.3 across sprints. Sprints 1, 5 and 6 are the lightest on purpose, because Sprint 6 overlaps the start of job applications.

Each sprint is split into Part A and Part B, about a week each, with a table showing the order to work in. Items are listed in ID order further down; where the Order column differs (for example S3.11 comes before S3.04), follow the Order column. Each sprint also has an *If you fall behind* line that names what to cut first.

**Calibrate early.** Add a line to `log.md` with your minutes each time you tick an item. After S1.04-S1.07, look at the *Actual / planned* column in the Progress table in `README.md`. If it is 1.5 or more, treat every sprint's hours as 1.5 times larger and start using the *If you fall behind* lines from Sprint 1 instead of waiting for Sprint 3.

## Setup

- **Python 3.10+** and these packages, all in `requirements.txt`: `numpy scipy pandas matplotlib scikit-learn torch statsmodels pytest` (`statsmodels` is for S1.16). Sprint 4 adds `transformers` (for loading GPT-2 weights); Sprint 5 adds `sentence-transformers faiss-cpu rank_bm25 tiktoken pydantic`; Sprint 6 adds `fastapi uvicorn onnx onnxruntime` plus a RAG library of your choice (LangChain or LlamaIndex); Sprint 8 adds `torchvision`; Sprint 9 adds `httpx` (and optionally `mlflow` or `locust`).
- **Other tools:** Docker (or Podman) for S6.07, and a GitHub repo with Actions enabled for CI.
- **Hardware:** a laptop is enough for everything. Sprint 4's GPT trains on a CPU with a small model; a free Google Colab GPU makes it faster, and helps with S8.05, S8.06 and S8.09.
- **An LLM for Sprints 5-6 and 9:** either an API key (most providers offer free or cheap tiers) or a free local model through [Ollama](https://ollama.com). For S5.08, pick a model that supports tool calling.
- **Datasets:** built into scikit-learn (`load_iris`, `load_breast_cancer`, `load_diabetes`, `make_blobs`, `make_classification`) unless an item says otherwise. Items that need an outside dataset (MovieLens 100K in S3.11, text8 in S7.08, an image set in S8.06) name it.

## How to follow along

1. Fork or copy this repo.
2. Each sprint has 10-16 items in two parts (A and B). Sprints 1-6 run 14 days; Sprints 7-9 run 12 days. Rewrites (Rule 3) and overruns come out of the same hour budget, which is what the *If you fall behind* lines are for.
3. Tick each box as you commit its solution, and add a line to `log.md` with your minutes. Your commit history becomes your progress log.
4. Missing a day is fine. Finishing is what matters. On a bad day, 25 minutes on the current item still counts as a session.
5. Sprints 7-9 are breadth. Their items are independent of each other (with the two exceptions noted in Sprint 7), so if time runs short, skip an item rather than rushing it.
6. At the end of each part, run `pytest` on the whole sprint folder and fix anything that broke. That is the checkpoint.

## Rules

1. **Blank file every time.** Look up APIs in official docs or search engines, but don't open an existing implementation of the item until yours is committed. No code assistant, no inline autocomplete.
2. **30-minute rule.** Stuck for 30 minutes? First spend 10 minutes on paper: draw the shapes or how the data flows. Still stuck? Ask an AI for *one hint*, never code.
3. **Rewrite rule.** Anything you needed a hint for gets rewritten from a blank file the next day, in `code/rewrites/`.
4. **Prove it.** Every item ships with a test file run by `pytest`. Where a library equivalent exists (NumPy, scikit-learn, PyTorch), your output must match it within a stated tolerance (default `1e-6`).
5. **One commit per item**, message format: `S1.03: stratified split`.
6. **Scope lock.** If a sprint runs long, cut what its *If you fall behind* line names, starting with the decision tree items (S2.07-S2.09) in Sprint 2. Never add items mid-sprint; park ideas in `PARKED.md`.
7. **Defend it.** Optional, best for `M` and `L` items. Once an item is committed and its tests pass, ask an AI to critique it, not to fix it: numerical stability, edge cases, time and memory cost, and why each line is needed. Tick agree / disagree / will fix / won't fix on each point, with a one-line note only when you disagree. If you want a record, keep it in `code/critiques/<ID>.md`, one file per item, and add a new run when you critique again instead of overwriting the old one. Fixes go in a new commit, for example `S1.05: fix after critique`.

## Repo layout

```
code/                    (this folder; requirements.txt and pyproject.toml are one level up)
    sprint1_numpy_data_fluency/
        s1_01_pairwise.py
        test_s1_01_pairwise.py
        ...
    sprint2_classical_ml/
    sprint3_neural_nets/
    sprint4_transformers/
    sprint5_retrieval_llm/
    sprint6_rag/
    sprint7_classical_breadth/
    sprint8_deep_learning_breadth/
    sprint9_retrieval_serving_breadth/
    rewrites/
    critiques/           optional critique notes, one file per item
```

Solutions are `.py` modules with a matching `test_*.py`. Use a notebook only where an item asks for plots or a written report, and keep any logic it tests in a `.py` file.

---

## Sprint 1 · Days 1-14 · NumPy, data and statistics fluency

**Load:** 16 items, about 40 h (2.9 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 1-7 | Splits, metrics and pandas | S1.01-S1.09 | 19.5 |
| B | 8-14 | Preprocessing, leakage and statistics | S1.10-S1.16 | 20.5 |

**If you fall behind, cut:** S1.16, S1.15, S1.14 (in that order).

- [x] **S1.01 · Pairwise distances without loops.** `S` Given `X` of shape `(n, d)` and `Y` of shape `(m, d)`, return an `(n, m)` matrix of Euclidean distances using broadcasting only. Then do it again using the identity ‖x−y‖² = ‖x‖² + ‖y‖² − 2x·y. Clip tiny negatives to zero before the square root. *Test:* both match `scipy.spatial.distance.cdist` to 1e-6 on random data; explain in a comment why the second version is faster and where it can go numerically wrong.

- [x] **S1.02 · Numerically stable activations.** `S` Write `sigmoid(z)`, `softmax(z, axis)` and `logsumexp(z, axis)` that do not overflow for inputs like `[1000, 1001, 1002]` or `[-1000, 0]`. Softmax must work along any axis of a 2D array. *Test:* no `inf`/`nan` on extreme inputs; softmax sums to 1 along the chosen axis; matches `scipy.special.expit`, `softmax` and `logsumexp`.

- [x] **S1.03 · Data splits.** `S` Write `train_val_test_split(X, y, ratios=(0.7, 0.15, 0.15), seed)` that shuffles reproducibly. Then write a stratified version that preserves class proportions in each split. *Test:* the same seed gives identical splits; on 1,000 samples with a 90/10 label split, class proportions in every split are within 1 percentage point of the original.

- [x] **S1.04 · k-fold cross-validation.** `S` Write a generator `kfold(n, k, shuffle, seed)` yielding `(train_idx, val_idx)` pairs. Every index must appear in exactly one validation fold. Then write `cross_val_score(model_fn, X, y, k, metric)` that trains a fresh model per fold and returns the per-fold scores. *Test:* fold union equals all indices; folds are disjoint; sizes differ by at most one; `cross_val_score` runs with a trivial mean-predicting model.

- [x] **S1.05 · Classification metrics from raw arrays.** `S` Given `y_true` and `y_pred` (binary and multiclass), compute accuracy, confusion matrix, precision, recall, F1, and macro/micro averages. When a class is never predicted, return 0 for its precision. *Test:* matches `sklearn.metrics` (with `zero_division=0`) on five random cases, including one where a class has no predictions.

- [ ] **S1.06 · ROC-AUC from scores.** `M` Given binary `y_true` and continuous `scores`, compute the ROC curve (FPR, TPR at every threshold) and AUC by the trapezoidal rule. Then compute AUC a second way: the probability a random positive outranks a random negative, counting ties as half. *Test:* both methods agree with each other and with `roc_auc_score`, including on scores with ties.

- [ ] **S1.07 · Regression metrics.** `S` Implement MSE, RMSE, MAE, R², and MAPE (guard against zero targets). *Test:* matches `sklearn.metrics` on targets with no zeros; MAPE returns a finite value when a target is zero. Write one sentence on when MAE is a better choice than RMSE.

- [ ] **S1.08 · pandas cleaning.** `M` Take a messy public CSV with mixed types and dates, such as an export from a city or government open-data portal. Without AI: fix dtypes, parse dates, strip whitespace in strings, standardize categories with inconsistent spelling, handle missing values with a justified strategy per column, remove duplicates. *Deliverable:* a script that produces a clean file plus a log of every change and how many rows it affected.

- [ ] **S1.09 · pandas reshaping.** `M` On the cleaned data: a groupby with multiple aggregations and named output columns; a merge with a second small lookup table you build, in which some keys deliberately don't match, and which you detect and explain; a pivot table and its inverse `melt`; a rolling or cumulative computation within groups. *Test:* each operation cross-checked by a manual count on a small slice.

- [ ] **S1.10 · Solo EDA report.** `M` On a dataset you have never used, produce a notebook answering: shape and types, missing patterns, target distribution, three strongest univariate relationships with the target, one leakage risk, one surprising finding. Plots via matplotlib only. *Done when:* a stranger could read it and decide on a modeling approach.

- [ ] **S1.11 · One-hot and ordinal encoding.** `S` Implement one-hot encoding that handles categories unseen at fit time (ignore them, or map them to an "other" column), and ordinal encoding with an explicit order. Fit on train, transform on test. *Test:* column count and order are the same for train and test, including when test contains an unseen category.

- [ ] **S1.12 · Standardization without leakage.** `S` Implement a `StandardScaler`-like class with `fit`, `transform`, `inverse_transform`. Guard against zero-variance columns. *Test:* matches scikit-learn's `StandardScaler`; demonstrate in a comment why fitting on the full dataset before splitting is leakage.

- [ ] **S1.13 ★ · Leakage-safe splits.** `M` Write `time_split(df, time_col, cutoffs)` that trains on the past and validates on the future, and `group_kfold(groups, k, seed)` that guarantees no group (a user, patient or ticket ID, say) appears in both train and validation. Then build a small dataset in which rows from the same group are near-duplicates, and show with any model how a random split inflates the score compared with the group split. *Test:* in every time split, `max(train_time) < min(val_time)`; in every group fold, the train and validation group sets are disjoint and every group lands in exactly one validation fold; your demo shows a clear score gap and a one-sentence explanation.

- [ ] **S1.14 ★ · Bootstrap confidence intervals and a permutation test.** `M` Given predictions from two classifiers on the same test set, compute a 95% bootstrap confidence interval for each model's accuracy and for the difference in accuracy (resample test rows, using the same resampled indices for both models). Then run a paired permutation test for the difference by randomly swapping the two models' predictions row by row. Write a comment on why a single test-set number is not enough. *Test:* for two independent classifiers with the same true accuracy, the difference's 95% interval contains 0 in 91-99% of 200 simulated test sets; the interval width at n=1,600 is about half the width at n=400 (within 20%); the bootstrap standard error of accuracy matches √(p(1−p)/n) within 10%.

- [ ] **S1.15 ★ · Maximum likelihood and Bayesian updating.** `M` Derive on paper (a markdown cell is fine) the maximum likelihood estimates for a Bernoulli parameter and for a Gaussian's mean and variance. Implement them, then implement the Beta-Binomial update: a Beta(a, b) prior plus k successes in n trials gives a posterior, with its mean and a 95% credible interval from the quantiles. Show what happens with 0 successes in 5 trials under the maximum likelihood estimate versus the posterior mean. *Test:* the Gaussian estimates match `np.mean` and `np.var(ddof=0)`; the Bernoulli estimate equals k/n; posterior parameters equal (a+k, b+n−k); your credible interval matches `scipy.stats.beta.interval` to 1e-6; one sentence on why the difference matters when estimating rare-event rates.

- [ ] **S1.16 ★ · A/B test from scratch.** `M` Simulate a control/treatment conversion experiment. Implement the two-proportion z-test and a 95% confidence interval for the difference, a sample-size calculator for a target minimum detectable effect, significance level and power, and a simulation of "peeking" (testing after every 100 users and stopping at the first p < 0.05) versus testing once at the end. *Test:* the z-test p-value matches `statsmodels.stats.proportion.proportions_ztest` to 1e-6 (check which variance estimate its defaults use and match it) and a hand calculation on a small example; your sample size is within 5% of statsmodels' `NormalIndPower().solve_power` with `proportion_effectsize`; with no true effect, the single-look false-positive rate is 4-6% over 2,000 simulations while peeking pushes it above 15%.

---

## Sprint 2 · Days 15-28 · Classical ML by hand

**Load:** 12 items, about 45.5 h (3.2 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 15-21 | Linear models, kNN, Naive Bayes, k-means | S2.01-S2.06 | 21.5 |
| B | 22-28 | Trees, boosting, PCA and imbalanced data | S2.07-S2.12 | 24 |

**If you fall behind, cut:** S2.07-S2.09 first (Rule 6), then S2.12.

- [ ] **S2.01 · Linear regression, closed form.** `M` Implement fit via the normal equation with a bias term. Then fit via `np.linalg.lstsq` and explain in a comment why solving is preferred over inverting `XᵀX`. Add ridge (L2) regularization without penalizing the bias. *Test:* on `load_diabetes`, coefficients match `LinearRegression`, and `Ridge` with the same `alpha` (note that scikit-learn's ridge penalizes the sum of squared errors, not the mean).

- [ ] **S2.02 · Linear regression, gradient descent.** `M` Derive the MSE gradient by hand in a notebook markdown cell, then implement batch GD and mini-batch SGD with a learning-rate parameter. Plot loss vs iteration with and without feature scaling. *Test:* batch GD converges to the S2.01 solution within 1e-3; the plot shows scaling's effect.

- [ ] **S2.03 · Logistic regression.** `L` Implement binary logistic regression trained by gradient descent with a numerically stable log-loss (work from logits, not probabilities), L2 regularization, and separate `predict_proba` and `predict(threshold)` methods. Then extend to multiclass via softmax regression. *Test:* accuracy within 1 percentage point of scikit-learn's `LogisticRegression` on `load_breast_cancer` (binary) and `load_iris` (multiclass). To compare fairly, if your loss is mean log-loss plus (λ/2)‖w‖², set `C = 1/(n·λ)`. No `nan` when classes are perfectly separable. *Break:* after binary logistic regression passes its test, add softmax regression.

- [ ] **S2.04 · k-nearest neighbours.** `M` Vectorized kNN classifier and regressor using your S1.01 distance function. Support uniform and distance-weighted voting, and break ties deterministically. *Test:* predictions match `KNeighborsClassifier` with the same `k` and `weights` on data without distance ties; report accuracy vs k on a validation set and pick k.

- [ ] **S2.05 · Gaussian Naive Bayes.** `S` Fit per-class priors, means and variances; predict using log-probabilities to avoid underflow; add variance smoothing. *Test:* predictions match `GaussianNB` (implement its `var_smoothing`, which adds a fraction of the largest feature variance); explain in one line why working in log space matters.

- [ ] **S2.06 · k-means.** `M` Implement k-means with random init and k-means++ init. Stop when assignments no longer change or after `max_iter`. Handle an empty cluster by reseeding it from the farthest point. Return labels, centroids, and inertia. Run several restarts and keep the best. *Test:* on well-separated `make_blobs` data, recovers the true clusters; inertia is within 1% of scikit-learn's `KMeans`.

- [ ] **S2.07 · Decision tree splits.** `S` Write `gini(y)`, `entropy(y)`, and `best_split(X, y)` that searches every feature and threshold and returns the one with maximum impurity reduction. *Test:* on a hand-built 8-row dataset, your chosen split matches the one you compute on paper.

- [ ] **S2.08 · CART classifier.** `M` Build a recursive decision tree using S2.07 with `max_depth` and `min_samples_split` stopping rules, and a `predict` that walks the tree. *Test:* training accuracy reaches 100% with no depth limit on `load_iris`; test accuracy on `load_breast_cancer` is within 3 percentage points of `DecisionTreeClassifier` at the same depth.

- [ ] **S2.09 · Bagging.** `M` Wrap your tree in a bootstrap ensemble with majority voting and optional random feature subsets per split (a small random forest). *Test:* across 10 seeds, the ensemble's test accuracy has a higher mean and lower variance than a single tree's.

- [ ] **S2.10 · PCA.** `M` Implement PCA via SVD of centered data. Return components, explained variance ratio, `transform`, and `inverse_transform`. *Test:* matches scikit-learn's `PCA` up to sign flips; reconstruction error decreases as components increase.

- [ ] **S2.11 ★ · Gradient boosting.** `L` Implement gradient boosting for squared error: start from the target mean, fit a small regression tree to the residuals (use variance reduction; extend S2.08 or write a depth-limited version), add it with a learning rate, and repeat for `n_rounds`, recording train and validation loss each round. Then switch to log-loss for binary classification, where each tree fits the negative gradient (y − p). *Test:* with a small learning rate, training loss never increases; validation loss has a minimum you use for early stopping; on `load_diabetes` your validation MSE is within 10% of `GradientBoostingRegressor` with the same depth, rounds and learning rate (`subsample=1.0`). *Break:* after squared-error boosting passes, add the log-loss version.

- [ ] **S2.12 ★ · Imbalance and calibration.** `L` On a dataset with about 5% positives (`make_classification` with `weights=[0.95]`), compare plain logistic regression (S2.03), a class-weighted loss, and random oversampling of the minority class (training split only). Report accuracy, precision, recall, F1 and average precision, choosing the decision threshold on the validation set rather than using 0.5. Then draw a reliability diagram (10 bins), compute expected calibration error (ECE), and fix miscalibration with Platt scaling that you implement (a one-dimensional logistic fit on validation scores). *Test:* average precision matches `average_precision_score`; ECE matches a hand calculation on a 3-bin toy example; the all-negative baseline's accuracy exceeds 94% and your report explains why accuracy misleads here; ECE after Platt scaling is lower than before on the test split. *Break:* finish the comparison table and the threshold choice, then do calibration.

---

## Sprint 3 · Days 29-42 · Neural networks

**Load:** 11 items, about 42 h (3.0 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 29-35 | Neural networks from scratch in NumPy | S3.01-S3.03, S3.11, S3.04 | 20.5 |
| B | 36-42 | PyTorch workflow, optimizers, convolution and debugging | S3.05-S3.06, S3.09, S3.07-S3.08, S3.10 | 21.5 |

**If you fall behind, cut:** S3.10, then S3.11 (and S5.10 with it), then S3.08.

- [ ] **S3.01 · MLP forward pass in NumPy.** `S` A two-layer network (input → hidden with ReLU → output with softmax) with He initialization. Write the forward pass for a batch and return cached intermediates. *Test:* output shapes are correct; rows sum to 1.

- [ ] **S3.02 · Backpropagation in NumPy.** `L` Derive gradients for cross-entropy + softmax, the linear layers, and ReLU. Implement the backward pass. *Test:* gradient check with finite differences in `float64`, with relative error below 1e-5 on every parameter. *Break:* derive all gradients on paper first, then code them and run the gradient check.

- [ ] **S3.03 · Training a NumPy MLP.** `M` Train S3.01/S3.02 with mini-batch SGD on MNIST (via `torchvision` or `sklearn.datasets.fetch_openml`). Add momentum, and L2 or dropout. *Test:* test accuracy above 95%; learning curves saved as an image.

- [ ] **S3.04 · Tiny autograd engine.** `L` A scalar `Value` class supporting `+`, `*`, `**`, `tanh`, `relu` that builds a graph and runs backpropagation via topological sort. Train a small MLP with it. This is the idea behind Andrej Karpathy's micrograd; build yours before looking at it. *Test:* gradients match PyTorch on the same small expression. *Break:* get `Value` and `backward()` passing first, then train the MLP.

- [ ] **S3.05 · PyTorch data pipeline.** `S` Write a custom `Dataset` for a CSV or image folder, with transforms, and a `DataLoader` with shuffling and batching. *Test:* iterating one epoch returns every sample exactly once.

- [ ] **S3.06 · PyTorch training loop.** `M` From a blank file: model, optimizer, loss, train loop, eval loop under `torch.no_grad()` with `model.eval()`, device handling, a learning-rate scheduler, early stopping on validation loss, and checkpoint save/load. Save the model, optimizer, scheduler and random-number-generator states. *Test:* on CPU, stopping and resuming training gives final metrics within 1e-4 of an uninterrupted run with the same seed.

- [ ] **S3.07 · conv2d in NumPy.** `L` Implement a 2D convolution forward pass supporting stride, padding, multiple input and output channels, and batches. Like PyTorch, compute cross-correlation (no kernel flip). Do it with loops first, then with an im2col approach. *Test:* both match `torch.nn.functional.conv2d`; time both versions.

- [ ] **S3.08 · Debugging drill.** `M` Write a script that takes your working S3.06 loop and randomly injects one bug without telling you which: missing `zero_grad`, softmax applied before `CrossEntropyLoss`, missing `model.eval()` with dropout, a transposed tensor that silently broadcasts, a learning rate 100× too high, labels shuffled independently of inputs. (A friend can inject them instead.) Diagnose each from symptoms alone. *Deliverable:* `DEBUGGING.md` with symptom → cause → fix for each.

- [ ] **S3.09 ★ · Adam and AdamW.** `M` Implement SGD with momentum, RMSprop, Adam (with bias correction) and AdamW (decoupled weight decay) as classes with a `step(params, grads)` method. Train your S3.03 MLP with each and compare loss curves under the same seed. *Test:* in `float64` over 100 steps on a small quadratic and on a tiny MLP, your Adam and AdamW parameters match `torch.optim.Adam` and `torch.optim.AdamW` within 1e-6 (same betas, eps and weight decay); write one sentence on why AdamW differs from Adam with L2 regularization.

- [ ] **S3.10 ★ · Training sanity-check kit.** `M` Write `sanity_check(model, loader)` that runs pre-flight checks from a blank file: the initial loss is close to log(number of classes) for a classifier; the model can overfit a single batch of 16 samples to near-zero loss within 200 steps; every parameter has a finite, non-zero gradient; per-layer gradient norms are logged; and training on shuffled labels leaves validation accuracy near chance. *Test:* passes on your working S3.06 model, and fails with a clear message on three broken variants (missing `zero_grad`, wrong loss input, a frozen layer).

- [ ] **S3.11 ★ · Matrix factorization with SGD.** `M` Matrix factorization is the bridge from classical ML to learned embeddings: every user and item gets a vector, trained by SGD. On MovieLens 100K, hold out each user's most recent rating (or use a time-based split). Implement the model r̂ = μ + b_u + b_i + p_u·q_i, trained by SGD on the observed ratings with L2 regularization, with the number of factors, learning rate and regularization as parameters. Compare against two baselines: the global mean, and the user-plus-item-bias model without factors. *Test:* training RMSE falls every epoch; test RMSE is clearly below the global-mean baseline and is reported next to the bias-only baseline (a tuned factor model should match or beat it); the analytic gradient for one rating matches finite differences in `float64` to 1e-5; in a comment, explain what the cold-start problem is for a user or item with no ratings.

---

## Sprint 4 · Days 43-56 · Transformers

**Load:** 13 items, about 43 h (3.1 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 43-49 | Attention, blocks and a character GPT | S4.01-S4.05, S4.10, S4.06-S4.07 | 20.5 |
| B | 50-56 | Tokenizer, KV cache, GPT-2 and LoRA | S4.08-S4.09, S4.11-S4.13 | 22.5 |

**If you fall behind, cut:** S4.10, then S4.11-S4.12 together. Keep S4.13 (LoRA).

- [ ] **S4.01 · Scaled dot-product attention.** `S` Given `Q (b, t, d)`, `K (b, s, d)`, `V (b, s, d)` and an optional boolean mask where `True` means "may attend" (PyTorch's convention), return outputs and attention weights. Apply the mask before a stable softmax; scale by √d. *Test:* outputs match `torch.nn.functional.scaled_dot_product_attention`; masked positions receive zero weight.

- [ ] **S4.02 · Causal and padding masks.** `S` Build a causal mask for sequence length `t`, and a padding mask from a batch of variable-length sequences. Combine them correctly. *Test:* a token never attends to future or padded positions.

- [ ] **S4.03 · Multi-head attention.** `M` Implement MHA with projection layers, splitting into heads, attention, concatenation, and output projection, in PyTorch. *Test:* outputs match `nn.MultiheadAttention(batch_first=True)` after copying its `in_proj_weight`, `in_proj_bias` and `out_proj` weights into yours.

- [ ] **S4.04 · Positional encoding.** `S` Implement sinusoidal encodings and learned position embeddings. *Test:* sinusoidal values match the formula in "Attention Is All You Need" at a few hand-computed positions; plot the encoding matrix and the dot product between positions as distance grows.

- [ ] **S4.05 · Transformer block.** `S` Pre-LayerNorm block: LN → MHA → residual → LN → MLP (GELU) → residual, with dropout. *Test:* output shape equals input shape; after one backward pass, every parameter has a non-zero gradient.

- [ ] **S4.06 · Character-level GPT.** `L` Stack blocks into a decoder-only model with token and position embeddings and a tied output head. Train a small model (around 1M parameters) on a public-domain book, for example from Project Gutenberg. *Test:* validation loss falls well below the unigram baseline (the loss from predicting each character's overall frequency); samples look locally plausible. *Break:* build the model and a short sanity run first, then the full training run (start it and do something else while it trains).

- [ ] **S4.07 · Sampling strategies.** `S` Implement greedy, temperature, top-k, and top-p (nucleus) sampling. *Test:* at a very low temperature (e.g. 1e-4) and with top-k at k=1, output matches greedy; top-p never samples a token outside the nucleus.

- [ ] **S4.08 · Minimal byte-level BPE tokenizer.** `L` Train byte-pair encoding on a text's UTF-8 bytes: count adjacent pairs, merge the most frequent, repeat for N merges. Implement `encode` and `decode`. *Test:* `decode(encode(text)) == text` on unseen text, including non-ASCII characters such as Bengali or emoji. *Break:* training merges first, then `encode` and `decode`.

- [ ] **S4.09 · KV cache.** `M` Add a key/value cache to your GPT so generation reuses past keys and values instead of recomputing them. *Test:* generated tokens are identical with and without the cache under greedy decoding; measure the speedup at length 256.

- [ ] **S4.10 ★ · RMSNorm and SwiGLU block.** `M` Implement RMSNorm and a SwiGLU feed-forward layer (`silu(gate(x)) * up(x)`, then a down projection). Assemble a Llama-style block (pre-RMSNorm → attention → residual → pre-RMSNorm → SwiGLU → residual) that can replace your S4.05 block. *Test:* RMSNorm matches `torch.nn.RMSNorm` (PyTorch 2.4+) within 1e-6, or the formula on a hand-computed case if your version lacks it; the block preserves input shape; a SwiGLU layer with hidden size 8d/3 (rounded) has a parameter count within 5% of a GELU MLP with hidden size 4d, and you explain in a comment why that ratio is used.

- [ ] **S4.11 ★ · GPT-2 architecture from scratch.** `M` Implement GPT-2 small's architecture yourself: 12 layers, 12 heads, width 768, learned positions (1,024), pre-LayerNorm blocks, the tanh-approximation GELU that GPT-2 uses, and an output head tied to the token embedding. Name your modules so each one can be mapped to a Hugging Face parameter in S4.12. *Test:* a forward pass on random token ids returns logits of shape `(batch, length, 50257)`; your parameter count equals `sum(p.numel() for p in GPT2LMHeadModel(GPT2Config()).parameters())` (a randomly initialized model needs no download); changing a later token never changes earlier logits.

- [ ] **S4.12 ★ · Load GPT-2 weights into your own model.** `M` Download GPT-2 small through `transformers` and copy its weights into your S4.11 model by name. GPT-2's `Conv1D` layers store weights transposed relative to `nn.Linear`, so check every shape as you map. Add your S4.09 key/value cache to this model. *Test:* logits for five prompts match `GPT2LMHeadModel` within 1e-4 at every position; your S4.07 samplers produce readable text from your model; cached and uncached generation agree.

- [ ] **S4.13 ★ · LoRA.** `L` Implement `LoRALinear`, which wraps a frozen `nn.Linear` with trainable matrices A (r × in) and B (out × r), scaling α/r, and B initialized to zero. Add `merge()` and `unmerge()` that fold the adapter into the base weight and back. Fine-tune your S4.06 character GPT or the S4.12 GPT-2 on a small text in a new style, with adapters on the attention projections only. *Test:* at initialization the wrapped layer's output equals the base layer's exactly; before and after `merge()` outputs match within 1e-5; trainable parameters are under 2% of the total; the loss on the new text drops while the base weights stay bit-identical (assert it). *Break:* `LoRALinear` with its tests first, then the fine-tuning run.

---

## Sprint 5 · Days 57-70 · Retrieval, ranking and LLM engineering

Pick one document set at the start of this sprint (your notes, a project's documentation, or a public-domain book split into files), roughly 50-500 pages. You'll use it for every item here and in Sprint 6.

**Load:** 10 items, about 40.5 h (2.9 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 57-63 | Build and measure retrieval | S5.01-S5.05, S5.09 | 21.5 |
| B | 64-70 | LLM client, structured output, agents and recommenders | S5.06-S5.08, S5.10 | 19 |

**If you fall behind, cut:** S5.10, then S5.09.

- [ ] **S5.01 · Document loading and chunking.** `M` Load a folder of text and markdown files. Implement fixed-size character chunking with overlap, then token-based chunking (with `tiktoken` or your S4.08 tokenizer), then structure-aware chunking that respects headings and paragraphs. Keep source file and character offsets as metadata on every chunk. *Test:* for each strategy, stitching chunks back together using their offsets reconstructs each document exactly.

- [ ] **S5.02 · BM25 from scratch.** `M` Tokenize, build an inverted index, compute IDF and BM25 scores with `k1` and `b` parameters. Return top-k chunks for a query. *Test:* using the same tokenizer and parameters, your top-10 rankings match `rank_bm25`'s `BM25Okapi` on ten queries (it floors the IDF of very common terms; replicate that or exclude such terms).

- [ ] **S5.03 · Dense retrieval.** `M` Embed chunks with a sentence-transformer model (one library call is fine), L2-normalize, store as a NumPy matrix on disk, and retrieve top-k by cosine similarity using your own matrix code. *Test:* the same top-k as a FAISS `IndexFlatIP` over the same vectors.

- [ ] **S5.04 · Retrieval evaluation.** `M` Hand-label 30-50 queries with their relevant chunk IDs. Implement recall@k, precision@k, MRR, and nDCG@k. *Test:* each metric matches a hand calculation on two queries. *Deliverable:* a table comparing BM25 and dense retrieval at k = 1, 5, 10.

- [ ] **S5.05 · Hybrid search.** `S` Combine BM25 and dense results with reciprocal rank fusion. *Test:* on your S5.04 labeled set, add a hybrid row to the table and report whether it beats each method alone.

- [ ] **S5.06 · Robust LLM client.** `L` Wrap an LLM API with: retries with exponential backoff and jitter on rate-limit and server errors, a timeout, concurrent batching of many prompts with a concurrency limit, token counting, and a running cost tally. *Test:* a small mock server that randomly returns 429 and 500 errors or stalls; confirm the client retries, backs off, and times out as designed. *Break:* retries and timeouts first, then batching and the cost tally.

- [ ] **S5.07 · Structured output.** `M` Ask the model to return JSON matching a schema; validate with pydantic; on validation failure, re-prompt once with the error message. *Test:* over 50 prompts, report the valid-JSON rate before and after the re-prompt, and log every failure.

- [ ] **S5.08 · Tool-calling agent, no framework.** `L` Implement the loop yourself: send messages plus tool definitions, parse tool calls, execute the Python functions, append results, repeat until a final answer or a max-step limit. Give it two tools: a calculator and document search (your S5.05 hybrid retriever). *Test:* solves five multi-step questions you write in advance; a question designed to loop hits the step limit and stops. *Break:* one tool working end to end first, then the second tool and the step limit.

- [ ] **S5.09 ★ · Approximate nearest-neighbour index.** `L` Build an IVF-style index from your own parts: cluster chunk embeddings with your S2.06 k-means into `nlist` cells, store each chunk in its nearest cell, and at query time search only the `nprobe` closest cells. If your document set has fewer than about 10,000 chunks, add a larger public corpus for this item only, so approximation has something to save. *Test:* with `nprobe = nlist`, results equal your S5.03 exact search; plot recall@10 (against exact search) versus queries per second across several `nprobe` values; compare with FAISS `IndexIVFFlat` at the same settings and note where yours is slower. *Break:* build the index first, then the recall-versus-speed sweep.

- [ ] **S5.10 ★ · Top-N recommendation and ranking metrics.** `M` Extend your S3.11 model into a recommender. Write `recommend(user, n)` that scores every item the user has not rated and returns the top `n`, excluding items seen in training. Evaluate with precision@10, recall@10 and nDCG@10 on each user's held-out item (reuse your S5.04 metric functions; with one held-out item per user, recall@10 is the hit rate), and compare against a most-popular baseline. *Test:* no recommended item was seen in training; nDCG@10 matches a hand calculation for two users; you report whether the factor model beats the popularity baseline, and a comment explains why a model with better RMSE can rank worse.

---

## Sprint 6 · Days 71-84 · Ship a RAG app from your own parts

This sprint assembles your Sprint 5 components into a working question-answering app over your Sprint 5 document set, then measures it against a standard library-built baseline. Do the exam, S6.06, last.

**Load:** 10 items, about 40.5 h (2.9 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 71-77 | Assemble, compare and serve | S6.01-S6.04 | 19 |
| B | 78-84 | Harden, optimize, measure, and the exam | S6.05, S6.07-S6.10, S6.06 | 21.5 |

**If you fall behind, cut:** S6.10, S6.09, S6.08, then S6.07 shrunk to CI only. Keep S6.06 (the exam).

- [ ] **S6.01 · Assemble the pipeline.** `L` Ingest → chunk → index → hybrid retrieve → prompt with citations → answer, using only your Sprint 5 components. If the retrieved context doesn't contain the answer, the app must say so instead of guessing. *Test:* on ten questions, every cited chunk ID contains the supporting text; on three questions your documents can't answer, the app says so. *Break:* ingest, chunk and index first; prompt and answer second.

- [ ] **S6.02 · Library baseline.** `M` Build the same pipeline in under 50 lines with a standard stack (for example LangChain or LlamaIndex with FAISS), using the same documents, embedding model and LLM. Rule 1 doesn't apply here: this is the comparison, not the exercise. *Done when:* both versions answer the same ten questions.

- [ ] **S6.03 · Head-to-head evaluation.** `L` Write a golden set of 30+ question/answer pairs (extending your S5.04 queries is fine). Compare your pipeline against the baseline on recall@k, MRR, nDCG, answer correctness, and latency per query. Score answer correctness with an LLM judge, and check the judge against 20 of your own manual labels. *Deliverable:* one results table, the judge's agreement with your labels, and three sentences on what caused the gaps. *Break:* write the golden set first, then run the comparison and the judge check.

- [ ] **S6.04 · API and failure handling.** `M` Expose `/ingest` and `/query` with FastAPI and pydantic models; log latency and token cost per query. Inject failures (rate limits, timeouts, malformed JSON) and confirm the app returns a clear error instead of crashing. *Test:* a failure-injection script that passes.

- [ ] **S6.05 · Tests and write-up.** `M` pytest suites for every component plus one end-to-end test with a mocked LLM; `pytest` passes from a fresh clone. Then a `sprint6_rag/README.md` explaining every design decision, the evaluation results, where the library beat you and why, and what you'd keep in production.

- [ ] **S6.06 · Final exam.** `S` From a blank file, timed, with no internet or docs: k-means, logistic regression, and scaled dot-product attention with masking, each in under 30 minutes. *Test:* each passes your earlier tests from S2.06, S2.03 and S4.01. Record your times below.

| Exam item           | Time | Passed tests? |
| ------------------- | ---- | ------------- |
| k-means             |      |               |
| Logistic regression |      |               |
| Attention           |      |               |

- [ ] **S6.07 ★ · CI, container and drift check.** `L` Add a GitHub Actions workflow that installs the requirements and runs `pytest` on every push, with the LLM mocked so CI needs no keys. Write a Dockerfile for the S6.04 app and confirm `/query` works from the container. Add a drift check: store reference statistics from your golden set (the distribution of top-1 retrieval similarity and of query length), then compare a new batch of queries against them with a two-sample Kolmogorov-Smirnov test or the population stability index, and flag drift. *Test:* CI is green on a fresh push (put the badge in the README); the container answers a request; the drift check flags a batch of queries deliberately drawn from a different domain and stays quiet on a held-out batch from the same domain. *Break:* CI first, then Docker, then the drift check.

- [ ] **S6.08 ★ · ONNX export and benchmark.** `M` Export a small PyTorch model from this plan (your S3.06 classifier, or the pooling head of an embedding model; a full GPT is optional) to ONNX with a dynamic batch dimension, run it with ONNX Runtime, and compare with PyTorch. *Test:* outputs match PyTorch within 1e-4 for batch sizes 1 and 32; a table of median latency for PyTorch on CPU, ONNX Runtime on CPU, and (optionally) ONNX with int8 dynamic quantization; one paragraph on what ONNX helped with and what it didn't.

- [ ] **S6.09 ★ · int8 quantization.** `M` Implement symmetric per-tensor and per-channel int8 quantization of a linear layer's weights (scale = max|w| / 127), and a quantized forward pass that accumulates in int32 and then dequantizes. On your S4.06 or S4.12 model, quantize every linear layer and measure weight memory, the output error (max and mean absolute), and the change in validation cross-entropy. *Test:* `dequantize(quantize(w))` is within scale/2 of `w` per element; per-channel error is no larger than per-tensor error on a weight matrix with one very large row; quantized weights use about 4× less memory than float32; three sentences on where outliers hurt.

- [ ] **S6.10 ★ · Latency and throughput benchmark.** `M` Benchmark generation for your GPT with and without the KV cache, at batch sizes 1, 4 and 16 and prompt lengths 32 and 256: time to first token, tokens per second, and peak memory. Warm up first, use `torch.inference_mode()`, time with `time.perf_counter`, and report the median and p95 over repeated runs rather than a single run. *Test:* results saved to a CSV and plotted; the KV-cache speedup grows with prompt length; repeating the whole benchmark in a fresh session gives medians within 10%; a paragraph explaining why latency and throughput trade off as batch size grows. Optional: add a row for your S6.09 quantized model.

---

## Sprint 7 · Days 85-96 · Data, classical ML and representation breadth

Sprints 7-9 are breadth. Items are independent of each other, with two exceptions noted in the items (S7.08 feeds S7.09, and S7.10 feeds S9.03). Skip freely if time runs short.

**Load:** 10 items, about 40 h (3.3 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 85-90 | Data, evaluation and linear models | S7.01-S7.05 | 20 |
| B | 91-96 | Iterative fitting and representations | S7.06-S7.10 | 20 |

**If you fall behind, cut:** S7.04, S7.07, S7.03. Keep S7.10 if you plan to do S9.03.

- [ ] **S7.01 · Array fluency drills.** `M` Three short pieces: (a) rewrite five loop-based computations (batched matrix products, pairwise differences, one-hot encoding via indexing, a moving average, a row-wise gather by argmax) using `einsum` and broadcasting; (b) find the top-k of a large array with `np.argpartition` and with a heap, and compare against a full sort; (c) reservoir sampling of k items from a stream of unknown length. *Test:* the `einsum` versions match the loop versions; the top-k results equal the sorted top-k as sets; over 20,000 trials with n=20 and k=5, each item's frequency in the reservoir is within 5% (relative) of k/n.

- [ ] **S7.02 · SQL for ML work.** `L` Load your cleaned S1.08 data into SQLite with `sqlite3`. Write queries for: a left join with deliberately non-matching keys that counts the unmatched rows; a window function (running total and rank within group); a cohort retention table; deduplication with `ROW_NUMBER()`; and a feature table with a 7-day rolling count per user, built without leaking future rows. *Test:* each query's result equals the pandas equivalent from S1.09 on the same data; an assertion that every rolling feature uses only earlier timestamps. *Break:* the first three queries first, then the cohort and rolling-feature queries.

- [ ] **S7.03 · Hyperparameter search and learning curves.** `M` Implement grid and random search over a model of your choice with the S1.04 cross-validation, using a seeded sampler. Then draw a validation curve (score vs model complexity) and a learning curve (score vs training size). *Test:* results are reproducible with a seed; the chosen parameters are evaluated once on a held-out test set that the search never saw; your two-sentence diagnosis of high bias or high variance matches what the curves show.

- [ ] **S7.04 · Linear SVM.** `M` Implement a linear SVM with hinge loss and L2 regularization, trained by SGD with a decaying learning rate (Pegasos-style), and multiclass by one-vs-rest. *Test:* accuracy within 2 percentage points of `LinearSVC` (or `SGDClassifier(loss="hinge")`) on `load_breast_cancer` and `load_iris`; report how many training points violate the margin.

- [ ] **S7.05 · Lasso via coordinate descent.** `M` Implement the soft-thresholding update on standardized features, and produce the coefficient path over a grid of alphas. *Test:* matches scikit-learn's `Lasso` within 1e-4 (its objective is (1/(2n))‖y − Xw‖² + α‖w‖₁); the path plot shows coefficients entering as alpha decreases; one sentence on why L1 gives exact zeros and L2 does not.

- [ ] **S7.06 · Newton's method for logistic regression (IRLS).** `M` Implement Newton/IRLS using the Hessian XᵀWX plus a ridge term, and compare iterations to convergence against gradient descent from S2.03. *Test:* converges in under 15 iterations on standardized `load_breast_cancer`; coefficients match your S2.03 and scikit-learn's `lbfgs` solution within 1e-3 under the same regularization; stays finite on perfectly separable data.

- [ ] **S7.07 · Gaussian mixture model with EM.** `L` Implement EM for a GMM with full or diagonal covariances, using log-sum-exp for stability, initialized from your S2.06 k-means. Regularize covariances so they never become singular. *Test:* the log-likelihood never decreases between iterations; on `make_blobs` it recovers well-separated cluster means; the final log-likelihood is within 1% of scikit-learn's `GaussianMixture` with comparable settings. *Break:* diagonal covariances first, then full.

- [ ] **S7.08 · Word2vec: data and negative sampling.** `M` Word2vec, part 1: the data. On text8 (or a few MB of text), build the vocabulary with a minimum count, subsample frequent words with the word2vec formula, generate (centre, context) pairs with a random window size, and build a unigram^0.75 table for negative sampling. *Test:* on a short hand-made sentence with a fixed window, the pair generator yields exactly the pairs you listed on paper; subsampling never drops words rarer than the threshold and drops frequent words at about the rate the formula gives; the empirical frequencies of 100,000 negative samples match normalized unigram^0.75 within 5% (relative) for the 20 most frequent words.

- [ ] **S7.09 · Word2vec: skip-gram training and evaluation.** `M` Word2vec, part 2: skip-gram with negative sampling. Using your S7.08 pipeline, train word and context embeddings with SGD. *Test:* the loss decreases; the gradient for one (word, context, negatives) example matches PyTorch autograd; nearest neighbours of five words you choose are sensible; analogy accuracy on a sample is above chance (report the number).

- [ ] **S7.10 · InfoNCE contrastive loss.** `M` Implement InfoNCE with in-batch negatives and a temperature, in a numerically stable form (cross-entropy over the similarity matrix). Train a small two-tower model on synthetic paired data in which each input is paired with a noisy copy of itself. *Test:* matches `F.cross_entropy` on the similarity matrix; the loss at random initialization is close to log(batch size); recall@1 on held-out pairs rises during training; a plot of the effect of temperature.

---

## Sprint 8 · Days 97-108 · Deep learning and transformer internals breadth

**Load:** 11 items, about 39.5 h (3.3 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 97-102 | Training mechanics | S8.01-S8.05 | 20 |
| B | 103-108 | Transfer learning and transformer internals | S8.06-S8.11 | 19.5 |

**If you fall behind, cut:** S8.04 (LSTM), S8.06, S8.10.

- [ ] **S8.01 · BatchNorm with a backward pass.** `M` Implement BatchNorm for `(batch, features)` inputs with learnable scale and shift, running mean and variance (with momentum) for eval mode, and a hand-written backward pass. *Test:* forward matches `torch.nn.BatchNorm1d` in train and eval modes, and the running statistics match after several batches; gradient checks against finite differences in `float64` with relative error below 1e-5 for the input, scale and shift.

- [ ] **S8.02 · LayerNorm and dropout with backward passes.** `M` Implement LayerNorm (normalizing over the feature axis) and inverted dropout, each with a hand-written backward pass. *Test:* LayerNorm forward matches `torch.nn.LayerNorm`; gradient checks against finite differences in `float64` with relative error below 1e-5; dropout preserves the expected activation (mean within 2% over many draws), is the identity in eval mode, and its backward pass applies the same mask and scaling as the forward pass.

- [ ] **S8.03 · Initialization and gradient-clipping experiments.** `M` Train a 10-layer MLP with tanh and with ReLU under zero, small-normal, Xavier and He initialization, logging per-layer activation and gradient standard deviations. Then provoke exploding gradients and fix them with clipping by global norm. *Test:* plots show vanishing and exploding behaviour where you expect it; your clipping function matches `torch.nn.utils.clip_grad_norm_`; a short note on which initialization suits which activation.

- [ ] **S8.04 · LSTM cell speed-run.** `L` Implement the forward and backward passes of a single LSTM cell and a sequence unrolled over time. Skip this if you already have an LSTM from scratch that you trust; otherwise time yourself and aim for under 90 minutes. *Test:* forward matches `torch.nn.LSTM` after copying its weights; gradient check passes in `float64`. *Break:* forward pass and its test first, then backward.

- [ ] **S8.05 · Gradient accumulation and mixed precision.** `M` Add gradient accumulation (effective batch = micro-batch × steps) and `torch.autocast` with bf16 (or fp16 with `GradScaler` on a GPU) to your S3.06 loop. *Test:* in `float64` with no dropout, accumulating over 4 micro-batches (loss divided by 4) gives parameter updates equal to one batch four times the size within 1e-5; the mixed-precision loss curve tracks full precision; report memory and speed.

- [ ] **S8.06 · Fine-tune a pretrained ResNet.** `M` On a small image dataset (a 5,000-image subset of CIFAR-10, or Flowers102), replace the classification head and train it with the backbone frozen, then unfreeze the last block with a lower learning rate. Use your S3.06 loop. *Test:* validation accuracy beats training from scratch under the same compute budget; a table comparing freeze-all, partial and full fine-tuning; one note on when you'd stop.

- [ ] **S8.07 · RoPE.** `S` Implement rotary position embeddings applied to queries and keys, and swap them into your attention. *Test:* attention scores depend only on relative position (shifting both positions by the same offset leaves q·k unchanged within 1e-5); a hand-computed 2D rotation case matches; a plot of the rotation frequencies across dimensions.

- [ ] **S8.08 · Grouped-query attention.** `S` Implement GQA, in which `n_heads` query heads share `n_kv_heads` key/value heads, with multi-query attention as the special case `n_kv_heads=1`. *Test:* with `n_kv_heads == n_heads` the output equals your S4.03 MHA with the same weights; the KV-cache memory shrinks by the group factor, and you show the numbers.

- [ ] **S8.09 · Online softmax (the flash-attention idea).** `L` Implement attention in tiles over the key dimension, keeping a running maximum and running sum so the full t × s score matrix is never materialized. *Test:* matches your S4.01 within 1e-5 for sequence lengths 128 and 1,024 with a causal mask; peak memory (via `tracemalloc` or `torch.cuda.max_memory_allocated`) is lower at long sequence lengths. *Break:* the tiled loop without a mask first, then add the causal mask.

- [ ] **S8.10 · Beam search.** `M` Implement beam search with length normalization and an end-of-sequence stop, and compare it with greedy and sampling on your GPT. *Test:* beam width 1 equals greedy; scores are non-increasing in rank; on a hand-built toy model where you know the best sequence, length penalty 0 versus 1 shows the length bias.

- [ ] **S8.11 · Perplexity and evaluation.** `M` Compute token-level cross-entropy and perplexity on a held-out split, handling padding correctly and, for long texts, a sliding window with overlapping context. Evaluate your character GPT, the S4.12 GPT-2, and a quantized version from S6.09. *Test:* GPT-2's perplexity on a small text matches Hugging Face's reference computation within 1%; bits-per-character reported for the character model; a short note on why perplexities from different tokenizers aren't comparable.

---

## Sprint 9 · Days 109-120 · Retrieval, serving and alignment breadth, final exam

**Load:** 10 items, about 38.5 h (3.2 h a day).

| Part | Days | Focus | Order | Hours |
| --- | --- | --- | --- | --- |
| A | 109-114 | Retrieval quality and safety | S9.01-S9.05 | 20.5 |
| B | 115-120 | Serving, tracking, alignment and the exam | S9.06-S9.10 | 18 |

**If you fall behind, cut:** S9.08, S9.04, S9.06. Keep S9.10 (the exam).

- [ ] **S9.01 · TF-IDF and cosine search.** `M` Build a TF-IDF vectorizer (smoothed IDF, L2 normalization, sparse storage with `scipy.sparse`) and a cosine-similarity search over it. *Test:* matches `TfidfVectorizer` with the same settings and tokenizer within 1e-6, and the top-5 results agree on ten queries; a comment on how this ranking differs from your S5.02 BM25. Then add a TF-IDF row to your S5.04 comparison table.

- [ ] **S9.02 · Cross-encoder reranking.** `S` Add a reranking stage over your S5.05 top-50 using a pretrained cross-encoder (a library model is fine). *Test:* add a row to your S5.04 table with nDCG@10 and latency per query; show three example queries where reranking helps and where it hurts.

- [ ] **S9.03 · Contrastive fine-tuning of embeddings.** `L` Fine-tune a small sentence-embedding model on (query, relevant chunk) pairs built from your document set (synthetic queries are fine), using in-batch negatives with your S7.10 loss and hard negatives from BM25. *Test:* held-out recall@5 improves over the off-the-shelf model, with no query overlap between train and evaluation (assert it); the improvement reported with a bootstrap confidence interval from S1.14. *Break:* build the pairs and measure the off-the-shelf baseline first, then fine-tune.

- [ ] **S9.04 · Faithfulness check.** `L` Given an answer and its cited chunks, split the answer into claims and check each against the chunks, using an LLM judge with a strict prompt and a simple string-overlap baseline. *Test:* on 30 answers you labeled (some deliberately unfaithful), report precision and recall of the "unfaithful" flag for both methods, with the judge's agreement against your labels. *Break:* claim splitting and the string-overlap baseline first, then the LLM judge.

- [ ] **S9.05 · Prompt-injection tests.** `M` Add documents to your corpus that contain instructions aimed at the model (override attempts, fake system messages, requests to reveal the prompt). Write a suite of at least 15 such attacks against your own app, then implement two mitigations: delimiting retrieved text and instructing the model to treat it as data, and a post-hoc output filter. *Test:* report the attack success rate before and after each mitigation; state clearly that no mitigation is complete and what each one misses.

- [ ] **S9.06 · Semantic cache.** `M` Cache answers keyed by query embedding, returning a cached answer when cosine similarity exceeds a threshold. *Test:* sweep the threshold and plot hit rate against wrong-answer rate on a set of paraphrased queries and of near-miss queries with different answers; choose a threshold and justify it; report latency and cost saved.

- [ ] **S9.07 · Load test and tail latency.** `M` Load-test your S6.04 API with concurrent users (`httpx` with `asyncio`, or `locust`) at 1, 5, 20 and 50 concurrent requests, first with the LLM mocked at a fixed delay, then with the real one. *Test:* a table of p50, p95 and p99 latency and error rate by concurrency; timing logs that identify the bottleneck (embedding, retrieval or LLM); one change that improves p95, with before and after numbers.

- [ ] **S9.08 · Experiment tracking and versioning.** `M` Add lightweight experiment tracking (MLflow or a JSON-lines log) to your training scripts, recording parameters, metrics, the git commit, a data hash, and the seed. Version datasets by content hash (or with DVC). *Test:* a run can be reproduced from its logged record, with metrics within tolerance; a table comparing five runs.

- [ ] **S9.09 · DPO loss.** `L` Implement the Direct Preference Optimization loss from policy and reference log-probabilities of chosen and rejected completions, with β, computing sequence log-probabilities from your GPT. Train on a toy preference set (for example, prefer completions that end with a particular token). *Test:* when the policy equals the reference, the loss is exactly log 2; the margin between chosen and rejected log-ratios grows during training; implicit-reward accuracy rises on a held-out set; three sentences on how this differs from RLHF with PPO. *Break:* the loss and its log 2 test first, then training.

- [ ] **S9.10 · Final exam II.** `S` From a blank file, timed, with no internet or docs: a gradient boosting regressor, BM25 retrieval over a small hand-made index, and a LoRA linear layer with merge, each in under 30 minutes. *Test:* each passes your earlier tests from S2.11, S5.02 and S4.13. Record your times below.

| Exam item          | Time | Passed tests? |
| ------------------ | ---- | ------------- |
| Gradient boosting  |      |               |
| BM25 retrieval     |      |               |
| LoRA layer + merge |      |               |

---

## License

MIT. Use, adapt and share this plan freely.
