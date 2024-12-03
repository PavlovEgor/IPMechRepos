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


shp = (110, 4000)

V=Ofpp.parse_internal_field('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/2D/Hele-Shaw/l=200mm,w=5.5mm/ClPhi=1.0Xi=1e-6/0.00279971/Qdot')
V = V.reshape(shp)

# x, y = find_slope(V, 0.05)
# print(x)
# t = np.zeros(shp)
#
# t.T[int(x / 0.05)] = 2*y*np.ones(70)
# V += t

plt.imshow(V)

plt.show()

# a = np.array([[1, 3], [2, 4], [5, 6]])
# b = a.reshape((1, 6))[0]
# print(b)
# print(b.argsort()[-2:][::-1] % 2)
# # ind = np.argpartition(a, -4)[-4:]
#
# # print(a[a.argsort()[-2:][::-1]])