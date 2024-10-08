

def make_concentration_CH4_H2_air(phi=1, xi=0.05):
    stoichiometric_fuel_air = (2 - 1.5 * xi)
    alpha = 3.762  # 78.084 / 20.946

    X_O2 = 1 / (1 + alpha + (phi / stoichiometric_fuel_air))

    X_CH4 = ((1 - xi) * phi / stoichiometric_fuel_air) * X_O2

    X_H2 = (xi * phi / stoichiometric_fuel_air) * X_O2

    X_N2 = alpha * X_O2

    M_CH4 = 16.04
    M_H2 = 2.02
    M_O2 = 32.00
    M_N2 = 28.01

    X = [X_CH4, X_H2, X_O2, X_N2]
    M = [M_CH4, M_H2, M_O2, M_N2]
    name = ['CH4', 'H2', 'O2', 'N2']
    Y = [0] * 4
    for i in range(4):
        Y[i] = X[i] * M[i] / (X_CH4*M_CH4 + X_H2*M_H2 + X_O2*M_O2 + X_N2*M_N2)
        print(f'Y_{name[i]}   ', Y[i], ';')


def make_concentration_CH4_air(phi=1):
    stoichiometric_fuel_air = 2

    alpha = 3.762  # 78.084 / 20.946

    X_O2 = stoichiometric_fuel_air /  (2 * (alpha + 1) + phi)
    X_CH4 = 1 - (alpha + 1) * X_O2
    X_N2 = alpha * X_O2

    M_CH4 = 16.04
    M_O2 = 32.00
    M_N2 = 28.01

    X = [X_CH4, X_O2, X_N2]
    M = [M_CH4, M_O2, M_N2]
    name = ['CH4', 'O2', 'N2']
    Y = [0] * 3
    for i in range(3):
        Y[i] = X[i] * M[i] / (X_CH4*M_CH4 + X_O2*M_O2 + X_N2*M_N2)
        print(f'Y_{name[i]}   ', Y[i], ';')


make_concentration_CH4_H2_air(phi=1, xi=0.05)