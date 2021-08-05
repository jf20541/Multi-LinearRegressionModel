import pandas as pd 
import numpy as np 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import config

df = pd.read_csv(config.TRAINING_FILE)

# train, target = datasets.make_regression(n_samples=100, n_features=100, noise=10, random_state=4)
# x_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.2, random_state=42)

train = df["MSFT"]
target = df["SPY"]
print(train.shape, target.shape)

x_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.2, random_state=42)

print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)


class LinearRegression():
    def __init__(self, lr=0.001, n_iters=100):
        self.lr = lr 
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    def fit(self, train, target):
        # init parameters
        n_samples, n_features = train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # iterate process 
        for _ in range(self.n_iters):
            # y = mx + b
            y_pred = np.dot(train, self.weights) + self.bias

            # taking the derivative 
            # np.dot =  sum product over the last axis of a and b array 
            dw = (1/n_samples) * np.dot(train.T, (y_pred - target))
            db = (1/n_samples) * np.sum(y_pred - target)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, train):
        y_pred = np.dot(train, self.weights) + self.bias
        return y_pred

if __name__ == '__main__':
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    pred = reg.predict(x_test)
    mse = r2_score(y_test, pred)
    print(mse)
