import  numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

diem=[10,9,8,9,7]
sinhvien=["Thọ","Thanh","Tài","Toàn","Trường"]
data={"Diem":diem,"SinhVien":sinhvien}

df1=DataFrame(data)
print(df1)

ind="A B C D E".split()
cols="col1 col2 col3 cpl4 col5".split()
x=[]
for i in range(25):
    x.append(np.random.randint(1,100))
x=np.array(x)
x=x.reshape(5,5)
df3=DataFrame(x,index=ind,columns=cols)
print(df3)

print(df3[df3["col1"]>40])
df3.drop("A")
df3.drop("col1",axis=1)
print(df3)