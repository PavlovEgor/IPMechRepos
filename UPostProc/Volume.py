import openfoamparser_mai as Ofpp
import numpy as np


"""
postProcess -func writeCellVolumes
"""


path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/3D/angleSearch/a-10/BlockMesh/h-35/l-50/100CH4-0H2-air-6-step3D/'
time = '0.00400258'

V = Ofpp.parse_internal_field(path + time + '/V')  # x-координата элементов сетки | shape = (n, 1)

print(np.sum(V) / ((5e-6) ** 3))
