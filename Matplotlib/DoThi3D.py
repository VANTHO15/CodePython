import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[5,3,6,7,8,5,6,7,8,3]
z=[3,4,2,3,4,5,3,4,6,7]

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot(x,y,z,'x')
plt.show()