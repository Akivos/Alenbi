import unittest
from residents import Residents
from residents import Worker

res1 = Residents("Dalik", "Oslander", 42, "Movies")
res2 = Residents("Shlomi", "Mizrahi", 38, "Singing")
res3 = Residents("Nahum", "Cohen", 48, "Enjoying the moment")
worker1 = Worker("Akiva", "Botesazan", 22, "Music")

worker1.add_res(res1)

class ResTest(unittest.TestCase):

	def setUp(self):
		self.res1 = res1
		self.res2 = res2
		self.res3 = res3
		self.worker1 = worker1

	def test_first(self):
		self.assertEqual(self.res1.first, "Dalik")
		self.assertEqual(self.res2.first, "Shlomi")
		self.assertEqual(self.res3.first, "Nahum")
		self.assertEqual(self.worker1.first, "Akiva")

	def test_last(self):
		self.assertEqual(self.res1.last, "Oslander")
		self.assertEqual(self.res2.last, "Mizrahi")
		self.assertEqual(self.res3.last, "Cohen")
		self.assertEqual(self.worker1.last, "Botesazan")

	def test_full(self):
		self.assertEqual(self.res1.full_name, "Dalik Oslander")
		self.assertEqual(self.res2.full_name, "Shlomi Mizrahi")
		self.assertEqual(self.res3.full_name, "Nahum Cohen")
		self.assertEqual(self.worker1.full_name, "Akiva Botesazan")

	def test_age(self):
		self.assertEqual(self.res1.age, 42)
		self.assertEqual(self.res2.age, 38)
		self.assertEqual(self.res3.age, 48)
		self.assertEqual(self.worker1.age, 22)

	def test_hobby(self):
		self.assertEqual(self.res1.hobby, "Movies")
		self.assertEqual(self.res2.hobby, "Singing")
		self.assertEqual(self.res3.hobby, "Enjoying the moment")
		self.assertEqual(self.worker1.hobby, "Music")

	def test_email(self):
		self.assertEqual(self.res1.email, "Dalik.Oslander@gmail.com")
		self.assertEqual(self.res2.email, "Shlomi.Mizrahi@gmail.com")
		self.assertEqual(self.res3.email, "Nahum.Cohen@gmail.com")
		self.assertEqual(self.worker1.email, "Akiva.Botesazan@gmail.com")

	def test_personal(self):
		self.assertEqual(self.worker1.personal_guidence, ["Dalik Oslander"])

	

if __name__ == "__main__":
	unittest.main()


