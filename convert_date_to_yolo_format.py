import pandas as pd
import os
import cv2
import yaml

class bounding:
    def __init__(self , path_dataset , output_path , new_size):
        self.path_dataset = path_dataset
        self.output_path  = output_path
        self.new_size = new_size
        path_images = os.path.join(self.output_path , "images")
        path_label = os.path.join(self.output_path , "labels")

        for folder in os.listdir(self.path_dataset):
            print(f"folder is {folder}")
            if folder == "Train":
                  self.resiz_img(os.path.join(self.path_dataset , folder) , os.path.join(path_images , "train") , self.new_size)

            elif folder == "Test":
                  self.resiz_img_test(os.path.join(self.path_dataset , folder) , os.path.join(path_images , "val") , self.new_size)  

            elif folder == "Train.csv":
                 self.file_bound(os.path.join(self.path_dataset , folder) , os.path.join(path_label,"train") , self.new_size[0] , self.new_size[1])
            
            elif folder == "Test.csv":
                 self.file_bound_test(os.path.join(self.path_dataset , folder) , os.path.join(path_label,"val") , self.new_size[0] , self.new_size[1])
            
            else :
                 print("finished file")
            
        self.Yaml_file(os.path.join(self.output_path , 'data.yaml'))

            
    
    def resiz_img(self , path_folder , output_folder , new_size):
        li = [d for d in os.listdir(path_folder) if os.path.isdir(os.path.join(path_folder , d))]
        # print("li : " , li)
        os.makedirs(output_folder , exist_ok= True)
        for img_ in li:
            path_c = os.path.join(path_folder , img_)
            class_path = os.listdir(path_c) 
            if not os.path.isdir(path_c):
                    continue
            # print(class_path)
            for img in class_path:
                if img.endswith(('.jpg' , '.png' , '.jpeg')):
                        img_read = cv2.imread(os.path.join(path_c ,img))
                        img_resiz = cv2.resize(img_read , new_size)
                        new_name = f"{img_}_{img}"
                        cv2.imwrite(os.path.join(output_folder ,new_name) , img_resiz )


    def resiz_img_test(self , path_folder , output_folder , new_size):
        os.makedirs(output_folder , exist_ok= True)
        for img in os.listdir(path_folder)  :
                if img.endswith(('.jpg' , '.png' , '.jpeg')):
                        img_read = cv2.imread(os.path.join(path_folder ,img))
                        img_resiz = cv2.resize(img_read , new_size)
                        new_name = f"{img}"
                        cv2.imwrite(os.path.join(output_folder ,new_name) , img_resiz )


    def file_bound(self  , path_file , output_folder_path ,width , heitht):
        os.makedirs(output_folder_path , exist_ok=True)
        data = pd.read_csv(path_file)
        # print(data.info())
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

    def file_bound_test(self  , path_file , output_folder_path ,width , heitht):
        os.makedirs(output_folder_path , exist_ok=True)
        data = pd.read_csv(path_file)
        # print(data.info())
        for index, row in data.iterrows():
            width_opject = (row['Roi.X2'] - row['Roi.X1']) / width
            height_opject = (row['Roi.Y2'] - row['Roi.Y1']) / heitht
            x_center = ((row['Roi.X2'] + row['Roi.X1']) / 2) / width
            y_center = ((row['Roi.Y2'] + row['Roi.Y1']) / 2 )/ heitht
            image_name = f"{os.path.splitext(os.path.basename(row['Path']))[0]}"
            label_path = os.path.join(output_folder_path , f"{image_name}.txt")
            with open(label_path , 'a'  ) as f :
                f.write(f"{row['ClassId']} {x_center} {y_center} {width_opject} {height_opject}" )

        print(f"All YOLO label file saved in {output_folder_path}")    

    def Yaml_file(self , path_yaml):
         
        data = {
             "train" : os.path.join(os.path.join(self.output_path , "images") , "train") , 
             "val" : os.path.join(os.path.join(self.output_path , "images") , "val")  ,
             "nc" : len(data['names']) ,
             "names" :   ['Speed limit (20km/h)', 'Speed limit (30km/h)', 'Speed limit (50km/h)',
   'Speed limit (60km/h)', 'Speed limit (70km/h)', 'Speed limit (80km/h)',
   'End of speed limit (80km/h)', 'Speed limit (100km/h)', 'Speed limit (120km/h)',
   'No passing', 'No passing for vehicles over 3.5 metric tons', 'Right-of-way at the next intersection',
   'Priority road', 'Yield', 'Stop', 'No vehicles', 'Vehicles over 3.5 metric tons prohibited',
   'No entry', 'General caution', 'Dangerous curve to the left', 'Dangerous curve to the right',
   'Double curve', 'Bumpy road', 'Slippery road', 'Road narrows on the right', 'Road work',
   'Traffic signals', 'Pedestrians', 'Children crossing', 'Bicycles crossing', 'Beware of ice/snow',
   'Wild animals crossing', 'End of all speed and passing limits', 'Turn right ahead', 'Turn left ahead',
   'Ahead only', 'Go straight or right', 'Go straight or left', 'Keep right', 'Keep left',
   'Roundabout mandatory', 'End of no passing', 'End of no passing by vehicles over 3.5 metric tons']

        }

        with open(path_yaml , 'w' ) as f:
             yaml.dump(data , f)
         
    
    

        


