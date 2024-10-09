import numpy as np
import matplotlib.pyplot as plt

sin_wave = np.load("task7_sin.py.npy")
cos_wave = np.load("task7_cos.py.npy")

x = np.linspace(0, 10, 101)
plt.plot (x, sin_wave, label = "Sine", color = 'b')
plt.plot (x, cos_wave, label = "Cosine")
plt.legend()
plt.show()
