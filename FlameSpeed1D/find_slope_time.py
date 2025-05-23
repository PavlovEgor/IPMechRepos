import numpy as np
from FlameSpeed1D.find_time_steps import find_time
from FlameSpeed1D.find_data_in_file import find_data_in_file
from FlameSpeed1D.find_slope import find_slope


def find_slope_time(path, n, field_name, dx, writeType='ascii') -> (list, list):

    T, T_name = find_time(path)
    slope_time = np.empty(len(T))

    for i, t_name in enumerate(T_name):
        slope_time[i] = find_slope(find_data_in_file(path + '/' + t_name + '/' + field_name, n, writeType), dx)

    return T, slope_time