

def find_n(filename, writeType='ascii'):
    type = 'r'

    if writeType == 'binary':
        type = 'rb'

    with open(filename, type) as file:

        while line := file.readline():
            if line == b'internalField   nonuniform List<scalar> \n' or line == 'internalField   nonuniform List<scalar> \n':
                return int(file.readline()[:-1])

# print(find_n('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/ClPhi=1Xi=0.05/0.0010009/H2O'))

