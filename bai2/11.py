import numpy as np
# Tạo mảng
a = np.array([1,2,3])

# In mảng
print(a)

# In ra 1 phần tử
element = a[1]
print(element)

# Tạo mảng 2 chiều
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:")
print(matrix)

# In một phần tử
element = matrix[1, 2]
print(element)

# Cách tạo mảng
# Tạo mảng toàn là số 0
a = np.zeros(5)
print(a)

# Tạo mảng toàn là số 1
a = np.ones(5)
print(a)

# Tạo mảng
a = np.empty(5)
print(a)

# Tạo mảng từ 0 đến 100
a = np.arange(100)
print(a)

# Tạo mảng gồm các phần tử với khoảng cách đều nhau
a = np.linspace(0, 10, num=5)
print(a)


# Xác định kiểu dữ liệu
a = np.ones(5, dtype=np.int64)
