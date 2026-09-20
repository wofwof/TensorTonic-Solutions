import numpy as np

def dot_product(x: list, y: list) -> float:
    x_vec = np.array(x)
    y_vec = np.array(y)
    return float(np.dot(x_vec,y_vec))