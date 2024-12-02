class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

# Example usage
account = BankAccount(100)
print(f"Initial Balance: {account.balance}")

# Direct modification of the balance (even negative values can be set)
account.balance = -50
print(f"Modified Balance: {account.balance}")
