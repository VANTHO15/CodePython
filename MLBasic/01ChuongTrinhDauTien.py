#Bài toán xác định xem có bị bệnh tim hay không ?

# Dữ liệu
# Nhẹ    1                   bị bênh tim         giá trị
# Thấp   2                       có                  1
# Trung Bình 3                   không               0
# Cao    4
# Nặng   5         Đoán xem Nhẹ, cao, trung bình, ít
# Ít 6              Đoán xem Nhẹ, cao, trung bình, nhiều
# Nhiều  7


# Bước 1: Thu thập dữu liệu
# Bước 2: Xử lý dữ liệu
# Bước 3: Cho vào Model Tranning, xây dựng model
# Bước 4: Dự đoán kết quả
# Bước 5: Đánh giá xem model có hiệu quả hay không

from sklearn import tree

my_tree=tree.DecisionTreeClassifier()
dactrung=[[1, 3, 3, 7],
          [5, 2, 4, 6],
          [1, 2, 4, 6],
          [5, 4, 4, 3],
          [1, 4, 4, 7],
          [3, 2, 3, 7],
          [3, 3, 3, 6],
          [5, 2, 2, 7]]
nhan=[0, 1, 1, 0, 0, 0, 0, 1]
result= my_tree.fit(dactrung, nhan)

BenhNhan1= result.predict([[1, 4, 3, 6]])
BenhNhan2= result.predict([[1, 4, 3, 7]])

if BenhNhan1[0]==1:
    print("Người 1 bị bệnh")
else:
    print("Người 1 không bị bệnh")

if BenhNhan2[0]==1:
    print("Người 2 bị bệnh")
else:
    print("Người 2 không bị bệnh")


