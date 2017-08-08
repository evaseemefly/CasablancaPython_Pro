
class Animal:
	def __init__(self,name):
		self.name=name

	def talk(self):
		pass

	@staticmethod
	def animal_talk(obj):
		obj.talk()

class Cat(Animal):
	def talk(selfs):
		print("瞄")

class Dog(Animal):
	def talk(self):
		print("旺旺")

d=Dog("腊肠犬")
c=Cat("小猫")
Animal.animal_talk(c)
Animal.animal_talk(d)