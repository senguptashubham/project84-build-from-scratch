# **S1.04 · k-fold cross-validation.** `S` Write a generator `kfold(n, k, shuffle, seed)` yielding `(train_idx, val_idx)` pairs. Every index must appear in exactly one validation fold. Then write `cross_val_score(model_fn, X, y, k, metric)` that trains a fresh model per fold and returns the per-fold scores.

import numpy as np
from numpy.typing import ArrayLike
from typing import Tuple, Callable, Any

def kfold(n:ArrayLike, k:int, shuffle:bool=True, seed:int=42) -> list[Tuple[np.ndarray, np.ndarray]]:
  indices = np.asarray(n)
  rng = np.random.default_rng(seed=seed)
  if shuffle:
    indices = rng.permutation(indices)
  fold_size = int(len(indices) / k)
  remaining = len(indices) % k
  sizes = [fold_size] * k
  for i in range(remaining):
    sizes[i] += 1
  folds = []
  j = 0
  for s in range(len(sizes)):
    folds.append(indices[j : j+sizes[s]])
    j += sizes[s]
  pairs = []
  for k in range(len(folds)):
    test = np.asarray(folds[k])
    train = folds[:k] + folds[k+1:]
    train = np.asarray([element for fold in train for element in fold])
    pairs.append((train, test))
  return pairs


def cross_val_score(model_fn:Any, X:ArrayLike, y:ArrayLike, k:int, metric:Callable[[ArrayLike, ArrayLike], float], seed:int) -> np.ndarray:
  X = np.asarray(X)
  y = np.asarray(y)
  n = range(len(y))
  indices = kfold(n, k, seed=seed)
  scores = []
  for train_idx, val_idx in indices:
    print(f"train_idx shape: {train_idx.shape}\tval_idx shape: {val_idx.shape}")
    X_train, y_train = X[train_idx[0]], y[train_idx[0]]
    print(f"X_train shape: {X_train.shape}\ty_train shape: {y_train.shape}")
    X_val, y_val = X[[val_idx]], y[val_idx]
    model_fn.fit(X_train, y_train)
    y_pred = model_fn.predict(X_val)
    score = metric(y_val, y_pred)
    scores.append(score)
  print("scores: ------", scores)
  return np.asarray(scores)