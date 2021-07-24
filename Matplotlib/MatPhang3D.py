import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''
mat phang 2x+3y-4z-5=0
'''
x1= np.linspace(-5,5)
y1= np.linspace(-5,5)
X, Y=np.meshgrid(x1,y1)
Z=(2*X +3*Y -5)/4
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_surface(X,Y,Z)
plt.show()