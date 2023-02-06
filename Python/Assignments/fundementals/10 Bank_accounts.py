class BankAccount:
    all_accounts = []

    def __init__(self, user, int_rate, balance):
        self.user = user
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else:
            print("Zero Balance")
        return self

    @classmethod
    def print_instances(cls):
        for account in cls.all_accounts:
            print(account.display_account_info())


micahel = BankAccount("michael", 1.05, 200)
anna = BankAccount("anna", 1.10, 100)

micahel.deposit(50).deposit(50).deposit(50).withdraw(
    100).yield_interest().display_account_info()

anna.deposit(100).deposit(100).withdraw(10).withdraw(
    10).withdraw(10).withdraw(10).display_account_info()

BankAccount.print_instances()
