import random

class PortfolioManager:
    def __init__(self):
        self.portfolio = {}
        self.cash = 10000  # Starting cash
        self.transactions = []

    def buy_stock(self, symbol, price, shares):
        cost = price * shares
        if cost > self.cash:
            return "Not enough cash to buy the stock."
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
            self.portfolio[symbol]['total_cost'] += cost
        else:
            self.portfolio[symbol] = {'shares': shares, 'total_cost': cost}
        self.cash -= cost
        self.transactions.append((symbol, 'buy', price, shares))
        return f"Bought {shares} shares of {symbol} at ${price} each."

    def sell_stock(self, symbol, price, shares):
        if symbol not in self.portfolio or self.portfolio[symbol]['shares'] < shares:
            return "Not enough shares to sell."
        revenue = price * shares
        self.portfolio[symbol]['shares'] -= shares
        if self.portfolio[symbol]['shares'] == 0:
            del self.portfolio[symbol]
        self.cash += revenue
        self.transactions.append((symbol, 'sell', price, shares))
        return f"Sold {shares} shares of {symbol} at ${price} each."

    def view_portfolio(self):
        portfolio_details = "\nCurrent Portfolio:\n"
        for symbol, data in self.portfolio.items():
            average_cost = data['total_cost'] / data['shares']
            portfolio_details += f"Stock: {symbol}, Shares: {data['shares']}, Average Cost: ${average_cost:.2f}\n"
        portfolio_details += f"Cash: ${self.cash:.2f}\n"
        return portfolio_details

    def view_transactions(self):
        transaction_history = "\nTransaction History:\n"
        for transaction in self.transactions:
            symbol, action, price, shares = transaction
            transaction_history += f"{action.title()} {shares} shares of {symbol} at ${price} each\n"
        return transaction_history

    def get_stock_prices(self, symbol):
        # This is a mock function. Replace with actual data retrieval.
        prices = [random.uniform(50, 150) for _ in range(30)]
        return prices

class User:
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password

def login(users):
    print("\n--- Login ---")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    for user in users:
        if user.phone == phone and user.password == password:
            print(f"Welcome {user.name}!")
            return user
    print("Invalid phone number or password. Please try again.")
    return None

def register(users):
    print("\n--- Register ---")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    users.append(User(name, phone, password))
    print("Registration successful!")

def main():
    print("\n               ------- Portfolio Manager----------             ")

    users = []
    manager = PortfolioManager()
    current_user = None

    while True:
        if not current_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("\nEnter your choice: ")

            if choice == '1':
                register(users)
            elif choice == '2':
                current_user = login(users)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\n1. Buy Stock")
            print("2. Sell Stock")
            print("3. View Portfolio")
            print("4. View Transactions")
            print("5. Logout")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                symbol = input("\nEnter stock symbol: ").upper()
                try:
                    price = float(input("\nEnter price per share: "))
                    shares = int(input("\nEnter number of shares: "))
                    result = manager.buy_stock(symbol, price, shares)
                    print(result)
                except ValueError:
                    print("Invalid input. Please enter numeric values for price and shares.")

            elif choice == '2':
                symbol = input("\nEnter stock symbol: ").upper()
                try:
                    price = float(input("\nEnter price per share: "))
                    shares = int(input("\nEnter number of shares: "))
                    result = manager.sell_stock(symbol, price, shares)
                    print(result)
                except ValueError:
                    print("Invalid input. Please enter numeric values for price and shares.")

            elif choice == '3':
                portfolio_details = manager.view_portfolio()
                print(portfolio_details)

            elif choice == '4':
                transaction_history = manager.view_transactions()
                print(transaction_history)

            elif choice == '5':
                current_user = None

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
