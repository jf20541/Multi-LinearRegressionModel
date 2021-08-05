import yfinance as yf
import pandas as pd
import config

if __name__ == "__main__":
    tickers = ["MSFT", "SPY"]
    df = yf.download(tickers, start="2002-01-01", end="2021-04-30")
    df = df["Adj Close"].reset_index(drop=True)
    df.to_csv(config.TRAINING_FILE, index=False)
