import numpy as np
from scipy import interpolate


def der(t, x) -> np.array:

    tck = interpolate.splrep(t, x)

    return interpolate.splev(t, tck, der=1)



