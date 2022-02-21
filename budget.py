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
        spend_by_cat[k] = int(str(round(v / abs(total_spend) * 100) - round(v / abs(total_spend) * 100) % 10)[0]) + 1

    key_list = []
    lens = []
    percentage_lengths = []  # [8, 1]
    for k, v in spend_by_cat.items():
        key_list.append(k)
        lens.append(len(k))
        percentage_lengths.append(v)

    amend_keys = [(k + " " * (max(lens) - len(k))) if len(k) < max(lens) else k for k in key_list]

    amend_keys_list = list(amend_keys[0])
    first_key = ["     " + str(amend_keys_list[i]) for i in range(len(amend_keys_list))]
    amend_keys[0] = first_key

    column_descriptions = ""
    for i in range(max(lens)):  # columns
        for key in amend_keys:  # rows
            column_descriptions += key[i] + "  "
        column_descriptions += "\n"

    raw_dots = [l * "o" for l in percentage_lengths]
    amend_raw_dots = [(" " * (11 - len(dots)) + dots) if len(dots) < 11 else dots for dots in raw_dots]

    percentage_bar = []
    for p in range(100, -10, -10):
        percentage_bar.append((str(p) + "| ").rjust(5))

    # Constructing the first line of the percentage bar
    # Get the first string from the amend_raw_dots
    first_spend_line = amend_raw_dots[0]
    # split first_spend_line into a list of characters including the empty spaces
    first_spend_line_list = list(first_spend_line)
    # combine two lists - first_spend_line_list and percentage_bar - into pairs
    first_bar_line = [str(percentage_bar[i]) + first_spend_line_list[i] for i in range(len(percentage_bar))]
    # Replace the first item in the amend_raw_dots with the constructed first_bar_line
    amend_raw_dots[0] = first_bar_line

    percentage_dots = ""
    for i in range(11):  # columns
        for dot in amend_raw_dots:  # rows
            percentage_dots += dot[i] + "  "
        percentage_dots += "\n"
    percentage_dots += "    " + "-" * (len(raw_dots) * 2 + 4) + "\n"

    return "Percentage spent by category" + "\n" + percentage_dots + column_descriptions.rstrip("\n")


# if __name__ == "__main__":
#
#     food = Category("Food")
#     entertainment = Category("Entertainment")
#     business = Category("Business")
#     food.deposit(900, "deposit")
#     entertainment.deposit(900, "deposit")
#     business.deposit(900, "deposit")
#     food.withdraw(105.55)
#     entertainment.withdraw(33.40)
#     business.withdraw(10.99)
#     print(create_spend_chart([business, food, entertainment]))

