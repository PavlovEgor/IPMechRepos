import openfoamparser_mai as Ofpp
import numpy as np
import matplotlib.pyplot as plt
from find_time_steps import find_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate


def find_data_in_file(filename: str, shape_of_data: (int, int)) -> np.array:
    data = Ofpp.parse_internal_field(filename)
    return data.reshape(shape_of_data)


def find_slope(data: np.array, dx: float) -> (float, float):  # find mean max Q_dot coordinate

    ny, nx = data.shape
    k = 20
    tmp = data.reshape((1, nx * ny))[0]

    jump_coordinate = dx * np.mean(tmp.argsort()[-k:][::-1] % nx)
    ampl = np.mean(tmp[tmp.argsort()[-k:][::-1]])
    return jump_coordinate


def find_slope_time(path: str, dx: float, shape_of_data: (int, int)) -> (list, list):

    T, T_name = find_time(path)
    slope_time = np.empty(len(T))

    for i, t_name in enumerate(T_name):
        slope_time[i] = find_slope(find_data_in_file(path + '/' + t_name + '/' + 'Qdot', shape_of_data), dx)

    return T, slope_time


shp = (70, 10000)
path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/2D/Hele-Shaw_XZ/l=500mm,w=3.5mm/ClPhi=1.0Xi=1e-6_heatlose'
dx = 0.05
T, slope_time = find_slope_time(path, dx, shp)

left_t_lim = 0.0
right_t_lim = 0.01

plot_time_flame_coordinate(T, slope_time, left_t_lim, right_t_lim)

plt.show()
