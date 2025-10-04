# app.py
from flask import Flask, render_template, request
from stocks import fetch_stock_data, plot_stock
from chatbot import ask_bot
import schedule, threading, time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    chart_file = ""
    if request.method == "POST":
        question = request.form["question"]
        print(f"[DEBUG] User asked: {question}")
        data = fetch_stock_data("AAPL")
        chart_file = plot_stock(data, "AAPL")
        response = ask_bot(question, data)
        print(f"[DEBUG] Bot response: {response}")
    return render_template("index.html", response=response, chart=chart_file)

def update_data():
    data = fetch_stock_data("AAPL")
    plot_stock(data, "AAPL")

def run_scheduler():
    schedule.every(1).hours.do(update_data)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Run scheduler in background
threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    print("Template folder:", app.template_folder)
    app.run(debug=True)
