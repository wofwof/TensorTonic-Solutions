import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    succ = p
    fail = 1 - succ
    pmf = [fail if result == 0 else succ for result in x]

    # Write code here
    return {"pmf": np.array(pmf), "mean": float(p), "variance": float(p * (1 - p))}