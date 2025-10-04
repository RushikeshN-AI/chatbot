import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker="AAPL"):
    print(f"[DEBUG] Fetching stock data for {ticker}...")
    data = yf.download(ticker, period="1d", interval="1h")
    if data.empty:
        print("[DEBUG] No data returned!")
    else:
        print(f"[DEBUG] Retrieved {len(data)} rows of data.")
        print(data.tail())  # show last few rows
    return data

def plot_stock(data, ticker="AAPL"):
    if data.empty:
        print("[DEBUG] No data to plot.")
        return None
    plt.figure(figsize=(8,4))
    data['Close'].plot(title=f"{ticker} Stock Price")
    filename = f"static\\{ticker}_chart.png"
    plt.savefig(filename)
    plt.close()
    print(f"[DEBUG] Chart saved to {filename}")
    return filename
