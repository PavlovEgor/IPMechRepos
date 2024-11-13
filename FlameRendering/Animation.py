"""


"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable

from Data import Data


class Animation:
    def __init__(self, path_of_case: str, dim: int, shape_of_mesh=(0, 0), figsize=(12, 8)):
        self.path_of_case = path_of_case
        self.dim = dim
        self.figsize = figsize
        self.Data = Data(path_of_case, dim, shape_of_mesh)

    def time_iter(self, fig, ax, cax, i, T_name, field_name='Qdot', scale=1):
        field = self.Data.load_field_in_time_moment(T_name[i], field_name)
        if self.dim == 1:
            x = np.arange(field.shape[0]) * scale
            ax.plot(x, field)

        elif self.dim == 2:
            # x, y = np.mgrid[:field.shape[0], :field.shape[1]]
            # pos = ax.contourf(field, cmap='Reds')
            pos = ax.imshow(field, cmap='Reds', interpolation='bilinear')
            fig.colorbar(pos, cax=cax, orientation="horizontal")


    def make_amine(self, field_name: str, scale=1):
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111)
        div = make_axes_locatable(ax)
        cax = div.append_axes('bottom', size="50%", pad=0.25)

        T, T_name = self.Data.find_time()

        def update_frame(i):
            self.time_iter(fig, ax, cax, i, T_name[1:], field_name, scale)


        ani = animation.FuncAnimation(fig, update_frame, frames=len(T) - 1, repeat=False)
        plt.show()
