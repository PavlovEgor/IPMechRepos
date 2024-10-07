import numpy as np
import matplotlib.pyplot as plt
from find_time_steps import find_time
from find_data_in_file import find_data_in_file
from find_slope import find_slope
from find_speed import der
from find_interesting_interval import find_interesting_interval

n = 1000
path = '/home/tgd323/OpenFoamStudy/run/1Dreact'
field_name = 'H2O'
T, T_name = find_time(path)
x = np.linspace(0, 1, n)
slope_time = np.empty(len(T))
Data = np.empty((n, len(T)))

for i, t_name in enumerate(T_name):
    slope_time[i] = find_slope(find_data_in_file(path + '/'+ t_name + '/' + field_name, n), n)

plt.plot(T, slope_time)
# left_t_lim = 1
# right_t_lim = 6
#
# plt.plot(*find_interesting_interval(T[1:], der(T, slope_time), left_t_lim, right_t_lim))
plt.show()

