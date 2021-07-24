import  numpy as np

x= np.random.randint(1,10)
print(x)

x=[]
y=[]
for i in range(10):
    x.append(np.random.randint(1,15))
    y.append(np.random.randint(1,20))
print(x," ",y)
x=np.array(x)
y=np.array(y)
print(x,y)

binhphuong=np.square(x)
can=np.sqrt(y)
mu=np.power(x,y)
m=x/y
x=x.sort()   # sắp xếp
print(binhphuong,can,mu,m,x)
