# *Test:* fold union equals all indices; folds are disjoint; sizes differ by at most one; `cross_val_score` runs with a trivial mean-predicting model.

from sprint1_numpy_data_fluency.s1_04_kfold_cv import *
import numpy as np
import logging
from sklearn.datasets import fetch_california_housing

LOGGER = logging.getLogger(__name__)
X, y = fetch_california_housing(return_X_y=True)

class MeanModel:
  def fit(self, X, y):
    self.mean_ = np.mean(y)
    return self

  def predict(self, X):
    return np.full(len(X), self.mean_)

def test_kfold_union(caplog):
  test_idx = np.asarray(range(100))
  pairs = kfold(test_idx, k=13, seed=1)
  for train, val in pairs:
    fold_union = np.union1d(train, val)
    assert np.all(np.isin(test_idx, fold_union)), "All elements of test indices present in fold union"


def test_kfold_disjoint(caplog):
  test_idx = np.asarray(range(500))
  pairs = kfold(test_idx, k=29, seed=7)
  for i in range(len(pairs)-1):
    for j in range(i+1, len(pairs)):
      val_i = pairs[i][1]
      val_j = pairs[j][1]
      assert not np.any(np.isin(val_i, val_j)), f"Any element of validation set {i} not present in validation set {j}"


def test_kfold_sizes(caplog):
  test_idx = np.asarray(range(500))
  pairs = kfold(test_idx, k=23, seed=3)
  expected_size = int(500 / 23)
  print (f"first pair : {pairs[0]}")
  for _, val in pairs:
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"validation set size {len(val)}, expected fold size = {expected_size}")
    assert abs(len(val) - expected_size) <= 1, f"Sizes match across folds"


def test_cross_val_score(caplog):
  X = np.random.randn(500, 3)
  y = np.ones(500)
  y_mean = np.mean(y)
  mean_model = MeanModel()
  scores = cross_val_score(mean_model, X, y, 5, rms_loss, seed=42)
  assert len(scores) == 5, "number of folds matches number of scores"
  mean_score = np.mean(scores)
  model = MeanModel()
  model.fit(X, y)
  known_pred = model.predict(X)
  known_score = rms_loss(y, known_pred)
  assert np.isclose(mean_score, known_score), f"mean score {mean_score} is close to known score {known_score}"


def rms_loss(original:ArrayLike, predicted:ArrayLike) -> float:
  org = np.asarray(original)
  pred = np.asarray(predicted)
  return np.sqrt(np.mean((org - pred) ** 2))