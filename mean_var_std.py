import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape((3, 3))

    # Compute mean, variance, standard deviation, maximum, minimum, and sum
    mean = arr.mean(axis=0), arr.mean(axis=1), arr.mean()
    variance = arr.var(axis=0), arr.var(axis=1), arr.var()
    standard_deviation = arr.std(axis=0), arr.std(axis=1), arr.std()
    maximum = arr.max(axis=0), arr.max(axis=1), arr.max()
    minimum = arr.min(axis=0), arr.min(axis=1), arr.min()
    total = arr.sum(axis=0), arr.sum(axis=1), arr.sum()

    # Convert the results to lists
    mean = [m.tolist() for m in mean]
    variance = [v.tolist() for v in variance]
    standard_deviation = [s.tolist() for s in standard_deviation]
    maximum = [max_val.tolist() for max_val in maximum]
    minimum = [min_val.tolist() for min_val in minimum]
    total = [t.tolist() for t in total]

    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": maximum,
        "min": minimum,
        "sum": total
    }

    return calculations
