# Given `y_true` and `y_pred` (binary and multiclass), compute accuracy, confusion matrix, precision, recall, F1, and macro/micro averages. When a class is never predicted, return 0 for its precision.

import numpy as np
from typing import Literal
from numpy.typing import NDArray

def get_accuracy(y_true:NDArray, y_pred:NDArray) -> float:
  # (True Positive + True Negative) / (True Positive + True Negative + False Positive + False Negative)
  # out of all the labels, how many the model predicted correctly
  y_true = np.asarray(y_true)
  y_pred = np.asarray(y_pred)
  accuracy = 0 if len(y_true)==0 else (y_true == y_pred).astype(int).sum() / len(y_true)
  return accuracy

def get_precision(y_true:NDArray, y_pred:NDArray, average:Literal['micro', 'macro', 'weighted', 'binary']='binary') -> float:
  # True Positive / (True Positive + False Positive)
  # out of all the positive predictions by the model, how many are correct
  y_true = np.asarray(y_true)
  y_pred = np.asarray(y_pred)
  distinct = np.union1d(np.unique(y_true), np.unique(y_pred))
  precisions = {}
  true_positives = {}
  false_positives = {}
  for label in distinct:
    tp = get_TP(y_true, y_pred, label)
    fp = get_FP(y_true, y_pred, label)
    precisions[label] = 0 if (tp + fp) == 0 else tp / (tp + fp)
    true_positives[label] = tp
    false_positives[label] = fp
  if average == 'micro':
    # calculate average on total counts
    precision = 0 if sum(true_positives.values()) + sum(false_positives.values()) == 0 else sum(true_positives.values()) / (sum(true_positives.values()) + sum(false_positives.values()))
  elif average == 'macro':
    # calculate average on labelwise counts without weights
    precision = 0 if len(precisions) == 0 else sum(precisions.values()) / len(precisions)
  elif average == 'weighted':
    # calculate weighted average on labelwise counts
    w_sum = 0
    for l, p in precisions.items():
      w_sum += 0 if len(y_true) == 0 else (p * sum((y_true==l).astype(int)) / len(y_true))
    precision = w_sum
  else:
    # default binary
    if len(distinct) > 2:
      raise ValueError("Expected 2 unique labels for binary calssification")
    pos_label = sorted(precisions.keys())[-1]
    precision = precisions[pos_label]
  return precision

def get_recall(y_true:NDArray, y_pred:NDArray, average:Literal['micro', 'macro', 'weighted', 'binary']='binary') -> float:
  # True Positive / (True Positive + False Negative)
  # out of all the postive labels, how many model predicted correctly
  y_true = np.asarray(y_true)
  y_pred = np.asarray(y_pred)
  distinct = np.union1d(np.unique(y_true), np.unique(y_pred))
  recalls = {}
  true_positives = {}
  false_negatives = {}
  for label in distinct:
    tp = get_TP(y_true, y_pred, label)
    fn = get_FN(y_true, y_pred, label)
    recalls[label] = tp / (tp + fn) if (tp + fn) > 0 else 0
    true_positives[label] = tp
    false_negatives[label] = fn
  if average == 'micro':
    # calculate average on total counts
    recall = 0 if sum(true_positives.values()) + sum(false_negatives.values()) == 0 else sum(true_positives.values()) / (sum(true_positives.values()) + sum(false_negatives.values()))
  elif average == 'macro':
    # calculate average on labelwise counts without weights
    recall = 0 if len(recalls) == 0 else sum(recalls.values()) / len(recalls)
  elif average == 'weighted':
    # calculate weighted average on labelwise counts
    w_sum = 0
    for l, r in recalls.items():
      w_sum += 0 if len(y_true) == 0 else (r * sum((y_true==l).astype(int)) / len(y_true))
    recall = w_sum
  else:
    # default binary
    if len(distinct) > 2:
      raise ValueError("Expected 2 unique labels for binary calssification")
    pos_label = sorted(recalls.keys())[-1]
    recall = recalls[pos_label]
  return recall

def get_f1(y_true:NDArray, y_pred:NDArray, average:Literal['micro', 'macro', 'weighted', 'binary']='binary') -> float:
  # (2 * Precision * Recall) / (Precision + Recall) --> Harmonic mean of Precision and Recall
  # TP / (TP + 0.5 * (FP + FN))
  y_true = np.asarray(y_true)
  y_pred = np.asarray(y_pred)
  distinct = np.union1d(np.unique(y_true), np.unique(y_pred))
  true_positives = {}
  false_positives = {}
  false_negatives = {}
  f1_scores = {}
  for label in distinct:
    tp = get_TP(y_true, y_pred, label)
    fp = get_FP(y_true, y_pred, label)
    fn = get_FN(y_true, y_pred, label)
    f1_scores[label] = 0 if tp + 0.5 * (fp + fn) == 0 else tp / (tp + 0.5 * (fp + fn))
    true_positives[label] = tp
    false_positives[label] = fp
    false_negatives[label] = fn  
  if average == 'micro':
    # calculate average on total counts
    f1_score = 0 if sum(true_positives.values()) + 0.5 * (sum(false_positives.values()) + sum(false_negatives.values())) == 0 else sum(true_positives.values()) / (sum(true_positives.values()) + 0.5 * (sum(false_positives.values()) + sum(false_negatives.values())))
  elif average == 'macro':
    # calculate average on labelwise counts without weights
    f1_score = 0 if len(f1_scores) == 0 else sum(f1_scores.values()) / len(f1_scores)
  elif average == 'weighted':
    # calculate weighted average on labelwise counts
    w_sum = 0
    for l, f1 in f1_scores.items():
      w_sum += 0 if len(y_true) == 0 else (f1 * sum((y_true==l).astype(int)) / len(y_true))
    f1_score = w_sum
  else:
    # default binary
    if len(distinct) > 2:
      raise ValueError("Expected 2 unique labels for binary calssification")
    pos_label = sorted(f1_scores.keys())[-1]
    f1_score = f1_scores[pos_label]  
  return f1_score

def get_confusion_matrix(y_true:NDArray, y_pred:NDArray) -> NDArray:
  y_true = np.asarray(y_true)
  y_pred = np.asarray(y_pred)
  all_classes = np.union1d(np.unique(y_true), np.unique(y_pred))
  dim = len(all_classes)
  matrix = np.zeros((dim, dim))
  for i in range(dim):
    for j in range(dim):
      if i==j:
        matrix[i][j] = get_TP(y_true, y_pred, all_classes[i])
      else:
        matrix[i][j] = get_class_FN(y_true, y_pred, all_classes[i], all_classes[j])
  return matrix



def get_TP(y_true:NDArray, y_pred:NDArray, label) -> float:
  actual_pos = (y_true == label).astype(int)
  predicted_pos = (y_pred == label).astype(int)
  tp = (actual_pos + predicted_pos == 2).sum()
  return tp

def get_FP(y_true:NDArray, y_pred:NDArray, label) -> float:
  actual_neg = (y_true != label).astype(int)
  predicted_pos = (y_pred == label).astype(int)
  fp = (actual_neg + predicted_pos == 2).sum()
  return fp

def get_class_FN(y_true:NDArray, y_pred:NDArray, true_label, predicted_label) -> float:
  label_pos = (y_true == true_label).astype(int)
  predicted_pos = (y_pred == predicted_label).astype(int)
  fn = (label_pos + predicted_pos == 2).sum()
  return fn

def get_FN(y_true:NDArray, y_pred:NDArray, label) -> float:
  actual_pos = (y_true == label).astype(int)
  predicted_neg = (y_pred != label).astype(int)
  fn = (actual_pos + predicted_neg == 2).sum()
  return fn
