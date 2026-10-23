# *Test:* matches `sklearn.metrics` (with `zero_division=0`) on five random cases, including one where a class has no predictions.

from sprint1_numpy_data_fluency.s1_05_classification_metrics import get_accuracy, get_precision, get_recall, get_f1, get_confusion_matrix
import numpy as np
import logging
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

LOGGER = logging.getLogger(__name__)

BINARY_TRUE = np.asarray([1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1])
BINARY_PRED = np.asarray([1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0])

BINARY_ZERO_D_TRUE = np.zeros(shape=(10,))
BINARY_ZERO_D_PRED = np.ones(shape=(10,))
BINARY_TRUE_ARRAYS = [BINARY_TRUE, BINARY_ZERO_D_TRUE]
BINARY_PRED_ARRAYS = [BINARY_PRED, BINARY_ZERO_D_PRED]

MULTI_TRUE = np.asarray([2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 1.0, 3.0, 3.0, 2.0])
MULTI_PRED = np.asarray([1.0, 3.0, 2.0, 2.0, 1.0, 3.0, 3.0, 1.0, 3.0, 2.0, 1.0])

rng = np.random.default_rng(seed=42)
ZERO_D_TRUE_1 = rng.integers(low=5, high=10, size=10)
ZERO_D_PRED_1 = rng.integers(low=0, high=5, size=10)
ZERO_D_TRUE_2 = rng.integers(low=5, high=15, size=10)
ZERO_D_PRED_2 = rng.integers(low=7, high=10, size=10)
ZERO_D_TRUE_3 = rng.integers(low=7, high=11, size=10)
ZERO_D_PRED_3 = rng.integers(low=0, high=15, size=10)
ZERO_D_TRUE_4 = rng.integers(low=7, high=15, size=10)
ZERO_D_PRED_4 = rng.integers(low=0, high=6, size=10)
ZERO_D_TRUE_ARRAYS = [ZERO_D_TRUE_1, ZERO_D_TRUE_2, ZERO_D_TRUE_3, ZERO_D_TRUE_4]
ZERO_D_PRED_ARRAYS = [ZERO_D_PRED_1, ZERO_D_PRED_2, ZERO_D_PRED_3, ZERO_D_PRED_4]

def test_binary_accuracy(caplog):
  sklearn_accuracy = accuracy_score(BINARY_TRUE, BINARY_PRED)
  your_accuracy = get_accuracy(BINARY_TRUE, BINARY_PRED)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"sk learn accuracy score: {sklearn_accuracy}, your accuracy score: {your_accuracy}")
  assert np.isclose(sklearn_accuracy, your_accuracy, atol=1e-6)

def test_binary_precision(caplog):
  for binary_true, binary_pred in zip(BINARY_TRUE_ARRAYS, BINARY_PRED_ARRAYS):
    sklearn_precision = precision_score(binary_true, binary_pred, zero_division=0)
    your_precision = get_precision(binary_true, binary_pred)
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{binary_true}, predicted labels:{binary_pred}")
      LOGGER.info(f"sk learn precision score: {sklearn_precision}, your precision score: {your_precision}")
    assert np.isclose(sklearn_precision, your_precision, atol=1e-6), f"asserted precision value for true labels:{binary_true}, predicted labels:{binary_pred}"

def test_binary_recall(caplog):
  for binary_true, binary_pred in zip(BINARY_TRUE_ARRAYS, BINARY_PRED_ARRAYS):
    sklearn_recall = recall_score(binary_true, binary_pred, zero_division=0)
    your_recall = get_recall(binary_true, binary_pred)
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{binary_true}, predicted labels:{binary_pred}")
      LOGGER.info(f"sk learn recall score: {sklearn_recall}, your recall score: {your_recall}")
    assert np.isclose(sklearn_recall, your_recall, atol=1e-6), f"asserted recall value for true labels:{binary_true}, predicted labels:{binary_pred}"

def test_binary_f1(caplog):
  for binary_true, binary_pred in zip(BINARY_TRUE_ARRAYS, BINARY_PRED_ARRAYS):
    sklearn_f1 = f1_score(BINARY_TRUE, BINARY_PRED)
    your_f1 = get_f1(BINARY_TRUE, BINARY_PRED)
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{binary_true}, predicted labels:{binary_pred}")
      LOGGER.info(f"sk learn f1 score: {sklearn_f1}, your f1 score: {your_f1}")
    assert np.isclose(sklearn_f1, your_f1, atol=1e-6), f"asserted f1 value for true labels:{binary_true}, predicted labels:{binary_pred}"

def test_multiclass_accuracy(caplog):
  sklearn_accuracy = accuracy_score(MULTI_TRUE, MULTI_PRED)
  your_accuracy = get_accuracy(MULTI_TRUE, MULTI_PRED)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"sk learn accuracy score: {sklearn_accuracy}, your accuracy score: {your_accuracy}")
  assert np.isclose(sklearn_accuracy, your_accuracy, atol=1e-6)

def test_multiclass_precision(caplog):
  sklearn_precision_micro = precision_score(MULTI_TRUE, MULTI_PRED, average='micro', zero_division=0)
  sklearn_precision_macro = precision_score(MULTI_TRUE, MULTI_PRED, average='macro', zero_division=0)
  sklearn_precision_weighted = precision_score(MULTI_TRUE, MULTI_PRED, average='weighted', zero_division=0)
  your_precision_micro = get_precision(MULTI_TRUE, MULTI_PRED, average='micro')
  your_precision_macro = get_precision(MULTI_TRUE, MULTI_PRED, average='macro')
  your_precision_weighted = get_precision(MULTI_TRUE, MULTI_PRED, average='weighted')
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"for micro average, sk learn precision score: {sklearn_precision_micro}, your precision score: {your_precision_micro}")
    LOGGER.info(f"for macro average, sk learn precision score: {sklearn_precision_macro}, your precision score: {your_precision_macro}")
    LOGGER.info(f"for weighted average, sk learn precision score: {sklearn_precision_weighted}, your precision score: {your_precision_weighted}")
  assert np.isclose(sklearn_precision_micro, your_precision_micro, atol=1e-6), "micro average asserted for precision"
  assert np.isclose(sklearn_precision_macro, your_precision_macro, atol=1e-6), "macro average asserted for precision"
  assert np.isclose(sklearn_precision_weighted, your_precision_weighted, atol=1e-6), "weighted average asserted for precision"

def test_multiclass_recall(caplog):
  sklearn_recall_micro = recall_score(MULTI_TRUE, MULTI_PRED, average='micro', zero_division=0)
  sklearn_recall_macro = recall_score(MULTI_TRUE, MULTI_PRED, average='macro', zero_division=0)
  sklearn_recall_weighted = recall_score(MULTI_TRUE, MULTI_PRED, average='weighted', zero_division=0)
  your_recall_micro = get_recall(MULTI_TRUE, MULTI_PRED, average='micro')
  your_recall_macro = get_recall(MULTI_TRUE, MULTI_PRED, average='macro')
  your_recall_weighted = get_recall(MULTI_TRUE, MULTI_PRED, average='weighted')
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"for micro average, sk learn recall score: {sklearn_recall_micro}, your recall score: {your_recall_micro}")
    LOGGER.info(f"for macro average, sk learn recall score: {sklearn_recall_macro}, your recall score: {your_recall_macro}")
    LOGGER.info(f"for weighted average, sk learn recall score: {sklearn_recall_weighted}, your recall score: {your_recall_weighted}")
  assert np.isclose(sklearn_recall_micro, your_recall_micro, atol=1e-6), "micro average asserted for recall"
  assert np.isclose(sklearn_recall_macro, your_recall_macro, atol=1e-6), "macro average asserted for recall"
  assert np.isclose(sklearn_recall_weighted, your_recall_weighted, atol=1e-6), "weighted average asserted for recall"

def test_multiclass_f1(caplog):
  sklearn_f1_micro = f1_score(MULTI_TRUE, MULTI_PRED, average='micro', zero_division=0)
  sklearn_f1_macro = f1_score(MULTI_TRUE, MULTI_PRED, average='macro', zero_division=0)
  sklearn_f1_weighted = f1_score(MULTI_TRUE, MULTI_PRED, average='weighted', zero_division=0)
  your_f1_micro = get_f1(MULTI_TRUE, MULTI_PRED, average='micro')
  your_f1_macro = get_f1(MULTI_TRUE, MULTI_PRED, average='macro')
  your_f1_weighted = get_f1(MULTI_TRUE, MULTI_PRED, average='weighted')
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"for micro average, sk learn f1 score: {sklearn_f1_micro}, your f1 score: {your_f1_micro}")
    LOGGER.info(f"for macro average, sk learn f1 score: {sklearn_f1_macro}, your f1 score: {your_f1_macro}")
    LOGGER.info(f"for weighted average, sk learn f1 score: {sklearn_f1_weighted}, your f1 score: {your_f1_weighted}")
  assert np.isclose(sklearn_f1_micro, your_f1_micro, atol=1e-6), "micro average asserted for f1"
  assert np.isclose(sklearn_f1_macro, your_f1_macro, atol=1e-6), "macro average asserted for f1"
  assert np.isclose(sklearn_f1_weighted, your_f1_weighted, atol=1e-6), "weighted average asserted for f1"

def test_confusion_matrix(caplog):
  sklearn_cm = confusion_matrix(MULTI_TRUE, MULTI_PRED)
  your_cm = get_confusion_matrix(MULTI_TRUE, MULTI_PRED)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"sk learn confusion matrix:\n{sklearn_cm}\n, your confusion matrix:\n{your_cm}")
  assert np.allclose(sklearn_cm, your_cm), "confusion matrix all values asserted" 

def test_precision_zero_division(caplog):
  for zero_d_true, zero_d_pred in zip(ZERO_D_TRUE_ARRAYS, ZERO_D_PRED_ARRAYS):
    sklearn_precision_micro = precision_score(zero_d_true, zero_d_pred, average='micro', zero_division=0)
    sklearn_precision_macro = precision_score(zero_d_true, zero_d_pred, average='macro', zero_division=0)
    sklearn_precision_weighted = precision_score(zero_d_true, zero_d_pred, average='weighted', zero_division=0)
    your_precision_micro = get_precision(zero_d_true, zero_d_pred, average='micro')
    your_precision_macro = get_precision(zero_d_true, zero_d_pred, average='macro')
    your_precision_weighted = get_precision(zero_d_true, zero_d_pred, average='weighted')
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{zero_d_true}, predicted labels:{zero_d_pred}")
      LOGGER.info(f"for micro average, sk learn precision score: {sklearn_precision_micro}, your precision score: {your_precision_micro}")
      LOGGER.info(f"for macro average, sk learn precision score: {sklearn_precision_macro}, your precision score: {your_precision_macro}")
      LOGGER.info(f"for weighted average, sk learn precision score: {sklearn_precision_weighted}, your precision score: {your_precision_weighted}")
    assert np.isclose(sklearn_precision_micro, your_precision_micro, atol=1e-6), f"micro average asserted for precision for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_precision_macro, your_precision_macro, atol=1e-6), f"macro average asserted for precision for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_precision_weighted, your_precision_weighted, atol=1e-6), f"weighted average asserted for precision for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"

def test_recall_zero_division(caplog):
  for zero_d_true, zero_d_pred in zip(ZERO_D_TRUE_ARRAYS, ZERO_D_PRED_ARRAYS):
    sklearn_recall_micro = recall_score(zero_d_true, zero_d_pred, average='micro', zero_division=0)
    sklearn_recall_macro = recall_score(zero_d_true, zero_d_pred, average='macro', zero_division=0)
    sklearn_recall_weighted = recall_score(zero_d_true, zero_d_pred, average='weighted', zero_division=0)
    your_recall_micro = get_recall(zero_d_true, zero_d_pred, average='micro')
    your_recall_macro = get_recall(zero_d_true, zero_d_pred, average='macro')
    your_recall_weighted = get_recall(zero_d_true, zero_d_pred, average='weighted')
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{zero_d_true}, predicted labels:{zero_d_pred}")
      LOGGER.info(f"for micro average, sk learn recall score: {sklearn_recall_micro}, your recall score: {your_recall_micro}")
      LOGGER.info(f"for macro average, sk learn recall score: {sklearn_recall_macro}, your recall score: {your_recall_macro}")
      LOGGER.info(f"for weighted average, sk learn recall score: {sklearn_recall_weighted}, your recall score: {your_recall_weighted}")
    assert np.isclose(sklearn_recall_micro, your_recall_micro, atol=1e-6), f"micro average asserted for recall for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_recall_macro, your_recall_macro, atol=1e-6), f"macro average asserted for recall for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_recall_weighted, your_recall_weighted, atol=1e-6), f"weighted average asserted for recall for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"

def test_f1_zero_division(caplog):
  for zero_d_true, zero_d_pred in zip(ZERO_D_TRUE_ARRAYS, ZERO_D_PRED_ARRAYS):
    sklearn_f1_micro = f1_score(zero_d_true, zero_d_pred, average='micro', zero_division=0)
    sklearn_f1_macro = f1_score(zero_d_true, zero_d_pred, average='macro', zero_division=0)
    sklearn_f1_weighted = f1_score(zero_d_true, zero_d_pred, average='weighted', zero_division=0)
    your_f1_micro = get_f1(zero_d_true, zero_d_pred, average='micro')
    your_f1_macro = get_f1(zero_d_true, zero_d_pred, average='macro')
    your_f1_weighted = get_f1(zero_d_true, zero_d_pred, average='weighted')
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"LOGGING FOR true labels:{zero_d_true}, predicted labels:{zero_d_pred}")
      LOGGER.info(f"for micro average, sk learn f1 score: {sklearn_f1_micro}, your f1 score: {your_f1_micro}")
      LOGGER.info(f"for macro average, sk learn f1 score: {sklearn_f1_macro}, your f1 score: {your_f1_macro}")
      LOGGER.info(f"for weighted average, sk learn f1 score: {sklearn_f1_weighted}, your f1 score: {your_f1_weighted}")
    assert np.isclose(sklearn_f1_micro, your_f1_micro, atol=1e-6), f"micro average asserted for f1 for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_f1_macro, your_f1_macro, atol=1e-6), f"macro average asserted for f1 for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"
    assert np.isclose(sklearn_f1_weighted, your_f1_weighted, atol=1e-6), f"weighted average asserted for f1 for true labels:{zero_d_true}, predicted labels:{zero_d_pred}"