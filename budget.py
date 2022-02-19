import collections

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

    def __str__(self):
        stars_len = (30 - len(self.name)) // 2
        budget_string = '*' * stars_len + self.name + '*' * stars_len + '\n'
        total_amount = 0
        for entry in self.ledger:
            description = entry["description"]
            amount = entry["amount"]
            total_amount += amount
            budget_string += description[:23].ljust(23) + "{:>7.2f}".format(amount) + "\n"

        return budget_string + "Total: " + str(total_amount)


def create_spend_chart(categories_list):
    bar_chart = "Percentage spent by category"
    total_spend = 0
    separate_amounts = []
    for cat in categories_list:
        for entry in cat.ledger:
            amount = entry["amount"]
            if amount < 0:
                total_spend += amount
                separate_amounts.append({cat.name: abs(amount)})

    counter = collections.Counter()
    for d in separate_amounts:
        counter.update(d)
    spend_by_cat = dict(counter)

    for k, v in spend_by_cat.items():
        spend_by_cat[k] = round(v/abs(total_spend) * 100)

    return spend_by_cat





if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    entertainment.deposit(45, "cinema")
    entertainment.withdraw(5)

    food.deposit(900, "deposit")
    food.withdraw(5, "milk, cereal, eggs, bacon, bread")
    food.transfer(20, entertainment)
    # print(food.get_balance())
    print(food.ledger)
    print(entertainment.ledger)
    #print(food)

    print(create_spend_chart([food, entertainment]))

    # print(entertainment.get_balance())

    # print(entertainment.check_funds(30))
    # print(food.check_funds(20))
    # print(entertainment.balance)
    # print(entertainment.ledger)
