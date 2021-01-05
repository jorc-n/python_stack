
class BankAccount:
    def __init__(self, int_rate, balance):
        self.interes = int_rate
        self.monto=balance

    def deposit(self, amount):
        self.monto+=amount
        return self

    def withdraw(self, amount):
        if self.monto<amount:
            print("Fondos Insuficiente: cobrar una tarifa de $5")
            self.monto-=5
        else:
            self.monto-=amount
        return self

    def display_account_info(self):
        print("saldo:", self.monto)
        return self

    def yield_interest(self):
        if self.monto>0:
            self.monto+=self.monto*self.interes
            return self
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, monto):
        self.account.deposit(monto)
        return self

    def make_withdrawal(self, cantidad):
        self.account.withdraw(cantidad)
        return self

    def display_user_balance(self):
        print("Usuario ", self.name, self.account.display_account_info())
        return self

cuenta1=BankAccount(0.1,100)
jorge=User("Jorge","j@mail.com")
gustavo=User("Gustavo","g@mail.com")
oscar=User("Oscar", "o@mail.com")
jorge.make_deposit(30).make_deposit(10).make_deposit(20).make_withdrawal(10).display_user_balance()
gustavo.make_deposit(30).make_deposit(30).make_withdrawal(20).make_withdrawal(10).display_user_balance()
oscar.make_deposit(50).make_withdrawal(10).make_withdrawal(15).make_withdrawal(10).display_user_balance()

