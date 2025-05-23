import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class PastProcessingData:

    def __init__(self):
        self.Data = pd.DataFrame({'Time': np.array([]),
                     'FlamaArea': np.array([]),
                     'Qdot_integral': np.array([]),
                     'WallHeatFlux': np.array([])})

    def plot_flame_area_t(self, save=False):
        plt.plot(self.Data['Time'].array, self.Data['FlamaArea'].array)
        plt.title("Зависимость площади пламени от времени")
        plt.ylabel("Площадь, м^-2")
        plt.xlabel("Время, с")
        plt.grid(True)
        if save:
            plt.savefig("flame_area_t.png")
        plt.show()

    def plot_Qdot_t(self, save=False):
        plt.plot(self.Data['Time'].array, self.Data['Qdot_integral'].array)
        plt.title("Зависимость выделяемой энергии от времени")
        plt.ylabel("Qdot, Вт")
        plt.xlabel("Время, с")
        plt.grid(True)
        if save:
            plt.savefig("Qdot_t.png")
        plt.show()

    def plot_WallHeatFlux_t(self, save=False):
        plt.plot(self.Data['Time'].array, self.Data['WallHeatFlux'].array)
        plt.title("Зависимость потока тепла через стенки от времени")
        plt.ylabel("Поток, Вт")
        plt.xlabel("Время, с")
        plt.grid(True)
        if save:
            plt.savefig("WallHeatFlux_t.png")
        plt.show()

    def plot_flame_area_Qdot(self, save=False):
        plt.plot(self.Data['FlamaArea'].array, self.Data['Qdot_integral'].array)
        plt.title("Зависимость выделяемой энергии от площади пламени")
        plt.xlabel("Площадь, м^-2")
        plt.ylabel("Qdot, Вт")
        plt.grid(True)
        if save:
            plt.savefig("flame_area_Qdot.png")
        plt.show()

    def plot_flame_area_WHF(self, save=False):
        plt.plot(self.Data['FlamaArea'].array, self.Data['WallHeatFlux'].array)
        plt.title("Зависимость потока тепла через стенки от площади пламени")
        plt.xlabel("Площадь, м^-2")
        plt.ylabel("Поток, Вт")
        plt.grid(True)
        if save:
            plt.savefig("flame_area_WHF.png")
        plt.show()

    def plot_Qdot_WHF_t(self, save=False):
        fig, ax1 = plt.subplots(figsize=(10, 6))

        ax1.set_ylabel("Qdot, Вт")
        ax1.set_xlabel("Время, с")
        plot_1 = ax1.plot(self.Data['Time'].array, self.Data['Qdot_integral'].array, c='tab:red', label="Qdot")
        ax1.tick_params(axis='y', labelcolor='tab:red')

        ax2 = ax1.twinx()
        plot_2 = ax2.plot(self.Data['Time'].array, -self.Data['WallHeatFlux'].array, c='tab:blue', label="Wall heat flux")
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        plt.title("Зависимость потока тепла через стенки и выделяемой энергии от времени \n 100%CH4 0%H2 angle=10deg, h=3.5mm ")
        ax2.set_ylabel("Поток, Вт")


        lns = plot_1 + plot_2
        labels = [l.get_label() for l in lns]
        plt.legend(lns, labels, loc=0)
        ax1.set_ylim(0, 255)
        ax2.set_ylim(0, 255)
        plt.grid(True)
        if save:
            plt.savefig("Qdot_WHF_t.png")
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

    def read_wallHeatFlux1(self, file_path):
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
                            h_tmp += float(h)
                            line = file.readline()
                        except Exception:
                            break

                    T.append(float(t))
                    H.append(h_tmp)

        T = np.array(T)
        H = np.array(H)

        self.Data["WallHeatFlux"] = np.interp(self.Data["Time"], T, H)

    def reduce_data(self, newsize):
        self.Data = self.Data.iloc[:newsize]


path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/100CH4-0H2-air-6-step3D_h-35_l-60_DyM/postProcessing/'

t = "0.0450225"

AF      =  "AFlame_volIntegrate/"   + t + "/volFieldValue.dat"
Qdot    =  "Qdot_volIntegrate/"     + t + "/volFieldValue.dat"
WHF     =  "wallHeatFlux1/"         + t + "/wallHeatFlux.dat"

D = PastProcessingData()
D.read_AFlame_volIntegrate(path + AF)
D.read_Qdot_volIntegrate(path + Qdot)
D.read_wallHeatFlux1(path + WHF)

# D.reduce_data(40 - 13)

# D.plot_flame_area_t(save=True)
# D.plot_Qdot_t(save=True)
# D.plot_WallHeatFlux_t(save=True)
#
# D.plot_flame_area_Qdot(save=True)
# D.plot_flame_area_WHF(save=True)

D.plot_Qdot_WHF_t(True)