import numpy as np
from find_time_steps import find_time
from find_data_in_file import find_data_in_file
from find_slope import find_slope


def find_slope_time(path, n, field_name) -> (list, list):

    T, T_name = find_time(path)
    slope_time = np.empty(len(T))

    for i, t_name in enumerate(T_name):
        slope_time[i] = find_slope(find_data_in_file(path + '/' + t_name + '/' + field_name, n), n)

    return T, slope_time