#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from misc.matrix import *
import numpy as np, unittest


class TestNormalizeWeightMatrix(unittest.TestCase):
    def test(self):
        np.testing.assert_array_almost_equal(
            np.array([
                [1/2, 1/2, 0,    0],
                [1/2, 1/6, 1/6,  1/6],
                [0,   1/6, 5/12, 5/12],
                [0,   1/6, 5/12, 5/12]
            ]),
            normalize_weight_matrix(np.array([
                [1, 1, 0, 0],
                [1, 1, 1, 1],
                [0, 1, 1, 1],
                [0, 1, 1, 1]
            ]))
        )
