"""


"""

import matplotlib.pyplot as plt
import numpy as np

from Data import Data



class Plotting:
    def __init__(self, path_of_case: str, dim: int, shape_of_mesh=(0, 0), figsize=(12, 8)):
        self.path_of_case = path_of_case
        self.dim = dim
        self.figsize = figsize

        self.Data = Data(path_of_case, dim, shape_of_mesh)

    def plot_time_flame_coordinate(self, left_t_lim=0, right_t_lim=np.inf, scale=1):
        """
        plot figure x - time, y - position of flame: max Qdot point
        """
        T, T_name = self.Data.find_time()
        slope_time = np.empty(len(T))

        if self.dim == 1:
            for i, time_name in enumerate(T_name):
                slope_time[i] = self.Data.find_slope_1D(time_name, scale)

        elif self.dim == 2:
            for i, time_name in enumerate(T_name):
                slope_time[i] = self.Data.find_slope_2D(time_name, scale)

        fig, ax = plt.subplots(figsize=self.figsize)

        ax.plot(T, slope_time)


        plt.plot(*self.Data.line_approximate(T, slope_time, left_t_lim, right_t_lim))

        Y = np.max(slope_time)
        plt.plot([left_t_lim, left_t_lim], [0, Y], c='tab:red')
        plt.plot([right_t_lim, right_t_lim], [0, Y], c='tab:red')



    def plot_field_in_time_moment(self, time_name: str, field_name: str, scale=1/30):

        fig, ax = plt.subplots(figsize=self.figsize)
        field = self.Data.load_field_in_time_moment(time_name, field_name)

        if self.dim == 1:
            x = np.arange(field.shape[0]) * scale

            ax.plot(x, field)

        return ax

    def create_legend(self, ax, title='', xlabel='', ylabel=''):
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

path = r'C:\Users\Mi\Documents\PycharmProjects\IPMechRepos'
time_name = '1D_time_moment'
P = Plotting(path, 1)
ax = P.plot_field_in_time_moment(time_name, 'H2O')
# P.create_legend(ax, 'gg', 'ff', 'yy')
plt.show()
