####################################
####################################
##                                ##
##   Python Part 1 Cheat Sheet    ##
##                                ##
####################################
####################################


################
#   Comments   #
################

# This is a comment - Not run in the program but good for notes


######################
#   Variable Types   #
######################

this_is_var = "This is a Variable"			# variables store values by name
											# variable name can be a combination of
											# letters, numbers, or _
											# uses snake_case and can't start with number

int_var = 32								# integer
float_var = 64.2							# number with decimal
str_var = "This is not a number"			# string of characters
bool_var = True								# boolean - must be title case (True or False)

int_var_to_str = str(12)					# changes to a string
str_to_float = float("6.4")					# changes to a float
float_to_int = int(1.6)						# changes to int


#########################
#   Simple Operations   #
#########################

int_var = 32 / 8							# division - now eqals 4
float_var = 64.2 + 3						# addition - now equals 67.2
int_var = 8 * 2								# multiplication - now equals 16
float_var = 67.2 - 7						# subtraction - now equals 60.2

int_var = (16 / 2) + 8						# parentheses performed first

int_var = 16**2								# exponent - now equals 256
int_var = 256**(1/2)						# exponent - now equals 16

int_var = 16 // 5							# floor division (drops remainder) - now equals 3
int_var = 3 % 2								# modulo (returns remainder) - now equals 1

int_var += 1								# adds the right to the left and saves it to the variable
											# - now equals 2
											# can use -= *= /= %= //= **= for different operations


############################
#   Playing with Strings   #
############################

print(str_var)								# outputs string to console (drops outer quotations)
new_str = input("Type something here: ")	# takes input from the user(as string)
print(new_str)

str_var = 'This is a string'				# single ' or " can also be used for strings
print(new_str)

str_var = "This \nis \na \nstring"			# \n creates a new line for the text
print(str_var)

str_var = 'This is Gento\'s text'			# \ allows use of function characters within string
print(str_var)

str_var = "This " + "is a string"			# strings can be added to make one string
print(str_var)

str_var = "This is the number " + str(12)	# numbers need to be converted to strings to add
print(str_var)

str_var = "string" * 3						# can multiple string by an integer to repeat
print(str_var)


####################################
#   Comparisons and Conditionals   #
####################################

1 == 1										# == returns True if both sides are equal
1 != 1										# != returns True is not equal

2 > 1										# > returns True if left side is greater
2 >= 1										# >= returns True if left side is greater or equal
1 < 2										# < returns True if left side is lesser
1 <= 2										# <= returns True if left side is lesser or equal

1 == 1 and 2 == 2							# and check is True only if both sides True
1 == 2 or 1 == 1							# or check is True if at least one side is True
not 1 == 2									# not check is True statement after is False

if 1 == 1:									# checks statement and runs if True (needs 
	print("This is True")					# inside needs tab - tabs indicate what's inside
	
if 1 == 2:									# if False won't run what's inside
	print("You won't see this in execute")
elif 1 == 3:								# elif will run if previous if / elif is False
	print("You won't see this either")		# - and the check is True (must follow if / elif)
	if 1 == 1:								# these checks and statements can be nested
		print("This is a nested if")
else:										# else will run if previous if / elif is False
	print("This is from an else statement")	# - (must be at end of if / elif chain)


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

this_list = [1, 2, 3, 4]					# lists are made with brackets
int_var = this_list [0]						# calls in specific value in that index
											# index starts at 0 - this_list index is 0-3

for item in this_list:						# for cycles through a list and preforms what"s inside
	print(item)

counter = 0
while counter < 3:							# while loop runs what's inside repeatedly if True
	print("In a loop")						# - this prints the string 3 times
	counter += 1
