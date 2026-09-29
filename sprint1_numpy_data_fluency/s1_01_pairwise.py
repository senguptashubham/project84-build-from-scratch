# Pairwise distances without loops.** Given `X` of shape `(n, d)` and `Y` of shape `(m, d)`, return an `(n, m)` matrix of Euclidean distances using broadcasting only. Then do it again using the identity ‖x−y‖² = ‖x‖² + ‖y‖² − 2x·y. Clip tiny negatives to zero before the square root.

import math
import numpy as np


def pairwise_distances_bc(X:np.ndarray, Y:np.ndarray) -> np.ndarray:
  n, d = X.shape
  m, g = Y.shape 
  if d != g:
    raise ValueError("dimension not matching for computing distance")
  else:
    X_r = X[:, np.newaxis, :]             # n * 1 * d
    Y_r = Y[np.newaxis, :, :]             # 1 * m * d
    # print(f"X_r now {X_r.shape}:\n{X_r}")
    # print(f"Y_r now {Y_r.shape}:\n{Y_r}")
    sub = np.subtract(X_r, Y_r)           # n * m * d
    # print(f"sub shape {sub.shape}:\n{sub}")
    res = np.linalg.norm(sub, axis=2)     # n * m
    return res

# def row_dist(row1:np.ndarray, row2:np.ndarray):
#   if row1.shape != row2.shape:
#     raise ValueError("row shape must match for calculating row difference")
#   else:
#     return np.linalg.norm(row1 - row2)

def pairwise_distances_id(X:np.ndarray, Y:np.ndarray) -> np.ndarray:
  n, d = X.shape
  m, g = Y.shape 
  if d != g:
    raise ValueError("dimension not matching for computing distance")
  else:
    X_sq = np.linalg.norm(X, axis=1) ** 2                # n * ,
    Y_sq = np.linalg.norm(Y, axis=1) ** 2               # m * ,
    # print(f"X_sq shape {X_sq.shape}:\n{X_sq.shape}")
    # print(f"Y_r shape {Y_sq.shape}:\n{Y_sq.shape}")
    two_XY = 2 * (X @ Y.T)                          # n * m
    X_sq_plus_Y_sq = X_sq[:, np.newaxis] + Y_sq[np.newaxis, :] # (n * 1) + (1 * m) = n * m
    sub = np.subtract(X_sq_plus_Y_sq, two_XY)     # n * m 
    res = np.sqrt(np.clip(sub, 0, float('inf')))
    return res
