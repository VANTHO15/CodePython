import matplotlib.pyplot as plt
import numpy as np

# x_number=[1,2,3,4,5,8,9,11]
# y_number=[2,4,5,7,2,11,44,12]
#
# plt.plot(x_number,y_number,"x")
# plt.show()
#
# x= np.linspace(0,10)
# line=plt.plot(x,np.sin(x))
# plt.show()

# x= np.linspace(-8,6)
# #x**2 +2x-1
# func=np.poly1d(np.array([1,2,-1]).astype(float))
# line=plt.plot(x,func(x))
# plt.show()

def drawForce(x,y):
    plt.plot(x,y,'o')
    plt.xlabel("Distance in meter")
    plt.ylabel("Gravitation force in Newton")
    plt.title("Force and Distance")
    plt.show()
def genarateForce():
    r=range(100,900,10)
    F=[]
    G=6.67*(10**(-11))
    m1=100
    m2=70
    for dis in r:
        force=G*(m1*m2)/(dis**2)
        F.append(force)
    drawForce(r,F)
genarateForce()
