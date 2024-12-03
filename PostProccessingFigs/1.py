import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/75CH4-25H2-air-6-step3D_DyM'

class PastProcessingData:

    def __init__(self):
        self.Data = pd.DataFrame({'Time': np.array([]),
                     'FlamaArea': np.array([]),
                     'Qdot_integral': np.array([]),
                     'WallHeatFlux': np.array([])})

    def plot_flame_area_t(self):
        plt.plot(self.Data['Time'].array, self.Data['FlamaArea'].array)
        plt.show()

    def plot_Qdot_t(self):
        plt.plot(self.Data['Time'].array, self.Data['Qdot_integral'].array)
        plt.show()

    def read_two_column_data_file(self, filename):
        X = []
        Y = []

        with open(filename) as file:
            while line := file.readline():
                if line[0] == '#':
                    continue

                else:
                    x, y = list(map(float, line.split()))
                    X.append(x)
                    Y.append(y)
        file.close()
        return np.array(X), np.array(Y)

    def read_AFlame_volIntegrate(self, filename):
        self.Data["Time"], self.Data["FlamaArea"] = self.read_two_column_data_file(filename)

    def read_Qdot_volIntegrate(self, filename):
        self.Data["Time"], self.Data["Qdot_integral"] = self.read_two_column_data_file(filename)

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
                        try:
                            t, patch, min_, max_, h = line.split()
                            print(t)
                            h_tmp += float(h)
                            line = file.readline()
                        except Exception:
                            break

                    T.append(float(t))
                    H.append(h_tmp)

        return np.array(T), np.array(H)




D = PastProcessingData()
D.read_AFlame_volIntegrate('/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/75CH4-25H2-air-6-step3D_DyM/postProcessing/AFlame_volIntegrate/0.00900758/volFieldValue_0.00900758.dat')
D.plot_flame_area_t()
print(D.Data["Time"], D.Data["FlamaArea"])
