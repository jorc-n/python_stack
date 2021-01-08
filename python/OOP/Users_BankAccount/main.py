class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0,name)


class BankAccount:
    def __init__(self, int_rate, balance,name):
        self.interes = int_rate
        self.monto = balance
        self.name=name

    def deposit(self, amount):
        self.monto += amount
        return self

    def withdraw(self, amount):
        if self.monto < amount:
            print("Fondos Insuficiente: cobrar una tarifa de $5")
            self.monto -= 5
        else:
            self.monto -= amount
        return self

    def display_account_info(self):
        print("usuario", self.name, "--saldo:", self.monto)
        return self

    def yield_interest(self):
        if self.monto > 0:
            self.monto += self.monto * self.interes
            return self


jorge = User("Jorge", "j@mail.com")
gustavo = User("Gustavo", "g@mail.com")
oscar = User("Oscar", "o@mail.com")

jorge.account.deposit(1000).deposit(800).withdraw(500).yield_interest().display_account_info()
gustavo.account.deposit(5000).deposit(500).withdraw(4000).yield_interest().display_account_info()
oscar.account.deposit(1500).deposit(500).withdraw(3000).yield_interest().display_account_info()