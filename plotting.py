import matplotlib.pyplot as plt
import numpy as np

h = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a = h*h

plt.plot(h, a, label='areal')

plt.xlabel("h")
plt.ylabel("a")

plt.legend()
plt.grid()

plt.show()