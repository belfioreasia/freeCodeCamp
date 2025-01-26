import numpy as np


def calculate(in_list):
    """
    input  --> list of 9 digits
    output --> {mean, variance, standard deviation, max, min, sum}
                dictionary for each row, column, and element 
                in a 3 x 3 matrix 
    """
    if len(in_list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        m = np.array(in_list).reshape(3, 3)
        mean = [list(m.mean(axis=0)), list(m.mean(axis=1)), m.mean()]
        var = [list(m.var(axis=0)), list(m.var(axis=1)), m.var()]
        std = [list(m.std(axis=0)), list(m.std(axis=1)), m.std()]
        max = [list(m.max(axis=0)), list(m.max(axis=1)), m.max()]
        min = [list(m.min(axis=0)), list(m.min(axis=1)), m.min()]
        sum = [list(m.sum(axis=0)), list(m.sum(axis=1)), m.sum()]
        return {
            "mean": mean,
            "variance": var,
            "standard deviation": std,
            "max": max,
            "min": min,
            "sum": sum
        }
