class BankAccount:
	def __init__(self, first_name, last_name, amount):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__amount = amount

class CurrentAccount(BankAccount):
	pass