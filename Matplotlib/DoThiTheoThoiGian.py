import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig =plt.figure()
ax=fig.add_subplot(1,1,1)
dem=0
def refreshInputData(i):
    print("Refresh data...")
    nhietdoData=open("nhietso.txt","r").read()
    lines=nhietdoData.split("\n")
    Xvalue=[]
    Yvalue=[]
    for line in lines:
        if len(line)>1:
            x,y= line.split(",")
            Xvalue.append(x)
            Yvalue.append(y)
        ax.clear()
        ax.plot(Xvalue,Yvalue)
ani= animation.FuncAnimation(fig,refreshInputData,interval=1000)
plt.show()
