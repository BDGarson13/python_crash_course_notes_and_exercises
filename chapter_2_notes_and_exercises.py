
name = "steve jobs"
print(name.title())

#The title() term after the variable, name, is categorised as a "method."  Methods are defined as actions that Python is capaable of performing on pieces of data.
#In our case, the title() method causes the first letters of each word in the string to be turned from its lower case into its upper case.
#The . tells Python to perform the method on the variable name.

name = "Steve Jobs"

print(name.lower())
print(name.upper())

#The lower() and upper() methods above either return the variable's letters all in the lower case or upper case, respectively.
#The lower() method is supposedly useful for data collection when you don't trust the use of a capitalization.

#Occasionally you'll want to use variables in strings, this can be achieved in the following way:

first_name = "steve"
last_name = "jobs"
full_name = f"{first_name} {last_name}"
print(full_name)

#In order for you to substitute the variables' values into strings, the f letter must be used outside of the quotation marks.
#One can do all manner of things with f strings, such as composing the following message:

print(f"Hello, {full_name.title()}!")

#Why not just denote the above as a new variable named message?  If we were having to repeatedly print it then it would save us a lot of time in the future.

message = f"Hello, {full_name.title()}!"
print(message)

#The addition of whitespace to strings can be done in two important ways.  The first of which is to indent whatever it is that you're trying to print.

print("Apple")
print("\tApple")

#Should one want to start a new line, the use of the charater combination \n should be observed as follows:

print("Tech Companies: \nApple \nMicrosoft \nFacebook \nTwitter")

#But what if you also want to indent the preceding terms as well as start new lines?

print("Tech Companies:\n\tApple\n\tMicrosoft\n\tFacebook\n\tTwitter")

#EXERCISES 2.3 --> 2.7.:

#EXERCISE 2.3:

name = "Holly"
message = f"Hello, {name}, I hope that you're doing well in spite of the fact that you live with the biggest of degens known to Man!"
print(message)

#EXERCISE 2.4:

name = "George Hinchliffe"
print(name.lower())
print(name.upper())
print(name.title())

#EXERCISE 2.5:

quote = '\tAyn Rand once very wisely, as always seems to be the case, said that "You can ignore reality, but \n\tyou cannot ignore the consequences of ignoring reality."'
print(quote)

#EXERCISE 2.6:

famous_person = "Ayn Rand"
quote = "You can ignore reality, but \n\tyou cannot ignore the consequences of ignoring reality."
message = f'\t{famous_person} once very wisely, as always seems to be the case, said that "{quote}"'
print(message)

#Should one want to add two numbers together, one simply creates a variable, in this case, number_addition, to subsequently print the variable. 

number_addition = 2 + 3
print(number_addition)

#The various other operations are expressed as follows:

number_subtraction = 2 - 3
print(number_subtraction)

number_multiplication = 2 * 3
print(number_multiplication)

number_division = 2 / 3
print(number_division)

number_exponentiation = 3 ** 2
print(number_exponentiation)

#In Python, as well as other coding programs, a float is a term ascribed to numbers in which a decimal point features.  
#The word float is used due to a decomal place appearing anywhere in the number.

float_addition_1 = 0.1 + 0.1
print(float_addition_1)

float_addition_2 = 0.2 + 0.1
print(float_addition_2)

#I don't know why, but as has been made clear from the float sums in the terminal, you can see that an arbitrary number of decimal places can sometimes follow.
#Should you divide two numbers by each other, even if they're integers, a float is obtained as can be seen from the terminal below:

integer_division = 4/2
print(integer_division)

#Also, should one mix an integer and a float with each other, one obtains a float.

integer_and_float = 1 + 2.0
print(integer_and_float)

#One will encounter large numbers a lot, especially when doing a project on the simulation of the solar system!  
#In order to more easily read the number, one can place underscores in appropriate places, for example:

universe_age = 14_000_000_000
print(universe_age) 