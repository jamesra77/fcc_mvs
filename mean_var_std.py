import numpy as np
import pprint

def calculate(list):
    calculations = {}

    # raise ValueError if passed in list doesn't contain 9 elements
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # convert list to 3x3 np array
    a = np.array(list).reshape((3,3))

    # calculate means
    mean0 = np.mean(a, axis=0).tolist()
    mean1 = np.mean(a, axis=1).tolist()
    mean = float(np.mean(a))
    calculations["mean"] = [mean0, mean1, mean]

    # calculate variances
    var0 = np.var(a, axis=0).tolist()
    var1 = np.var(a, axis=1).tolist()
    var = float(np.var(a))
    calculations["variance"] = [var0, var1, var]

    # calculate std devs
    s0 = np.std(a, axis=0).tolist()
    s1 = np.std(a, axis=1).tolist()
    s = float(np.std(a))
    calculations["standard deviation"] = [s0, s1, s]

    # calculate extrema and sum
    max0 = np.max(a, axis=0).tolist()
    max1 = np.max(a, axis=1).tolist()
    max = int(np.max(a))
    calculations["max"] = [max0, max1, max]

    min0 = np.min(a, axis=0).tolist()
    min1 = np.min(a, axis=1).tolist()
    min = int(np.min(a))
    calculations["min"] = [min0, min1, min]

    sum0 = np.sum(a, axis=0).tolist()
    sum1 = np.sum(a, axis=1).tolist()
    sum = int(np.sum(a))
    calculations["sum"] = [sum0, sum1, sum]


    return calculations