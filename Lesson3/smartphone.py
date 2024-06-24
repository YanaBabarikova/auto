class Smartphone:
    def __init__(self, brand, model, number):
		self.brand = brand
		self.model = model
		self.number = number

    def print_smartphone(self):
		print(" Ваш телефон ", self.brand, "-", self.model, self.number)
