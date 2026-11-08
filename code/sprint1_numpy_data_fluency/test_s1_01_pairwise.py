# *Test:* both match `scipy.spatial.distance.cdist` to 1e-6 on random data; explain in a comment why the second version is faster and where it can go numerically wrong.

from sprint1_numpy_data_fluency.s1_01_pairwise import pairwise_distances_bc, pairwise_distances_id
import numpy as np
import scipy
import logging
import time

LOGGER = logging.getLogger(__name__)

def test_pairwise_distance_bc(caplog):
  
  X = np.random.randn(3, 4)
  Y = np.random.randn(2, 4)
  dist = scipy.spatial.distance.cdist(X, Y, w=None, out=None)
  bc_dist = pairwise_distances_bc(X, Y)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"X:\n{X}\nY:\n{Y}\ndistance by scipy:\n{dist}")
    LOGGER.info(f"pairwise distance by broadcasting:\n{bc_dist}")
  assert np.allclose(dist, bc_dist, atol=1e-6)

def test_pairwise_distance_id(caplog):
  
  X = np.random.randn(3, 4)
  Y = np.random.randn(2, 4)
  dist = scipy.spatial.distance.cdist(X, Y, w=None, out=None)
  id_dist = pairwise_distances_id(X, Y)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"X:\n{X}\nY:\n{Y}\ndistance by scipy:\n{dist}")
    LOGGER.info(f"pairwise distance by identity:\n{id_dist}")
  assert np.allclose(dist, id_dist, atol=1e-6)

def test_speed_compare(caplog):
  X = np.random.randn(300, 400)
  Y = np.random.randn(200, 400)
  # Timing one call each is noisy (the first call pays BLAS/memory warm-up, and CI runners are busy),
  # so warm both up once, then compare the best of several runs.
  pairwise_distances_id(X, Y)
  pairwise_distances_bc(X, Y)

  def best_of(fn, runs=5):
    best = float("inf")
    for _ in range(runs):
      start = time.perf_counter()
      fn(X, Y)
      best = min(best, time.perf_counter() - start)
    return best

  elapsed_id = best_of(pairwise_distances_id)
  elapsed_bc = best_of(pairwise_distances_bc)
  with caplog.at_level(logging.INFO):
      LOGGER.info(f"time taken by bc:\n{elapsed_bc}")
      LOGGER.info(f"time taken by id:\n{elapsed_id}")
  assert elapsed_id < elapsed_bc #bc creates higher dimensional matrix n * m * d but id creates lower dimensional matrix n * m