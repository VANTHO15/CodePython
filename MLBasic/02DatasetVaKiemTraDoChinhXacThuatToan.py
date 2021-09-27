from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

iris_dataset = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, random_state=0)
#75% vao x_tran, 25% vao x_test  ketqua bo vao 75% y_tran va 25%y_test

model = DecisionTreeClassifier()
mymodel = model.fit(x_train, y_train)

X_new = np.array([[6.0, 3.32, 4.5, 2.0]])
print(mymodel.predict(X_new))     # Kiểm tra nó thuộc nhóm hoa nào
print(mymodel.score(x_test, y_test))  # xem độ chính xác của nó
