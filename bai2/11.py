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


# Thêm, xóa, sắp xếp mảng

# Tạo mảng ban đầu
arr = np.array([3, 1, 2, 4, 5])
print(arr)

# Sắp xếp
arr = np.sort(arr)
print(arr)

# Sắp xếp ngược
arr = np.sort(arr)[::-1]
print(arr)

# Thêm phần tử vào mảng
arr = np.append(arr, 100)
print(arr)

# Xóa đi một ví trí nào đó trong mảng
arr = np.delete(arr, 3)
print(arr)

# Tạo một mảng 2 chiều
arr = np.array([[3, 1, 2],
                [4, 6, 8],
                [9, 7, 5]])

sap_xep_theo_hang = np.sort(arr, axis=1) # tăng dần
print(sap_xep_theo_hang)

sap_xep_theo_cot = np.sort(arr, axis=0) # tăng dần
print(sap_xep_theo_cot)

# Tạo một mảng 2 chiều
arr = np.array([[3, 1, 2],
                [4, 6, 8],
                [9, 7, 5]])

sap_xep_theo_hang = -np.sort(-arr, axis=1) # giảm dần
print(sap_xep_theo_hang)

sap_xep_theo_cot = -np.sort(-arr, axis=0) # giảm dần
print(sap_xep_theo_cot)

# Tạo một mảng 2D
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Sử dụng các thuộc tính để lấy thông tin về mảng
so_chieu = arr.ndim  # Số chiều (2 chiều)
kich_thuoc = arr.size  # Kích thước (tổng số phần tử, 6)
hinh_dang = arr.shape  # Hình dạng (số hàng x số cột, (2, 3))

print("Số chiều:", so_chieu)
print("Kích thước:", kich_thuoc)
print("Hình dạng:", hinh_dang)


# Chuyển đổi kiểu dữ liệu
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(float)
print(arr_float)

# Thay đổi hình dạng của mảng
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
reshaped_arr = arr.reshape(3,2)
print(reshaped_arr)

reshaped_arr = reshaped_arr.flatten() # Chuyển thành mảng 1 chiều
print(reshaped_arr)

# Cắt lát mảng
arr = np.array([1, 2, 3, 4, 5])

sub_arr = arr[1:4]  # Cắt từ phần tử thứ 1 đến 4
print(sub_arr) # 2 3 4 5

sub_arr = arr[:-1]  # 1 2 3 4
print(sub_arr)

sub_arr = arr[-2:]  # 4 5 
print(sub_arr)

# Chuyển vị mảng
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
# Để chuyển vị mảng, chúng ta có thể sử dụng .T hoặc hàm numpy.transpose().
transposed_arr = arr.T
print(transposed_arr)

# Nối mảng
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# II. Hàm tính tổng (Sum)
# - Hàm numpy.sum() cho phép tính tổng các phần tử trong mảng.
arr = np.array([1, 2, 3, 4, 5])
total = np.sum(arr)
print("Tổng của mảng arr:", total)

# III. Hàm tính trung bình (Mean)
# - Hàm numpy.mean() tính giá trị trung bình của các phần tử trong mảng.
average = np.mean(arr)
print("Giá trị trung bình của mảng arr:", average)

# IV. Hàm tìm giá trị lớn nhất và nhỏ nhất (Max và Min)
# - Hàm numpy.max() và numpy.min() dùng để tìm giá trị lớn nhất và nhỏ nhất trong mảng.
max_value = np.max(arr)
min_value = np.min(arr)
print("Giá trị lớn nhất trong mảng arr:", max_value)
print("Giá trị nhỏ nhất trong mảng arr:", min_value)

# V. Hàm tính độ lệch chuẩn (Standard Deviation)
# - Hàm numpy.std() tính độ lệch chuẩn của mảng, đo lường mức độ phân tán của dữ liệu.
std_deviation = np.std(arr)
print("Độ lệch chuẩn của mảng arr:", std_deviation)

# VI. Hàm tính phương sai (Variance)
# - Hàm numpy.var() tính phương sai của mảng, đo lường mức độ biến thiên của dữ liệu.
variance = np.var(arr)
print("Phương sai của mảng arr:", variance)

# VII. Hàm tính tổng tích chập (Dot Product)
# - Hàm numpy.dot() tính tổng tích chập của hai mảng (vector).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
dot_product = np.dot(arr1, arr2)
print("Tổng tích chập của arr1 và arr2:", dot_product)