n=int(input("Moi Nhap Sô Fibonaxi : "))
def Fibonaci(n):
    if (n==1) | (n==2):
        return 1
    else:
        return Fibonaci(n-1)+Fibonaci(n-2)
print(Fibonaci(n))