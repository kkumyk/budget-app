class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # If there are not enough funds, nothing should be added to the ledger.
        # This method should return True if the withdrawal took place, and False otherwise.
        if amount < self.balance:
            self.balance -= amount
            self.ledger.append({"amount": (amount * -1), "description": description})
            return True
        return False





    # def transfer(self, amount, name):
    #     pass
    #
    # def check_funds(self):
    #     pass

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    # entertainment.deposit(45, "cinema")

    food.deposit(900, "deposit")
    food.deposit(10, "tips")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")


    print(food.balance)
    print(food.ledger)

    # print(entertainment.balance)
    # print(entertainment.ledger)

# print(food.get_balance())


# def transfer(self, amount, name):
#     self.amount = amount
#     self.name = name
#
#     if self.balance - amount > 0:
#         self.balance -= amount
#         self.ledger.append({"amount": (amount * -1), "description: Transfer to": name})


#
#
#
# def create_spend_chart(categories):
#     pass
