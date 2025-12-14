import yfinance as yf


def get_latest_price(ticker: str) -> float:
    """Fetch latest closing price using yfinance."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    if hist.empty:
        raise ValueError(f"No price data for {ticker}")

    return float(hist["Close"].iloc[-1])


def get_market_price(row):
    return get_latest_price(row["ticker"])
