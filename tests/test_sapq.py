import numpy as np
from src.sapq.qubo import to_qubo_cost_matrix
from src.sapq.classical_baselines import simulated_annealing

def test_qubo_annealing():
    n = 16
    Q = to_qubo_cost_matrix(n)
    def cost(x):
        return float(x @ Q @ x)
    best_x, best_cost = simulated_annealing(cost, n=n, steps=200)
    assert isinstance(best_cost, float)
