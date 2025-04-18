import matplotlib.pyplot as plt
import numpy as np

from find_slope_time import find_slope_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate
from find_num_of_cells import find_n

dir = 'ClPhi=0.8Xi=0.3'

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/OpPhi=1.1Xi=0.3/'


writeType = 'ascii'
field_name = 'H2O'
n = find_n(path + '/0/T', writeType)
dx = 0.05 / 1000  # [mm]
print(n)

T, slope_time = find_slope_time(path, n, field_name, dx, writeType)

left_t_lim = 0.01
right_t_lim = 0.1

plot_time_flame_coordinate(T, slope_time, field_name, left_t_lim, right_t_lim)
# plot_time_flame_speed(T, slope_time, field_name, left_t_lim, right_t_lim)
# plt.savefig('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/FlameSpeedData/' + dir + 'Speed' + '.png')
# plt.savefig('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/FlameSpeedData/' + dir + 'pos' + '.png')
# plt.savefig('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/FlameSpeedData/' + dir + 'Ti=2000, cells=3000' + '.png')
# plt.savefig('/home/tgd323/OpenFOAM/tgd323-v2406/run/1Step/1D/CHEMCantera/FlameSpeedData/' + dir + 'Speed' + '.png')
# t = np.linspace(left_t_lim, right_t_lim, 1000)
# Tb = 2000
# T0 = 300
# alpha = 1
# cp = 1
# rho0 = 1
# beta = alpha / (cp * rho0)
# D = 37 / (1 - ((Tb - T0) / Tb) * np.exp(-beta * t))
# plt.plot(t, D)
plt.plot()
plt.show()

