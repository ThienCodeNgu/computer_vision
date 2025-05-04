import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh và hiển thị
img = Image.open(my_path)
plt.imshow(img)
#plt.show()

#vẽ đồ thị cơ bản
x = [1, 2, 3, 4, 5]
y = [10, 16, 20, 30, 25]
plt.plot(x,y, color = 'red')
plt.title('Ví dụ về biểu đồ')
#plt.axis('off') tắt hệ trục tọa độ
#plt.show()

#vẽ trên hình ảnh
#đọc ảnh
x = [100, 100, 400, 400]
y = [200, 300, 200, 300]
plt.imshow(img)
plt.plot(x,y, 'r*') #đánh dấu các điểm
plt.plot(x,y, 'ks:')
plt.show()