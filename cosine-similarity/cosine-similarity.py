import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    x_vec = np.array(a)
    y_vec = np.array(b)

    norm_x = np.linalg.norm(x_vec)
    norm_y = np.linalg.norm(y_vec)
    if norm_x == 0 or norm_y == 0:
        return 0.0

    return float(np.dot(x_vec, y_vec) / (norm_x * norm_y))