# from https://walkingrandomly.com/?p=2720

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def complex_function(X, Y):
    return (
        np.exp(-X**2 - Y**2 / 2) * np.cos(4 * X) +
        np.exp(-3 * ((X + 0.5)**2 + Y**2 / 2))
    )

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = complex_function(X, Y)
Z[Z > 0.001] = 0.001
Z[Z < -0.001] = -0.001

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=1) 

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Hi')

plt.show()
