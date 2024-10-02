# By QuasiNewton on https://walkingrandomly.com/?p=2720

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# wow
def complex_function(x, y):
    return (
        np.exp(-(x**2 + y**2 - 32)**2) +
        np.exp(-((x + 2)**4 + (y + 2)**4)) +
        np.exp(-((3*x + 6 + 0.5*y)**4 + (y - 2)**4)) +
        np.exp(-(x**2 + y**2 - 16)**2) * (np.arctan(50*x - 40) / np.pi + 0.5) +
        np.exp(-(8*x**2 + y**2 - 48)**2) * np.exp(-2*x**2)
    )


x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = complex_function(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=1)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Wink')

plt.show()
