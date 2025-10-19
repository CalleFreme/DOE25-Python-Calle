import datetime


class Transaction:

    def __init__(self, type, amount, category, descr=None, date="00-00-00"):
        self.type = type
        self.amount = amount
        self.category = category
        self.descr = descr
        self.date = date
        self.sign = self.get_sign()

    def __str__(self):
        return f"{self.date} {self.category}: {self.sign}{self.amount}kr"

    def __repr__(self):
        return f"{self.date} {self.category}: {self.sign}{self.amount}kr"

    def __lt__(self, other):
        # lt = less than
        # Sort by date:
        return self.date < other.date

    def __eq__(self, other):
        # eq = equal
        if self.date == other.date:
            return self.amount == other.amount
        return False

    def get_sign(self):
        if self.type == "e":
            return "-"
        else:
            return ""
