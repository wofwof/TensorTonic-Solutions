import numpy as np

def sample_var_std(x: list) -> dict:
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    
    mean = sum / len(x)
    deviationSum = 0
    for i in range(len(x)):
        deviationSum += (x[i] - mean)**2
    sampleVariance = float(deviationSum / (len(x) - 1))
    std_dev = math.sqrt(sampleVariance)
    return {"variance":sampleVariance,"standard_deviation":std_dev}