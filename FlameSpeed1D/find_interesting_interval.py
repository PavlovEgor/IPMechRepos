import numpy as np


def find_interesting_interval(x, y, left, right):
    x0 = np.array(x)
    y0 = np.array(y)

    x1 = x0[x0 > left]
    y1 = y0[x0 > left]

    x2 = x1[x1 < right]
    y2 = y1[x1 < right]

    return x2, y2



