import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/75CH4-25H2-air-6-step3D_DyM'


Data = pd.DataFrame({'Time': np.array([]),
                     'FlamaArea': np.array([]),
                     'Qdot_integral': np.array([]),
                     'WallHeatFlux': np.array([])})

def read_AFlame_volIntegrate(file_path):
    T = []
    S = []

    with open(file_path) as file:
        while line := file.readline():
            if line[0] == '#':
                continue

            else:
                t, s = list(map(float, line.split()))
                T.append(t)
                S.append(s)
    file.close()
    return np.array(T), np.array(S)


def read_Qdot_volIntegrate(file_path):
    T = []
    Q = []

    with open(file_path) as file:
        while line := file.readline():
            if line[0] == '#':
                continue

            else:
                t, q = list(map(float, line.split()))
                T.append(t)
                Q.append(q)
    file.close()
    return np.array(T), np.array(Q)

def read_wallHeatFlux1(file_path):
    T = []
    H = []
    patches = []

    def find_patches():
        with open(file_path) as file:
            while line := file.readline():
                if line[0] == '#':
                    continue

                else:
                    t, patch, min_, max_, h = line.split()

                    if patch in patches:
                        file.close()
                        break
                    else:
                        patches.append(patch)

    find_patches()
    with open(file_path) as file:

        while line := file.readline():
            if line[0] == '#':
                continue

            else:
                h_tmp = 0
                for i in range(len(patches)):
                    t, patch, min_, max_, h = line.split()
                    h_tmp += float(h)
                T.append(float(t))
                H.append(h_tmp)

    return np.array(T), np.array(H)


T, H = read_wallHeatFlux1('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/75CH4-25H2-air-6-step3D_DyM/postProcessing/wallHeatFlux1/0.00900758/wallHeatFlux_0.00900758.dat')

plt.plot(T, H)
plt.show()