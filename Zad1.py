class Account:
    def __init__(self, name, account_id, balance):
        self.name = name
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def payment(self, price):
        self.balance -= price

acc = Account("Dani", "4321", 420)
acc.payment(50)
print(acc.balance)    