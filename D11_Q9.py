class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Balance:", self.__balance)

acc = Account()
acc.deposit(1000)
acc.withdraw(300)
acc.display_balance()