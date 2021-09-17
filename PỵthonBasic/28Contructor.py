class HocSinh():
    def __init__(self,Ten,Lop):
        print("Tên là :",Ten," Tuổi là : ",Lop)
    def __str__(self):
        return "Bạn vừa Gọi hả"
    def __del__(self):
        print("Bạn vừa Xóa rồi ")
tho=HocSinh("Nguyễn Văn Thọ","18CDT1")
print(tho)
