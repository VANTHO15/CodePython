import matplotlib.pyplot as plt

# x1=[1,3,5,7,9]
# x2=[4,5,8,7,12]
# plt.bar(x1,x2,label="This is BarOne",width=0.5,color="#F00")
#
# x1=[2,4,6,8,10]
# x2=[2,3,4,5,10]
# plt.bar(x1,x2,label="This is BarOne",width=0.5,color="#FF0")
#
# plt.xlabel("Truc X")
# plt.ylabel("Truc Y")
# plt.title("Bieu Do")
# plt.legend()
# plt.show()

mobileBranches=["Appble","SamSung","Nokia","Huway"]
slices= [30,30,20,20]
colors= ["red","blue","yellow","purple"]
explode=[0.1,0,0,0]
plt.pie(slices,
        labels=mobileBranches,
        colors=colors,
        startangle=0,
        explode=explode,
        autopct="%1.1f%%"
        )
plt.title("Chart")
plt.show()