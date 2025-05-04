from PIL import Image
from IPython.display import display
from imgtool import *

#đường dẫn ảnh
my_path = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image/anh1.jpg'

#đọc ảnh
img = load_image(my_path)
#img.show()

#định vị khu vưc cắt 
region = (100 ,100, 250, 250)
#cắt vuungf ảnh
cropped_img = img.crop(region)
cropped_img.show()

#dán 
paste_position = (250, 250)
img.paste(cropped_img, paste_position)
img.show()