import numpy as np


def find_slope(data, n) -> float:

    # Вычисление производной
    derivative = np.diff(data)

    # Нахождение индекса максимальной производной
    max_derivative_index = np.argmax(np.abs(derivative))

    # Координата скачка
    jump_coordinate = max_derivative_index / n

    return jump_coordinate