#!/bin/python3

from Children import children

kenan = children("Kenan", 7, "Male")
mariam = children("Mariam", 2, "Female")
helmi = children("Helmi", 31, "Male")


print(kenan.name, kenan.age, kenan.gender) 
kenan.isAdult()
print("\n", mariam.name, mariam.age, mariam.gender) 
mariam.isAdult()
print("\n", helmi.name, helmi.age, helmi.gender) 
helmi.isAdult()
