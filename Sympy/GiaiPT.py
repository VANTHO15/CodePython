from __future__ import division
from sympy import *
x,y,z,t=symbols("x y z t")
f,g,h=symbols("f g h",cls=Function)
k,m ,n=symbols("k m n",integer=true)

f=2*x-1
k=solve(f,x)
print(k)

print(solve((x+5*y-2,-3*x+6*y-15),x,y))

print(solve(sin(30)-x))

g=1/x - y**2
print(solve_linear(g))