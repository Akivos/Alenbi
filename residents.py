class Residents:

	add_year = 1

	def __init__(self, first, last, age, hobby):
		self.first = first
		self.last = last
		self.age = age
		self.hobby = hobby

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.first, self.last)


	def __repr__(self):
		return f"{self.first} {self.last} {self.age} {self.hobby}"

	def __str__(self):
		return "{}, hobby: {}".format(self.full_name, self.hobby)

	def birthday(self):
		self.age = self.age + self.add_year


