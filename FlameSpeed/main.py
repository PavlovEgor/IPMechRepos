import matplotlib.pyplot as plt
import numpy as np

from find_slope_time import find_slope_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate
from find_num_of_cells import find_n

dir = 'OpPhi=1Xi=1e-6'
# path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/1Step/1D/CHEMreactingFoam/' + dir
# path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/CH4-1step/' +dir
path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/OpPhi=1Xi=1e-6'
# path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=0.05'
# path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/1Step/1D/CHEMCantera/' + dir

writeType = 'ascii'
field_name = 'H2O'
n = find_n(path + '/0/T', writeType)
print(n)

T, slope_time = find_slope_time(path, n, field_name, writeType)

left_t_lim = 0.2
right_t_lim = 2.0

plot_time_flame_coordinate(T, slope_time, field_name)
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

