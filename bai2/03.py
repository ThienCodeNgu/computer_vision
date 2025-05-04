
from PIL import Image
from IPython.display import display
from imgtool import *

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh
img = load_image(my_path)
img.show()

#thay đổi kích thước ảnh
new_size = (100, 100)

# tạo ảnh mới
new_image = img.resize(new_size)
new_image.show()