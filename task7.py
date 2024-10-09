import numpy as np


x = np.linspace(0, 10, 101)
sin_wave = np.sin(x)
cos_wave = np.cos(x)

np.save("task7_sin.py", sin_wave)
np.save("task7_cos.py", cos_wave)