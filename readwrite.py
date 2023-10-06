#!/bin/python3

#READ AND WRITE TO FILE

with open("months.txt", "r") as file:

	months = file.read()
	print(months)

with open("months.txt", "a") as filewrite:
	filewrite.write("\nThe year is 2023.")


with open("months.txt", "r") as file2:	
	newcontent = file2.read()
	print(newcontent)

