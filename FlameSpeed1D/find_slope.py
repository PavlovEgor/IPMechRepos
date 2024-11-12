import numpy as np


def find_slope(data, dx) -> float:

    # Вычисление производной
    derivative = np.diff(data)

    # Нахождение индекса максимальной производной
    max_derivative_index = np.argmax(np.abs(derivative)[:-10])

    # Координата скачка
    jump_coordinate = dx * max_derivative_index

    return jump_coordinate