from src.data_process import DataDNN
from split import split
from models.CNN_model import maneual_model_cnn
import matplotlib.pyplot as plt
from src.convert_date_to_yolo_format import bounding


"""path = r"D:\my_projects\GermanTrafficSignDetection\traffic\src\dataset\archive (1)\Train.csv"
path_folder =  r"D:\my_projects\GermanTrafficSignDetection\traffic\src\dataset\archive (1)"
x = DataDNN()
featuer , labels = x.read_csv(csv_file = path , path_folder= path_folder)
print(featuer)
print(labels)


for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(featuer[i], cmap='gray')
    plt.title(f"Class: {labels[i]}")
    plt.axis('off')

plt.show()

y = split(featuer= featuer , labels= labels , size_test= 0.2)
x_train , x_test , y_train , y_test = y.data_split()
print("x_train shape : " , x_train)

u = maneual_model_cnn(x_train , y_train  , x_test , y_test)
v = u.to_categorical()
print(v)
img = u.images()
print(img)
u.train()"""


path_data = r"D:\my_projects\GermanTrafficSignDetection\traffic\dataset\archive (1)"
output_path = r"D:\my_projects\GermanTrafficSignDetection\traffic\dataset"
size = (650 , 650)
b = bounding(path_data , output_path= output_path , new_size= size)




