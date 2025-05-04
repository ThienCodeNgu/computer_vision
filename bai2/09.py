from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# Đường dẫn ảnh
my_path = 'C:/Users/tungi/OneDrive/Documents/src_cv/img/01/1.jpg'
# Đọc ảnh
im = Image.open(my_path)
plt.imshow(im)
# Chuyển sang ảnh xám
im_gray = im.convert('L')
plt.imshow(im_gray, cmap='gray')
im_array = np.array(im_gray)
print(im_array)
# Tạo một hình vẽ mới
plt.figure()
plt.hist(im_array.flatten(), bins=128)
plt.title('Biểu đồ Histogram của ảnh')
plt.xlabel('Giá trị của pixel')
plt.ylabel('Số lượng')
plt.show()

# Làm nổi bật đường biên
plt.figure()
plt.gray()
plt.contour(im_gray, origin="image")
plt.show()

# Đường dẫn ảnh
my_path = 'C:/Users/tungi/OneDrive/Documents/src_cv/img/01/face1.jpg'

# Đọc ảnh và hiển thị ảnh với trục tọa độ
im = Image.open(my_path).convert("L")

# Hiển thị ảnh trên trục tọa độ
plt.imshow(im)

# Tạo một ình vẽ mới
plt.figure()

# Đặt màu sắc là xám
plt.gray()

# Vẽ biểu đồ đường biên (contour) của ảnh
plt.contour(im, origin="image")

# Đảm bảo tỷ lệ trục x và trục y trên biểu đồ là bằng nhau
plt.axis('equal')

# hiển thị ảnh
plt.show()