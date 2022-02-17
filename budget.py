class Category:
    def __init__(self, name, initial_amount=0.0):
        self.name = name
        self.balance = initial_amount
        self.ledger = []

    def deposit(self, amount, description=None):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=None):
        # If there are not enough funds, nothing should be added to the ledger.
        # This method should return True if the withdrawal took place, and False otherwise.
        if amount > self.balance:
            self.balance -= amount
            self.ledger.append({"amount": (amount * -1), "description": description})
            return False
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, name):
        pass

    def check_funds(self):
        pass


if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    #print(food, entertainment, business)
    food.deposit(200)
    food.deposit(1000, "initial deposit")
    print(food.get_balance())


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
