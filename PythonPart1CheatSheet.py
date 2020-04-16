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


#############################
#   Data Types & Variables  #
#############################

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


#######################
#   Data Structures   #
#######################

# strings are made with single or double quotes
this_string = "This is a string"
# mult-line strings can be made with triple quotes
muli_line = '''This is 
a string 
on mulitple lines'''
# strings are immutable - they cannot be changed (need to reassign the variable to change)

# lists are made with brackets
this_list = [1, 2, 3, 4]
# calls in specific value in that index (starts at 0)
int_var = this_list [0]
# this_list index is 0-3
# lists are mutable - they can be changed

# tuples are made with parentheses
this_tuple = (1, 2, 3, 4)
# tuples similar to lists but immutable

# strings, lists, and tuples are ordered - stay in their sequence and allow repeats

# sets are made with curly brackets
this_set = {1, 2, 3, 4}
# sets are mutable
#sets are unordered - no repeats or defined sequence

# dictionaries


############################
#   Playing with Strings   #
############################

# takes input from the user(as string)
input_str = input("Type something here: ")
# outputs string to console (drops outer quotations)
print(input_str)

# \n creates a new line for the text
str_var = "This \nis \na \nstring"

# \ allows use of function characters within string
str_var = 'This is Gento\'s text'

# strings can be added to make one string
str_var = "This " + "is a string"

# numbers need to be converted to strings to add
str_var = "This is the number " + str(12)

# can multiple string by an integer to repeat
str_var = "string" * 3


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


#############
#   Loops   #
#############

# cycles through a data structure
# preforms what's inside for each element
for item in this_list:
	print(item)

# while loop runs what's inside repeatedly if True
counter = 0
while counter < 3:
	print("In a loop")
	counter += 1
# this prints the string 3 times


#################################
#   Exceptions and Assertions   #
#################################

# catch exceptions(errors) and determine what to do with them

# runs what's inside and checks for exceptions
try:
	print(1 / int(input("Divide 1 by: ")))
# if the specific exception occurs, runs what's inside (must follow try)
except ZeroDivisionError:
	print("You cannot divide by 0")
	# can raise an error anytime (more info in paranthesis)
	raise ValueError("There was an Error")
# if any exception occurs, runs what's inside (must follow try)
except:
	print("Error")
	# raises the exception that occured to cause the program to go to except again
	raise
# in no exception occurs, runs what's inside
else:
	print("Success")
# runs at the end no matter if there is an exception or not (must follow try)
finally:
	print("Finished")

# program will continue if exceptions are handled in the try-except block
# if another exception is raised that's not handled by except, program stops with an error

# checks if what comes after is true
# if false raises AssertionError exception
# more info after comma
assert 1==1, "One does not egual one"


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

# example used in Built-in Functions section
def this_function(something):
	if something == 1:
		return True
	else:
		return False


##########################
#   Built-in Functions   #
##########################

# returns absolute value of integer or float
abs(-1)

# returns a data structure with values that failed a True/False function filtered out
# arg1 is a function and arg2 is a data structure filter
filter(this_function, this_list)

# returns a float from a number or string of a number
float(int_var)

# returns user input as a string (prompt for the user as argument)
input("Type something: ")

# returns an integer from a number or string of a number
# drops the decimal (rounds down)
int(float_var)

# return the length or a data structure as an integer
len(this_list)

# return a list of the elements of a data structure
list("This is a list of letters and spaces")

# returns a data structure with a function applied to each element
map(this_function, this_list)

# output argument to terminal as string
print(this_string)

# return a rounded integer or float
# arg 1 is the number to be rounded and arg2 is the decimal places to round to
# exclude arg2 to return an integer
round(float_var, 1)

# returns a set of the elements of a data structure
set(this_list)

# returns a string
str(int_var)

# returns the sum of elements of a data structure
sum(this_list)

# returns a tuple from a given data structure
tuple(this_list)

# A more complete list of the build-in functions:
# - https://docs.python.org/3/library/functions.html


###############
#   Modules   #
###############

# modules are separate scripts that can be imported for use
# can import modules from:
# - standard library (comes with python install)
# - installed modules (installed using pip from PyPi, or other)
# - your own modules (modules in your project - directory path separated by dot
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
