import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

N = 200
X = 20
mesh = np.linspace(0, X, N)
t = np.empty_like(mesh)
n = 7


# for i in range(N):
#     def F(t):
#         return  np.log((t - 1) / (n - 1)) + mesh[i]
#
#     def F_prime(t):
#         return 1 / (t - 1)
#
#
#     t[i] = newton(F, t[i-1] if i != 0 else n, maxiter=3000, fprime=F_prime)
#     print(i, t[i])
def Analitical_T(x):
    return 1 / (1 - ((n - 1) / n) * np.exp(-x))

def second(x):
    return 1 + (n-1) * np.exp(-x)

# plt.plot(mesh, t, c='red')
plt.plot(mesh, Analitical_T(mesh), c='red')
plt.plot(mesh, second(mesh), c='blue')
plt.ylim(1, n + 1)
plt.xlim(0, X)
plt.show()


