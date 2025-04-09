# Traffic Sign Classification Project 🚦
## [preprocessing](#preprocessing)
## [Building a Custom CNN Model](#building-a-custom-cnn-model)
## [Using a Pre-trained Model](#using-a-pre-trained-model)
## [Object Detection with YOLO](#object-detection-with-yolo)


## 📌 Overview
This project aims to classify traffic signs using machine learning and deep learning techniques.  
The dataset used is [Traffic Sign Dataset](https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification/data).  



## 🚀 Steps
## preprocessing

  - ### Step 1: Analyze Class Distribution
      - The first step in this project is to analyze the distribution of images across different classes. This helps identify any imbalances in the dataset, which can affect the model's performance
      To achieve this, we:
        Count the number of images per class.
        Visualize the distribution using a bar chart.
        Identify underrepresented and overrepresented classes.
        This analysis guides preprocessing steps such as data augmentation, oversampling, or undersampling to ensure a balanced dataset

## Building a Custom CNN Model
- ### Initial Approach: Training Without Class Balancing

    Before applying any data balancing techniques, we will first train the model on the dataset as it is. This will help us analyze its performance and understand whether class imbalance significantly affects the results.

    - Let’s start by loading the dataset and training a baseline model without any modifications to the class distribution.
 
- Train a Convolutional Neural Network (CNN) from scratch  
- Evaluate the model  

## Using a Pre-trained Model
- Apply transfer learning (ResNet50, EfficientNet, etc.)  
- Compare performance with the custom CNN  

## Object Detection with YOLO
- ##  Convert dataset to YOLO format  
  - First, in the file CSV, I found the (x_mini, x_max, y_mini, y_max), from this, we can find the bounding box of the object in the image.
  - width = x_max - x_mini
  - height = y_max - y_mini
  - x_center = x_mini + ((x_max - x_mini)/2) = (x_max +x_mini)/2
  - y_center = y_mini + ((y_max - y_mini)/2) = (y_max +y_mini)/2
  and then convert this number into normalized by dividing by width and height, to yolo can able to know the place of the object in the size of the image.
  - width = width/width of image
  - height = height/height of image
  - x_center = x_center / width of image
  - y_center = y_center / hight of imege
  - ### The shape of the file is :
     - class_id x_center y_center width hight 

- Train YOLO for detecting traffic signs  
