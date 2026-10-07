# Write `train_val_test_split(X, y, ratios=(0.7, 0.15, 0.15), seed)` that shuffles reproducibly. Then write a stratified version that preserves class proportions in each split.

import numpy as np
from numpy.typing import ArrayLike
from typing import Tuple


def train_val_test_split(X:ArrayLike, y:ArrayLike, ratios:Tuple[float, float, float], seed:int=42) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
  X = np.asarray(X)
  y = np.asarray(y)
  rng = np.random.default_rng(seed)

  if X.shape[0] != y.shape[0]:
    raise ValueError("shape mismatch for features and labels")
  elif not np.isclose(sum(ratios), 1):
    raise ValueError("ratios don't add up to 1")
  else:
    indexes = [i for i in range(X.shape[0])]
    shuffled = rng.permutation(indexes)

    train_count = int(X.shape[0] * ratios[0])
    val_count = int(X.shape[0] * ratios[1])

    train_idx = shuffled[ : train_count]
    val_idx = shuffled[train_count : train_count + val_count]
    test_idx = shuffled[train_count + val_count : ]

    if len(X.shape) < 2:
      train_x, val_x, test_x = X[train_idx], X[val_idx], X[test_idx]
    else:
      train_x, val_x, test_x = X[train_idx,:], X[val_idx,:], X[test_idx,:]
    if len(y.shape) < 2:
      train_y, val_y, test_y = y[train_idx], y[val_idx], y[test_idx]
    else:
      train_y, val_y, test_y = y[train_idx,:], y[val_idx,:], y[test_idx,:]

    return train_x, train_y, val_x, val_y, test_x, test_y


def startified_split(X:ArrayLike, y:ArrayLike, ratios:Tuple[float, float, float], seed:int=42) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
  X = np.asarray(X)
  y = np.asarray(y)
  rng = np.random.default_rng(seed)
  if X.shape[0] != y.shape[0]:
    raise ValueError("shape mismatch for features and labels")
  elif not np.isclose(sum(ratios), 1):
    raise ValueError("ratios don't add up to 1")
  else:
    all_labels = {}
    for i in range(len(y)):
      if len(y.shape) < 2:
        label = y[i]
      else:
        label = tuple(y[i])
      if label not in all_labels:
        all_labels[label] = [i]
      else:
        all_labels[label].append(i)

    train_x, val_x, test_x = [], [], []
    train_y, val_y, test_y = [], [], []

    # divide X and y as per ratio labels and pass each to split function, accumulate result in respective arrays
    for label, idx in all_labels.items():
      if len(X.shape) < 2:
        X_r = X[idx]
      else:
        X_r = X[idx, :]
      if len(y.shape) < 2:
        y_r = y[idx]
      else:
        y_r = y[idx, :]
      
      train_xr, train_yr, val_xr, val_yr, test_xr, test_yr = train_val_test_split(X=X_r, y=y_r, ratios=ratios, seed=seed)
      train_x.append(train_xr)
      train_y.append(train_yr)
      val_x.append(val_xr)
      val_y.append(val_yr)
      test_x.append(test_xr)
      test_y.append(test_yr)

    train_x = np.concatenate(train_x)
    train_y = np.concatenate(train_y)
    val_x = np.concatenate(val_x)
    val_y = np.concatenate(val_y)
    test_x = np.concatenate(test_x)
    test_y = np.concatenate(test_y)

    rng.shuffle(train_x)
    rng.shuffle(train_y)
    rng.shuffle(val_x)
    rng.shuffle(val_y)
    rng.shuffle(test_x)
    rng.shuffle(test_y)
    
    return train_x, train_y, val_x, val_y, test_x, test_y