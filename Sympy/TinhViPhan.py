from sympy import *
x,y,z,t=symbols("x y z t")
f,g,h=symbols("f g h",cls=Function)
k,m ,n=symbols("k m n",integer=true)
init_printing(use_unicode=true)

f=diff(x**2 + 2*x -1,x)  # cấp 1
print(f)

f= diff(x**4-5*x**3-3*x,x,3) # đạo hàm cấp 3
print(f)

'''
đạo hàm nhiều biến , nó đạo hàm theo biến x, xong rồi đạo hàm theo biến y rồi đạo hàm theo biến z
'''
f=x**3*y**2*z**4+3*x**3*y**2-3*y**5*z**7
g=diff(f,x)
h=diff(f,x,y)
t=diff(f,x,y,z)
print(g," ",h," ",t)


