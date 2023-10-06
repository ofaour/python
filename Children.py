#!/bin/python3

class children:
	
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
	
	def isAdult(self):
		if self.age >= 18:
			print("This child is an adult.")
		else:
			print("This child is NOT an adult.")
