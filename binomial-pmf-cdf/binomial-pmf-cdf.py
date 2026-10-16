import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    pmf = 0
    cfd = 0
    for index in range(k + 1):
        p_index = math.comb(n, index) * p**index * (1 - p) ** (n - index)
        if index == k:
            pmf = p_index
        cfd += p_index

    return {"pmf": float(pmf), "cdf": float(cfd)}