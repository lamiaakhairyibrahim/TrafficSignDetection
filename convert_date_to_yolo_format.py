import pandas as pd
import os
import cv2
class bounding:
    def __init__(self ):
        pass
    
    def resiz_img(self , path_folder , output_folder , new_size):
        li = [d for d in os.listdir(path_folder) if os.path.isdir(os.path.join(path_folder , d))]
        print("li : " , li)
       
        os.makedirs(output_folder , exist_ok= True)
        for img_ in li:
            path_c = os.path.join(path_folder , img_)
            class_path = os.listdir(path_c) 
            if not os.path.isdir(path_c):
                    continue
            print(class_path)
            for img in class_path:
                if img.endswith(('.jpg' , '.png' , '.jpeg')):
                        img_read = cv2.imread(os.path.join(path_c ,img))
                        img_resiz = cv2.resize(img_read , new_size)
                        new_name = f"{img_}_{img}"
                        cv2.imwrite(os.path.join(output_folder ,new_name) , img_resiz )


    def file_bound(self  , path_file , output_folder_path ,width , heitht):
        os.makedirs(output_folder_path , exist_ok=True)
        data = pd.read_csv(path_file)
        print(data.info())
        for index, row in data.iterrows():
            width_opject = (row['Roi.X2'] - row['Roi.X1']) / width
            height_opject = (row['Roi.Y2'] - row['Roi.Y1']) / heitht
            x_center = ((row['Roi.X2'] + row['Roi.X1']) / 2) / width
            y_center = ((row['Roi.Y2'] + row['Roi.Y1']) / 2 )/ heitht
            image_name = f"{row['ClassId']}_{os.path.splitext(os.path.basename(row['Path']))[0]}"
            label_path = os.path.join(output_folder_path , f"{image_name}.txt")
            with open(label_path , 'a'  ) as f :
                f.write(f"{row['ClassId']} {x_center} {y_center} {width_opject} {height_opject}" )

        print(f"All YOLO label file saved in {output_folder_path}")    
    
    

        


