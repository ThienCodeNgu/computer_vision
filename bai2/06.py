from PIL import Image
from IPython.display import display
from imgtool import *

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh
img = load_image(my_path)
#img.show()

#chuyển ảnh từ RGB sang ảnh xám
gray_img = img.convert("L")
gray_img.show()

#phân ảnh RGB thành 3 tầng màu khác nhau
red_band, green_band, blue_band = img.split()
red_band.show()
green_band.show()
blue_band.show()

#trộn ảnh
merged_img = Image.merge("RGB", (red_band, green_band, blue_band))
merged_img.show()