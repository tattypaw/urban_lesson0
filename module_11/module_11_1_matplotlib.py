import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, np.pi / 10)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, label='Синусоида')
y = np.cos(x)
ax.plot(x, y, label='Kocинусоида')
ax.legend()
ax.set_title("Тригонометрические функции")
ax.set_xlabel('Ось Х')
ax.set_ylabel('Ось У')
plt.show()