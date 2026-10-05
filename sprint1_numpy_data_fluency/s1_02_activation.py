# **S1.02 · Numerically stable activations.** Write `sigmoid(z)`, `softmax(z, axis)` and `logsumexp(z, axis)` that do not overflow for inputs like `[1000, 1001, 1002]` or `[-1000, 0]`. Softmax must work along any axis of a 2D array. 

import numpy as np

def sigmoid(z:np.ndarray) -> np.ndarray:
  # σ(z) = 1 / (1 + e⁻ᶻ) or σ(z) = eᶻ / (1 + eᶻ)
  def pos_sigmoid(x:np.ndarray):
    return 1 / (1 + np.exp(-x))
  def neg_sigmoid(x:np.ndarray):
    return np.exp(x) / (1 + np.exp(x))
  res = np.empty_like(z, dtype=float)
  pos_vals = np.where(z >= 0)
  neg_vals = np.where(z < 0)
  if pos_vals[0].size > 0:
    res[pos_vals] = pos_sigmoid(z[pos_vals])
  if neg_vals[0].size > 0:
    res[neg_vals] = neg_sigmoid(z[neg_vals])
  return res

def softmax(z:np.ndarray, axis:int) -> np.ndarray:
  dims = z.shape
  if axis not in range(len(dims)):
    raise ValueError("axis out of bound")
  else:
    z_max = np.max(z, axis, keepdims=True)
    z = z - z_max
    z_exp = np.exp(z)
    sums = np.sum(z_exp, axis=axis, keepdims=True)
    return z_exp / sums.reshape(sums.shape)

def logsumexp(z:np.ndarray, axis:int) -> np.ndarray:
  dims = z.shape
  if axis not in range(len(dims)):
    raise ValueError("axis out of bound")
  else:
    z_max = np.max(z, axis, keepdims=True)
    exp_z = np.exp(z - z_max)
    sum_exp_z = np.sum(exp_z, axis=axis, keepdims=True)
    logsum_exp_z = z_max + np.log(sum_exp_z)
    return np.squeeze(logsum_exp_z, axis=axis)