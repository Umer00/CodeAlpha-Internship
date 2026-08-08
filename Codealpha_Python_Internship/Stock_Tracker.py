# Fixed stock prices
stocks = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.20,
    "AMZN": 155.30,
    "MSFT": 380.00
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock_name = input("\nEnter stock name or 'done' to finish: ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stocks:
        print("Stock not found!")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

print("\n--- Your Portfolio ---")
for stock, qty in portfolio.items():
    value = stocks[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares = ${value:.2f}")

print(f"\n💰 Total Investment: ${total_investment:.2f}")

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(str(portfolio))
print("Portfolio saved to portfolio.txt")