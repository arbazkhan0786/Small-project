class BankAccount:
    def __init__(self, accountNumber, name, balance=0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance}")

# Creating an instance of BankAccount
account = BankAccount("123456", "Alice", 1000)

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)

# Displaying account information
account.display_info()