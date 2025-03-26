import os
import cv2
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class DataDNN:
    def __init__(self ):
        pass


    def count_file_in_folder(self , folder_path):
         
        if folder_path is None:
            print("Error: No folder path specified!")
            return None, None

        images = []  #    list of image storage
        labels = []  #    Labels storage

        for label, subdir in enumerate(os.listdir(folder_path)):
            subdir_path = os.path.join(folder_path, subdir)
            if not os.path.isdir(subdir_path):
                continue

            for file in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file)

                try:
                    image = cv2.imread(file_path)
                    if image is None:
                        print(f"Could not read {file_path}")
                        continue

                    image = cv2.resize(image, (64, 64))
                    images.append(image)
                    labels.append(label)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue

        # The 'images' list initially stores individual images as 2D arrays (64x64).
        # Each element in the list represents a grayscale image of shape (64, 64).
        # After converting 'images' to a NumPy array, it becomes a 3D array of shape (num_images, 64, 64),
        # where 'num_images' is the total number of images in the dataset.

        images = np.array(images) 
        labels = np.array(labels)
        return images,labels
    
    def read_csv(self , csv_file , path_folder):

        df = pd.read_csv(csv_file)
        print(df.info())
        count_class = df['ClassId'].value_counts().sort_index()
        print(df.head())
        plt.bar(count_class.index, count_class.values, color="blue")
        plt.xlabel("Class ID")
        plt.ylabel("Number of Images")
        plt.title("Distribution of Images per Class")
        plt.show()
        
        images = []
        labels = []
        x = zip(df['ClassId'] , df['Path'])
        for i , v in x :
            path_img = os.path.normpath(os.path.join(path_folder , v))
            if not os.path.isfile(path_img):
                continue

            try :
                img = cv2.imread(path_img )
         
                if img is None:
                        print(f"Could not read {path_img}")
                        continue

                img = cv2.resize(img, (64, 64))
                images.append(img)
                labels.append(i)

            except Exception as e :
                print(f"Error processing {path_img}: {e}")
                continue

        images = np.array(images)
        labels = np.array(labels)

        return images , labels




