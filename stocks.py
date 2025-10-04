# stocks.py
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker="AAPL"):
    data = yf.download(ticker, period="1d", interval="1h")
    return data

def plot_stock(data, ticker="AAPL"):
    plt.figure(figsize=(8,4))
    data['Close'].plot(title=f"{ticker} Stock Price")
    filename = f"static\\{ticker}_chart.png"  # Windows-friendly path
    plt.savefig(filename)
    plt.close()
    return filename
