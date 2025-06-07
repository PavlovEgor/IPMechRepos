
import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графика
x = np.logspace(0, -9, num=100)  # Инвертируем логарифмическую шкалу по оси X
y1 = np.logspace(1, 0, num=100)[::-1]  # Инвертируем данные для первой линии
y2 = np.logspace(0, -1, num=100)[::-1]  # Инвертируем данные для второй линии
y3 = np.logspace(-1, -2, num=100)[::-1]  # Инвертируем данные для третьей линии
y4 = np.logspace(-2, -3, num=100)[::-1]  # Инвертируем данные для четвертой линии

# Создаем график
plt.figure(figsize=(10, 8))

# Линии на графике
plt.plot(x, y1, label='OREGO', marker='o', linestyle='-')
plt.plot(x, y2, label='RODAS', marker='s', linestyle='--')
plt.plot(x, y3, label='LSODE', marker='^', linestyle='-.')
plt.plot(x, y4, label='SEULEX', marker='d', linestyle=':')

# Логарифмическая шкала
plt.xscale('log')
plt.yscale('log')
plt.gca().invert_xaxis()  # Инвертируем ось X

# Подписи осей
plt.xlabel('Погрешность')
plt.ylabel('Сек')

# Заголовок и легенда
plt.title('Сравнение методов')
plt.legend()

# Показываем график
plt.grid(True, which="both", ls="-")
plt.show()
