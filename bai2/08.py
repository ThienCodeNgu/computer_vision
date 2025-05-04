import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image

#Vẽ biểu đồ: Line Chart
x = [1, 2, 3, 4, 5]
y = [10, 16, 20, 30, 25]

x2 = [1, 2, 3, 4, 5]
y2 = [20, 16, 10, 40, 15]

#plt.plot(x,y,'bo-', label='Dữ liệu 1')
#plt.plot(x2,y2,'ro-', label='Dữ liệu 2')
#plt.title("Ví dụ")
#plt.xlabel('Trục x')
#plt.ylabel('Trục y')
#plt.legend()
#plt.show()


#vẽ biểu đồ cột bar chart 
categories = ['A', 'B', 'C', 'D', 'E']
values = [15,10, 25, 12, 18]

#plt.bar(categories, values, color = 'g', alpha = 0.6)
#plt.xlabel('Danh mục')
#plt.ylabel('Giá trị')
#plt.legend()
#plt.show()

#biểu đồ hình tròn pie chart 
my_labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
my_colors = ['red', 'green', 'blue', 'yellow']

plt.pie(sizes, labels = my_labels, colors=my_colors, autopct='%1.1f%%')
plt.title("Biểu đồ hình tròn")
plt.show()