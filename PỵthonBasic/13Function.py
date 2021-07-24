def  UCLN(x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x
print(UCLN(3,9))
def Tong(*data):
    s=0
    for i in data:
        s+=i
    return s
print(Tong(1,2,3,4,5))
def Sum(x1,x2,x3,*data,**list):
    t1=t2=t3=0
    t1=x1+x2+x3
    for i in data:
        t2+=i
    for k,v in list.items():
        t3+=v
    li=[t1,t2,t3]
    return li
print(Sum(1,2,3,4,5,6,7,8,a=1,b=2,c=10,d=99))

def SoChan(n):
    for i in range(n):
        if i%2==0:
            yield i
x=SoChan(10)
print(type(x))

