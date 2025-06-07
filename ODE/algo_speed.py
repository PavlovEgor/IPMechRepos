import numpy as np
import matplotlib.pyplot as plt

path = "KIMKIM/"
# path = "HIRES/"

seulex  = np.loadtxt(path + "seulex.txt")
rd34 = np.loadtxt(path + "Rb34.txt")
rodas34 = np.loadtxt(path + "rodas34.txt")
rodas23 = np.loadtxt(path + "rodas23.txt")
trap = np.loadtxt(path + "trapezoid.txt")
# rkf = np.loadtxt(path + "rkf45.txt")
# sibs = np.loadtxt(path + "sibs.txt")

plt.figure(figsize=(10, 6))


plt.plot(*seulex.T, 'o-', label='SEULEX')
plt.plot(*rd34.T, 'o-', label='Rosenbrock34')
plt.plot(*rodas34.T, 'o-', label='RODAS34')
plt.plot(*rodas23.T, 'o-', label='RODAS23')
plt.plot(*trap.T, 'o-', label="Trapezoidal")
# plt.plot(*rkf.T, 'o-', label="RKF45")
# plt.plot(*sibs.T, 'o-', label="SIBS")


# Логарифмическая шкала
plt.xscale('log')
plt.yscale('log')
plt.gca().invert_xaxis()  # Инвертируем ось X

# Подписи осей
plt.xlabel('Погрешность')
plt.ylabel('Сек')

# Заголовок и легенда
plt.title('Сравнение методов по глобальному механизму')
plt.legend()

# Показываем график
plt.grid(True, which="both", ls="-")


plt.show()