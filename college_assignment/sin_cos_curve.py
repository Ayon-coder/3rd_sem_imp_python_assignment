import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)

sin_y = np.sin(X)
cos_y = np.cos(X)

plt.plot(X, sin_y, label = "sin(X)")
plt.plot(X, cos_y, label = "cos(X)")

plt.title("sin and cos curve")
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()