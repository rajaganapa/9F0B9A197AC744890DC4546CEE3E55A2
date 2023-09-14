class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

# Example usage of the BankAccount class
if __name__ == "__main__":
    account1 = BankAccount("123456", "John Doe", 1000)
    account2
    account1.deposit(500)
    account1.withdraw(200)
    account1.check_balance()
    account2.deposit(2000)
    account2.withdraw(1500)
    account2.check_balance()