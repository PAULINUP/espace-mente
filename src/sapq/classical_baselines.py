from __future__ import annotations
import numpy as np
import random
from typing import Callable

def simulated_annealing(cost_fn: Callable[[np.ndarray], float], n: int, steps: int = 2000, T0: float = 2.0):
    x = np.random.randint(0, 2, size=n).astype(np.int8)
    best_x, best_cost = x.copy(), cost_fn(x)
    T = T0
    for s in range(1, steps + 1):
        i = random.randrange(n)
        x_new = x.copy()
        x_new[i] ^= 1
        c_new = cost_fn(x_new)
        dc = c_new - cost_fn(x)
        if dc < 0 or np.exp(-dc / max(1e-6, T)) > random.random():
            x = x_new
            if c_new < best_cost:
                best_x, best_cost = x.copy(), c_new
        T = T0 * (1 - s / steps)
    return best_x, best_cost
