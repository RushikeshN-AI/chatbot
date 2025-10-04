# chatbot.py
# Basic chatbot logic – later you can upgrade with GPT-4/5

def ask_bot(question, stock_data):
    question = question.lower()
    last_price = stock_data["Close"].iloc[-1]

    if "price" in question or "close" in question:
        return f"The last closing price is ${last_price:.2f}."
    elif "up" in question:
        change = stock_data["Close"].iloc[-1] - stock_data["Close"].iloc[-2]
        if change > 0:
            return f"Yes, it went up by ${change:.2f}."
        else:
            return f"No, it went down by ${abs(change):.2f}."
    elif "down" in question:
        change = stock_data["Close"].iloc[-1] - stock_data["Close"].iloc[-2]
        if change < 0:
            return f"Yes, it went down by ${abs(change):.2f}."
        else:
            return f"No, it went up by ${change:.2f}."
    else:
        return "I can tell you the last price and whether the stock went up or down. Try asking 'Did AAPL go up?'"
