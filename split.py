from sklearn.model_selection import train_test_split


class split:
    def __init__(self , featuer , labels , size_test):
        self.featuer = featuer
        self.labels = labels 
        self.size_test = size_test
        self.data_split()
    
    def data_split(self):
        x_train , x_test , y_train , y_test = train_test_split(self.featuer , self.labels , test_size= self.size_test , random_state= 0)
        return  x_train , x_test , y_train , y_test
