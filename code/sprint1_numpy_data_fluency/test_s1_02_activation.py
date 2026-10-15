# *Test:* no `inf`/`nan` on extreme inputs; softmax sums to 1 along the chosen axis; matches `scipy.special.expit`, `softmax` and `logsumexp`.
from sprint1_numpy_data_fluency.s1_02_activation import sigmoid, softmax, logsumexp
import numpy as np
import scipy
import logging
import time

LOGGER = logging.getLogger(__name__)


def test_sigmoid(caplog):
  input = np.random.randn(23, 12, 11)
  scipy_sigmoid = scipy.special.expit(input)
  numpy_sigmoid = sigmoid(input)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"scipy sigmoid shape:\n{scipy_sigmoid.shape}")
    LOGGER.info(f"numpy sigmoid shape:\n{numpy_sigmoid.shape}")
  assert np.allclose(numpy_sigmoid, scipy_sigmoid, atol=1e-6)

def test_sigmoid_edge(caplog):
  inputs = [np.array([1000, 1001, 1002]), np.array([0, -1001]), np.array([0.0, 2000.0])]
  scipy_sigmoid = [scipy.special.expit(input) for input in inputs]
  numpy_sigmoid = [sigmoid(input) for input in inputs]
  for i in range(len(inputs)):
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"scipy sigmoid for {inputs[i]}:\n {scipy_sigmoid[i]}\n")
      LOGGER.info(f"numpy softmax for {inputs[i]}:\n {numpy_sigmoid[i]}\n")
    assert np.allclose(numpy_sigmoid[i], scipy_sigmoid[i], atol=1e-6)

def test_softmax(caplog):
  input = np.random.randn(12, 21, 4, 100)
  axis = np.random.randint(0,len(input.shape))
  scipy_softmax = scipy.special.softmax(input, axis)
  numpy_softmax = softmax(input, axis)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"scipy softmax of shape {scipy_softmax.shape}:\n")
    LOGGER.info(f"numpy softmax of shape {numpy_softmax.shape}:\n")
  assert np.allclose(numpy_softmax, scipy_softmax, atol=1e-6)

def test_softmax_edge(caplog):
  inputs = [np.array([1000, 1001, 1002]), np.array([0, -1001]), np.array([0.0, 2000.0])]
  scipy_softmax = [scipy.special.softmax(input, axis=0) for input in inputs]
  numpy_softmax = [softmax(input, axis=0) for input in inputs]
  for i in range(len(inputs)):
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"scipy softmax for {inputs[i]}:\n {scipy_softmax[i]}\n")
      LOGGER.info(f"numpy softmax for {inputs[i]}:\n {numpy_softmax[i]}\n")
    assert np.allclose(numpy_softmax[i], scipy_softmax[i], atol=1e-6)

def test_logsumexp(caplog):
  input = np.random.randn(12, 19, 24)
  axis = np.random.randint(0,len(input.shape))
  scipy_logsumexp = scipy.special.logsumexp(input, axis)
  numpy_logsumexp = logsumexp(input, axis)
  with caplog.at_level(logging.INFO):
    LOGGER.info(f"scipy logsumexp of shape {scipy_logsumexp.shape}:\n")
    LOGGER.info(f"numpy logsumexp of shape {numpy_logsumexp.shape}:\n")
  assert np.allclose(numpy_logsumexp, scipy_logsumexp, atol=1e-6)

def test_logsumexp_edge(caplog):
  inputs = [np.array([1000, 1001, 1002]), np.array([0, -1001]), np.array([0.0, 2000.0])]
  scipy_logsumexp = [scipy.special.logsumexp(input, axis=0) for input in inputs]
  numpy_logsumexp = [logsumexp(input, axis=0) for input in inputs]
  for i in range(len(inputs)):
    with caplog.at_level(logging.INFO):
      LOGGER.info(f"scipy logsumexp for {inputs[i]}:\n {scipy_logsumexp[i]}\n")
      LOGGER.info(f"numpy logsumexp for {inputs[i]}:\n {numpy_logsumexp[i]}\n")
    assert np.allclose(numpy_logsumexp[i], scipy_logsumexp[i], atol=1e-6)