import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

from FlameSpeed1D.find_slope_time import find_slope_time
from FlameSpeed1D.Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate
from FlameSpeed1D.find_num_of_cells import find_n
import openfoamparser_mai as Ofpp
from scipy.fft import fft, fftfreq

dir = 'ClPhi=0.8Xi=0.3'

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=1e-6'


writeType = 'ascii'
field_name = 'H2O'
n = 3000 # find_n(path + '/0.100005/T', writeType)
dx = 1 / 3000  # [mm]
print(n)

T, slope_time = find_slope_time(path, n, field_name, dx, writeType)
P = []

for t in T[1:]:
    data = Ofpp.parse_internal_field(
        '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=1e-6/' + f"{t}" + '/p')
    P.append(data[-1])

P = np.array(P)

N = len(T)-1
yf = fft(P)
xf = fftfreq(N, T[-1] - T[-2])[:N//2]

plt.plot(xf[100:], 2.0/N * np.abs(yf[0:N//2])[100:])
plt.show()
plt.plot(T[1:], P)
plt.show()