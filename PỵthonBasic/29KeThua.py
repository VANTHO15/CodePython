class Person:
    def printName(self,name):
        print("Tên là : ",name)
class Student(Person):
    def printClass(self,Lop):
        print("Lớp :",Lop)
tho=Student()
tho.printName("Nguyễn Văn Thọ")
tho.printClass("18CDT1")
# kế thừa cả hàm init
class Animal:
    def __init__(self,wedth,age):
        print("Khối Lượng: ",wedth," Tuổi :",age)
class Dog(Animal):
    def __init__(self,wedth,age,name):
        Animal.__init__(self,wedth,age)
        print("Tên :",name)
MickeyDog=Dog(100,17,"Mickey")