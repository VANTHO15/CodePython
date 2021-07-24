def DocFile():
    file=open("Danhsach.txt","r",encoding="utf-8")
    for i in file:
        print(i.strip())
    file.close()
DocFile()


