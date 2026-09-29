# Build From Scratch: 84 Days

A 12-week, six-sprint ladder for building ML and AI engineering code without an AI assistant - from NumPy fluency to transformers to a working retrieval-augmented generation (RAG) app. Each item is a problem statement: read it, open a blank file, solve it, test it, commit it.

## Why

AI assistants make it easy to ship code you couldn't write yourself. That's fine for getting work done, but interviews, debugging and research all depend on what you can build from a blank file. This plan rebuilds that ability one small, testable piece at a time. The items are drawn from what ML and AI engineering interviews commonly ask candidates to implement from scratch.

## Who it's for

Anyone comfortable with basic Python (functions, classes, list comprehensions) who has met the core ML ideas (loss functions, gradient descent, train/test splits) and wants to be able to write them without help. This plan tests implementation, not theory; if a concept is new to you, learn it first, then come back to the item.

## What this doesn't cover

Data structures and algorithms. Many companies, especially in India, still open ML interviews with a standard coding round, but it's a separate skill with good tracked resources already. If your target roles need it, work through a list like [NeetCode 150](https://neetcode.io/practice) alongside this plan, rather than squeezing it into the same hour.

## Setup

- **Python 3.10+** and these packages: `numpy scipy pandas matplotlib scikit-learn torch pytest`. Sprint 5 adds `sentence-transformers faiss-cpu rank_bm25 tiktoken pydantic`; Sprint 6 adds `fastapi uvicorn` plus a RAG library of your choice (LangChain or LlamaIndex).
- **Hardware:** a laptop is enough for everything. Sprint 4's GPT trains on a CPU with a small model; a free Google Colab GPU makes it faster.
- **An LLM for Sprints 5–6:** either an API key (most providers offer free or cheap tiers) or a free local model through [Ollama](https://ollama.com). For S5.08, pick a model that supports tool calling.
- **Datasets:** built into scikit-learn (`load_iris`, `load_breast_cancer`, `load_diabetes`, `make_blobs`, `make_classification`) unless an item says otherwise.

## How to follow along

1. Fork or copy this repo.
2. Each sprint is 14 days with 6–12 items. Early items take about an hour; later ones can take several sessions. Spare days are for rewrites, catching up, and items that run long.
3. Tick each box as you commit its solution. Your commit history becomes your progress log.
4. Missing a day is fine. Finishing is what matters.

## Rules

1. **Blank file every time.** Look up APIs in official docs or search engines, but don't open an existing implementation of the item until yours is committed. No code assistant, no inline autocomplete.
2. **30-minute rule.** Stuck for 30 minutes? Ask an AI for *one hint*, never code.
3. **Rewrite rule.** Anything you needed a hint for gets rewritten from a blank file the next day, in `rewrites/`.
4. **Prove it.** Every item ships with a test file run by `pytest`. Where a library equivalent exists (NumPy, scikit-learn, PyTorch), your output must match it within a stated tolerance (default `1e-6`).
5. **One commit per item**, message format: `S1.03: stratified split`.
6. **Scope lock.** If a sprint runs long, cut the decision tree items (S2.07–S2.09) first. Never add items mid-sprint; park ideas in `PARKED.md`.

## Repo layout

```
requirements.txt
sprint1_numpy_data/
    s1_01_pairwise.py
    test_s1_01_pairwise.py
    ...
sprint2_classical_ml/
sprint3_neural_nets/
sprint4_transformers/
sprint5_retrieval_llm/
sprint6_rag/
rewrites/
PARKED.md
```

Solutions are `.py` modules with a matching `test_*.py`. Use a notebook only where an item asks for plots or a written report, and keep any logic it tests in a `.py` file.

---

## Sprint 1 · Days 1–14 · NumPy and data fluency

- [X] **S1.01 · Pairwise distances without loops.** Given `X` of shape `(n, d)` and `Y` of shape `(m, d)`, return an `(n, m)` matrix of Euclidean distances using broadcasting only. Then do it again using the identity ‖x−y‖² = ‖x‖² + ‖y‖² − 2x·y. Clip tiny negatives to zero before the square root. *Test:* both match `scipy.spatial.distance.cdist` to 1e-6 on random data; explain in a comment why the second version is faster and where it can go numerically wrong.

- [ ] **S1.02 · Numerically stable activations.** Write `sigmoid(z)`, `softmax(z, axis)` and `logsumexp(z, axis)` that do not overflow for inputs like `[1000, 1001, 1002]` or `[-1000, 0]`. Softmax must work along any axis of a 2D array. *Test:* no `inf`/`nan` on extreme inputs; softmax sums to 1 along the chosen axis; matches `scipy.special.expit`, `softmax` and `logsumexp`.

- [ ] **S1.03 · Data splits.** Write `train_val_test_split(X, y, ratios=(0.7, 0.15, 0.15), seed)` that shuffles reproducibly. Then write a stratified version that preserves class proportions in each split. *Test:* the same seed gives identical splits; on 1,000 samples with a 90/10 label split, class proportions in every split are within 1 percentage point of the original.

- [ ] **S1.04 · k-fold cross-validation.** Write a generator `kfold(n, k, shuffle, seed)` yielding `(train_idx, val_idx)` pairs. Every index must appear in exactly one validation fold. Then write `cross_val_score(model_fn, X, y, k, metric)` that trains a fresh model per fold and returns the per-fold scores. *Test:* fold union equals all indices; folds are disjoint; sizes differ by at most one; `cross_val_score` runs with a trivial mean-predicting model.

- [ ] **S1.05 · Classification metrics from raw arrays.** Given `y_true` and `y_pred` (binary and multiclass), compute accuracy, confusion matrix, precision, recall, F1, and macro/micro averages. When a class is never predicted, return 0 for its precision. *Test:* matches `sklearn.metrics` (with `zero_division=0`) on five random cases, including one where a class has no predictions.

- [ ] **S1.06 · ROC-AUC from scores.** Given binary `y_true` and continuous `scores`, compute the ROC curve (FPR, TPR at every threshold) and AUC by the trapezoidal rule. Then compute AUC a second way: the probability a random positive outranks a random negative, counting ties as half. *Test:* both methods agree with each other and with `roc_auc_score`, including on scores with ties.

- [ ] **S1.07 · Regression metrics.** Implement MSE, RMSE, MAE, R², and MAPE (guard against zero targets). *Test:* matches `sklearn.metrics` on targets with no zeros; MAPE returns a finite value when a target is zero. Write one sentence on when MAE is a better choice than RMSE.

- [ ] **S1.08 · pandas cleaning.** Take a messy public CSV with mixed types and dates, such as an export from a city or government open-data portal. Without AI: fix dtypes, parse dates, strip whitespace in strings, standardize categories with inconsistent spelling, handle missing values with a justified strategy per column, remove duplicates. *Deliverable:* a script that produces a clean file plus a log of every change and how many rows it affected.

- [ ] **S1.09 · pandas reshaping.** On the cleaned data: a groupby with multiple aggregations and named output columns; a merge with a second small lookup table you build, in which some keys deliberately don't match, and which you detect and explain; a pivot table and its inverse `melt`; a rolling or cumulative computation within groups. *Test:* each operation cross-checked by a manual count on a small slice.

- [ ] **S1.10 · Solo EDA report.** On a dataset you have never used, produce a notebook answering: shape and types, missing patterns, target distribution, three strongest univariate relationships with the target, one leakage risk, one surprising finding. Plots via matplotlib only. *Done when:* a stranger could read it and decide on a modeling approach.

- [ ] **S1.11 · One-hot and ordinal encoding.** Implement one-hot encoding that handles categories unseen at fit time (ignore them, or map them to an "other" column), and ordinal encoding with an explicit order. Fit on train, transform on test. *Test:* column count and order are the same for train and test, including when test contains an unseen category.

- [ ] **S1.12 · Standardization without leakage.** Implement a `StandardScaler`-like class with `fit`, `transform`, `inverse_transform`. Guard against zero-variance columns. *Test:* matches scikit-learn's `StandardScaler`; demonstrate in a comment why fitting on the full dataset before splitting is leakage.

---

## Sprint 2 · Days 15–28 · Classical ML by hand

- [ ] **S2.01 · Linear regression, closed form.** Implement fit via the normal equation with a bias term. Then fit via `np.linalg.lstsq` and explain in a comment why solving is preferred over inverting `XᵀX`. Add ridge (L2) regularization without penalizing the bias. *Test:* on `load_diabetes`, coefficients match `LinearRegression`, and `Ridge` with the same `alpha` (note that scikit-learn's ridge penalizes the sum of squared errors, not the mean).

- [ ] **S2.02 · Linear regression, gradient descent.** Derive the MSE gradient by hand in a notebook markdown cell, then implement batch GD and mini-batch SGD with a learning-rate parameter. Plot loss vs iteration with and without feature scaling. *Test:* batch GD converges to the S2.01 solution within 1e-3; the plot shows scaling's effect.

- [ ] **S2.03 · Logistic regression.** Implement binary logistic regression trained by gradient descent with a numerically stable log-loss (work from logits, not probabilities), L2 regularization, and separate `predict_proba` and `predict(threshold)` methods. Then extend to multiclass via softmax regression. *Test:* accuracy within 1 percentage point of scikit-learn's `LogisticRegression` on `load_breast_cancer` (binary) and `load_iris` (multiclass). To compare fairly, if your loss is mean log-loss plus (λ/2)‖w‖², set `C = 1/(n·λ)`. No `nan` when classes are perfectly separable.

- [ ] **S2.04 · k-nearest neighbours.** Vectorized kNN classifier and regressor using your S1.01 distance function. Support uniform and distance-weighted voting, and break ties deterministically. *Test:* predictions match `KNeighborsClassifier` with the same `k` and `weights` on data without distance ties; report accuracy vs k on a validation set and pick k.

- [ ] **S2.05 · Gaussian Naive Bayes.** Fit per-class priors, means and variances; predict using log-probabilities to avoid underflow; add variance smoothing. *Test:* predictions match `GaussianNB` (implement its `var_smoothing`, which adds a fraction of the largest feature variance); explain in one line why working in log space matters.

- [ ] **S2.06 · k-means.** Implement k-means with random init and k-means++ init. Stop when assignments no longer change or after `max_iter`. Handle an empty cluster by reseeding it from the farthest point. Return labels, centroids, and inertia. Run several restarts and keep the best. *Test:* on well-separated `make_blobs` data, recovers the true clusters; inertia is within 1% of scikit-learn's `KMeans`.

- [ ] **S2.07 · Decision tree splits.** Write `gini(y)`, `entropy(y)`, and `best_split(X, y)` that searches every feature and threshold and returns the one with maximum impurity reduction. *Test:* on a hand-built 8-row dataset, your chosen split matches the one you compute on paper.

- [ ] **S2.08 · CART classifier.** Build a recursive decision tree using S2.07 with `max_depth` and `min_samples_split` stopping rules, and a `predict` that walks the tree. *Test:* training accuracy reaches 100% with no depth limit on `load_iris`; test accuracy on `load_breast_cancer` is within 3 percentage points of `DecisionTreeClassifier` at the same depth.

- [ ] **S2.09 · Bagging.** Wrap your tree in a bootstrap ensemble with majority voting and optional random feature subsets per split (a small random forest). *Test:* across 10 seeds, the ensemble's test accuracy has a higher mean and lower variance than a single tree's.

- [ ] **S2.10 · PCA.** Implement PCA via SVD of centered data. Return components, explained variance ratio, `transform`, and `inverse_transform`. *Test:* matches scikit-learn's `PCA` up to sign flips; reconstruction error decreases as components increase.

---

## Sprint 3 · Days 29–42 · Neural networks

- [ ] **S3.01 · MLP forward pass in NumPy.** A two-layer network (input → hidden with ReLU → output with softmax) with He initialization. Write the forward pass for a batch and return cached intermediates. *Test:* output shapes are correct; rows sum to 1.

- [ ] **S3.02 · Backpropagation in NumPy.** Derive gradients for cross-entropy + softmax, the linear layers, and ReLU. Implement the backward pass. *Test:* gradient check with finite differences in `float64`, with relative error below 1e-5 on every parameter.

- [ ] **S3.03 · Training a NumPy MLP.** Train S3.01/S3.02 with mini-batch SGD on MNIST (via `torchvision` or `sklearn.datasets.fetch_openml`). Add momentum, and L2 or dropout. *Test:* test accuracy above 95%; learning curves saved as an image.

- [ ] **S3.04 · Tiny autograd engine.** A scalar `Value` class supporting `+`, `*`, `**`, `tanh`, `relu` that builds a graph and runs backpropagation via topological sort. Train a small MLP with it. This is the idea behind Andrej Karpathy's micrograd; build yours before looking at it. *Test:* gradients match PyTorch on the same small expression.

- [ ] **S3.05 · PyTorch data pipeline.** Write a custom `Dataset` for a CSV or image folder, with transforms, and a `DataLoader` with shuffling and batching. *Test:* iterating one epoch returns every sample exactly once.

- [ ] **S3.06 · PyTorch training loop.** From a blank file: model, optimizer, loss, train loop, eval loop under `torch.no_grad()` with `model.eval()`, device handling, a learning-rate scheduler, early stopping on validation loss, and checkpoint save/load. Save the model, optimizer, scheduler and random-number-generator states. *Test:* on CPU, stopping and resuming training gives final metrics within 1e-4 of an uninterrupted run with the same seed.

- [ ] **S3.07 · conv2d in NumPy.** Implement a 2D convolution forward pass supporting stride, padding, multiple input and output channels, and batches. Like PyTorch, compute cross-correlation (no kernel flip). Do it with loops first, then with an im2col approach. *Test:* both match `torch.nn.functional.conv2d`; time both versions.

- [ ] **S3.08 · Debugging drill.** Write a script that takes your working S3.06 loop and randomly injects one bug without telling you which: missing `zero_grad`, softmax applied before `CrossEntropyLoss`, missing `model.eval()` with dropout, a transposed tensor that silently broadcasts, a learning rate 100× too high, labels shuffled independently of inputs. (A friend can inject them instead.) Diagnose each from symptoms alone. *Deliverable:* `DEBUGGING.md` with symptom → cause → fix for each.

---

## Sprint 4 · Days 43–56 · Transformers

- [ ] **S4.01 · Scaled dot-product attention.** Given `Q (b, t, d)`, `K (b, s, d)`, `V (b, s, d)` and an optional boolean mask where `True` means "may attend" (PyTorch's convention), return outputs and attention weights. Apply the mask before a stable softmax; scale by √d. *Test:* outputs match `torch.nn.functional.scaled_dot_product_attention`; masked positions receive zero weight.

- [ ] **S4.02 · Causal and padding masks.** Build a causal mask for sequence length `t`, and a padding mask from a batch of variable-length sequences. Combine them correctly. *Test:* a token never attends to future or padded positions.

- [ ] **S4.03 · Multi-head attention.** Implement MHA with projection layers, splitting into heads, attention, concatenation, and output projection, in PyTorch. *Test:* outputs match `nn.MultiheadAttention(batch_first=True)` after copying its `in_proj_weight`, `in_proj_bias` and `out_proj` weights into yours.

- [ ] **S4.04 · Positional encoding.** Implement sinusoidal encodings and learned position embeddings. *Test:* sinusoidal values match the formula in "Attention Is All You Need" at a few hand-computed positions; plot the encoding matrix and the dot product between positions as distance grows.

- [ ] **S4.05 · Transformer block.** Pre-LayerNorm block: LN → MHA → residual → LN → MLP (GELU) → residual, with dropout. *Test:* output shape equals input shape; after one backward pass, every parameter has a non-zero gradient.

- [ ] **S4.06 · Character-level GPT.** Stack blocks into a decoder-only model with token and position embeddings and a tied output head. Train a small model (around 1M parameters) on a public-domain book, for example from Project Gutenberg. *Test:* validation loss falls well below the unigram baseline (the loss from predicting each character's overall frequency); samples look locally plausible.

- [ ] **S4.07 · Sampling strategies.** Implement greedy, temperature, top-k, and top-p (nucleus) sampling. *Test:* at a very low temperature (e.g. 1e-4) and with top-k at k=1, output matches greedy; top-p never samples a token outside the nucleus.

- [ ] **S4.08 · Minimal byte-level BPE tokenizer.** Train byte-pair encoding on a text's UTF-8 bytes: count adjacent pairs, merge the most frequent, repeat for N merges. Implement `encode` and `decode`. *Test:* `decode(encode(text)) == text` on unseen text, including non-ASCII characters such as Bengali or emoji.

- [ ] **S4.09 · KV cache.** Add a key/value cache to your GPT so generation reuses past keys and values instead of recomputing them. *Test:* generated tokens are identical with and without the cache under greedy decoding; measure the speedup at length 256.

---

## Sprint 5 · Days 57–70 · Retrieval and LLM engineering

Pick one document set at the start of this sprint (your notes, a project's documentation, or a public-domain book split into files), roughly 50–500 pages. You'll use it for every item here and in Sprint 6.

- [ ] **S5.01 · Document loading and chunking.** Load a folder of text and markdown files. Implement fixed-size character chunking with overlap, then token-based chunking (with `tiktoken` or your S4.08 tokenizer), then structure-aware chunking that respects headings and paragraphs. Keep source file and character offsets as metadata on every chunk. *Test:* for each strategy, stitching chunks back together using their offsets reconstructs each document exactly.

- [ ] **S5.02 · BM25 from scratch.** Tokenize, build an inverted index, compute IDF and BM25 scores with `k1` and `b` parameters. Return top-k chunks for a query. *Test:* using the same tokenizer and parameters, your top-10 rankings match `rank_bm25`'s `BM25Okapi` on ten queries (it floors the IDF of very common terms; replicate that or exclude such terms).

- [ ] **S5.03 · Dense retrieval.** Embed chunks with a sentence-transformer model (one library call is fine), L2-normalize, store as a NumPy matrix on disk, and retrieve top-k by cosine similarity using your own matrix code. *Test:* the same top-k as a FAISS `IndexFlatIP` over the same vectors.

- [ ] **S5.04 · Retrieval evaluation.** Hand-label 30–50 queries with their relevant chunk IDs. Implement recall@k, precision@k, MRR, and nDCG@k. *Test:* each metric matches a hand calculation on two queries. *Deliverable:* a table comparing BM25 and dense retrieval at k = 1, 5, 10.

- [ ] **S5.05 · Hybrid search.** Combine BM25 and dense results with reciprocal rank fusion. *Test:* on your S5.04 labeled set, add a hybrid row to the table and report whether it beats each method alone.

- [ ] **S5.06 · Robust LLM client.** Wrap an LLM API with: retries with exponential backoff and jitter on rate-limit and server errors, a timeout, concurrent batching of many prompts with a concurrency limit, token counting, and a running cost tally. *Test:* a small mock server that randomly returns 429 and 500 errors or stalls; confirm the client retries, backs off, and times out as designed.

- [ ] **S5.07 · Structured output.** Ask the model to return JSON matching a schema; validate with pydantic; on validation failure, re-prompt once with the error message. *Test:* over 50 prompts, report the valid-JSON rate before and after the re-prompt, and log every failure.

- [ ] **S5.08 · Tool-calling agent, no framework.** Implement the loop yourself: send messages plus tool definitions, parse tool calls, execute the Python functions, append results, repeat until a final answer or a max-step limit. Give it two tools: a calculator and document search (your S5.05 hybrid retriever). *Test:* solves five multi-step questions you write in advance; a question designed to loop hits the step limit and stops.

---

## Sprint 6 · Days 71–84 · Ship a RAG app from your own parts

This sprint assembles your Sprint 5 components into a working question-answering app over your Sprint 5 document set, then measures it against a standard library-built baseline.

- [ ] **S6.01 · Assemble the pipeline.** Ingest → chunk → index → hybrid retrieve → prompt with citations → answer, using only your Sprint 5 components. If the retrieved context doesn't contain the answer, the app must say so instead of guessing. *Test:* on ten questions, every cited chunk ID contains the supporting text; on three questions your documents can't answer, the app says so.

- [ ] **S6.02 · Library baseline.** Build the same pipeline in under 50 lines with a standard stack (for example LangChain or LlamaIndex with FAISS), using the same documents, embedding model and LLM. Rule 1 doesn't apply here: this is the comparison, not the exercise. *Done when:* both versions answer the same ten questions.

- [ ] **S6.03 · Head-to-head evaluation.** Write a golden set of 30+ question/answer pairs (extending your S5.04 queries is fine). Compare your pipeline against the baseline on recall@k, MRR, nDCG, answer correctness, and latency per query. Score answer correctness with an LLM judge, and check the judge against 20 of your own manual labels. *Deliverable:* one results table, the judge's agreement with your labels, and three sentences on what caused the gaps.

- [ ] **S6.04 · API and failure handling.** Expose `/ingest` and `/query` with FastAPI and pydantic models; log latency and token cost per query. Inject failures (rate limits, timeouts, malformed JSON) and confirm the app returns a clear error instead of crashing. *Test:* a failure-injection script that passes.

- [ ] **S6.05 · Tests and write-up.** pytest suites for every component plus one end-to-end test with a mocked LLM; `pytest` passes from a fresh clone. Then a `sprint6_rag/README.md` explaining every design decision, the evaluation results, where the library beat you and why, and what you'd keep in production.

- [ ] **S6.06 · Final exam.** From a blank file, timed, with no internet or docs: k-means, logistic regression, and scaled dot-product attention with masking, each in under 30 minutes. *Test:* each passes your earlier tests from S2.06, S2.03 and S4.01. Record your times below.

| Exam item | Time | Passed tests? |
|---|---|---|
| k-means | | |
| Logistic regression | | |
| Attention | | |

---

## License

MIT. Use, adapt and share this plan freely.
