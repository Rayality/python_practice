# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
class BankAccount:
    def __init__(self, opening_balance):
        self.bal = opening_balance

    def get_balance(self):
        return self.bal

    def deposit(self, ammount):
        self.bal += ammount
        return

    def withdraw(self, ammount):
        self.bal -= ammount
        return


account = BankAccount(100)
#
print(account.get_balance())  # prints 100
account.withdraw(50)
print(account.get_balance())  # prints 50
account.deposit(120)
print(account.get_balance())  # prints 170
