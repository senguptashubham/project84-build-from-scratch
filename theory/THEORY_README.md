# ML Theory Track: Modules, Checklists and Cheat Sheets

A standalone tracker for learning the theory behind ML/AI engineering well enough to answer "why does this work?" in interviews and to read papers without friction. It runs alongside the Project 84 code tracker (`CODE_README.md`) and the on-paper derivations (`derivation/DERIVATION_README.md`). The repo's `README.md` puts all three in one sequence; this file holds only the theory content.

Tick a row here when it is done. `README.md` shows where it falls in the sequence and copies the tick when you refresh it. Rows marked `opt` are optional: skip them when time is short, and the master will not block on them.

## How the track works

Nine modules, M0 to M8, plus a consolidation module M9. Each module has the same parts:

1. **Topics.** Numbered rows (`T1.1`, `T1.2`, ...) with an hour estimate and the resource to use.
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
3. **Sheet from memory.** At the end of each module, write the cheat sheet blank-page first. Only then compare with the source and fix gaps in a different colour or marker.
4. **Answer aloud.** Say each Q&A answer out loud in two minutes or less before writing it.
5. **No copying code.** Theory checks that need code are a few lines of NumPy that you write yourself.
6. **One commit per module.** The sheet and Q&A for that module go in together, with a message such as `T3.S: cheat sheet M3`.

## Repo layout (suggested)

```
theory/
  notes/M0-math.md ... M8-llm-systems-evaluation.md (reading notes, one per module)
  cheatsheets/M0.md ... M8.md, ALL.md
  qa/M0.md ... M8.md
  log.md
```

(`ALL.md` is the merged four-page sheet from M9. It is not the sequence file `README.md`.)

## Load

About 101 hours including 9.5 hours of optional rows (91.5 hours required). The 13.5 hours of derivations are in `derivation/DERIVATION_README.md`, not here.

| Module | Topic | Required | Optional | Total |
| --- | --- | --- | --- | --- |
| M0 | Math you will use | 9 h | 0 | 9 h |
| M1 | Estimation, bias-variance, information, priors | 8 h | 0 | 8 h |
| M2 | Optimization and regularization | 6 h | 0 | 6 h |
| M3 | Classical supervised learning and evaluation | 12 h | 1 h | 13 h |
| M4 | Unsupervised learning, PCA and EM | 8 h | 0 | 8 h |
| M5 | Neural nets, backprop and training | 10 h | 1 h | 11 h |
| M6 | Attention and the Transformer | 11 h | 2 h | 13 h |
| M7 | LLMs: pretraining to alignment | 11.5 h | 2 h | 13.5 h |
| M8 | LLM systems, applications and evaluation | 10 h | 3.5 h | 13.5 h |
| M9 | Consolidation | 6 h | 0 | 6 h |
| | | **91.5 h** | **9.5 h** | **101 h** |

**Calibrate.** After M1, compare real hours with the table. If you ran 1.5 times over, scale the later modules and start using the cut order early.

**Cut order if behind.** Keep the sheets; cut reading breadth first.
1. Every row marked `opt`.
2. Second-pass Murphy lookups.
3. Do **not** cut M1, M5, M6 or the blind re-derivations. They are where interviews probe.

---

## M0. Math you will use

**Related:** Project 84 Sprint 1; derivation D02 needs T0.4 first.

- [ ] **T0.1 · Probability.** `2.5 h` Random variables, joint, marginal, conditional, Bayes' rule, expectation and variance, independence, covariance, common distributions (Bernoulli, Binomial, Gaussian, Categorical). Murphy Ch. 2; Shervine *Probability and Statistics*.
- [ ] **T0.2 · Linear algebra.** `2 h` Vectors and matrices as linear maps, matrix multiplication shapes, transpose, inverse, rank, eigenvectors and eigenvalues, positive semi-definite matrices, SVD in one paragraph. Shervine *Algebra and Calculus*.
- [ ] **T0.3 · Calculus and matrix calculus.** `1.5 h` Gradients, the chain rule, Jacobians, the gradient of a quadratic form, the Hessian.
- [ ] **T0.4 · Maximum likelihood basics.** `1 h` The maximum likelihood section of Murphy Ch. 4, read early because derivation D02 needs it.
- [ ] **T0.S · Cheat sheet M0.** `1 h` Shape rules for matrix products and gradients; the five matrix-calculus identities you use most; expectation and variance rules; Bayes' rule with a worked numeric example.
- [ ] **T0.Q · Q&A M0.** `1 h` Huyen's math section (pick 4 on probability and linear algebra). Self-test with no notes, 20 minutes: gradient of `‖y − Xw‖²` with respect to `w` including shapes; Bayes' rule from the definition of conditional probability; why a covariance matrix is positive semi-definite.

---

## M1. Estimation, bias-variance, information and priors

**Related:** S1.14, S1.15; derivations D02, D04, D05, D10.

- [ ] **T1.1 · Maximum likelihood, MAP and priors.** `2 h` MLE and MAP, and what a prior means; ridge as a Gaussian prior and lasso as a Laplace prior. Murphy Ch. 4.
- [ ] **T1.2 · Bias, variance and validation.** `2 h` Bias, variance and noise; underfitting versus overfitting; train, validation and test splits; cross-validation. Shervine *Tips and Tricks* for the vocabulary.
- [ ] **T1.3 · Information theory.** `2 h` Entropy, cross-entropy, KL divergence, mutual information (briefly). Murphy Ch. 6.
- [ ] **T1.S · Cheat sheet M1.** `1 h` The MLE recipe in four lines; the normal equations and when `XᵀX` is invertible; the bias-variance formula and its faked step; the cross-entropy, KL and NLL identity; MLE, MAP and Bayesian estimation in one line each.
- [ ] **T1.Q · Q&A M1.** `1 h` Huyen's statistics and ML basics sections. Include "why squared error?", "why log-likelihood?" and "explain bias-variance with an example".

---

## M2. Optimization and regularization

**Related:** S2.01, S2.02, S3.09, S7.05; derivation D05.

- [ ] **T2.1 · Gradient descent and its variants.** `2.5 h` Convexity and why it matters; gradient descent, learning rate, stochastic and mini-batch gradient descent; momentum; conditioning and why scaling features helps. Murphy Ch. 8, selectively.
- [ ] **T2.2 · Regularization.** `1.5 h` L2 and L1, early stopping, and the Bayesian view of a penalty.
- [ ] **T2.S · Cheat sheet M2.** `1 h` The gradient descent update and its convergence picture; why L1 gives sparsity and L2 shrinks; the ridge closed form; the soft-thresholding result; learning-rate failure modes.
- [ ] **T2.Q · Q&A M2.** `1 h` "L1 versus L2", "why does feature scaling help?", "what goes wrong with a large learning rate?"

---

## M3. Classical supervised learning and evaluation

**Related:** S2.03 to S2.05, S2.07 to S2.09, S2.11, S2.12, S7.04, S7.06; derivation D03.

- [ ] **T3.1 · Logistic regression and generalized linear models.** `2 h` The model, the loss, why it is convex, and the link to softmax regression.
- [ ] **T3.2 · Naive Bayes and k-nearest neighbours.** `1.5 h` Assumptions, failure modes, and how each handles high dimensions.
- [ ] **T3.3 · Decision trees, bagging and random forests.** `2.5 h` Impurity, greedy splits, overfitting; bagging and why it reduces variance.
- [ ] **T3.4 · Boosting.** `1.5 h` The gradient boosting idea, and what XGBoost-style models add.
- [ ] **T3.5 · SVM and kernels.** `opt` `1 h` Margin intuition; kernels in one page.
- [ ] **T3.6 · Evaluation.** `1.5 h` Accuracy, precision, recall, F1, ROC and PR curves, AUC, calibration, class imbalance, data leakage, and choosing a metric for a business problem. Shervine *Supervised Learning*; Huyen for the questions.
- [ ] **T3.S · Cheat sheet M3.** `1.5 h` One block per model with the same five lines (assumptions, loss, training, strengths, failure modes); the metrics table with when to use each; the leakage checklist; bagging versus boosting in two sentences each.
- [ ] **T3.Q · Q&A M3.** `1.5 h` The largest set in the track. Do 8 to 10 questions, including "random forest versus gradient boosting", "why is accuracy misleading?", "how do you handle imbalance?" and "how would you detect leakage?"

---

## M4. Unsupervised learning, PCA and EM

**Related:** S2.06, S2.10, S7.07; derivations D06, D09.

- [ ] **T4.1 · Clustering.** `2 h` k-means and its failure modes; hierarchical clustering in outline; Gaussian mixture models.
- [ ] **T4.2 · PCA and SVD.** `2 h` PCA, SVD and the link between them; dimensionality reduction for visualization versus for modelling. Shervine *Unsupervised Learning*.
- [ ] **T4.3 · EM and the ELBO.** `2 h` EM and the evidence lower bound as a general idea; why latent-variable models are hard to fit. Murphy's EM chapter as a lookup.
- [ ] **T4.S · Cheat sheet M4.** `1 h` The k-means objective and algorithm; PCA in four steps and the variance-explained rule; the EM loop in words with the E-step and M-step formulas (fill these in after derivation D09); when to use which method.
- [ ] **T4.Q · Q&A M4.** `1 h` "Why center before PCA?", "k-means versus GMM", "how do you choose k?"

---

## M5. Neural nets, backprop and training

**Related:** S3.01 to S3.11, S8.01 to S8.03, S8.05; derivations D01, D08.

- [ ] **T5.1 · MLPs, activations and backpropagation.** `2.5 h` Perceptron to MLP; ReLU, GELU, sigmoid, tanh and why saturation hurts; backpropagation as the chain rule on a graph; vanishing and exploding gradients. Karpathy's micrograd and makemore videos if backprop does not feel automatic.
- [ ] **T5.2 · Initialization, normalization and regularizers.** `1.5 h` Xavier and He initialization, batch norm versus layer norm, dropout, weight decay, residual connections.
- [ ] **T5.3 · Optimizers and schedules.** `1.5 h` SGD with momentum, RMSProp, Adam, AdamW; learning-rate schedules and warmup.
- [ ] **T5.4 · CNN essentials.** `1.5 h` Convolution, pooling, receptive field.
- [ ] **T5.5 · RNNs and LSTMs as context.** `opt` `1 h` A brief view, as context for attention.
- [ ] **T5.S · Cheat sheet M5.** `1.5 h` Backprop in five lines with the shape rule; an activation table; init rules and why; batch norm versus layer norm; the Adam update with the bias-correction line; a debugging checklist for a network that does not train. Shervine *Deep Learning* to check.
- [ ] **T5.Q · Q&A M5.** `1.5 h` "Why does ReLU help?", "batch norm versus layer norm", "what happens if you initialize all weights to zero?", "explain vanishing gradients", "how do you debug a loss that does not go down?"

---

## M6. Attention and the Transformer

**Related:** S4.01 to S4.08, S8.07; derivation D07.

- [ ] **T6.1 · Attention.** `2.5 h` Why attention (the bottleneck of fixed-size encodings); queries, keys and values; self-attention and multi-head attention; masking. CME 295 lecture 1.
- [ ] **T6.2 · The Transformer block.** `2.5 h` Residuals, layer norm placement, feed-forward layer, positional information (sinusoidal, learned, rotary), parameter and compute counts. CME 295 cheatsheet to check.
- [ ] **T6.3 · Tokenization.** `1 h` Byte-pair encoding and why subwords exist.
- [ ] **T6.4 · Karpathy: Let's build GPT.** `2 h` Watch first, then build your own blind. About 1 h 56 min of video.
- [ ] **T6.5 · Karpathy: Let's build the GPT Tokenizer.** `opt` `2 h` About 2 h 13 min of video; useful extra depth on top of T6.3.
- [ ] **T6.S · Cheat sheet M6.** `1.5 h` The attention formula with shapes; the √d argument in two lines; a diagram of one Transformer block; the cost of attention (`O(n²d)` time, `O(n²)` memory) and why it matters; positional encoding options; tokenization in one paragraph.
- [ ] **T6.Q · Q&A M6.** `1.5 h` "Why scale by √d?", "why multi-head?", "encoder versus decoder models", "what is the cost of attention and how is it reduced?", "how does BPE work?"

---

## M7. LLMs: pretraining to alignment

**Related:** S4.07, S4.13, S8.10, S8.11, S9.09.

- [ ] **T7.1 · Pretraining and scaling laws.** `2 h` Next-token prediction, data and its quality, scaling laws and what they claim. CME 295 lecture 2.
- [ ] **T7.2 · Decoding.** `1 h` Greedy, beam, temperature, top-k, top-p.
- [ ] **T7.3 · Adaptation.** `2.5 h` Instruction tuning, parameter-efficient finetuning (LoRA), and when to finetune versus prompt. CME 295 lecture 3.
- [ ] **T7.4 · Alignment.** `2.5 h` RLHF in outline (reward model, policy optimization), DPO as the simpler alternative, and what reward hacking means. CME 295 lecture 4.
- [ ] **T7.5 · Derivation-lite.** `0.5 h` Write the next-token loss as a sum of cross-entropies and connect it back to D10. Cap at 30 minutes. (Write the DPO loss from its definition only if the lecture presents it.)
- [ ] **T7.6 · Reference pass.** `opt` `2 h` Xiao and Zhu chapters on pretraining and alignment, or CS224N slides, for any topic that lands thin.
- [ ] **T7.S · Cheat sheet M7.** `1.5 h` The LLM training pipeline as one diagram; decoding methods with the effect of each knob; LoRA in three lines (the low-rank update and why it saves memory); RLHF versus DPO in two columns; the scaling-law statement with its caveats.
- [ ] **T7.Q · Q&A M7.** `1.5 h` "How does temperature work?", "what is LoRA?", "RLHF versus DPO", "why do LLMs hallucinate?", "what does perplexity measure and what are its limits?"

---

## M8. LLM systems, applications and evaluation

**Related:** S4.09, S5.01 to S5.08, S6.01 to S6.03, S6.09, S6.10, S9.04, S9.05, and your LLM-judge calibration capstone.

- [ ] **T8.1 · Inference.** `2.5 h` The KV cache, why decoding is memory-bound, batching, quantization, and the latency versus throughput trade-off. CME 295 lecture 5.
- [ ] **T8.2 · Retrieval-augmented generation.** `2 h` Embeddings, chunking, retrieval quality, and where RAG fails. Huyen, *AI Engineering*.
- [ ] **T8.3 · Evaluation.** `2.5 h` Benchmarks and their contamination, human evaluation, LLM-as-judge and its biases (position, verbosity), and calibration. CME 295 lecture 7; Huyen.
- [ ] **T8.4 · Agents.** `opt` `1.5 h` Tool use, planning loops, and failure modes. CME 295 lecture 6.
- [ ] **T8.5 · Diffusion LLMs and trending topics.** `opt` `2 h` CME 295 lectures 8 and 9.
- [ ] **T8.S · Cheat sheet M8.** `1.5 h` The KV-cache size formula and why it limits context length; a table of RAG failure modes and fixes; the evaluation methods table with biases for each; a quantization summary (what is lost, what is gained).
- [ ] **T8.Q · Q&A M8.** `1.5 h` "How would you evaluate an LLM application?", "RAG or finetuning?", "what is the KV cache?", "how do you detect and reduce judge bias?"

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