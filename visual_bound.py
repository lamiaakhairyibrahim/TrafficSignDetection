import cv2
import os

def show_bounding_boxes(image_path, label_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        class_id, x_center, y_center, w, h = map(float, parts)
        
      
        x_center = int(x_center * width)
        y_center = int(y_center * height)
        w = int(w * width)
        h = int(h * height)

        x_min = x_center - w // 2
        y_min = y_center - h // 2
        x_max = x_center + w // 2
        y_max = y_center + h // 2

      
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"D:\my_projects\GermanTrafficSignDetection\traffic\dataset\images\val\00100.png"
label_path = r"D:\my_projects\GermanTrafficSignDetection\traffic\dataset\labels\val\00100.txt"
show_bounding_boxes(image_path, label_path)