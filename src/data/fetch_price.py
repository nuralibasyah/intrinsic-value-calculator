import yfinance as yf
import pandas as pd


def get_latest_price(ticker: str) -> float:
    """Fetch latest closing price using yfinance."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    if hist.empty:
        raise ValueError(f"No price data for {ticker}")

    return float(hist["Close"].iloc[-1])


def get_price_history(ticker: str, period: str = "5y") -> pd.DataFrame:
    """Fetch historical OHLCV data."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)

    if hist.empty:
        raise ValueError(f"No historical data for {ticker}")

    return hist.reset_index()
