def LuuFile(path):
    file=open(path,"w",encoding="utf-8")
    file.writelines("1;Nguyễn Văn Thọ;18CDT1\n")
    file.writelines("2;Nguyễn Văn Thanh;18CDT1\n")
    file.writelines("3;Nguyễn Văn Tài;18CDT1")
    file.close()
LuuFile("Danhsach.txt")