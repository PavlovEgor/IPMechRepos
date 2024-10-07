import matplotlib.pyplot as plt
import numpy as np
from find_speed import der
from find_interesting_interval import find_interesting_interval

def plot_time_flame_coordinate(x, y):

    plt.plot(x, y)
    plt.xlabel('Время, с')
    plt.ylabel('Координата пламени')
    plt.title('Зависимость положения пламени от времени')


def plot_time_flame_speed(x, y, left_t_lim=0, right_t_lim=np.infty):

    plt.plot(*find_interesting_interval(x[1:], der(x, y), left_t_lim, right_t_lim))
    plt.xlabel('Время, с')
    plt.ylabel('Скорость пламени')
    plt.title('Зависимость скорости пламени от времени')


