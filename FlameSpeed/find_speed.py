import numpy as np


def der(t, x) -> np.array:
    dy = np.diff(x)
    dx = np.diff(t)
    derivative = dy / dx

    return derivative
