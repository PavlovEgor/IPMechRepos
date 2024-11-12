import matplotlib.pyplot as plt
import numpy as np
from find_speed import der, line_approximate, line
from find_interesting_interval import find_interesting_interval

def plot_time_flame_coordinate(x, y, field_name, left_t_lim=0, right_t_lim=np.infty):

    y_in_cm = 100 * y

    plt.plot(x, y_in_cm)
    plt.xlabel('Время, с')
    plt.ylabel('Координата пламени, см')
    a, b = line_approximate(*find_interesting_interval(x, y_in_cm, left_t_lim, right_t_lim))
    nx, ny = find_interesting_interval(x, line(np.array(x, dtype=np.float64), a, b), left_t_lim, right_t_lim)
    plt.plot(nx, ny)

    plt.title(
        f'Зависимость положения пламени от времени по {field_name} \n {a} cm/s')

    Y = np.max(y_in_cm)

    plt.plot([left_t_lim, left_t_lim], [0, Y], c='tab:red')
    plt.plot([right_t_lim, right_t_lim], [0, Y], c='tab:red')

def plot_time_flame_speed(x, y, field_name, left_t_lim=0, right_t_lim=np.infty):
    nx, ny = find_interesting_interval(x, 100*der(x, y), left_t_lim, right_t_lim)
    plt.plot(nx, ny)
    plt.xlabel('Время, с')
    plt.ylabel('Скорость пламени, cм/с')
    plt.title(f'Зависимость скорости пламени от времени по {field_name} \n средняя скорость {np.mean(ny)}')

