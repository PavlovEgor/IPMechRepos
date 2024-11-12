import openfoamparser_mai as Ofpp
import matplotlib.pyplot as plt
import numpy as np


def find_slope(data: np.array, dx: float) -> (float, float):  # find mean max Q_dot coordinate

    ny, nx = data.shape
    k = 20
    tmp = data.reshape((1, nx * ny))[0]

    jump_coordinate = dx * np.mean(tmp.argsort()[-k:][::-1] % nx)
    ampl = np.mean(tmp[tmp.argsort()[-k:][::-1]])
    return jump_coordinate, ampl


shp = (70, 4000)

V=Ofpp.parse_internal_field('Qdot')
V = V.reshape(shp)

x, y = find_slope(V, 0.05)
print(x)
t = np.zeros(shp)

t.T[int(x / 0.05)] = 2*y*np.ones(70)
V += t

plt.imshow(V)

plt.show()

# a = np.array([[1, 3], [2, 4], [5, 6]])
# b = a.reshape((1, 6))[0]
# print(b)
# print(b.argsort()[-2:][::-1] % 2)
# # ind = np.argpartition(a, -4)[-4:]
#
# # print(a[a.argsort()[-2:][::-1]])