import pandas as pd
import math
import LR_config
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression


def metrics(y_test, predict):
    # calculate the mean squared error.
    model_mse = mean_squared_error(y_test, predict)

    # calculate the mean absolute error.
    model_mae = mean_absolute_error(y_test, predict)

    # calulcate the root mean squared error
    model_rmse = math.sqrt(model_mse)
    # calculate the r2
    model_r2 = r2_score(y_test, predict)

    # display the output
    print(f"MSE: {model_mse:.3}, MAE: {model_mae:.3}, RMSE: {model_rmse:.3}")
    print(f"R2: {model_r2:.2}")


if __name__ == "__main__":
    df = pd.read_csv(LR_config.TRAINING_FILE)
    # define IV and DV and reshape to be 2 dimensional
    feature = df["MSFT"].values.reshape(-1, 1)
    target = df["SPY"].values.reshape(-1, 1)

    # split the data train/test set
    x_train, x_test, y_train, y_test = train_test_split(
        feature, target, test_size=0.20, random_state=1
    )

    # initiate and fit the model
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    predict = lr.predict(x_test)
    print(metrics(y_test, predict))
