"""


"""
import os
import numpy as np
from scipy import interpolate
from scipy.optimize import curve_fit
import openfoamparser_mai as Ofpp


class Data:
    def __init__(self, path_of_case: str, dim: int, shape_of_mesh=(0, 0)):
        self.path_of_case = path_of_case
        self.dim = dim
        if dim != 1:
            self.shape_of_mesh = shape_of_mesh
            if shape_of_mesh == (0, 0):
                print("In 2D mesh don't specified shape of mesh")

    def load_field_in_time_moment(self, time_name: str, field_name: str) -> np.array:
        field = Ofpp.parse_internal_field(self.path_of_case + '/' + time_name + '/' + field_name)

        if type(field) == float:  # uniform field
            if self.dim != 1:
                field = np.ones_like(self.shape_of_mesh) * field
            elif self.dim == 1:
                field = np.ones_like(self.shape_of_mesh) * field


        if self.dim == 2:
            field.resize(self.shape_of_mesh)

        return field


    def load_field_Alltime(self):
        pass

    def find_slope_2D(self, time_name: str, scale: float) -> float:  # find mean max Q_dot coordinate
        data = self.load_field_in_time_moment(time_name, 'Qdot')
        ny, nx = data.shape
        k = 20
        tmp = data.reshape((1, nx * ny))[0]

        jump_coordinate = scale * np.mean(tmp.argsort()[-k:][::-1] % nx)
        return jump_coordinate

    def find_slope_1D(self, time_name: str, scale: float) -> float:
        data = self.load_field_in_time_moment(time_name, 'H2O')
        # Вычисление производной
        derivative = np.diff(data)

        # Нахождение индекса максимальной производной
        max_derivative_index = np.argmax(np.abs(derivative)[:-10])

        # Координата скачка
        jump_coordinate = scale * max_derivative_index
        return jump_coordinate

    def find_time(self) -> (list, list):

        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        dir_list = os.listdir(self.path_of_case)
        T = []
        T_name = []

        for name in dir_list:
            if is_float(name):
                T.append(float(name))
                T_name.append(name)

        combined = list(zip(T, T_name))
        sorted_combined = sorted(combined, key=lambda x: x[0])

        return zip(*sorted_combined)



    def line_approximate(self, x, y, left_t_lim=0, right_t_lim=np.inf):

        def line(x, a, b):
            return a * x + b

        def find_interesting_interval(x, y, left, right):
            x0 = np.array(x)
            y0 = np.array(y)

            x1 = x0[x0 > left]
            y1 = y0[x0 > left]

            x2 = x1[x1 < right]
            y2 = y1[x1 < right]

            return x2, y2

        popt, pcov = curve_fit(line, x, y)
        nx, ny = find_interesting_interval(x, line(np.array(x, dtype=np.float64), *popt), left_t_lim,
                                                     right_t_lim)

        return nx, ny

