import  numpy as np

a = np.array([2,4,2,5,6,3])

# Phương sai
print(np.var(a))

# muốn chia cho n-1
print(np.var(a, ddof=1))

# muốn chia cho n-2
print(np.var(a, ddof=2))