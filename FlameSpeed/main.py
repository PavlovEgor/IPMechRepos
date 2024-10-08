import matplotlib.pyplot as plt
from find_slope_time import find_slope_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate
from find_num_of_cells import find_n

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/CH4-H2-CO-6step/Phi=1Xi=0.05'
field_name = 'H2O'
n = find_n(path + '/0/T')
print(n)

T, slope_time = find_slope_time(path, n, field_name)

left_t_lim = 1
right_t_lim = 6

plot_time_flame_coordinate(T, slope_time, field_name)
# plot_time_flame_speed(T, slope_time, field_name, left_t_lim, right_t_lim)
plt.show()

