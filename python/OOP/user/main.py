

class usuario:
    def __init__(self, nombre, mail):
        self.nombre=nombre
        self.mail=mail
        self.cta_bancaria=0

    def make_deposit(self, monto):
        self.cta_bancaria+=monto
        return self

    def make_withdrawal(self, cantidad):
        self.cta_bancaria-=cantidad
        return self

    def display_user_balance(self):
        print("Usuario ",self.nombre, "Monto ",self.cta_bancaria)
        return self

    def transfer_money (self, other_user,cantidad):
        self.make_withdrawal(cantidad)
        other_user.make_deposit(cantidad)
        return self

    
jorge=usuario("Jorge","j@mail.com")
gustavo=usuario("Gustavo","g@mail.com")
oscar=usuario("Oscar", "o@mail.com")
jorge.make_deposit(30).make_deposit(10).make_deposit(20).make_withdrawal(10).display_user_balance()
gustavo.make_deposit(30).make_deposit(30).make_withdrawal(20).make_withdrawal(10).display_user_balance()
oscar.make_deposit(50).make_withdrawal(10).make_withdrawal(15).make_withdrawal(10).display_user_balance()
jorge.transfer_money(oscar,30).display_user_balance()
oscar.display_user_balance()