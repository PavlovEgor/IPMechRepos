import openfoamparser_mai as Ofpp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def is_float(value):
    try:
        a = float(value)
        if a > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def find_time(dir_name) -> (list, list):
    dir_list = os.listdir(dir_name)
    T = []
    T_name = []

    for name in dir_list:
        if is_float(name):
            T.append(float(name))
            T_name.append(name)

    combined = list(zip(T, T_name))
    sorted_combined = sorted(combined, key=lambda x: x[0])

    return zip(*sorted_combined)


# path = r"/home/tgd323/OpenFOAM/tgd323-v2406/run/H2/Phi=0_7_Xi=0_7_X640_Y240/"
# shp = (14, 240, 640)

path = r"/home/tgd323/OpenFOAM/tgd323-v2406/run/H2/Phi=0_7_Xi=0_7_X640_Y240/"
shp = (14, 240, 640)

# path = r"/reserve/Projects/LamFlame/H2_CH4_air/Phi=0_7_Xi=0_7_X330_Y330/"
# shp = (35, 330, 330)


A = np.zeros((shp[1], shp[2]))
T, T_name = find_time(path)
k = 10

for t_name in T_name[::k]:
    Qdot = Ofpp.parse_internal_field(path + t_name + '/Qdot')  # скорость массив из векторов [Ux, Uy, Uz] | shape = (n, 3)
    A += Qdot.reshape(shp)[shp[0]-1, :, :]

plt.imshow(-A, cmap='RdYlBu')
plt.show()