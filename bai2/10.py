import matplotlib.pyplot as plt
from PIL import Image

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh
img = Image.open(my_path)

#chuyển đổi backend
plt.switch_backend('tkagg')

#hiển thị hình ảnh
plt.imshow(img)
plt.title('Click on the image to select points')

#sử dụng hàm ginput để chọn điểm trên ảnh
points = plt.ginput(5)
print(points)
plt.show()
plt.close()
plt.imshow(img)
for point in points:
    x,y = point
    plt.plot(x,y, 'r*')
#hiển thị
plt.show()
