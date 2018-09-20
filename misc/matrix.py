#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
__all__ = ['normalize_weight_matrix']


def normalize_weight_matrix(M: np.ndarray) -> np.ndarray:
    """Converts a symmetric adjacency matrix to a corresponding weight matrix.

    Given matrix must be a symmetric adjacency (binary) matrix whose corresponding graph is connected and undirected.
    Returned matrix satisfies the following properties:
        1. every element is nonnegative and the matrix is symmetric,
        2. zeroness and positivity of each element are kept, and
        3. the sum of any column or any row is 1.
    """
    M = M.astype(np.float64)
    for i in range(M.shape[0]):
        sum_ = np.sum(M[i, i:])
        if sum_ > 0.:
            M[i, i:] *= (1. - np.sum(M[i, :i])) / sum_
            M[i + 1:, i] = M[i, i + 1:]
    return M
