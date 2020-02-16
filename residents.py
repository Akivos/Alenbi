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


class Worker(Residents):
	def __init__(self, first, last, age, hobby, personal_guidence=None):
		super().__init__(first, last, age, hobby)
		if personal_guidence is None:
			self.personal_guidence = []
		else:
			self.personal_guidence = personal_guidence

	def add_res(self, res):
		if res not in self.personal_guidence:
			self.personal_guidence.append(res.full_name)

	def remove_res(self, res):
		if res in self.personal_guidence:
			self.personal_guidence.remove(res.full_name)







