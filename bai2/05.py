from PIL import Image
from IPython.display import display
from imgtool import *

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh
img = load_image(my_path)
img.show()

#xoay ảnh
rotated_img = img.rotate(90)
rotated_img.show()

#đảo chiều ảnh
transposed_img = img.transpose(Image.Transpose.ROTATE_90)
transposed_img.show()
