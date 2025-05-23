import numpy as np
import matplotlib.pyplot as plt


n = 7

def T_article(t, t_):
    return 1 / (1 - (1 - (1 / n)) * np.exp(- (t - t_)))

def x_article(t, t_):
    return t_ + np.log((1 - (1 - (1/n)) * np.exp(-t)) / (1 - (1 - (1/n)) * np.exp(-(t - t_))))

def T_inf(x):
    return 1 + (n - 1) * np.exp(-x)

t = 1
t_ = np.linspace(0, t, 1000)
X = x_article(t, t_)
X = X[-1] - X
T_a = T_article(t, t_)
T_mi = T_inf(X)

plt.plot(X, np.log((T_a - 1) / (n - 1)) + X)
# plt.plot(X, T_mi)
plt.show()