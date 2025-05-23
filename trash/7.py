import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Пример данных волнистой кривой (синусоидальный сигнал)
t = np.linspace(0, 10, 1000)  # Время от 0 до 10 секунд
signal = np.sin(2 * np.pi * 0.5 * t) + 0.5 * np.sin(2 * np.pi * 2 * t)  # Сигнал с двумя частотами

# Нахождение всех максимумов
peaks, _ = find_peaks(signal)

# Построение графика сигнала и максимумов
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Сигнал')
plt.plot(t[peaks], signal[peaks], "x", label='Максимумы')
plt.title('Сигнал и его максимумы')
plt.xlabel('Время [с]')
plt.ylabel('Амплитуда')
plt.legend()
plt.show()

# Вывод индексов и значений максимумов
print('Индексы максимумов:', peaks)
print('Значения максимумов:', signal[peaks])
