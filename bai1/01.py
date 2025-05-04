#import lớp hình ảnh
from PIL import Image

#thư mục chứa hình ảnh
dir = 'C:/Users/Vo Thien/OneDrive/Desktop/TGMT/bai1/image'

#đường dẫn đến hình ảnh
image_path = dir +'/anh1.JPG'
print(image_path)

#image open dùng để đọc ảnh
img01 = Image.open(image_path)

#hàm hiển thị hình ảnh
img01.show()

#in một số thông tin 
#in định dạng ảnh
print("Định dạng ảnh: "+ img01.format)
print("Kích thước hình ảnh: ", img01.size)

#đóng tập tin
#img01.close()

#lưu ảnh
new_img_01_path = dir + '/new_01.JPG'
new_img_01_png_path = dir + '/new_01.PNG'
img01.save(new_img_01_path)
