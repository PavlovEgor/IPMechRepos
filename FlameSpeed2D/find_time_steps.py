import os


def is_float(value):
    try:
        a = float(value)
        if a > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def find_time(dir_name='../1Dreact') -> (list, list):
    dir_list = os.listdir(dir_name)
    T = []
    T_name = []

    for name in dir_list:
        if is_float(name):
            T.append(float(name))
            T_name.append(name)

    combined = list(zip(T, T_name))
    sorted_combined = sorted(combined, key=lambda x: x[0])

    return zip(*sorted_combined)