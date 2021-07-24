import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')

t= np.linspace(0,10)
x=3+ 3*t
y=-1+ 2*t
z=2+t
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot(x,y,z)
plt.show()