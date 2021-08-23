import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import LR_config


def model(feature, target):
    """Initiate Linear Regression Model
    Args:
        feature [float]: pandas series, feature variable
        target [foat]: pandas series, target variable
    Returns:
        [float]: slope-coefficient and intercept
    """
    lr = LinearRegression()

    feature = feature.values.reshape(-1, 1)
    target = target.values.reshape(-1, 1)

    # fit the model
    lr.fit(feature, target)

    # define slope and intercept
    slope = lr.coef_[0][0]
    intercept = lr.intercept_[0]
    return slope, intercept


if __name__ == "__main__":
    df = pd.read_csv(LR_config.TRAINING_FILE)
    slope, intercept = model(df["MSFT"], df["SPY"])
    print(f"Slope: {slope:.2f} and Intercept: {intercept:.2f}")
