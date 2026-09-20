import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    a_nd: np.ndarray = np.asarray(A)
    n, m = a_nd.shape
    trans = np.zeros((m, n), dtype=a_nd.dtype)
    for i in range(n):
        for j in range(m):
            trans[j, i] = a_nd[i, j]
    return trans