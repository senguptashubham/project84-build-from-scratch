# Project 84: Build ML and AI Engineering From Scratch

A 120-day plan for becoming able to build ML and AI engineering work without an AI assistant, and to explain why it works. It runs two tracks side by side: **code** (103 problems, from NumPy to transformers to a working retrieval-augmented generation app) and **derivations** (ten on-paper derivations). This page puts both in one order, week by week. The project keeps its original name, Project 84, after its first 84 days: Sprints 1-6 (Days 1-84) are the core ladder, and Sprints 7-9 (Days 85-120) extend it.

A third track, theory (modules M0 to M9 with notes, cheat sheets and Q&A), was retired in Nov 2026 to keep the plan lean. It lives on, unchanged, in [archive/](archive/README.md). Book reading (MML, Murphy PML, D2L) now happens outside this repo and is not tracked here.

## Why

AI assistants make it easy to ship code you couldn't write yourself. That is fine for getting work done, but interviews, debugging and research all depend on what you can build from a blank file and what you can explain from first principles. This plan rebuilds both, one small, testable piece at a time: the code items are drawn from what ML and AI engineering interviews commonly ask candidates to implement from scratch, and the derivations cover the reasoning those interviews probe next.

## Who it's for

Anyone comfortable with basic Python (functions, classes, list comprehensions) who has met the core ML ideas (loss functions, gradient descent, train/test splits) and wants to write them without help. If a concept in a code item is new to you, read just enough about it to solve the item.

## What this doesn't cover

Data structures and algorithms. Many companies, especially in India, still open ML interviews with a standard coding round, but it is a separate skill with good tracked resources already. Work through a list like [NeetCode 150](https://neetcode.io/practice) alongside this plan, and budget roughly 10 hours a week for it on top of the hours below. It is deliberately not tracked here.

## The two tracks

| Track | File | IDs | What it holds |
| --- | --- | --- | --- |
| Code | [code/CODE_README.md](code/CODE_README.md) | S1.01 to S9.10 | The 103 problem statements, the rules, setup and the cut line for each sprint |
| Derivations | [derivation/DERIVATION_README.md](derivation/DERIVATION_README.md) | D01 to D10 | Ten derivations to do on paper, each with a blind re-derive check |

The trackers hold the details and the checkboxes. This page holds only the order. When you finish something, tick it once, in its tracker file, and run `python master.py` to copy the tick onto this page.

## Daily rules

1. **One commit a day that moves a sprint problem forward.** Take the next unticked code row from "Next up" and push it a step closer to done. Finishing it takes as many days as it takes.
2. **Read just enough.** Look up the theory you need to solve the problem, from the book or paper of your choice, and no more. No notes are required.
3. **Stuck for 45 minutes? Ask for hints or steps, never code.** First spend 10 minutes on paper, then ask. This is rule 2 in [code/CODE_README.md](code/CODE_README.md#rules).
4. **Optional log.** If something tripped you, put 2 to 3 lines at the top of the solution file under `Looked up:`. A log, not notes, and never required.
5. **Derivations stay on paper.** They are scheduled in the weeks below, right after the code they explain.

## At a glance

| Track | Items | Hours |
| --- | --- | --- |
| Code | 103 | 369.5 |
| Derivations | 10 | 13.5 |
| **Total** | **113** | **383** |

That averages about 21 hours a week over 18 weeks. Weeks run 18-27.5 hours, which leaves room to catch up. The weekly hours are on each week's header below. Each week is one Part of a Project 84 sprint.

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
3. Click an item's title for its details: derivations open their note file, code items open their sprint section in the code tracker. Do the item, tick it in the tracker file, and add a line to `log.md` with your minutes.
4. Commit the work and the tick. The commit hook runs `master.py` and adds the refreshed `README.md` to the same commit; if the trackers disagree with this page, it stops the commit and says why. You can also run `python master.py` or `python master.py --check` by hand.
5. Missing a day is fine. Finishing is what matters. On a bad day, 25 minutes on the current item still counts as a session. Unfinished rows slide into the next week; nothing is dropped.
6. At the end of each week, run `pytest` on that sprint's folder and fix anything that broke. That is the checkpoint. If you have spare time, redo one finished code item from a couple of weeks earlier from a blank file in `code/rewrites/`, in 60 minutes at most. Favour the items the final exams lean on, such as k-means, logistic regression and attention. A redo is not a plan item and has no checkbox.
7. Read a paper that touches the plan? Fold what matters into the specs of the items where it adds real understanding or a test worth having, tagged `(arXiv <id>)`, so you meet it when you get there. A small result may touch two items; a big one may touch ten. Untick a finished item whose spec changes, so it shows up as open work again. Use `PARKED.md` only for ideas outside the plan. A personal Claude Code command, `/research <url>`, kept in the git-ignored `.claude/` folder, automates this: it proposes changes and writes only the ones you pick.

**Calibrate early.** After S1.04-S1.07, look at the *Actual / planned* column in the Progress table below (it is filled from `log.md`). If it is 1.5 or more, treat every week's hours as 1.5 times larger and start using the *If you fall behind* lines from the first sprint instead of waiting.

## How the sequence works

- The two tracks are interleaved inside each week. A derivation comes right after the code it explains. The one exception is D01, which comes before S3.02 because S3.02 asks you to derive that gradient yourself.
- "Next up" lists the next three unticked rows in plan order, whichever track they belong to.
- Rows marked *(optional)* never block "Next up"; skip them when time is short.
- Weeks 1-12 are seven days; weeks 13-18 are six. The plan assumes a full working week. With six days, expect to slide about one row in six into the next week.
- Weekly hours include optional rows.
- When you fall behind, use the *If you fall behind* lines in `code/CODE_README.md`. Cutting a code item does not cut its derivation.

## Rules for the code track

The eight rules live in one place, [code/CODE_README.md](code/CODE_README.md#rules): blank file every time, the 45-minute rule, the rewrite rule, prove it with tests, one commit per item, scope lock, the optional critique and the optional `Looked up:` log. This page does not repeat them, so they cannot drift apart.

Derivations have their own working rules at the top of their tracker file.

## Repo layout

```
README.md                this page (sequence and progress)
master.py                refreshes this page from the two trackers
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
derivation/
    DERIVATION_README.md derivations tracker
    D01-<title>.md ... D10-<title>.md   one note file per derivation (scans or photos can sit beside them)
archive/
    README.md            what was retired and why
    theory/              the retired theory track, kept unchanged
```

Solutions are `.py` modules with a matching `test_*.py`. Use a notebook only where an item asks for plots or a written report, and keep any logic it tests in a `.py` file.

## Progress

| Track | Required rows done | Hours done | Hours in plan | Actual hours logged | Actual / planned |
| --- | --- | --- | --- | --- | --- |
| Code | 5 / 103 | 7.5 | 369.5 | 0 | - |
| Derivations | 0 / 10 | 0 | 13.5 | 0 | - |
| **All** | **5 / 113** | **7.5** | **383** | **0** | **-** |

*Actual / planned* compares logged time with the size tags, for finished rows that have minutes in `log.md`.

## Next up

The next 3 unticked rows in plan order, across both tracks. Optional rows are skipped.

1. **S1.06** · ROC-AUC from scores (Code, Week 1)
2. **S1.07** · Regression metrics (Code, Week 1)
3. **S1.08** · pandas cleaning (Code, Week 1)

## Week 1 · Project 84 days 1-7 · Sprint 1 Part A: Splits, metrics, pandas

**Hours:** 19.5 (Code 19.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☑ | S1.01 | [Pairwise distances without loops](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.02 | [Numerically stable activations](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.03 | [Data splits](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.04 | [k-fold cross-validation](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☑ | S1.05 | [Classification metrics from raw arrays](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.06 | [ROC-AUC from scores](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.07 | [Regression metrics](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.08 | [pandas cleaning](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.09 | [pandas reshaping](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |

## Week 2 · Project 84 days 8-14 · Sprint 1 Part B: Preprocessing, leakage and statistics

**Hours:** 21.5 (Code 20.5 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S1.10 | [Solo EDA report](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.11 | [One-hot and ordinal encoding](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.12 | [Standardization without leakage](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 1.5 |
| ☐ | S1.13 | [Leakage-safe splits ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.14 | [Bootstrap confidence intervals and a permutation test ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.15 | [Maximum likelihood and Bayesian updating ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | S1.16 | [A/B test from scratch ★](code/CODE_README.md#sprint-1--days-1-14--numpy-data-and-statistics-fluency) | 3.5 |
| ☐ | D10 | [Cross-entropy, KL divergence and negative log-likelihood](derivation/D10-cross-entropy-kl-divergence-and-negative-log-likelihood.md) | 1 |

## Week 3 · Project 84 days 15-21 · Sprint 2 Part A: Linear models, kNN, Naive Bayes, k-means

**Hours:** 27.5 (Code 21.5 · Derivations 6)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S2.01 | [Linear regression, closed form](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | D02 | [Least squares as maximum likelihood](derivation/D02-least-squares-as-maximum-likelihood.md) | 1.5 |
| ☐ | D05 | [Ridge and lasso as MAP estimates](derivation/D05-ridge-and-lasso-as-map-estimates.md) | 1.5 |
| ☐ | S2.02 | [Linear regression, gradient descent](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.03 | [Logistic regression](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |
| ☐ | D03 | [Logistic regression: gradient and Hessian](derivation/D03-logistic-regression-gradient-and-hessian.md) | 1.5 |
| ☐ | S2.04 | [k-nearest neighbours](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.05 | [Gaussian Naive Bayes](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 1.5 |
| ☐ | D04 | [Bias-variance decomposition](derivation/D04-bias-variance-decomposition.md) | 1.5 |
| ☐ | S2.06 | [k-means](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |

## Week 4 · Project 84 days 22-28 · Sprint 2 Part B: Trees, boosting, PCA and imbalanced data

**Hours:** 25.5 (Code 24 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S2.07 | [Decision tree splits](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 1.5 |
| ☐ | S2.08 | [CART classifier](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.09 | [Bagging](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | S2.10 | [PCA](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 3.5 |
| ☐ | D06 | [PCA from maximum variance](derivation/D06-pca-from-maximum-variance.md) | 1.5 |
| ☐ | S2.11 | [Gradient boosting ★](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |
| ☐ | S2.12 | [Imbalance and calibration ★](code/CODE_README.md#sprint-2--days-15-28--classical-ml-by-hand) | 6 |

## Week 5 · Project 84 days 29-35 · Sprint 3 Part A: Neural networks from scratch in NumPy

**Hours:** 21.5 (Code 20.5 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S3.01 | [MLP forward pass in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 1.5 |
| ☐ | D01 | [Softmax + cross-entropy gradient](derivation/D01-softmax-cross-entropy-gradient.md) | 1 |
| ☐ | S3.02 | [Backpropagation in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |
| ☐ | S3.03 | [Training a NumPy MLP](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.11 | [Matrix factorization with SGD ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.04 | [Tiny autograd engine](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |

## Week 6 · Project 84 days 36-42 · Sprint 3 Part B: PyTorch workflow, optimizers, convolution, debugging

**Hours:** 22.5 (Code 21.5 · Derivations 1)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S3.05 | [PyTorch data pipeline](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 1.5 |
| ☐ | S3.06 | [PyTorch training loop](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.09 | [Adam and AdamW ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | D08 | [Adam's bias correction](derivation/D08-adams-bias-correction.md) | 1 |
| ☐ | S3.07 | [conv2d in NumPy](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 6 |
| ☐ | S3.08 | [Debugging drill](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |
| ☐ | S3.10 | [Training sanity-check kit ★](code/CODE_README.md#sprint-3--days-29-42--neural-networks) | 3.5 |

## Week 7 · Project 84 days 43-49 · Sprint 4 Part A: Attention, blocks and a character GPT

**Hours:** 22 (Code 20.5 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S4.01 | [Scaled dot-product attention](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | D07 | [Attention backward pass and the square-root-d scale](derivation/D07-attention-backward-pass-and-the-square-root-d-scale.md) | 1.5 |
| ☐ | S4.02 | [Causal and padding masks](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.03 | [Multi-head attention](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.04 | [Positional encoding](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.05 | [Transformer block](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |
| ☐ | S4.10 | [RMSNorm and SwiGLU block ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.06 | [Character-level GPT](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |
| ☐ | S4.07 | [Sampling strategies](code/CODE_README.md#sprint-4--days-43-56--transformers) | 1.5 |

## Week 8 · Project 84 days 50-56 · Sprint 4 Part B: Tokenizer, KV cache, GPT-2 and LoRA

**Hours:** 22.5 (Code 22.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S4.08 | [Minimal byte-level BPE tokenizer](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |
| ☐ | S4.09 | [KV cache](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.11 | [GPT-2 architecture from scratch ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.12 | [Load GPT-2 weights into your own model ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 3.5 |
| ☐ | S4.13 | [LoRA ★](code/CODE_README.md#sprint-4--days-43-56--transformers) | 6 |

## Week 9 · Project 84 days 57-63 · Sprint 5 Part A: Build and measure retrieval

**Hours:** 21.5 (Code 21.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S5.01 | [Document loading and chunking](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.02 | [BM25 from scratch](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.03 | [Dense retrieval](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.04 | [Retrieval evaluation](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.05 | [Hybrid search](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 1.5 |
| ☐ | S5.09 | [Approximate nearest-neighbour index ★](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |

## Week 10 · Project 84 days 64-70 · Sprint 5 Part B: LLM client, structured output, agents, recommenders

**Hours:** 19 (Code 19 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S5.06 | [Robust LLM client](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |
| ☐ | S5.07 | [Structured output](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |
| ☐ | S5.08 | [Tool-calling agent, no framework](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 6 |
| ☐ | S5.10 | [Top-N recommendation and ranking metrics ★](code/CODE_README.md#sprint-5--days-57-70--retrieval-ranking-and-llm-engineering) | 3.5 |

## Week 11 · Project 84 days 71-77 · Sprint 6 Part A: Assemble, compare and serve

**Hours:** 19 (Code 19 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S6.01 | [Assemble the pipeline](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.02 | [Library baseline](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.03 | [Head-to-head evaluation](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.04 | [API and failure handling](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |

## Week 12 · Project 84 days 78-84 · Sprint 6 Part B: Harden, optimize, measure, and the exam

**Hours:** 21.5 (Code 21.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S6.05 | [Tests and write-up](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.07 | [CI, container and drift check ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 6 |
| ☐ | S6.08 | [ONNX export and benchmark ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.09 | [int8 quantization ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.10 | [Latency and throughput benchmark ★](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 3.5 |
| ☐ | S6.06 | [Final exam](code/CODE_README.md#sprint-6--days-71-84--ship-a-rag-app-from-your-own-parts) | 1.5 |

## Week 13 · Project 84 days 85-90 · Sprint 7 Part A: Data, evaluation and linear models

**Hours:** 20 (Code 20 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S7.01 | [Array fluency drills](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.02 | [SQL for ML work](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 6 |
| ☐ | S7.03 | [Hyperparameter search and learning curves](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.04 | [Linear SVM](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.05 | [Lasso via coordinate descent](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |

## Week 14 · Project 84 days 91-96 · Sprint 7 Part B: Iterative fitting and representations

**Hours:** 21.5 (Code 20 · Derivations 1.5)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S7.06 | [Newton's method for logistic regression (IRLS)](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.07 | [Gaussian mixture model with EM](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 6 |
| ☐ | D09 | [EM for a Gaussian mixture, via the ELBO](derivation/D09-em-for-a-gaussian-mixture-via-the-elbo.md) | 1.5 |
| ☐ | S7.08 | [Word2vec: data and negative sampling](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.09 | [Word2vec: skip-gram training and evaluation](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |
| ☐ | S7.10 | [InfoNCE contrastive loss](code/CODE_README.md#sprint-7--days-85-96--data-classical-ml-and-representation-breadth) | 3.5 |

## Week 15 · Project 84 days 97-102 · Sprint 8 Part A: Training mechanics

**Hours:** 20 (Code 20 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S8.01 | [BatchNorm with a backward pass](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.02 | [LayerNorm and dropout with backward passes](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.03 | [Initialization and gradient-clipping experiments](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.04 | [LSTM cell speed-run](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 6 |
| ☐ | S8.05 | [Gradient accumulation and mixed precision](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |

## Week 16 · Project 84 days 103-108 · Sprint 8 Part B: Transfer learning and transformer internals

**Hours:** 19.5 (Code 19.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S8.06 | [Fine-tune a pretrained ResNet](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.07 | [RoPE](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 1.5 |
| ☐ | S8.08 | [Grouped-query attention](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 1.5 |
| ☐ | S8.09 | [Online softmax (the flash-attention idea)](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 6 |
| ☐ | S8.10 | [Beam search](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |
| ☐ | S8.11 | [Perplexity and evaluation](code/CODE_README.md#sprint-8--days-97-108--deep-learning-and-transformer-internals-breadth) | 3.5 |

## Week 17 · Project 84 days 109-114 · Sprint 9 Part A: Retrieval quality and safety

**Hours:** 20.5 (Code 20.5 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S9.01 | [TF-IDF and cosine search](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.02 | [Cross-encoder reranking](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 1.5 |
| ☐ | S9.03 | [Contrastive fine-tuning of embeddings](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | S9.04 | [Faithfulness check](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | S9.05 | [Prompt-injection tests](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |

## Week 18 · Project 84 days 115-120 · Sprint 9 Part B: Serving, tracking, alignment, consolidation and the exam

**Hours:** 18 (Code 18 · Derivations 0)

| Done | ID | Item | Hours |
| --- | --- | --- | --- |
| ☐ | S9.06 | [Semantic cache](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.07 | [Load test and tail latency](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.08 | [Experiment tracking and versioning](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 3.5 |
| ☐ | S9.09 | [DPO loss](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 6 |
| ☐ | S9.10 | [Final exam II](code/CODE_README.md#sprint-9--days-109-120--retrieval-serving-and-alignment-breadth-final-exam) | 1.5 |

---

Generated by `master.py`. Edit the week blocks and the order of rows to change the sequence; everything below the Progress heading is overwritten on refresh.

## License

MIT. Use, adapt and share this plan freely.
