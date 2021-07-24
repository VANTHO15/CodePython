import numpy as np
a= np.array([1, 2, 3, 6, 3, 9, 5])
a1= np.array([[1, 2, 3, 2, 3, 9, 5],
              [1, 2, 3, 6, 3, 9, 5]])
print(a.ndim)  # số chiều
print(a1.ndim)  # số chiều

print(a1[0][2:5]) # cắt

print(a1.shape) # số hàng số cột
print(len(a1[0]))  # số cột

x1=np.array([[1,2,3,4],[3,2,4,2]])
x2=np.array([[1,4,2,5],[7,4,8,9]])
print(x1+x2)
print(x1-x2)
print(x1*x2)
print(x1/x2)
print(x1.T)
print(x1[1][2])
