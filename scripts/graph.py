import sys 
from matplotlib import color_sequences
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_csv("./output/data.csv")

nx = df["nx"]
ny = df["ny"]
nz = df["nz"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
x = np.sin(v) * np.cos(u)
y = np.sin(v) * np.sin(u)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color='lightblue', alpha=0.1)

ax.plot(nx, ny, nz, color='red', label='trace')
ax.scatter([nx[0]], [ny[0]], [nz[0]], color='green', label='start')
ax.scatter([nx.iloc[-1]], [ny.iloc[-1]], [nz.iloc[-1]], color='black', label='finish')

ax.set_xlabel("n_x")
ax.set_ylabel("n_y")
ax.set_zlabel("n_z")
ax.legend()
plt.show()
