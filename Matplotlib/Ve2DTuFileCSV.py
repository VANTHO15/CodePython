import csv
import matplotlib.pyplot as plt

def drawTemp(x,y):
    plt.plot(x,y,'k')
    plt.xlabel("Day")
    plt.ylabel("Template")
    plt.title("Subrice")
    plt.grid(True)
    plt.show()

days=[]
temps=[]
with open("NhietDo.csv",newline="") as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        days.append(int(row[0]))
        temps.append(float(row[1]))
print(days)
print(temps)
drawTemp(days,temps)


