import numpy as np
import matplotlib.pyplot as plt
from find_slope_time import find_slope_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate


path = '/home/tgd323/OpenFoamStudy/run/1Dreact'
n = 1000
field_name = 'H2O'

T, slope_time = find_slope_time(path, n, field_name)

left_t_lim = 1
right_t_lim = 6
x = np.linspace(0, 1, n)

# plot_time_flame_coordinate(T, slope_time)
plot_time_flame_speed(T, slope_time, left_t_lim, right_t_lim)
plt.show()

