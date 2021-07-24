dic={"so1":"Tho","so2":"Thanh","so3":"Tai"}
print(dic)
print(dic["so1"])
for i in dic:
    print(dic[i])
item=dic.items()
value=dic.values()
for i in item:
    print(i[1])
for i in value:
    print(i)
dic["Ahihi"]=123
print(dic)
dic.pop("so1")
print(dic)