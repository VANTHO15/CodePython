from random import randrange

n= int(input("Moi nhap n= "))
lst=[0]*n
for i in range(1,n):
    lst[i]=randrange(-100,100)
for i in lst:
    print(i,end=" ")

