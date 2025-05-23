import matplotlib.pyplot as plt
import numpy as np


def f(L, L0, b):
    return (-2 * ((10 / (3 * L)) - (7 * b / 900) * np.log(300 - b*L) + (7 * b / 900) * np.log(b*L)) -
            (-2 * ((10 / (3 * L0)) - (7 * b / 900) * np.log(300 - b*L0) + (7 * b / 900) * np.log(b*L0))))

L = np.linspace(0.1, 1, 100)
t = f(L, 0.01, 10)

plt.plot(t, L)
plt.show()