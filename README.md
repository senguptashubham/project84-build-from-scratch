# Project 84: Build ML and AI Engineering From Scratch

A 120-day plan for becoming able to build ML and AI engineering work without an AI assistant, with the maths and theory underneath it. It runs three tracks side by side: **code** (103 problems, from NumPy to transformers to a working retrieval-augmented generation app), **theory** (nine modules plus a consolidation module, each with a cheat sheet and Q&A) and **derivations** (ten on-paper derivations). This page puts all three in one order, week by week. The project keeps its original name, Project 84, after its first 84 days: Sprints 1-6 (Days 1-84) are the core ladder, and Sprints 7-9 (Days 85-120) extend it.

## Why

AI assistants make it easy to ship code you couldn't write yourself. That is fine for getting work done, but interviews, debugging and research all depend on what you can build from a blank file and what you can explain from first principles. This plan rebuilds both, one small, testable piece at a time: the code items are drawn from what ML and AI engineering interviews commonly ask candidates to implement from scratch, and the theory and derivations cover the reasoning those interviews probe next.

## Who it's for

Anyone comfortable with basic Python (functions, classes, list comprehensions) who has met the core ML ideas (loss functions, gradient descent, train/test splits) and wants to write them without help and explain why they work. If a concept in a code item is new to you, the theory track introduces it just ahead of the item that needs it.

## What this doesn't cover

Data structures and algorithms. Many companies, especially in India, still open ML interviews with a standard coding round, but it is a separate skill with good tracked resources already. Work through a list like [NeetCode 150](https://neetcode.io/practice) alongside this plan, and budget roughly 10 hours a week for it on top of the hours below. It is deliberately not tracked here.

## The three tracks

| Track | File | IDs | What it holds |
| --- | --- | --- | --- |
| Code | [code/CODE_README.md](code/CODE_README.md) | S1.01 to S9.10 | The 103 problem statements, the rules, setup and the cut line for each sprint |
| Theory | [theory/THEORY_README.md](theory/THEORY_README.md) | T0.1 to T9.4 | Ten modules (M0 to M9): readings, a cheat sheet and a Q&A set for each |
| Derivations | [derivation/DERIVATION_README.md](derivation/DERIVATION_README.md) | D01 to D10 | Ten derivations to do on paper, each with a blind re-derive check |

The trackers hold the details and the checkboxes. This page holds only the order. When you finish something, tick it once, in its tracker file, and run `python master.py` to copy the tick onto this page.

## At a glance

| Track | Items | Hours |
| --- | --- | --- |
| Code | 103 | 369.5 |
| Theory | 71 (3 optional) | 118 |
| Derivations | 10 | 13.5 |
| **Total** | **184** | **501** |

That averages about 28 hours a week over 18 weeks, but the load is front-heavy on purpose: weeks 1-9 run 29-34 hours, and weeks 10-18 are lighter (20-28 hours), which leaves room to catch up. The weekly hours are on each week's header below. Each week is one Part of a Project 84 sprint.

| Sprint | Days | Theme | Code items | Code hours |
| --- | --- | --- | --- | --- |
| 1 | 1-14 | NumPy, data and statistics fluency | 16 | 40 |
| 2 | 15-28 | Classical ML by hand | 12 | 45.5 |
| 3 | 29-42 | Neural networks | 11 | 42 |
| 4 | 43-56 | Transformers | 13 | 43 |
| 5 | 57-70 | Retrieval, ranking and LLM engineering | 10 | 40.5 |
| 6 | 71-84 | Ship a RAG app from your own parts | 10 | 40.5 |
| 7 | 85-96 | Data, classical ML and representation breadth | 10 | 40 |
| 8 | 97-108 | Deep learning and transformer internals breadth | 11 | 39.5 |
| 9 | 109-120 | Retrieval, serving and alignment breadth, final exam | 10 | 38.5 |

**★** marks a code item added to the original ladder after it was first published; it follows the same rules as every other item. Sprints 7-9 are entirely extension. Hours for code items come from the size tags (`S` about 1.5 h, `M` about 3.5 h, `L` about 6 h) and are planning estimates, not promises.

## How to follow it

1. Fork or copy this repo and set it up once. You need Python 3.10 or newer and git. In a terminal at the repo root:

   ```
   python -m venv .venv
   .venv\Scripts\activate          # Windows (macOS/Linux: source .venv/bin/activate)
   python bootstrap.py --install   # installs requirements.txt and turns on the commit hook
   pytest                          # should pass
   ```

   The commit hook refreshes this page on every commit. Conda works as well as `venv`: create and activate an environment, then run the last two commands. Packages for later sprints are listed in [code/CODE_README.md](code/CODE_README.md#setup); install each when you reach it.
2. Each day, open this page, find your week and take the next unticked rows. Do them in the order shown; the order is the point.
3. Click an item's title for its details: theory topics open their notes file, derivations and code items open their tracker entry. Do the item, tick it in the tracker file, and add a line to `log.md` with your minutes.
4. Commit the work and the tick. The commit hook runs `master.py` and adds the refreshed `README.md` to the same commit; if the trackers disagree with this page, it stops the commit and says why. You can also run `python master.py` or `python master.py --check` by hand.
5. Missing a day is fine. Finishing is what matters. On a bad day, 25 minutes on the current item still counts as a session. Unfinished rows slide into the next week; nothing is dropped.
6. At the end of each week, run `pytest` on that sprint's folder and fix anything that broke. That is the checkpoint. If you have spare time, redo one finished code item from a couple of weeks earlier from a blank file in `code/rewrites/`, in 60 minutes at most. Favour the items the final exams lean on, such as k-means, logistic regression and attention. A redo is not a plan item and has no checkbox.

**Calibrate early.** After S1.04-S1.07, look at the *Actual / planned* column in the Progress table below (it is filled from `log.md`). If it is 1.5 or more, treat every week's hours as 1.5 times larger and start using the *If you fall behind* lines from the first sprint instead of waiting.

## How the sequence works

- Theory is placed just ahead of the first code item that uses it, so you meet an idea before you implement it, and the three tracks are interleaved inside each week. A derivation comes right after the code it explains, and never before the theory it needs. The one exception is D01, which comes before S3.02 because S3.02 asks you to derive that gradient yourself.
- Some topics sit in a later week than the rest of their module (for example T4.5 and T7.4), so they arrive just before the code that uses them. When you do one, add it to that module's cheat sheet.
- "Next up" lists the next three unticked rows in plan order, whichever track they belong to.
- Rows marked *(optional)* never block "Next up"; skip them when time is short.
- Weeks 1-12 are seven days; weeks 13-18 are six. The plan assumes a full working week. With six days, expect to slide about one row in six into the next week.
- Weekly hours include optional rows.
- When you fall behind, use the *If you fall behind* lines in `code/CODE_README.md` and the cut order in `theory/THEORY_README.md`. Cutting a code item does not cut its derivation.

## Rules for the code track

The seven rules live in one place, [code/CODE_README.md](code/CODE_README.md#rules): blank file every time, the 30-minute rule, the rewrite rule, prove it with tests, one commit per item, scope lock, and the optional critique. This page does not repeat them, so they cannot drift apart.

Derivations and theory have their own working rules at the top of their tracker files.

## Repo layout

```
README.md                this page (sequence and progress)
master.py                refreshes this page from the three trackers
log.md                   your minutes per item (read by master.py)
tests/                   tests for master.py
bootstrap.py             one-time setup after cloning (enables the hook)
.githooks/pre-commit     runs master.py on every commit
.vscode/settings.json    shared editor settings
requirements.txt
pyproject.toml           pytest config (import paths: code/ and the repo root)
PARKED.md
code/
    CODE_README.md       code tracker: problem statements, setup, rules
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
theory/
    THEORY_README.md     theory tracker
    notes/               one notes file per theory row, in five area folders
    cheatsheets/         M0.md ... M8.md, ALL.md
    qa/                  M0.md ... M8.md
derivation/
    DERIVATION_README.md derivations tracker
    D01-<title>.md ... D10-<title>.md   one note file per derivation (scans or photos can sit beside them)
```

Solutions are `.py` modules with a matching `test_*.py`. Use a notebook only where an item asks for plots or a written report, and keep any logic it tests in a `.py` file.

## Progress

| Track | Required rows done | Hours done | Hours in plan | Actual hours logged | Actual / planned |
| --- | --- | --- | --- | --- | --- |
| Code | 4 / 103 | 6 | 369.5 | 0 | - |
| Theory | 0 / 68 | 0 | 118 | 0 | - |
| Derivations | 0 / 10 | 0 | 13.5 | 0 | - |
| **All** | **4 / 181** | **6** | **501** | **0** | **-** |

*Actual / planned* compares logged time with the size tags, for finished rows that have minutes in `log.md`.

## Next up

The next 3 unticked rows in plan order, across all three tracks. Optional rows are skipped.

1. **T0.2** · Linear algebra (Theory, Week 1)
2. **T0.1** · Probability (Theory, Week 1)
3. **T1.2** · Bias, variance and validation (Theory, Week 1)

## Week 1 · Project 84 days 1-7 · Sprint 1 Part A: Splits, metrics, pandas

**Hours:** 32.5 (Code 19.5 · Theory 13 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T0.2 | [Linear algebra](theory/notes/01-foundations/T0.2-linear-algebra.md) | 2 |
| ☑ | S1.01 | [Pairwise distances without loops](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.02 | [Numerically stable activations](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | T0.1 | [Probability](theory/notes/01-foundations/T0.1-probability.md) | 2.5 |
| ☐ | T1.2 | [Bias, variance and validation](theory/notes/01-foundations/T1.2-bias-variance-and-validation.md) | 2.5 |
| ☑ | S1.03 | [Data splits](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.04 | [k-fold cross-validation](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | T3.6 | [Evaluation](theory/notes/02-classical-ml/T3.6-evaluation.md) | 1.5 |
| ☐ | S1.05 | [Classification metrics from raw arrays](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.06 | [ROC-AUC from scores](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.07 | [Regression metrics](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.08 | [pandas cleaning](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.09 | [pandas reshaping](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | T0.3 | [Calculus and matrix calculus](theory/notes/01-foundations/T0.3-calculus-and-matrix-calculus.md) | 1.5 |
| ☐ | T0.4 | [Maximum likelihood basics](theory/notes/01-foundations/T0.4-maximum-likelihood-basics.md) | 1 |
| ☐ | T0.S | [Cheat sheet M0](theory/THEORY_README.md#m0-math-you-will-use) | 1 |
| ☐ | T0.Q | [Q&A M0](theory/THEORY_README.md#m0-math-you-will-use) | 1 |

## Week 2 · Project 84 days 8-14 · Sprint 1 Part B: Preprocessing, leakage and statistics

**Hours:** 33.5 (Code 20.5 · Theory 12 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S1.10 | [Solo EDA report](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.11 | [One-hot and ordinal encoding](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.12 | [Standardization without leakage](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.13 | [Leakage-safe splits ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | T1.4 | [Confidence intervals, bootstrap and hypothesis tests](theory/notes/01-foundations/T1.4-confidence-intervals-bootstrap-and-hypothesis-tests.md) | 2 |
| ☐ | S1.14 | [Bootstrap confidence intervals and a permutation test ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | T1.1 | [Maximum likelihood, MAP and priors](theory/notes/01-foundations/T1.1-maximum-likelihood-map-and-priors.md) | 2 |
| ☐ | S1.15 | [Maximum likelihood and Bayesian updating ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.16 | [A/B test from scratch ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | T1.3 | [Information theory](theory/notes/01-foundations/T1.3-information-theory.md) | 2 |
| ☐ | D10 | [Cross-entropy, KL divergence and negative log-likelihood](derivation/D10-cross-entropy-kl-divergence-and-negative-log-likelihood.md) | 1 |
| ☐ | T1.S | [Cheat sheet M1](theory/THEORY_README.md#m1-estimation-inference-bias-variance-information-and-priors) | 1 |
| ☐ | T1.Q | [Q&A M1](theory/THEORY_README.md#m1-estimation-inference-bias-variance-information-and-priors) | 1 |
| ☐ | T2.1 | [Gradient descent and its variants](theory/notes/01-foundations/T2.1-gradient-descent-and-its-variants.md) | 2.5 |
| ☐ | T2.2 | [Regularization](theory/notes/01-foundations/T2.2-regularization.md) | 1.5 |

## Week 3 · Project 84 days 15-21 · Sprint 2 Part A: Linear models, kNN, Naive Bayes, k-means

**Hours:** 33 (Code 21.5 · Theory 5.5 · Derivations 6)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S2.01 | [Linear regression, closed form](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | D02 | [Least squares as maximum likelihood](derivation/D02-least-squares-as-maximum-likelihood.md) | 1.5 |
| ☐ | D05 | [Ridge and lasso as MAP estimates](derivation/D05-ridge-and-lasso-as-map-estimates.md) | 1.5 |
| ☐ | S2.02 | [Linear regression, gradient descent](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | T3.1 | [Logistic regression and generalized linear models](theory/notes/02-classical-ml/T3.1-logistic-regression-and-generalized-linear-models.md) | 2 |
| ☐ | S2.03 | [Logistic regression](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |
| ☐ | D03 | [Logistic regression: gradient and Hessian](derivation/D03-logistic-regression-gradient-and-hessian.md) | 1.5 |
| ☐ | T3.2 | [Naive Bayes and k-nearest neighbours](theory/notes/02-classical-ml/T3.2-naive-bayes-and-k-nearest-neighbours.md) | 1.5 |
| ☐ | S2.04 | [k-nearest neighbours](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.05 | [Gaussian Naive Bayes](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 1.5 |
| ☐ | D04 | [Bias-variance decomposition](derivation/D04-bias-variance-decomposition.md) | 1.5 |
| ☐ | T4.1 | [Clustering](theory/notes/02-classical-ml/T4.1-clustering.md) | 2 |
| ☐ | S2.06 | [k-means](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |

## Week 4 · Project 84 days 22-28 · Sprint 2 Part B: Trees, boosting, PCA and imbalanced data

**Hours:** 33.5 (Code 24 · Theory 8 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T3.3 | [Decision trees, bagging and random forests](theory/notes/02-classical-ml/T3.3-decision-trees-bagging-and-random-forests.md) | 2.5 |
| ☐ | S2.07 | [Decision tree splits](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 1.5 |
| ☐ | S2.08 | [CART classifier](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.09 | [Bagging](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | T4.2 | [PCA and SVD](theory/notes/02-classical-ml/T4.2-pca-and-svd.md) | 2 |
| ☐ | S2.10 | [PCA](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | D06 | [PCA from maximum variance](derivation/D06-pca-from-maximum-variance.md) | 1.5 |
| ☐ | T3.4 | [Boosting](theory/notes/02-classical-ml/T3.4-boosting.md) | 1.5 |
| ☐ | S2.11 | [Gradient boosting ★](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |
| ☐ | S2.12 | [Imbalance and calibration ★](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |
| ☐ | T2.S | [Cheat sheet M2](theory/THEORY_README.md#m2-optimization-and-regularization) | 1 |
| ☐ | T2.Q | [Q&A M2](theory/THEORY_README.md#m2-optimization-and-regularization) | 1 |

## Week 5 · Project 84 days 29-35 · Sprint 3 Part A: Neural networks from scratch in NumPy

**Hours:** 31.5 (Code 20.5 · Theory 10 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T5.1 | [MLPs, activations and backpropagation](theory/notes/03-deep-learning/T5.1-mlps-activations-and-backpropagation.md) | 2.5 |
| ☐ | T5.2 | [Initialization, normalization and regularizers](theory/notes/03-deep-learning/T5.2-initialization-normalization-and-regularizers.md) | 1.5 |
| ☐ | S3.01 | [MLP forward pass in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 1.5 |
| ☐ | D01 | [Softmax + cross-entropy gradient](derivation/D01-softmax-cross-entropy-gradient.md) | 1 |
| ☐ | S3.02 | [Backpropagation in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |
| ☐ | T5.3 | [Optimizers and schedules](theory/notes/03-deep-learning/T5.3-optimizers-and-schedules.md) | 1.5 |
| ☐ | S3.03 | [Training a NumPy MLP](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | T4.4 | [Matrix factorization and embeddings](theory/notes/02-classical-ml/T4.4-matrix-factorization-and-embeddings.md) | 1.5 |
| ☐ | S3.11 | [Matrix factorization with SGD ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.04 | [Tiny autograd engine](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |
| ☐ | T3.S | [Cheat sheet M3](theory/THEORY_README.md#m3-classical-supervised-learning-and-evaluation) | 1.5 |
| ☐ | T3.Q | [Q&A M3](theory/THEORY_README.md#m3-classical-supervised-learning-and-evaluation) | 1.5 |

## Week 6 · Project 84 days 36-42 · Sprint 3 Part B: PyTorch workflow, optimizers, convolution, debugging

**Hours:** 29 (Code 21.5 · Theory 6.5 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S3.05 | [PyTorch data pipeline](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 1.5 |
| ☐ | S3.06 | [PyTorch training loop](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.09 | [Adam and AdamW ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | D08 | [Adam's bias correction](derivation/D08-adams-bias-correction.md) | 1 |
| ☐ | T5.4 | [CNN essentials](theory/notes/03-deep-learning/T5.4-cnn-essentials.md) | 1.5 |
| ☐ | S3.07 | [conv2d in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |
| ☐ | S3.08 | [Debugging drill](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.10 | [Training sanity-check kit ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | T5.S | [Cheat sheet M5](theory/THEORY_README.md#m5-neural-nets-backprop-and-training) | 1.5 |
| ☐ | T5.Q | [Q&A M5](theory/THEORY_README.md#m5-neural-nets-backprop-and-training) | 1.5 |
| ☐ | T4.S | [Cheat sheet M4](theory/THEORY_README.md#m4-unsupervised-learning-pca-em-and-embeddings) | 1 |
| ☐ | T4.Q | [Q&A M4](theory/THEORY_README.md#m4-unsupervised-learning-pca-em-and-embeddings) | 1 |

## Week 7 · Project 84 days 43-49 · Sprint 4 Part A: Attention, blocks and a character GPT

**Hours:** 33 (Code 20.5 · Theory 11 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T6.1 | [Attention](theory/notes/04-transformers-and-llms/T6.1-attention.md) | 2.5 |
| ☐ | S4.01 | [Scaled dot-product attention](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | D07 | [Attention backward pass and the square-root-d scale](derivation/D07-attention-backward-pass-and-the-square-root-d-scale.md) | 1.5 |
| ☐ | S4.02 | [Causal and padding masks](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.03 | [Multi-head attention](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | T6.2 | [The Transformer block](theory/notes/04-transformers-and-llms/T6.2-the-transformer-block.md) | 2.5 |
| ☐ | S4.04 | [Positional encoding](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.05 | [Transformer block](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.10 | [RMSNorm and SwiGLU block ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | T6.4 | [Karpathy: Let's build GPT](theory/notes/04-transformers-and-llms/T6.4-karpathy-lets-build-gpt.md) | 2 |
| ☐ | S4.06 | [Character-level GPT](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |
| ☐ | T7.2 | [Decoding](theory/notes/04-transformers-and-llms/T7.2-decoding.md) | 1 |
| ☐ | S4.07 | [Sampling strategies](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | T6.3 | [Tokenization](theory/notes/04-transformers-and-llms/T6.3-tokenization.md) | 1 |
| ☐ | T6.5 | [Karpathy: Let's build the GPT Tokenizer](theory/notes/04-transformers-and-llms/T6.5-karpathy-lets-build-the-gpt-tokenizer.md) *(optional)* | 2 |

## Week 8 · Project 84 days 50-56 · Sprint 4 Part B: Tokenizer, KV cache, GPT-2 and LoRA

**Hours:** 32.5 (Code 22.5 · Theory 10 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S4.08 | [Minimal byte-level BPE tokenizer](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |
| ☐ | T8.1 | [Inference](theory/notes/05-llm-systems/T8.1-inference.md) | 2.5 |
| ☐ | S4.09 | [KV cache](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | T7.1 | [Pretraining and scaling laws](theory/notes/04-transformers-and-llms/T7.1-pretraining-and-scaling-laws.md) | 2 |
| ☐ | S4.11 | [GPT-2 architecture from scratch ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.12 | [Load GPT-2 weights into your own model ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | T7.3 | [Adaptation](theory/notes/04-transformers-and-llms/T7.3-adaptation.md) | 2.5 |
| ☐ | S4.13 | [LoRA ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |
| ☐ | T6.S | [Cheat sheet M6](theory/THEORY_README.md#m6-attention-and-the-transformer) | 1.5 |
| ☐ | T6.Q | [Q&A M6](theory/THEORY_README.md#m6-attention-and-the-transformer) | 1.5 |

## Week 9 · Project 84 days 57-63 · Sprint 5 Part A: Build and measure retrieval

**Hours:** 29 (Code 21.5 · Theory 7.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T8.2 | [Retrieval-augmented generation](theory/notes/05-llm-systems/T8.2-retrieval-augmented-generation.md) | 2 |
| ☐ | S5.01 | [Document loading and chunking](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | T8.6 | [Retrieval and ranking](theory/notes/05-llm-systems/T8.6-retrieval-and-ranking.md) | 2 |
| ☐ | S5.02 | [BM25 from scratch](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.03 | [Dense retrieval](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.04 | [Retrieval evaluation](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.05 | [Hybrid search](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 1.5 |
| ☐ | S5.09 | [Approximate nearest-neighbour index ★](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |
| ☐ | T7.5 | [Derivation-lite](theory/notes/04-transformers-and-llms/T7.5-derivation-lite.md) | 0.5 |
| ☐ | T7.S | [Cheat sheet M7](theory/THEORY_README.md#m7-llms-pretraining-to-alignment) | 1.5 |
| ☐ | T7.Q | [Q&A M7](theory/THEORY_README.md#m7-llms-pretraining-to-alignment) | 1.5 |

## Week 10 · Project 84 days 64-70 · Sprint 5 Part B: LLM client, structured output, agents, recommenders

**Hours:** 20.5 (Code 19 · Theory 1.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S5.06 | [Robust LLM client](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |
| ☐ | T8.4 | [Agents](theory/notes/05-llm-systems/T8.4-agents.md) | 1.5 |
| ☐ | S5.07 | [Structured output](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.08 | [Tool-calling agent, no framework](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |
| ☐ | S5.10 | [Top-N recommendation and ranking metrics ★](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |

## Week 11 · Project 84 days 71-77 · Sprint 6 Part A: Assemble, compare and serve

**Hours:** 24.5 (Code 19 · Theory 5.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S6.01 | [Assemble the pipeline](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.02 | [Library baseline](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | T8.3 | [Evaluation](theory/notes/05-llm-systems/T8.3-evaluation.md) | 2.5 |
| ☐ | S6.03 | [Head-to-head evaluation](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.04 | [API and failure handling](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | T8.S | [Cheat sheet M8](theory/THEORY_README.md#m8-llm-systems-applications-and-evaluation) | 1.5 |
| ☐ | T8.Q | [Q&A M8](theory/THEORY_README.md#m8-llm-systems-applications-and-evaluation) | 1.5 |

## Week 12 · Project 84 days 78-84 · Sprint 6 Part B: Harden, optimize, measure, and the exam

**Hours:** 25 (Code 21.5 · Theory 3.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S6.05 | [Tests and write-up](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | T8.8 | [Shipping a model: tests, CI, containers and drift](theory/notes/05-llm-systems/T8.8-shipping-a-model-tests-ci-containers-and-drift.md) | 1.5 |
| ☐ | S6.07 | [CI, container and drift check ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.08 | [ONNX export and benchmark ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.09 | [int8 quantization ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.10 | [Latency and throughput benchmark ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.06 | [Final exam](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 1.5 |
| ☐ | T7.6 | [Reference pass](theory/THEORY_README.md#m7-llms-pretraining-to-alignment) *(optional)* | 2 |

## Week 13 · Project 84 days 85-90 · Sprint 7 Part A: Data, evaluation and linear models

**Hours:** 21 (Code 20 · Theory 1 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S7.01 | [Array fluency drills](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.02 | [SQL for ML work](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 6 |
| ☐ | S7.03 | [Hyperparameter search and learning curves](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | T3.5 | [SVM and kernels](theory/notes/02-classical-ml/T3.5-svm-and-kernels.md) | 1 |
| ☐ | S7.04 | [Linear SVM](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.05 | [Lasso via coordinate descent](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |

## Week 14 · Project 84 days 91-96 · Sprint 7 Part B: Iterative fitting and representations

**Hours:** 27.5 (Code 20 · Theory 6 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S7.06 | [Newton's method for logistic regression (IRLS)](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | T4.3 | [EM and the ELBO](theory/notes/02-classical-ml/T4.3-em-and-the-elbo.md) | 2 |
| ☐ | S7.07 | [Gaussian mixture model with EM](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 6 |
| ☐ | D09 | [EM for a Gaussian mixture, via the ELBO](derivation/D09-em-for-a-gaussian-mixture-via-the-elbo.md) | 1.5 |
| ☐ | T4.5 | [Word embeddings and contrastive learning](theory/notes/04-transformers-and-llms/T4.5-word-embeddings-and-contrastive-learning.md) | 2 |
| ☐ | S7.08 | [Word2vec: data and negative sampling](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.09 | [Word2vec: skip-gram training and evaluation](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.10 | [InfoNCE contrastive loss](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | T8.5 | [Diffusion LLMs and trending topics](theory/notes/05-llm-systems/T8.5-diffusion-llms-and-trending-topics.md) *(optional)* | 2 |

## Week 15 · Project 84 days 97-102 · Sprint 8 Part A: Training mechanics

**Hours:** 22.5 (Code 20 · Theory 2.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S8.01 | [BatchNorm with a backward pass](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.02 | [LayerNorm and dropout with backward passes](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | T5.6 | [Training at scale: clipping, accumulation and mixed precision](theory/notes/03-deep-learning/T5.6-training-at-scale-clipping-accumulation-and-mixed-precision.md) | 1 |
| ☐ | S8.03 | [Initialization and gradient-clipping experiments](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | T5.5 | [RNNs and LSTMs](theory/notes/03-deep-learning/T5.5-rnns-and-lstms.md) | 1.5 |
| ☐ | S8.04 | [LSTM cell speed-run](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 6 |
| ☐ | S8.05 | [Gradient accumulation and mixed precision](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |

## Week 16 · Project 84 days 103-108 · Sprint 8 Part B: Transfer learning and transformer internals

**Hours:** 22.5 (Code 19.5 · Theory 3 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S8.06 | [Fine-tune a pretrained ResNet](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | T6.6 | [RoPE, grouped-query attention and flash attention](theory/notes/04-transformers-and-llms/T6.6-rope-grouped-query-attention-and-flash-attention.md) | 2 |
| ☐ | S8.07 | [RoPE](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 1.5 |
| ☐ | S8.08 | [Grouped-query attention](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 1.5 |
| ☐ | S8.09 | [Online softmax (the flash-attention idea)](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 6 |
| ☐ | S8.10 | [Beam search](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | T7.7 | [Perplexity and language-model evaluation](theory/notes/05-llm-systems/T7.7-perplexity-and-language-model-evaluation.md) | 1 |
| ☐ | S8.11 | [Perplexity and evaluation](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |

## Week 17 · Project 84 days 109-114 · Sprint 9 Part A: Retrieval quality and safety

**Hours:** 22 (Code 20.5 · Theory 1.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S9.01 | [TF-IDF and cosine search](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.02 | [Cross-encoder reranking](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 1.5 |
| ☐ | S9.03 | [Contrastive fine-tuning of embeddings](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | T8.7 | [Hallucination, faithfulness and prompt injection](theory/notes/05-llm-systems/T8.7-hallucination-faithfulness-and-prompt-injection.md) | 1.5 |
| ☐ | S9.04 | [Faithfulness check](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | S9.05 | [Prompt-injection tests](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |

## Week 18 · Project 84 days 115-120 · Sprint 9 Part B: Serving, tracking, alignment, consolidation and the exam

**Hours:** 28 (Code 18 · Theory 10 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | T8.9 | [Serving at scale: caching, tail latency and tracking](theory/notes/05-llm-systems/T8.9-serving-at-scale-caching-tail-latency-and-tracking.md) | 1.5 |
| ☐ | S9.06 | [Semantic cache](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.07 | [Load test and tail latency](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.08 | [Experiment tracking and versioning](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | T7.4 | [Alignment](theory/notes/04-transformers-and-llms/T7.4-alignment.md) | 2.5 |
| ☐ | S9.09 | [DPO loss](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | T9.1 | [Master cheat sheet](theory/THEORY_README.md#m9-consolidation) | 2 |
| ☐ | T9.2 | [Question bank](theory/THEORY_README.md#m9-consolidation) | 1.5 |
| ☐ | T9.3 | [Blind pass](theory/THEORY_README.md#m9-consolidation) | 1.5 |
| ☐ | T9.4 | [Gap list](theory/THEORY_README.md#m9-consolidation) | 1 |
| ☐ | S9.10 | [Final exam II](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 1.5 |

---

Generated by `master.py`. Edit the week blocks and the order of rows to change the sequence; everything below the Progress heading is overwritten on refresh.

## License

MIT. Use, adapt and share this plan freely.
