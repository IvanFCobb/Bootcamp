class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
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
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else:
            print("Zero Balance")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


michael = User("Michael", "mSmith@yahoo.com")
michael.make_deposit(500)
michael.make_withdrawl(250)
michael.display_user_balance()
