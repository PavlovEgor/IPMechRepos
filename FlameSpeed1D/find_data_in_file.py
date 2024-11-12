import numpy as np


def find_data_in_file(filename, n, writeType='ascii') -> np.array:
    type = 'r'

    if writeType == 'binary':
        type = 'rb'


    with open(filename, type) as file:
        tmp = np.empty(n)
        while line := file.readline():
            if line == 'internalField   nonuniform List<scalar> \n' or line == b'internalField   nonuniform List<scalar> \n':

                file.readline()
                file.readline()

                for i in range(n):

                    line = file.readline()
                    if writeType == 'ascii':
                        tmp[i] = float(line.rstrip())
                    elif writeType == 'binary':
                        tmp[i] = float(line.decode('ascii').rstrip())

                file.close()
                break

    return tmp

# print(find_data_in_file('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=0.05/0.0010009/H2O',
#                         1000,
#                         'binary'))