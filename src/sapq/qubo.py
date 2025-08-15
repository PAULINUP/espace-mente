from __future__ import annotations
import numpy as np

def to_qubo_cost_matrix(n: int, penalty: float = 2.0) -> np.ndarray:
    Q = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        Q[i, i] += 1.0
    for i in range(n - 1):
        Q[i, i + 1] -= 0.2
        Q[i + 1, i] -= 0.2
    for i in range(n):
        Q[i, i] += penalty * (1.0 / n)
    return Q
