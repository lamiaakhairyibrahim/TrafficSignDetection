import tensorflow as tf
import keras 
from keras import layers 
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class maneual_model_cnn:
    def __init__(self, featuer , labels , x_test , y_test):
        self.featuer = featuer 
        self.labels = labels 
        self.x_test = x_test
        self.y_test = y_test
        self.y_train , self.y_test2 = self.to_categorical()
        self.images_train , self.images_test = self.images()
        self.model = self.modelCNN()
    
    def to_categorical(self):
        y_train = keras.utils.to_categorical(self.labels , num_classes= 43)
        y_test1 = keras.utils.to_categorical(self.y_test , num_classes= 43)
        return y_train , y_test1
    
    def images(self):
        img_train = self.featuer / 255.0
        img_test = self.x_test / 255.0
        return img_train , img_test
    
    def modelCNN(self):
        model = keras.models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),  # Input layer for RGB images
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),

            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),  # Reduce overfitting
            layers.Dense(43, activation='softmax')  # Output layer (43 classes)
        ])
        return model 
    def train(self):

            self.model.compile(optimizer='adam',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])

            # Summary of the model
            print(self.model.summary())
            print(self.featuer.shape)  
            print(self.labels.shape)

            datagen = ImageDataGenerator(rescale=1./255)  # Normalize images dynamically
            train_generator = datagen.flow(self.images_train, self.y_train, batch_size=8)
            test_generator = datagen.flow(self.images_test, self.y_test2, batch_size=8)

            history = self.model.fit(train_generator, epochs=15, validation_data=test_generator)
            """history = self.model.fit(self.images_train, self.y_train, epochs=15, 
                                     validation_data=(self.images_test, self.y_test2),batch_size=32)"""
            
                






