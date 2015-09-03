# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = [
    "test_constant_mean",
    "test_callable_mean",
    "test_gp_mean",
    "test_gp_white_noise",
    "test_gp_callable_mean",
]

import numpy as np

from ..gp import GP
from .. import kernels
from ..modeling import check_gradient
from ..models import ConstantModel, CallableModel


def test_constant_mean():
    m = ConstantModel(5.0)
    check_gradient(m, np.zeros(4))


def test_callable_mean():
    m = CallableModel(lambda x: 5.0 * x)
    check_gradient(m, np.zeros(4))


def test_gp_mean(N=50, seed=1234):
    np.random.seed(seed)
    x = np.random.uniform(0, 5)
    y = 5 + np.sin(x)
    gp = GP(10. * kernels.ExpSquaredKernel(1.3),
            mean=5.0, fit_mean=True)
    gp.compute(x)
    check_gradient(gp, y)


def test_gp_callable_mean(N=50, seed=1234):
    np.random.seed(seed)
    x = np.random.uniform(0, 5)
    y = 5 + np.sin(x)
    gp = GP(10. * kernels.ExpSquaredKernel(1.3),
            mean=lambda x: 5.0*x, fit_mean=True)
    gp.compute(x)
    check_gradient(gp, y)


def test_gp_white_noise(N=50, seed=1234):
    np.random.seed(seed)
    x = np.random.uniform(0, 5)
    y = 5 + np.sin(x)
    gp = GP(10. * kernels.ExpSquaredKernel(1.3),
            mean=5.0, fit_mean=True,
            white_noise=0.1, fit_white_noise=True)
    gp.compute(x)
    check_gradient(gp, y)
