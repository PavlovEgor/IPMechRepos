import numpy as np


def find_data_in_file(filename, n) -> np.array:

    with open(filename, 'r') as file:
        tmp = np.empty(n)
        while line := file.readline():
            if line == 'internalField   nonuniform List<scalar> \n':
                file.readline()
                file.readline()

                for i in range(1000):

                    line = file.readline()
                    tmp[i] = float(line.rstrip())

                file.close()
                break

    return tmp