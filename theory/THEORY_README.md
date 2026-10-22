# ML Theory Track: Modules, Checklists and Cheat Sheets

A standalone tracker for learning the theory behind ML/AI engineering well enough to answer "why does this work?" in interviews and to read papers without friction. It runs alongside the Project 84 code tracker (`CODE_README.md`) and the on-paper derivations (`derivation/DERIVATION_README.md`). The repo's `README.md` puts all three in one sequence; this file holds only the theory content.

Tick a row here when it is done. `README.md` shows where it falls in the sequence and copies the tick when you refresh it. Rows marked `opt` are optional: skip them when time is short, and the master will not block on them.

## How the track works

Nine modules, M0 to M8, plus a consolidation module M9. Each module has the same parts:

1. **Topics.** Numbered rows (`T1.1`, `T1.2`, ...) with an hour estimate and the resource to use. A row's description names every concept the code items it prepares will use, so nothing in the code arrives unannounced. Items that are plain tooling or practice (pandas reshaping and SQL, NumPy tricks, PyTorch data loading, loading pretrained weights, library and API plumbing: S1.09, S3.05, S4.12, S6.02, S6.04, S7.01, S7.02) and the two exams (S6.06, S9.10) have no theory row on purpose.
2. **Cheat sheet** (`T1.S`). One page you write from memory at the end of the module, then check against the source.
3. **Q&A** (`T1.Q`). A few interview questions answered aloud, then written as a short answer.
4. **Related code and derivations.** A static link to the Project 84 items and derivations the module feeds. This is not a schedule; `README.md` sets the order.

Hours are my estimates, not measurements. Calibrate after M1 (see "Load").

## Resources (kept deliberately short)

| Role | Resource | Use |
| --- | --- | --- |
| Foundations reference | Murphy, *Probabilistic Machine Learning: An Introduction* (free draft PDF) | Read Ch. 2, 4, 6, 8 properly. Everything else is a lookup. Skip Ch. 14, 22, 23 and skim Part IV. |
| Compact summaries | Stanford CS 229 cheatsheets by Shervine Amidi (6 PDFs) | Use them to **check** your own sheet, not to replace writing it. |
| Interview questions | Chip Huyen, *Introduction to Machine Learning Interviews* (free online) | Your question bank for M1 to M5. |
| Transformers and LLMs | Stanford CME 295 (lecture videos, slides, cheatsheet) | Main lecture track for M6 to M8. Check lecture-1 slides first; if too thin, lean on the video and the cheatsheet. |
| Intuition for the build | Karpathy, *Zero to Hero*: "Let's build GPT" and "Let's build the GPT Tokenizer" | Watch the GPT video before the Project 84 character GPT; rebuild blind afterwards. |
| LLM reference | Xiao and Zhu, *Foundations of Large Language Models* (arXiv 2501.09223) | Look-up when a lecture moves too fast. |
| Applied LLMs | Chip Huyen, *AI Engineering* | M8: evaluation, RAG, finetuning, inference trade-offs. |
| Depth top-ups | Stanford CS224N (2024 videos, 2026 slides) | Only for a topic CME 295 leaves thin. |

Not needed: more than one textbook per topic, CS336 (dropped), a second LLM course.

## Rules

1. **Intuition first.** Before any formula, write one plain-language sentence for what it does and why you would care.
2. **Name the faked step.** For every derivation and every formula on a sheet, write the step people usually skip.
3. **Sheet from memory.** At the end of each module, write the cheat sheet blank-page first. Only then compare with the source and fix gaps in a different colour or marker. For each *method* on the sheet (an algorithm or model, not a math fact), write three short bullets on when it fails or misleads before you summarize how it works. Keep it to three so the sheet still fits on one page. If a row arrives after its module's sheet (for example T4.5, T7.4 or T8.9), add its block to that sheet, and its questions to the module's Q&A, when you do the row.
4. **Answer aloud.** Say each Q&A answer out loud in two minutes or less before writing it.
5. **No copying code.** Theory checks that need code are a few lines of NumPy that you write yourself.
6. **One commit per module.** The sheet and Q&A for that module go in together, with a message such as `T3.S: cheat sheet M3`.

## Repo layout (suggested)

```
theory/
  notes/<area>/T<row>-<title>.md   one reading-notes file per topic row (see "Where the notes go")
  cheatsheets/M0.md ... M8.md, ALL.md
  qa/M0.md ... M8.md
  assets/                          images and diagrams pasted into notes (Obsidian saves them here)
```

(`ALL.md` is the merged four-page sheet from M9. It is not the sequence file `README.md`.)

## Where the notes go

Every theory topic row has exactly one note file, named after its row ID, for example `T1.2-bias-variance-and-validation.md`. The `Notes:` link at the end of each row opens it, and so does the item title on the README. Each note's `description:` field copies the row's text from this file; edit it here, then run `python master.py --sync-notes` to refresh the notes. Files sit in five numbered area folders under `notes/`, and each carries a `tags:` line with its area name (without the number), which Obsidian reads as a tag. Related rows link to each other under "See also". T7.6, the cheat sheet and Q&A rows and the M9 rows have no note file; notes from T7.6 go into the note for the topic it touches.

## Load

About 124.5 hours including 6 hours of optional rows (118.5 hours required). The 13.5 hours of derivations are in `derivation/DERIVATION_README.md`, not here.

| Module | Topic | Required | Optional | Total |
| --- | --- | --- | --- | --- |
| M0 | Math you will use | 10 h | 0 | 10 h |
| M1 | Estimation, inference, bias-variance, information, priors | 10.5 h | 0 | 10.5 h |
| M2 | Optimization and regularization | 7.5 h | 0 | 7.5 h |
| M3 | Classical supervised learning and evaluation | 16 h | 0 | 16 h |
| M4 | Unsupervised learning, PCA, EM and embeddings | 11.5 h | 0 | 11.5 h |
| M5 | Neural nets, backprop and training | 12.5 h | 0 | 12.5 h |
| M6 | Attention and the Transformer | 13 h | 2 h | 15 h |
| M7 | LLMs: pretraining to alignment | 12.5 h | 2 h | 14.5 h |
| M8 | LLM systems, applications and evaluation | 19 h | 2 h | 21 h |
| M9 | Consolidation | 6 h | 0 | 6 h |
| | | **118.5 h** | **6 h** | **124.5 h** |

**Calibrate.** After M1, compare real hours with the table. If you ran 1.5 times over, scale the later modules and start using the cut order early.

**Cut order if behind.** Keep the sheets; cut reading breadth first.
1. Every row marked `opt`.
2. Second-pass Murphy lookups.
3. Do **not** cut M1, M5, M6 or the blind re-derivations. They are where interviews probe.

---

## M0. Math you will use

**Related:** S1.01, S1.02, S2.02, S2.03, S2.05, S7.07; derivation D02 needs T0.4 first.

- [ ] **T0.1 · Probability.** `2.5 h` Random variables, joint, marginal, conditional, Bayes' rule, expectation and variance, independence, covariance, common distributions (Bernoulli, Binomial, Gaussian, Beta, Categorical), the law of large numbers and the central limit theorem. Murphy Ch. 2; Shervine *Probability and Statistics*. Notes: [T0.1-probability](notes/01-foundations/T0.1-probability.md).
- [ ] **T0.2 · Linear algebra.** `2 h` Vectors and matrices as linear maps, dot products, norms and Euclidean distance, matrix multiplication shapes, transpose, inverse, rank, eigenvectors and eigenvalues, positive semi-definite matrices, SVD in one paragraph. Shervine *Algebra and Calculus*. Notes: [T0.2-linear-algebra](notes/01-foundations/T0.2-linear-algebra.md).
- [ ] **T0.3 · Calculus and matrix calculus.** `1.5 h` Gradients, the chain rule, Jacobians, the gradient of a quadratic form, the Hessian, and checking a gradient numerically with finite differences. Notes: [T0.3-calculus-and-matrix-calculus](notes/01-foundations/T0.3-calculus-and-matrix-calculus.md).
- [ ] **T0.4 · Maximum likelihood basics.** `1 h` Likelihood and log-likelihood, the MLE recipe, and the Bernoulli and Gaussian worked examples. The maximum likelihood section of Murphy Ch. 4, read early because derivation D02 needs it. Notes: [T0.4-maximum-likelihood-basics](notes/01-foundations/T0.4-maximum-likelihood-basics.md).
- [ ] **T0.5 · Numerical stability.** `1 h` Floating point, overflow and underflow, catastrophic cancellation, the log-sum-exp trick, stable sigmoid, softmax and log-loss, and why we work in log space. Notes: [T0.5-numerical-stability](notes/01-foundations/T0.5-numerical-stability.md).
- [ ] **T0.S · Cheat sheet M0.** `1 h` Shape rules for matrix products and gradients; the five matrix-calculus identities you use most; expectation and variance rules; Bayes' rule with a worked numeric example; the log-sum-exp trick and the stable softmax.
- [ ] **T0.Q · Q&A M0.** `1 h` Huyen's math section (pick 4 on probability and linear algebra). Self-test with no notes, 20 minutes: gradient of `‖y − Xw‖²` with respect to `w` including shapes; Bayes' rule from the definition of conditional probability; why a covariance matrix is positive semi-definite.

---

## M1. Estimation, inference, bias-variance, information and priors

**Related:** S1.03, S1.04, S1.13 to S1.16, S7.03; derivations D02, D04, D05, D10.

- [ ] **T1.1 · Maximum likelihood, MAP and priors.** `2 h` MLE and MAP, and what a prior means; conjugate priors (Beta-Binomial), the posterior mean and credible intervals; ridge as a Gaussian prior and lasso as a Laplace prior. Murphy Ch. 4. Notes: [T1.1-maximum-likelihood-map-and-priors](notes/01-foundations/T1.1-maximum-likelihood-map-and-priors.md).
- [ ] **T1.2 · Bias, variance and validation.** `2.5 h` Bias, variance and noise; underfitting versus overfitting; train, validation and test splits with seeds for reproducibility; stratified splitting; k-fold cross-validation; time-based and group splits; learning curves and validation curves; grid and random hyperparameter search. Shervine *Tips and Tricks* for the vocabulary. Notes: [T1.2-bias-variance-and-validation](notes/01-foundations/T1.2-bias-variance-and-validation.md).
- [ ] **T1.3 · Information theory.** `2 h` Entropy, cross-entropy, KL divergence, mutual information (briefly), and the identity that links cross-entropy, KL and negative log-likelihood. Murphy Ch. 6. Notes: [T1.3-information-theory](notes/01-foundations/T1.3-information-theory.md).
- [ ] **T1.4 · Confidence intervals, bootstrap and hypothesis tests.** `2 h` Sampling distributions and the standard error; confidence intervals and what they do and do not mean; the bootstrap; hypothesis tests, p-values and the two error types; the permutation test and paired comparisons of two classifiers; the two-proportion z-test; statistical power, effect size, minimum detectable effect and sample size; A/B testing, multiple comparisons, and why peeking inflates false positives. Murphy Ch. 4, selectively; Shervine *Probability and Statistics*. Notes: [T1.4-confidence-intervals-bootstrap-and-hypothesis-tests](notes/01-foundations/T1.4-confidence-intervals-bootstrap-and-hypothesis-tests.md).
- [ ] **T1.S · Cheat sheet M1.** `1 h` The MLE recipe in four lines; the normal equations and when `XᵀX` is invertible; the bias-variance formula and its faked step; the cross-entropy, KL and NLL identity; MLE, MAP and Bayesian estimation in one line each; the bootstrap and hypothesis-test recipes, with the peeking warning.
- [ ] **T1.Q · Q&A M1.** `1 h` Huyen's statistics and ML basics sections. Include "why squared error?", "why log-likelihood?" and "explain bias-variance with an example", "what does a 95% confidence interval mean?" and "why does peeking break an A/B test?".

---

## M2. Optimization and regularization

**Related:** S2.01, S2.02, S3.09, S7.05, S7.06; derivation D05.

- [ ] **T2.1 · Gradient descent and its variants.** `2.5 h` Convexity and why it matters; gradient descent, learning rate, stochastic and mini-batch gradient descent; momentum; conditioning and why scaling features helps; Newton's method and IRLS in one paragraph (the second-order step that Sprint 7 uses). Murphy Ch. 8, selectively. Notes: [T2.1-gradient-descent-and-its-variants](notes/01-foundations/T2.1-gradient-descent-and-its-variants.md).
- [ ] **T2.2 · Regularization.** `1.5 h` L2 and L1 penalties, soft-thresholding, coordinate descent and the lasso path, early stopping, and the Bayesian view of a penalty. Notes: [T2.2-regularization](notes/01-foundations/T2.2-regularization.md).
- [ ] **T2.3 · Linear regression and least squares.** `1.5 h` The model with a bias term; squared loss; the normal equations and the projection view; why solving beats inverting XᵀX (conditioning); multicollinearity; ridge in closed form; R². Notes: [T2.3-linear-regression-and-least-squares](notes/02-classical-ml/T2.3-linear-regression-and-least-squares.md).
- [ ] **T2.S · Cheat sheet M2.** `1 h` The gradient descent update and its convergence picture; why L1 gives sparsity and L2 shrinks; the ridge closed form; the soft-thresholding result; learning-rate failure modes.
- [ ] **T2.Q · Q&A M2.** `1 h` "L1 versus L2", "why does feature scaling help?", "what goes wrong with a large learning rate?"

---

## M3. Classical supervised learning and evaluation

**Related:** S1.05 to S1.13, S2.03 to S2.05, S2.07 to S2.09, S2.11, S2.12, S7.04, S7.06; derivation D03.

- [ ] **T3.1 · Logistic regression and generalized linear models.** `2 h` The model, the log-loss, why it is convex, predicted probabilities versus decision thresholds, regularization, why the weights diverge on separable data, and the link to softmax regression for multiclass problems. Notes: [T3.1-logistic-regression-and-generalized-linear-models](notes/02-classical-ml/T3.1-logistic-regression-and-generalized-linear-models.md).
- [ ] **T3.2 · Naive Bayes and k-nearest neighbours.** `1.5 h` Naive Bayes (priors, the independence assumption, Gaussian likelihoods, log-probabilities, variance smoothing) and k-nearest neighbours (distance metrics, uniform versus distance-weighted voting, choosing k on a validation set); assumptions, failure modes, and how each handles high dimensions. Notes: [T3.2-naive-bayes-and-k-nearest-neighbours](notes/02-classical-ml/T3.2-naive-bayes-and-k-nearest-neighbours.md).
- [ ] **T3.3 · Decision trees, bagging and random forests.** `2.5 h` Impurity (Gini and entropy), greedy splits, stopping rules and pruning, overfitting; bootstrap sampling and majority voting; bagging, random feature subsets and why bagging reduces variance. Notes: [T3.3-decision-trees-bagging-and-random-forests](notes/02-classical-ml/T3.3-decision-trees-bagging-and-random-forests.md).
- [ ] **T3.4 · Boosting.** `1.5 h` The gradient boosting idea: fit the residual (the negative gradient), shrinkage with a learning rate, early stopping on validation loss, the log-loss gradient (y − p); and what XGBoost-style models add. Notes: [T3.4-boosting](notes/02-classical-ml/T3.4-boosting.md).
- [ ] **T3.5 · SVM and kernels.** `1 h` Margin intuition; the hinge loss and its link to regularization; training by SGD with a decaying learning rate; one-vs-rest for multiclass; kernels in one page. Notes: [T3.5-svm-and-kernels](notes/02-classical-ml/T3.5-svm-and-kernels.md).
- [ ] **T3.6 · Evaluation.** `2 h` Accuracy, the confusion matrix, precision, recall and F1 per class, and micro, macro and weighted averaging for multiclass; zero-division when a class is never predicted; ROC curves, thresholds and AUC (including AUC as the probability that a positive outranks a negative, and ties); PR curves; regression metrics (MSE, RMSE, MAE, R², MAPE) and when MAE beats RMSE; choosing a metric for a business problem. Shervine *Supervised Learning*; Huyen for the questions. Notes: [T3.6-evaluation](notes/02-classical-ml/T3.6-evaluation.md).
- [ ] **T3.7 · Class imbalance and calibration.** `1 h` Why accuracy misleads; class weights and resampling (training split only); choosing a decision threshold on validation data; average precision; reliability diagrams and expected calibration error; Platt scaling. Notes: [T3.7-class-imbalance-and-calibration](notes/02-classical-ml/T3.7-class-imbalance-and-calibration.md).
- [ ] **T3.8 · Data preparation: missing data, encoding, scaling and leakage.** `1.5 h` Types of missingness (MCAR, MAR, MNAR) and imputation strategies; duplicates and outliers; what to look for in EDA; one-hot, ordinal and target encoding and unseen categories; standardization and zero-variance columns; fitting every transform on training data only; kinds of leakage (target, train-test, temporal, group). Notes: [T3.8-data-preparation-missing-data-encoding-scaling-and-leakage](notes/02-classical-ml/T3.8-data-preparation-missing-data-encoding-scaling-and-leakage.md).
- [ ] **T3.S · Cheat sheet M3.** `1.5 h` One block per model with the same five lines (assumptions, loss, training, strengths, failure modes); the metrics table with when to use each; the leakage checklist; the imbalance and calibration recipe; the regression metrics; bagging versus boosting in two sentences each.
- [ ] **T3.Q · Q&A M3.** `1.5 h` The largest set in the track. Do 8 to 10 questions, including "random forest versus gradient boosting", "why is accuracy misleading?", "how do you handle imbalance?" and "how would you detect leakage?"

---

## M4. Unsupervised learning, PCA, EM and embeddings

**Related:** S2.06, S2.10, S3.11, S7.07 to S7.10, S9.03; derivations D06, D09.

- [ ] **T4.1 · Clustering.** `2 h` k-means (the objective, k-means++ initialization, restarts, inertia, empty clusters, choosing k) and its failure modes; hierarchical clustering in outline; Gaussian mixture models. Notes: [T4.1-clustering](notes/02-classical-ml/T4.1-clustering.md).
- [ ] **T4.2 · PCA and SVD.** `2 h` PCA (centering, covariance, explained variance ratio, reconstruction), SVD and the link between them; dimensionality reduction for visualization versus for modelling. Shervine *Unsupervised Learning*. Notes: [T4.2-pca-and-svd](notes/02-classical-ml/T4.2-pca-and-svd.md).
- [ ] **T4.3 · EM and the ELBO.** `2 h` EM and the evidence lower bound as a general idea; the E-step and M-step for a Gaussian mixture, log-sum-exp for stability and covariance regularization; why latent-variable models are hard to fit. Murphy's EM chapter as a lookup. Notes: [T4.3-em-and-the-elbo](notes/02-classical-ml/T4.3-em-and-the-elbo.md).
- [ ] **T4.4 · Matrix factorization and embeddings.** `1.5 h` Low-rank factorization of a ratings matrix and its link to SVD; user and item biases; explicit versus implicit feedback; regularized SGD or alternating least squares; RMSE and bias-only baselines; cold start; why a learned vector per item is an embedding. Notes: [T4.4-matrix-factorization-and-embeddings](notes/02-classical-ml/T4.4-matrix-factorization-and-embeddings.md).
- [ ] **T4.5 · Word embeddings and contrastive learning.** `2 h` The distributional idea; word2vec skip-gram with negative sampling, subsampling of frequent words, the context window and the unigram^0.75 noise distribution, and why the full softmax is avoided; contrastive losses, InfoNCE, in-batch and hard negatives, temperature, two-tower models; how the same idea trains sentence embeddings for retrieval. Jurafsky and Martin, *Speech and Language Processing*, the vector-semantics chapter, as a lookup. Notes: [T4.5-word-embeddings-and-contrastive-learning](notes/04-transformers-and-llms/T4.5-word-embeddings-and-contrastive-learning.md).
- [ ] **T4.S · Cheat sheet M4.** `1 h` The k-means objective and algorithm; PCA in four steps and the variance-explained rule; the matrix factorization objective and how it differs from PCA; the EM loop in words with the E-step and M-step formulas (fill these in after derivation D09); when to use which method.
- [ ] **T4.Q · Q&A M4.** `1 h` "Why center before PCA?", "k-means versus GMM", "how do you choose k?"

---

## M5. Neural nets, backprop and training

**Related:** S3.01 to S3.11, S8.01 to S8.06; derivations D01, D08.

- [ ] **T5.1 · MLPs, activations and backpropagation.** `2.5 h` Perceptron to MLP; ReLU, GELU, sigmoid, tanh and why saturation hurts; softmax with cross-entropy; backpropagation as reverse-mode differentiation on a computation graph (the chain rule, topological order); gradient checking; vanishing and exploding gradients. Karpathy's micrograd and makemore videos if backprop does not feel automatic. Notes: [T5.1-mlps-activations-and-backpropagation](notes/03-deep-learning/T5.1-mlps-activations-and-backpropagation.md).
- [ ] **T5.2 · Initialization, normalization and regularizers.** `1.5 h` Xavier and He initialization, batch norm (including running statistics at eval time) versus layer norm, inverted dropout, weight decay, residual connections; how common training bugs look (missing zero_grad, wrong loss input, train versus eval mode); sanity checks (initial loss near log of the class count, overfit one batch, gradient norms, shuffled labels). Notes: [T5.2-initialization-normalization-and-regularizers](notes/03-deep-learning/T5.2-initialization-normalization-and-regularizers.md).
- [ ] **T5.3 · Optimizers and schedules.** `1.5 h` SGD with momentum, RMSProp, Adam (with bias correction), AdamW (decoupled weight decay); learning-rate schedules, early stopping and warmup. Notes: [T5.3-optimizers-and-schedules](notes/03-deep-learning/T5.3-optimizers-and-schedules.md).
- [ ] **T5.4 · CNN essentials.** `1.5 h` Convolution as cross-correlation, stride, padding, channels, im2col, pooling, receptive field. Transfer learning: what to freeze, what to fine-tune, and why the learning rate is smaller. Notes: [T5.4-cnn-essentials](notes/03-deep-learning/T5.4-cnn-essentials.md).
- [ ] **T5.5 · RNNs and LSTMs.** `1.5 h` Recurrence and backpropagation through time; why gradients vanish over long sequences; the LSTM gates (forget, input, output) and the cell state; why this led to attention. Notes: [T5.5-rnns-and-lstms](notes/03-deep-learning/T5.5-rnns-and-lstms.md).
- [ ] **T5.6 · Training at scale: clipping, accumulation and mixed precision.** `1 h` Why gradients explode and how global-norm clipping works; gradient accumulation as a larger effective batch; fp32, fp16 and bf16, loss scaling, and what mixed precision keeps in fp32. Notes: [T5.6-training-at-scale-clipping-accumulation-and-mixed-precision](notes/03-deep-learning/T5.6-training-at-scale-clipping-accumulation-and-mixed-precision.md).
- [ ] **T5.S · Cheat sheet M5.** `1.5 h` Backprop in five lines with the shape rule; an activation table; init rules and why; batch norm versus layer norm; the Adam update with the bias-correction line; a debugging checklist for a network that does not train. Shervine *Deep Learning* to check.
- [ ] **T5.Q · Q&A M5.** `1.5 h` "Why does ReLU help?", "batch norm versus layer norm", "what happens if you initialize all weights to zero?", "explain vanishing gradients", "how do you debug a loss that does not go down?"

---

## M6. Attention and the Transformer

**Related:** S4.01 to S4.08, S4.10, S8.07 to S8.09; derivation D07.

- [ ] **T6.1 · Attention.** `2.5 h` Why attention (the bottleneck of fixed-size encodings); queries, keys and values; scaled dot-product attention and the √d scale; self-attention and multi-head attention; causal and padding masks. CME 295 lecture 1. Notes: [T6.1-attention](notes/04-transformers-and-llms/T6.1-attention.md).
- [ ] **T6.2 · The Transformer block.** `2.5 h` Residuals, layer norm placement (pre-LN), the feed-forward layer with GELU, decoder-only versus encoder models, the tied output head, positional information (sinusoidal, learned, rotary), RMSNorm and gated feed-forward layers (SwiGLU) as the Llama-style variants, parameter and compute counts. CME 295 cheatsheet to check. Notes: [T6.2-the-transformer-block](notes/04-transformers-and-llms/T6.2-the-transformer-block.md).
- [ ] **T6.3 · Tokenization.** `1 h` Byte-pair encoding, byte-level BPE over UTF-8 and its merges, and why subwords exist. Notes: [T6.3-tokenization](notes/04-transformers-and-llms/T6.3-tokenization.md).
- [ ] **T6.4 · Karpathy: Let's build GPT.** `2 h` Watch first, then build your own blind. About 1 h 56 min of video. Notes: [T6.4-karpathy-lets-build-gpt](notes/04-transformers-and-llms/T6.4-karpathy-lets-build-gpt.md).
- [ ] **T6.5 · Karpathy: Let's build the GPT Tokenizer.** `opt` `2 h` About 2 h 13 min of video; useful extra depth on top of T6.3. Notes: [T6.5-karpathy-lets-build-the-gpt-tokenizer](notes/04-transformers-and-llms/T6.5-karpathy-lets-build-the-gpt-tokenizer.md).
- [ ] **T6.6 · RoPE, grouped-query attention and flash attention.** `2 h` Rotary position embeddings and why they encode relative position; multi-query and grouped-query attention and the KV-cache memory saving; the online softmax trick, tiling, and why flash attention is faster without changing the result. Notes: [T6.6-rope-grouped-query-attention-and-flash-attention](notes/04-transformers-and-llms/T6.6-rope-grouped-query-attention-and-flash-attention.md).
- [ ] **T6.S · Cheat sheet M6.** `1.5 h` The attention formula with shapes; the √d argument in two lines; a diagram of one Transformer block; the cost of attention (`O(n²d)` time, `O(n²)` memory) and why it matters; positional encoding options; tokenization in one paragraph.
- [ ] **T6.Q · Q&A M6.** `1.5 h` "Why scale by √d?", "why multi-head?", "encoder versus decoder models", "what is the cost of attention and how is it reduced?", "how does BPE work?"

---

## M7. LLMs: pretraining to alignment

**Related:** S4.07, S4.13, S8.10, S8.11, S9.09.

- [ ] **T7.1 · Pretraining and scaling laws.** `2 h` Next-token prediction, data and its quality, scaling laws and what they claim. CME 295 lecture 2. Notes: [T7.1-pretraining-and-scaling-laws](notes/04-transformers-and-llms/T7.1-pretraining-and-scaling-laws.md).
- [ ] **T7.2 · Decoding.** `1 h` Greedy, beam search with length normalization, temperature, top-k, top-p. Notes: [T7.2-decoding](notes/04-transformers-and-llms/T7.2-decoding.md).
- [ ] **T7.3 · Adaptation.** `2.5 h` Instruction tuning, parameter-efficient finetuning (LoRA: the low-rank update, rank, α scaling, merging adapters), and when to finetune versus prompt. CME 295 lecture 3. Notes: [T7.3-adaptation](notes/04-transformers-and-llms/T7.3-adaptation.md).
- [ ] **T7.4 · Alignment.** `2.5 h` RLHF in outline (preference data, reward model, policy optimization), DPO as the simpler alternative (reference model, β, implicit reward), and what reward hacking means. CME 295 lecture 4. Notes: [T7.4-alignment](notes/04-transformers-and-llms/T7.4-alignment.md).
- [ ] **T7.5 · Derivation-lite.** `0.5 h` Write the next-token loss as a sum of cross-entropies and connect it back to D10. Cap at 30 minutes. (Write the DPO loss from its definition only if the lecture presents it.) Notes: [T7.5-derivation-lite](notes/04-transformers-and-llms/T7.5-derivation-lite.md).
- [ ] **T7.6 · Reference pass.** `opt` `2 h` Xiao and Zhu chapters on pretraining and alignment, or CS224N slides, for any topic that lands thin.
- [ ] **T7.7 · Perplexity and language-model evaluation.** `1 h` Perplexity as exponentiated cross-entropy; bits per token and per character; evaluating long texts with a sliding window; why tokenization changes the number; what perplexity does and does not tell you; compare models only on the same tokenizer and data. Notes: [T7.7-perplexity-and-language-model-evaluation](notes/05-llm-systems/T7.7-perplexity-and-language-model-evaluation.md).
- [ ] **T7.S · Cheat sheet M7.** `1.5 h` The LLM training pipeline as one diagram; decoding methods with the effect of each knob; LoRA in three lines (the low-rank update and why it saves memory); the scaling-law statement with its caveats. Add RLHF versus DPO in two columns after T7.4.
- [ ] **T7.Q · Q&A M7.** `1.5 h` "How does temperature work?", "what is LoRA?", and, after T7.4, T7.7 and T8.7, "RLHF versus DPO", "what does perplexity measure and what are its limits?" and "why do LLMs hallucinate?"

---

## M8. LLM systems, applications and evaluation

**Related:** S4.09, S5.01 to S5.10, S6.01 to S6.03, S6.07 to S6.10, S9.01, S9.02, S9.04 to S9.08, and your LLM-judge calibration capstone.

- [ ] **T8.1 · Inference.** `2.5 h` The KV cache, why decoding is memory-bound, batching, quantization (symmetric int8, per-tensor versus per-channel scales), the latency versus throughput trade-off, and how to measure it (time to first token, tokens per second, p50 and p95, warm-up). CME 295 lecture 5. Notes: [T8.1-inference](notes/05-llm-systems/T8.1-inference.md).
- [ ] **T8.2 · Retrieval-augmented generation.** `2 h` Embeddings, chunking (size, overlap, structure-aware), retrieval quality, citing sources and abstaining when the context lacks the answer, and where RAG fails. Huyen, *AI Engineering*. Notes: [T8.2-retrieval-augmented-generation](notes/05-llm-systems/T8.2-retrieval-augmented-generation.md).
- [ ] **T8.3 · Evaluation.** `2.5 h` Benchmarks and their contamination, human evaluation, golden sets, LLM-as-judge and its biases (position, verbosity), judge-versus-human agreement, and calibration. CME 295 lecture 7; Huyen. Notes: [T8.3-evaluation](notes/05-llm-systems/T8.3-evaluation.md).
- [ ] **T8.4 · Agents.** `1.5 h` Function calling and structured output, tool use, planning loops, and failure modes. CME 295 lecture 6. Notes: [T8.4-agents](notes/05-llm-systems/T8.4-agents.md).
- [ ] **T8.5 · Diffusion LLMs and trending topics.** `opt` `2 h` CME 295 lectures 8 and 9. Notes: [T8.5-diffusion-llms-and-trending-topics](notes/05-llm-systems/T8.5-diffusion-llms-and-trending-topics.md).
- [ ] **T8.6 · Retrieval and ranking.** `2 h` TF-IDF and BM25 (inverted index, IDF, the k1 and b parameters); dense retrieval and cosine similarity; hybrid search and reciprocal rank fusion; rerankers (cross-encoders); ranking metrics (recall@k, precision@k, MRR, nDCG) and when each fits; approximate nearest-neighbour indexes (IVF, HNSW) and the recall-latency trade-off; top-N recommendation and its metrics. Manning, Raghavan and Schütze, *Introduction to Information Retrieval* (free online), as a lookup. Notes: [T8.6-retrieval-and-ranking](notes/05-llm-systems/T8.6-retrieval-and-ranking.md).
- [ ] **T8.7 · Hallucination, faithfulness and prompt injection.** `1.5 h` Why models hallucinate; groundedness and faithfulness checks for RAG; prompt injection (direct and indirect), jailbreaks, data leakage through tools, and the limits of guardrails. Huyen, *AI Engineering*; the OWASP Top 10 for LLM applications. Notes: [T8.7-hallucination-faithfulness-and-prompt-injection](notes/05-llm-systems/T8.7-hallucination-faithfulness-and-prompt-injection.md).
- [ ] **T8.8 · Shipping a model: tests, CI, containers and drift.** `1.5 h` Reproducible environments and containers; what CI should run for an ML project; data drift and concept drift and how to detect them (population stability index, the KS test); monitoring and rollback; exporting to ONNX and what changes at runtime. Notes: [T8.8-shipping-a-model-tests-ci-containers-and-drift](notes/05-llm-systems/T8.8-shipping-a-model-tests-ci-containers-and-drift.md).
- [ ] **T8.9 · Serving at scale: caching, tail latency and tracking.** `1.5 h` Latency percentiles and why p99 matters; load testing and queueing; caching, exact versus semantic, and invalidation; batching and throughput; experiment tracking, data and model versioning, and reproducibility. Notes: [T8.9-serving-at-scale-caching-tail-latency-and-tracking](notes/05-llm-systems/T8.9-serving-at-scale-caching-tail-latency-and-tracking.md).
- [ ] **T8.10 · Calling LLM APIs reliably.** `1 h` Rate limits and transient errors; retries with exponential backoff and jitter; timeouts; concurrency limits; token counting and cost; logging every call. Notes: [T8.10-calling-llm-apis-reliably](notes/05-llm-systems/T8.10-calling-llm-apis-reliably.md).
- [ ] **T8.S · Cheat sheet M8.** `1.5 h` The KV-cache size formula and why it limits context length; a table of RAG failure modes and fixes; the evaluation methods table with biases for each; a quantization summary (what is lost, what is gained); the BM25 formula and the retrieval metrics (recall@k, MRR, nDCG) with when each fits.
- [ ] **T8.Q · Q&A M8.** `1.5 h` "How would you evaluate an LLM application?", "RAG or finetuning?", "what is the KV cache?", "how do you detect and reduce judge bias?" and "BM25 or dense retrieval?"

---

## M9. Consolidation

- [ ] **T9.1 · Master cheat sheet.** `2 h` Merge M0 to M8 into `theory/cheatsheets/ALL.md` of no more than four pages. Keep only what you cannot reconstruct in under a minute. Rewrite, do not paste.
- [ ] **T9.2 · Question bank.** `1.5 h` Collect every Q&A into one file, tag each question by module and confidence (solid / shaky / missing).
- [ ] **T9.3 · Blind pass.** `1.5 h` Re-derive five of the ten derivations from a blank page in 15 minutes each, chosen at random. Anything you miss goes back into the weekly revision loop.
- [ ] **T9.4 · Gap list.** `1 h` Write the topics that still feel shaky and decide which resource to revisit. Add nothing new unless a gap proves it is needed.

---

## Revision system

This is how the sheets become the thing you "read again and again" without raising your cognitive load.

| When | What | Time |
| --- | --- | --- |
| End of module | Write the sheet from memory, then check against the source | 1 to 1.5 h |
| +3 days | Redraw the sheet's key formulas and diagram on a blank page; compare | 15 min |
| +10 days | Answer three module questions aloud without notes | 20 min |
| +30 days | Blind re-derive one derivation from that module | 15 min |
| Weekly (30 min) | Skim the last two sheets, then answer one question per module so far | 30 min |
| Monthly | Read the merged cheat sheet and mark shaky items | 45 min |

These revision passes are habits, not rows in the master, and their time is not counted in the weekly totals.

**What goes on a sheet.** One page, same layout every time, so you can find things:

1. Core idea in one sentence of plain language.
2. Key formulas, with shapes.
3. Faked-step notes (one per derivation or formula).
4. When to use it, and when it fails.
5. Three common confusions.
6. Two interview one-liners.

## Which module feeds which derivation

| Derivation | Prepared in |
| --- | --- |
| D02 Least squares as MLE | T0.4, T1.1 |
| D04 Bias-variance | T1.2 |
| D10 Cross-entropy, KL, NLL | T1.3 |
| D05 Ridge and lasso as MAP | T1.1, T2.2 |
| D03 Logistic gradient and Hessian | T3.1 |
| D06 PCA from maximum variance | T4.2 |
| D01 Softmax and cross-entropy gradient | T5.1 |
| D08 Adam's bias correction | T5.3 |
| D07 Attention backward and √d | T6.1 |
| D09 EM for a Gaussian mixture | T4.3 |

M2, M7 and M8 feed no full derivation by design: M2 is about intuition for optimization, and M7 and M8 are about systems and trade-offs rather than algebra you can check numerically.

## Sources

- [Stanford CME 295 syllabus](https://cme295.stanford.edu/syllabus/)
- [Karpathy, Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- Murphy, *Probabilistic Machine Learning: An Introduction*; Huyen, *Introduction to Machine Learning Interviews* and *AI Engineering*; Xiao and Zhu, arXiv 2501.09223; Shervine Amidi's CS 229 cheatsheets (as recommended earlier in this project)

## License

MIT. Use, adapt and share this plan freely.
