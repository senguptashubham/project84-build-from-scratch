# the same seed gives identical splits; on 1,000 samples with a 90/10 label split, class proportions in every split are within 1 percentage point of the original.

from sprint1_numpy_data_fluency.s1_03_datasplits import train_val_test_split, startified_split
import numpy as np
import logging
from sklearn.datasets import load_iris
from numpy.typing import ArrayLike


LOGGER = logging.getLogger(__name__)
X, y = load_iris(return_X_y=True)


def test_train_val_test_split(caplog):
  train_x1, train_y1, val_x1, val_y1, test_x1, test_y1 = train_val_test_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=1)
  train_x2, train_y2, val_x2, val_y2, test_x2, test_y2 = train_val_test_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=1)
  train_x3, train_y3, val_x3, val_y3, test_x3, test_y3 = train_val_test_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=29)

  with caplog.at_level(logging.INFO):
    LOGGER.info(f"""1st set: ---------------------------\n
    train features:\n{train_x1[:3]}\nval features:\n{val_x1[:3]}\ntest features:\n{test_x1[:3]}\n
    train labels:\n{train_y1[:3]}\nval labels:\n{val_y1[:3]}\ntest labels:\n{test_y1[:3]}\n""")
    LOGGER.info(f"""2nd set: ---------------------------\n
    train features:\n{train_x2[:3]}\nval features:\n{val_x2[:3]}\ntest features:\n{test_x2[:3]}\n
    train labels:\n{train_y2[:3]}\nval labels:\n{val_y2[:3]}\ntest labels:\n{test_y2[:3]}\n""")
    LOGGER.info(f"""3rd set: ---------------------------\n
    train features:\n{train_x3[:3]}\nval features:\n{val_x3[:3]}\ntest features:\n{test_x3[:3]}\n
    train labels:\n{train_y3[:3]}\nval labels:\n{val_y3[:3]}\ntest labels:\n{test_y3[:3]}\n""")

  assert np.array_equal(train_x1, train_x2), "train set features matches for same seed"
  assert np.array_equal(train_y1, train_y2), "train set labels matches for same seed"
  assert np.array_equal(val_x1, val_x2), "val set features matches for same seed"
  assert np.array_equal(val_y1, val_y2), "val set labels matches for same seed"
  assert np.array_equal(test_x1, test_x2), "test set features matches for same seed"
  assert np.array_equal(test_y1, test_y2), "test set labels matches for same seed"
  assert not np.array_equal(train_x2, train_x3), "train set features doesn't match for different seed"
  assert not np.array_equal(train_y2, train_y3), "train set labels doesn't match for different seed"
  assert not np.array_equal(val_x2, val_x3), "val set features doesn't match for different seed"
  assert not np.array_equal(val_y2, val_y3), "val set labels doesn't match for different seed"
  assert not np.array_equal(test_x2, test_x3), "test set features doesn't match for different seed"
  assert not np.array_equal(test_y2, test_y3), "test set labels doesn't match for different seed"


def test_startified_split(caplog):
  train_x1, train_y1, val_x1, val_y1, test_x1, test_y1 = startified_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=1)
  train_x2, train_y2, val_x2, val_y2, test_x2, test_y2 = startified_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=1)
  train_x3, train_y3, val_x3, val_y3, test_x3, test_y3 = startified_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=29)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"""1st set: ---------------------------\n
    train features:\n{train_x1[:3]}\nval features:\n{val_x1[:3]}\ntest features:\n{test_x1[:3]}\n
    train labels:\n{train_y1[:3]}\nval labels:\n{val_y1[:3]}\ntest labels:\n{test_y1[:3]}\n""")
    LOGGER.info(f"""2nd set: ---------------------------\n
    train features:\n{train_x2[:3]}\nval features:\n{val_x2[:3]}\ntest features:\n{test_x2[:3]}\n
    train labels:\n{train_y2[:3]}\nval labels:\n{val_y2[:3]}\ntest labels:\n{test_y2[:3]}\n""")
    LOGGER.info(f"""3rd set: ---------------------------\n
    train features:\n{train_x3[:3]}\nval features:\n{val_x3[:3]}\ntest features:\n{test_x3[:3]}\n
    train labels:\n{train_y3[:3]}\nval labels:\n{val_y3[:3]}\ntest labels:\n{test_y3[:3]}\n""")
  assert np.array_equal(train_x1, train_x2), "train set features matches for same seed"
  assert np.array_equal(train_y1, train_y2), "train set labels matches for same seed"
  assert np.array_equal(val_x1, val_x2), "val set features matches for same seed"
  assert np.array_equal(val_y1, val_y2), "val set labels matches for same seed"
  assert np.array_equal(test_x1, test_x2), "test set features matches for same seed"
  assert np.array_equal(test_y1, test_y2), "test set labels matches for same seed"
  assert not np.array_equal(train_x2, train_x3), "train set features doesn't match for different seed"
  assert not np.array_equal(train_y2, train_y3), "train set labels doesn't match for different seed"
  assert not np.array_equal(val_x2, val_x3), "val set features doesn't match for different seed"
  assert not np.array_equal(val_y2, val_y3), "val set labels doesn't match for different seed"
  assert not np.array_equal(test_x2, test_x3), "test set features doesn't match for different seed"
  assert not np.array_equal(test_y2, test_y3), "test set labels doesn't match for different seed"


def test_stratification_startified_split(caplog):
  train_x1, train_y1, val_x1, val_y1, test_x1, test_y1 = startified_split(np.array(X), y, ratios=(0.5,0.3,0.2), seed=1)

  value_ratio = get_value_ratio(y)
  train_value_ratio = get_value_ratio(train_y1)
  val_value_ratio = get_value_ratio(val_y1)
  test_value_ratio = get_value_ratio(test_y1)

  with caplog.at_level(logging.INFO):
    for val, ratio in value_ratio.items():
      LOGGER.info(f"checking ratio for value: {val}, expected ratio: {ratio} ----------------\n")
      train_ratio = train_value_ratio[val]
      val_ratio = val_value_ratio[val]
      test_ratio = test_value_ratio[val]
      LOGGER.info(f"ration of {val}\n\tin train set: {train_ratio}\n\tin validation set: {val_ratio}\n\tin test set: {test_ratio}\n")
      assert abs(train_ratio - ratio) <= 1, f"ratio for {val} is within allowed range for train set"
      assert abs(val_ratio - ratio) <= 1, f"ratio for {val} is within allowed range for validation set"
      assert abs(test_ratio - ratio) <= 1, f"ratio for {val} is within allowed range for test set"


def get_value_ratio(y:ArrayLike) -> dict:
  y = np.asarray(y)
  values, counts = np.unique(y, return_counts=True)
  value_ratio = {}
  for val, cnt in zip(values, counts):
    value_ratio[val] = cnt / len(y)
  return value_ratio  