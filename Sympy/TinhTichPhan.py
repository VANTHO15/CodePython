from sympy import *
x,y,z,t=symbols("x y z t")
f,g,h=symbols("f g h",cls=Function)
k,m ,n=symbols("k m n",integer=true)
init_printing(use_unicode=true)

f=x**2+2*x
f1=integrate(f,x)
print(f1)

f=log(x)
f1=integrate(f,x)
print(f1)

f=x**2+2
f1=integrate(f,(x,1,3))
print(f1)

f=x**2+2
f1=integrate(f,(x,1,oo)) # oo là vô cùng
print(f1)

f=-x**2-2*y**2
f1=integrate(f,(x,1,2),(y,1,15)) # oo là vô cùng
print(f1)