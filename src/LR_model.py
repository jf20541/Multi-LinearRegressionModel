import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import LR_config


class LinearRegression:
    def __init__(self, lr=0.0001, n_iters=100):
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
            pred = np.dot(train, self.weights) + self.bias

            # taking the derivative
            # np.dot =  sum product over the last axis of a and b array
            dw = (1 / n_samples) * np.dot(train.T, (pred - target))
            db = (1 / n_samples) * np.sum(pred - target)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, train):
        return np.dot(train, self.weights) + self.bias


if __name__ == "__main__":
    df = pd.read_csv(LR_config.TRAINING_FILE)

    # define target and feature
    feature, target = df["MSFT"], df["SPY"]
    # split the data 80% training, 20% testing (no shuffling) since its time-series
    x_train, x_test, y_train, y_test = train_test_split(
        feature, target, test_size=0.2, random_state=42, shuffle=False
    )

    # initiate LinearRegression, fit and predict the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    pred = model.predict(x_test)

    # evaluate performance
    r2, mse = r2_score(y_test, pred), mean_squared_error(y_test, pred)
    print(f"R-Squared: {r2}, Mean Squared Error: {mse}")
