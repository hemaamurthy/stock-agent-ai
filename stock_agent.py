import openai
import yfinance as yf
import os

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to fetch stock data
def fetch_stock_price(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d")
    return hist["Close"].iloc[-1]

if __name__ == "__main__":
    symbol = input("Enter a stock symbol: ").upper()
    try:
        price = fetch_stock_price(symbol)
        print(f"The latest closing price of {symbol} is ${price:.2f}")
    except Exception as e:
        print("Error fetching stock data:", str(e))
