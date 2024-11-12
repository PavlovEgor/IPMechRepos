import numpy as np
from scipy import interpolate
from scipy.optimize import curve_fit


def der(t, x) -> np.array:

    tck = interpolate.splrep(t, x)

    return interpolate.splev(t, tck, der=1)


def line(x, a, b):
    return a * x + b


def line_approximate(x, y):

    popt, pcov = curve_fit(line, x, y)

    return popt