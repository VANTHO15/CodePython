import  numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

s1= Series([10,20,30,40])
print(s1)

s2=Series([10,20,30,40],index=["A","B","C","D"])
print(s2)

diem=[9,8,6,8,7,9]
hocsinh=["Tho","Thanh","Tai","A","B","C"]
s3=Series(diem,index=hocsinh)
print(s3,s3["Tho"])

s3d=s3.to_dict()
print(s3d)
s4=Series(s3d)
print(s3.index,s3.values)
print(s3[2])
print(s3[2:5])

x=list(range(11,16))
ind=["A","b","c","D","E"]
s5=Series(x,ind)
ind=["A","b","c","D","E","f","g"]
s6=s5.reindex(ind,fill_value=0)
print(s5,s6)

print(s5[["A","c"]])
print(s5[s5<14])





