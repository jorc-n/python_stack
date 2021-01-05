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

cuenta1=BankAccount(0.1,0)
cuenta2=BankAccount(0.05,0)

cuenta1.deposit(1000).deposit(1500).deposit(500).withdraw(800).yield_interest().display_account_info()
cuenta2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(100).yield_interest().display_account_info()