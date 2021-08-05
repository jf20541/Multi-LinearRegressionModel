import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import config


def model(xSeries, ySeries):
    """
    xSeries: pandas series, x variable
    ySeries: pandas series, y variable
    """
    # initiate linear regression model
    lr = LinearRegression()

    xVar = xSeries.values.reshape(-1, 1)
    yVar = ySeries.values.reshape(-1, 1)

    # fit the model
    lr.fit(xVar, yVar)

    # define slope and intercept
    slope = lr.coef_[0][0]
    intercept = lr.intercept_[0]
    return slope, intercept

if __name__ == "__main__":
    df = pd.read_csv(config.TRAINING_FILE)
    slope, intercept = model(df["MSFT"], df["SPY"])
    print(f"Slope: {slope:.2f} and Intercept: {intercept:.2f}")
