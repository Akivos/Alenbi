class Residents:

	add_year = 1

	def __init__(self, first, last, age, hobby):
		self.first = first
		self.last = last
		self.age = age
		self.hobby = hobby

	def __repr__(self):
		return f"{self.first}{self.last}{self.age}{self.hobby}"

	def __str__(self):
		return "{}{}, age: {}".format(self.last, self.first, self.age)

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.first, self.last)

	def apply_raise(self):
		self.age = (self.age + self.add_year)



	


