import matplotlib.pyplot as plt
import numpy as np


Phi = [0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1]

FS = np.array([130, 176, 222, 278, 330, 325, 335])
Ux = np.array([115, 150, 191, 243, 285, 280, 295])
plt.plot(Phi, FS-Ux)
plt.show()
