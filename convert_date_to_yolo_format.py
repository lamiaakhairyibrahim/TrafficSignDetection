import pandas as pd
import os

class bounding:
    def __init__(self , path_file , output_folder_path):
        self.path_file = path_file
        self.output_folder_path = output_folder_path
        os.makedirs(self.output_folder_path , exist_ok='True')

    def file_bound(self ):
        data = pd.read_csv(self.path_file)
        print(data.info())
        for index, row in data.iterrows():
            width_opject = (row['Roi.X2'] - row['Roi.X1']) / row['Width']
            height_opject = (row['Roi.Y2'] - row['Roi.Y1']) / row['Height']
            x_center = ((row['Roi.X2'] + row['Roi.X1']) / 2) / row['Width']
            y_center = ((row['Roi.Y2'] - row['Roi.Y1']) / 2 )/ row['Height']
            image_name = os.path.splitext(os.path.basename(row['Path']))[0]
            label_path = os.path.join(self.output_folder_path , f"{image_name}.txt")
            with open(label_path , 'a'  ) as f :
                f.write(f"{row['ClassId']} {x_center} {y_center} {width_opject} {height_opject}" )

        print(f"All YOLO label file saved in {self.output_folder_path}")    

        


