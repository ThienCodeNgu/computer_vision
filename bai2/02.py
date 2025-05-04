#import lớp hình ảnh
from PIL import Image
from IPython.display import display
from imgtool import *

#thư mục chứa hình ảnh
my_dir = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image'

imgs = get_image_list(my_dir)

#hiển thị toàn bộ ảnh
for img in imgs:
    print(img.size)
    display(img)
    img.show()

