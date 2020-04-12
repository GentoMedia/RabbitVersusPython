#############################
#############################
##                         ##
##   Python Cheat Sheet    ##
##                         ##
#############################
#############################


################
#   Comments   #
################

# This is a comment - Not run in the program but good for notes


######################
#   Variable Types   #
######################

# variables store values by name
this_is_var = "This is a Variable"
# variable name can be a combination of
# letters, numbers, or _
# uses snake_case and can't start with number

# integer
int_var = 32
# number with decimal
float_var = 64.2
# string of characters
str_var = "This is not a number"
# boolean - must be title case (True or False)
bool_var = True

# changes to a string
int_var_to_str = str(12)
# changes to a float
str_to_float = float("6.4")
# changes to int
float_to_int = int(1.6)


#########################
#   Simple Operations   #
#########################

# division
int_var = 32 / 8
# addition
float_var = 64.2 + 3
# multiplication
int_var = 8 * 2
# subtraction
float_var = 67.2 - 7

# parentheses performed first
int_var = (16 / 2) + 8

# exponent
int_var = 16**2	
int_var = 256**(1/2)

# floor division (drops remainder)
int_var = 16 // 5
# modulo (returns remainder) - now equals 1
int_var = 3 % 2

# adds the right to the left and saves it to the variable
int_var += 1
# now equals 2
# can use -= *= /= %= //= **= for different operations


############################
#   Playing with Strings   #
############################

# takes input from the user(as string)
input_str = input("Type something here: ")
# outputs string to console (drops outer quotations)
print(input_str)

# single ' or " can also be used for strings
new_str = 'This is a string'
print(new_str)

# \n creates a new line for the text
str_var = "This \nis \na \nstring"
print(str_var)

# \ allows use of function characters within string
str_var = 'This is Gento\'s text'
print(str_var)

# strings can be added to make one string
str_var = "This " + "is a string"
print(str_var)

# numbers need to be converted to strings to add
str_var = "This is the number " + str(12)
print(str_var)

# can multiple string by an integer to repeat
str_var = "string" * 3
print(str_var)


####################################
#   Comparisons and Conditionals   #
####################################

# returns True if both sides are equal
1 == 1
# != returns True is not equal
1 != 1

# > returns True if left side is greater
2 > 1
# >= returns True if left side is greater or equal
2 >= 1
# < returns True if left side is lesser
1 < 2
# <= returns True if left side is lesser or equal
1 <= 2

# True only if both sides True
1 == 1 and 2 == 2
# True if at least one side is True
1 == 2 or 1 == 1
# True if statement after is False
not 1 == 2

# checks statement and runs if True
if 1 == 1:
	print("This is True")

# if False won't run what's inside
if 1 == 2:
	print("You won't see this in execute")
# elif will run if previous if / elif is False and the check is True (must follow if / elif)
elif 1 == 3:
	print("You won't see this either")
	# these checks and statements can be nested
	if 1 == 1:
		print("This is a nested if")
# will run if previous if / elif is False
else:
	print("This is from an else statement")
# else will run if previous if / elif is False (must be at end of if / elif chain)

#############################
#   P E M D A S C N A O A   #
#############################

# Order of operations

# Parentheses
# Exponents
# Multiplication & Division
# Addition & Subtraction
# Comparison
# Not
# And
# Or
# Assignment


#######################
#   Lists and Loops   #
#######################

# lists are made with brackets
this_list = [1, 2, 3, 4]
# calls in specific value in that index (starts at 0)
int_var = this_list [0]
# this_list index is 0-3

# for cycles through a list and preforms what"s inside
for item in this_list:
	print(item)

# while loop runs what's inside repeatedly if True
counter = 0
while counter < 3:
	print("In a loop")
	counter += 1
# this prints the string 3 times


#################
#   Functions   #
#################

# a function is a word followed by parenthasis
# e.g. print()
# functions are objects

# define your own function before you run it
# if the function takes arguments, they should be in the parentheses (optional)
# arguments with an '=' sign are optional when function is called (optional)
def function_name(arg1, arg2 = "!"):
	""" Docstring to explain code
		It's multiline """
	sentence = arg1 + arg2
	# returns a value from the function (optional)
	return sentence

# function needs to be called to run
print(function_name("I want this printed"))


###############
#   Modules   #
###############

# modules are separate scripts that can be imported for use
# can import modules from:
# - standard library (comes with python install)
# - installed modules (installed using pip from PyPi, or other)
# - your own modules (modules in your project - directory path separated by '.'
#    - e.g. 'script_folder.module'

# imports the whole module
# - need to call the module name when using objects
import math

# imports specific objects from a module (use commas to separate multiple objects)
# - only need to call object when using
from time import sleep, tzname

# can give a different name to imported objects
from datetime import date as year_month_day

# calling the variables or functions from a module that's imported
print(math.pi)
for i in range(3):
	sleep(1)
	print(i)
print(tzname)
print(year_month_day.today())


#################################
#   Exceptions and Assertions   #
#################################


try:
	print(1 / int(input("Divide 1 by: ")))
except ZeroDivisionError:
	print("Error")
else:
	print("Success")
finally:
	print("Finished")


