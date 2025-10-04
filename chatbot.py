# chatbot.py
# Basic chatbot logic – later you can upgrade with GPT-4/5

def ask_bot(question, stock_data):
    question = question.lower()

    # Ensure we get a single float
    if stock_data.empty:
        return "No stock data available right now."
    
    last_price = float(stock_data["Close"].iloc[-1])
    previous_price = float(stock_data["Close"].iloc[-2])  # for up/down comparison

    if "price" in question or "close" in question:
        return f"The last closing price is ${last_price:.2f}."
    elif "up" in question:
        change = last_price - previous_price
        if change > 0:
            return f"Yes, it went up by ${change:.2f}."
        else:
            return f"No, it went down by ${abs(change):.2f}."
    elif "down" in question:
        change = last_price - previous_price
        if change < 0:
            return f"Yes, it went down by ${abs(change):.2f}."
        else:
            return f"No, it went up by ${change:.2f}."
    else:
        return "I can tell you the last price and whether the stock went up or down. Try asking 'Did AAPL go up?"
