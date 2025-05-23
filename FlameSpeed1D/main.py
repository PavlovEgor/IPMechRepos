from cProfile import label

import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

from FlameSpeed1D.find_interesting_interval import find_interesting_interval
from find_slope_time import find_slope_time
from Plotting_results import plot_time_flame_speed, plot_time_flame_coordinate
from find_num_of_cells import find_n

T_0 = 300
T_b = 2400
n = 8
alpha = 10
cp = 1040
rho0 = 1.18
un = 3.58
mu = 1e-2

dir = 'ClPhi=0.8Xi=0.3'

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=1e-6n=1600MA'


writeType = 'ascii'
field_name = 'H2O'
n = 16000 # find_n(path + '/0.100005/T', writeType)
dx = 1 / 16000  # [mm]
print(n)

T, slope_time = find_slope_time(path, n, field_name, dx, writeType)

from scipy.signal import find_peaks

# Пример данных волнистой кривой (синусоидальный сигнал)
t = np.array(T[60:120]) #np.linspace(0, 10, 1000)  # Время от 0 до 10 секунд
signal = np.array(slope_time[60:120]) - 2.42 * t # np.sin(2 * np.pi * 0.5 * t) + 0.5 * np.sin(2 * np.pi * 2 * t)  # Сигнал с двумя частотами

# Нахождение всех максимумов
peaks, _ = find_peaks(signal)

# Построение графика сигнала и максимумов
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Сигнал')
plt.plot(t[peaks], signal[peaks], "x", label='Максимумы')
plt.title('Сигнал и его максимумы')
plt.xlabel('Время [с]')
plt.ylabel('Амплитуда')
plt.legend()
plt.show()

# Вывод индексов и значений максимумов
print('Индексы максимумов:', peaks)
print('Значения максимумов:', signal[peaks])
print('Time:', t[peaks])


# Вычисление разностей между соседними измерениями
differences = np.diff(t[peaks])

# Вычисление среднего значения разностей
period = np.mean(differences)

print(f'Период колебаний: {period} с, частота: {1 / period} Гц')

left_t_lim = 0.4
right_t_lim = np.inf

plot_time_flame_coordinate(T , slope_time, field_name, left_t_lim, right_t_lim)
# plt.plot(np.array(T[2:-100]), np.array(slope_time[2:-100]))
# plt.xlim(2, 2.9)
plt.ylim(0, 100)
plt.xlabel(r'Время, с')
plt.ylabel(r'Положение фронта, см')

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

# plt.plot()
#
# plt.plot()
plt.show()

import openfoamparser_mai as Ofpp
M = 4
D = []
x_max = []
Dt = len(T) // M
for i in range(1, M-1):
    D.append(Ofpp.parse_internal_field('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=1e-6/' + f"{T[i * Dt]}"+'/T'))
    x_max.append(slope_time[i * Dt])
D.append( Ofpp.parse_internal_field('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=1e-6/' + f"{T[-1]}"+'/T'))
x_max.append(slope_time[-1])
# plt.plot(data)
# plt.show()
# for _ in range(len(T)):
#     print(T[_], slope_time[_])

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = "16"
plt.rcParams['figure.figsize'] = [9, 6]




def T_article(t, t_):
    return 1 / (1 - (1 - (1 / n)) * np.exp(- (t - t_)))

def x_article(t, t_):
    return t_ + np.log((1 - (1 - (1/n)) * np.exp(-t)) / (1 - (1 - (1/n)) * np.exp(-(t - t_))))

x0 = alpha / (un * cp * rho0)
t0 = alpha / (cp * rho0)

t = 0.13
t_ = np.linspace(0, t, 3000)
X2 = x_article(t, t_)
T2 = T_article(t, t_)
X2 = X2[-1] - X2


from find_speed import der, line_approximate, line

mar = ['--', ':', '-.']
for i in range(M-1):



    X1 = -(np.linspace(0, x0, 3000) - x_max[i] * x0 )
    T1 = D[i] / T_0
    Y = -np.log(T1 - 1) + np.log(n - 1)
    U, V = find_interesting_interval(X1, Y, 0, 3)
    ind_of_min = np.argmin(V)
    a, b = line_approximate(U, V)

    plt.plot(-U, -(V - b),
             label=fr"$\tau = {round(T[(i + 1) * Dt] * alpha / (cp * rho0), 1)}$", linewidth=3., ls=mar[i])

plt.plot(-U, -U, "r-", label='аналитическое решение')

import pandas as pd

# df = pd.DataFrame({'coord': X1, 'temp': T1})
# df.to_csv(f'a={alpha}_mu=0.1_tau={round(T[-1] * alpha / (cp * rho0), 3)}.csv')

# plt.plot(X1, T1, label=fr"$\alpha={alpha}, \; \mu=0.1, \; \tau={round(T[-1] * alpha / (cp * rho0), 3)}$")
plt.title(r"$\alpha = 6500$")
plt.xlabel(r"$\xi - \xi_{front}$")
plt.ylabel(r"$-\ln \frac{\theta - 1}{\theta_{max} - 1}$", fontsize=20.)

plt.xlim(-2, 0)
plt.ylim(-2, 0)

# plt.title("Профиль температуры за пламенем \n" + rf"$\tau = {round(T[-1] * alpha / (cp * rho0), 3)}$")
# plt.xlabel(r"$\alpha / (u_n C_p \rho_0) (x_f - x)$")
# plt.ylabel(r"$T/T_0$")
plt.legend(fontsize=18.)
plt.show()

# df2 = pd.read_csv("a=1000_mu=0.1_tau=2.44.csv")
# plt.plot(df2["coord"].array, -np.log(df2["temp"].array - 1) + np.log(n - 1), label=r"$\alpha=1000, \; \mu=0.1, \; \tau=2.44$")

# df3 = pd.read_csv("a=1200_mu=0.1_tau=2.249.csv")
# plt.plot(df3["coord"].array, -np.log(df3["temp"].array - 1) + np.log(n - 1), label=r"$\alpha=1200, \; \mu=0.1, \; \tau=2.249$")
#
# df4 = pd.read_csv("a=1400_mu=0.1_tau=3.423.csv")
# plt.plot(df4["coord"].array, -np.log(df4["temp"].array - 1) + np.log(n - 1), label=r"$\alpha=1400, \; \mu=0.1, \; \tau=3.423$")
#
# df5 = pd.read_csv("a=2500_mu=0.1_tau=2.444.csv")
# plt.plot(df5["coord"].array, -np.log(df5["temp"].array - 1) + np.log(n - 1), label=r"$\alpha=2500, \; \mu=0.1, \; \tau=2.444$")
#
# df6 = pd.read_csv("a=3500_mu=0.1_tau=3.423.csv")
# plt.plot(df6["coord"].array, -np.log(df6["temp"].array - 1) + np.log(n - 1), label=r"$\alpha=3500, \; \mu=0.1, \; \tau=2.444$")
# plt.plot(X2, T2)


plt.xlabel(r'$\tau$')
plt.ylabel(r'$\xi_{front}$')
# plt.title(f'')

# df = pd.DataFrame({'time': np.array(T[2:]) * alpha / (cp * rho0), 'coord': np.array(slope_time[2:]) * alpha / (cp * rho0 * un)})
# df.to_csv(f'fc_a={alpha}_mu={mu}_tau={round(T[-1] * alpha / (cp * rho0), 3)}.csv')

# df2 = pd.read_csv("fc_a=6500_mu=0.1_tau=5.295.csv")
# plt.plot(df2['time'].array , df2['coord'].array, label=r"$\alpha=6500, \mu = 0.1$", ls=':', lw=3.)
# df3 = pd.read_csv("fc_a=3000_mu=0.1_tau=6.703.csv")
# plt.plot(df3['time'].array , df3['coord'].array, label=r"$\alpha=3000, \mu = 0.1$", ls='--', lw=3.)
df4 = pd.read_csv("fc_a=6500_mu=4.5_tau=15.891.csv")
plt.plot(df4['time'].array , df4['coord'].array, label=r"$\alpha=6500, \mu = 4.5$", ls=':', lw=3.)
df5 = pd.read_csv("fc_a=3000_mu=2.0_tau=5.688.csv")
plt.plot(df5['time'].array , df5['coord'].array, label=r"$\alpha=3000, \mu = 2.0$", ls='--', lw=3.)
plt.plot(np.array(T[2:]) * alpha / (cp * rho0) , np.array(slope_time[2:]) * alpha / (cp * rho0 * un), label=fr"$\alpha={alpha}, \mu = {mu}$", ls='-.', lw=3.)

anal_time = np.linspace(0, 7, 100)
plt.plot(anal_time * alpha / (cp * rho0) , anal_time * alpha / (cp * rho0)  + np.log( 7 - 6 * np.exp(-np.array(anal_time) * alpha / (cp * rho0) )), 'r',label="аналитическое решение")

plt.xlim(0, 5)
plt.ylim(0, 7)
plt.legend()
plt.show()