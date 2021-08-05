import pandas as pd
import math
import config

import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def metrics():
    # calculate the mean squared error.
    model_mse = mean_squared_error(y_test, y_predict)

    # calculate the mean absolute error.
    model_mae = mean_absolute_error(y_test, y_predict)

    # calulcate the root mean squared error
    model_rmse = math.sqrt(model_mse)
    # calculate the r2
    model_r2 = r2_score(y_test, y_predict)

    # display the output
    print(f"MSE {model_mse:.3}")
    print(f"MAE {model_mae:.3}")
    print(f"RMSE {model_rmse:.3}")
    print(f"R2: {model_r2:.2}")


if __name__ == "__main__":
    df = pd.read_csv(config.TRAINING_FILE)
    # define IV and DV and reshape to be 2 dimensional
    X = df["MSFT"].values.reshape(-1, 1)
    Y = df["SPY"].values.reshape(-1, 1)

    # split the data train/test set
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.20, random_state=1
    )

    # initiate and fit the model
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_predict = lr.predict(x_test)
    print(metrics())
