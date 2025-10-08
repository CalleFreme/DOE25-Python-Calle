class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute
        self.__password = password
        self.is_logged_in = False

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.is_logged_in:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Successfully withdrew: ", amount)
            else:
                print("Invalid withdrawal amount.")
        else:
            print("User is not logged in.")

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            print("Wrong password.")

    def sign_in(self, password):
        if password == self.__password:
            print("Successfully logged in.")
            self.is_logged_in = True

bankacc1 = BankAccount("Alice", "bralosen123", 1000)
print(bankacc1.get_balance("bralosen321"))
bankacc1.sign_in("bralosen123")
print(bankacc1.withdraw(500))

