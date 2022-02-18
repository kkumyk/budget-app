class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if amount < self.balance:
            self.balance -= amount
            self.ledger.append({"amount": (amount * -1), "description": description})
            return True
        return False


    def get_balance(self):
        return self.balance

    def transfer(self, transfer_amount, category):
        if transfer_amount > self.balance:
            return False
        self.withdraw(transfer_amount, "Transfer to " + category.name)
        category.deposit(transfer_amount, "Transfer from " + self.name)
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    # entertainment.deposit(45, "cinema")

    food.deposit(900, "deposit")
    food.deposit(10, "tips")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    food.transfer(20, entertainment)

    print(food.get_balance())
    print(food.ledger)

    print(entertainment.get_balance())
    print(entertainment.ledger)

    print(entertainment.check_funds(30))
    print(food.check_funds(20))





    # print(entertainment.balance)
    # print(entertainment.ledger)






# def create_spend_chart(categories):
#     pass
