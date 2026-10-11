from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    lenght = len(x)
    sorted_x = sorted(x)
    if lenght == 0:
        return None
    counts = {}
    mode = sorted_x[0]
    maxCount = 1
    sum = 0

    for i in range(lenght):
        number = sorted_x[i]
        sum += number
        currentCount = counts.get(number, 0) + 1
        if currentCount > maxCount:
            mode = number
            maxCount = currentCount 
        counts[number] = currentCount

    if lenght % 2 == 0:
        median = (sorted_x[lenght // 2 - 1] + sorted_x[lenght // 2]) / 2
    else:
        median = float(sorted_x[lenght // 2])

    return {"mean": sum / lenght, "median": median, "mode": float(mode)}