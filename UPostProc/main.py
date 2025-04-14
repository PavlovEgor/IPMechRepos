import openfoamparser_mai as Ofpp
import numpy as np
import pandas as pd


"""
Программа для поиска скоростей в заданных точках.
До начала выполнения программы необходимо в рабочей папке openfoam выполнить команду
postProcess -func writeCellCentres

Входные данные: 
path - адресс папки с расчетом openfoam. 
time - время нужного кейса
InputData - датафрейм с эксель таблицей заданных точек. Формат смотреть пример.

Выходные данные: 
OutputData - датафрейм с эксель таблицей искомых скоростей.

Предостережения:
1) Программа не выдает ошибки, если заданная точка находится за пределами тела. 
2) 
"""
path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/angleSearch/a-10/BlockMesh/h-35/l-50/100CH4-0H2-air-6-step3D/'
time = '0.00400258'

U = Ofpp.parse_internal_field(path + time + '/U') # скорость массив из векторов [Ux, Uy, Uz] | shape = (n, 3)
Cx = Ofpp.parse_internal_field(path + time + '/Cx')  # x-координата элементов сетки | shape = (n, 1)
Cy = Ofpp.parse_internal_field(path + time + '/Cy')  # y-координата элементов сетки
Cz = Ofpp.parse_internal_field(path + time + '/Cz')  # z-координата элементов сетки


InputData = pd.read_csv("input.txt", sep="\t")  # массив заданных точек | shape = (num_of_points, 3)
# InputData = pd.read_exel("input.xlsx")  # массив заданных точек | shape = (num_of_points, 3)

num_of_points = InputData.shape[0]
InputData = InputData.T

OutputData= pd.DataFrame({"X": np.zeros(num_of_points),
                          "Y": np.zeros(num_of_points),
                          "Z": np.zeros(num_of_points),
                          "Ux": np.zeros(num_of_points),
                          "Uy": np.zeros(num_of_points),
                          "Uz": np.zeros(num_of_points),
                          "Umag": np.zeros(num_of_points)})  # | shape = (num_of_points, 7)


for point in range(num_of_points):
    r0 = InputData[point].array  # заданная точка

    residual = (Cx - r0[0]) ** 2 + (Cy - r0[1]) ** 2 + (Cz - r0[2]) ** 2  # массив расстояний до заданной точки
    ind = np.argmin(residual)  # индекс ячейки, от которой расстояние до заданной минимально

    OutputData.loc[point, "X"] = Cx[ind]
    OutputData.loc[point, "Y"] = Cy[ind]
    OutputData.loc[point, "Z"] = Cz[ind]
    OutputData.loc[point, "Ux"] = U[ind][0]
    OutputData.loc[point, "Uy"] = U[ind][1]
    OutputData.loc[point, "Uz"] = U[ind][2]
    OutputData.loc[point, "Umag"] = (OutputData.loc[point, "Ux"] ** 2 +
                                 OutputData.loc[point, "Uy"] ** 2 +
                                 OutputData.loc[point, "Uz"] ** 2) ** 0.5

OutputData.to_csv("output.txt", sep="\t")
# OutputData.to_xlsx("output.xlsx")
