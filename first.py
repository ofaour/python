#!/bin/python3

print("Hello World!")
print("""This string runs
multiple lines!""")
print("This string is " + "awesome") #we can also concatenate
print('\n') #new line
print('Test that new line out.')


print('\n')
#MATH
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over (remainder)
print(50.0 / 6) #division with decimals
print(50 // 6) #no remainder


print('\n')
#VARIABLES AND METHODS
quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters


name = "Heath" #string
age = 33 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No!

print("My name is " + name + " and I am " + str(age) + " years old.")

age +=1
print(age)

birthday = 1
age += birthday
print(age)


print('\n')
#FUNCTIONS
print("Here is an example function:")

def who_am_i(): #this is a function without parameters
	name = "Heath"
	age = 30 #local variable
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()	

#adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)


def nl():
	print('\n')
	
nl()


print('\n')
#BOOLEAN EXPRESSIONS (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
not_greater_than = 5 > 7
not_less_than = 7 < 5
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = greater_than and less_than #True
test_and2 = greater_than and not_greater_than #False
test_or = greater_than or less_than #True
test_or2 = greater_than or not_greater_than #True

test_not = not True #False

print(test_and)
print(test_and2)
print(test_or)
print(test_or2)


print('\n')
#CONDITIONAL STATEMENTS
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))


def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young!"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))


nl()
#LISTS
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list - index / indices
print(movies[0]) #returns the first item in the list
print(movies[1:3]) #returns the first number given until right before last number given
print(movies[1:4]) #returns all 
print(movies[1:]) #returns everything from number to end of list
print(movies[:1]) #everything before 1
print(movies[:2])
print(movies[-1]) #grabs last item

print(len(movies)) #counts items in list
movies.append("JAWS")
print(movies) #appends to end of list

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes last item
print(movies)

movies.pop(0) #removes first item 
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
print(grades[0][1])
grades[0][1] = 85
print(grades[0][1])


nl()
#TUPLES (Values can't be changed)
grades = ("a", "b", "c", "d", "f")

print(grades[1])


nl()
#LOOPS
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
#While loops - execute as long as true
i = 1

while i < 10:
	print(i)
	i += 1
	

nl()
#ADVANCED STRINGS
my_name = "Heath"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'" #show example
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello          "
print(too_much_space.strip())

print("A" in "Apple") #returns true
print("a" in "Apple") #returns false - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = 'The Hangover'
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s" % movie)
print(f"My favorite movie is {movie}")


nl()
#DICTIONARIES - key/value pairs {}
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))


nl()
#IMPORTING MODULES
import sys #system functions and parameters
from datetime import datetime as dt #import with alias 

print(sys.version)
print(dt.now())


nl()
#SOCKETS

