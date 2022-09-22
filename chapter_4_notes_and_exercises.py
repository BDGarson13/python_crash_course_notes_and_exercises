#In the previous chapter, we worked with lists.  However, what we find is that if you want to retrieve/do something with all of the individual items on the list, complications can arise.
#For example, if you want print all of the individual entries of a list, you'd have always had to keep up with the changing number of entries.
#We can save ourselves a lot of work by calling upon the "for" loop as can be demonstrated below:

friends = ["George", "Morgan", "Holly", "James"]
for friend in friends:
    print(friend)

#The best way to think about the above "for" loop is by reading it as "for every friend in friends, print the friend's name."

#One of the many other applications of a "for" loop is to write a message to every one of the entries in the following way:

for friend in friends:
    print(f"\n\t My dear {friend.title()}, it is a true privilige to have you in my life.")

#Provided that everything that you include after the "for" loop is indented, every action applies to all entries in the list in the following way:

for friend in friends:
    print(f"\n\t My dear {friend.title()}, it is a true privilige to have you in my life.")
    print(f"\t When can we meet again, {friend.title()}?  It's been far too long!")

#An important thing to notice here is that the "for" loop will loop the first entry through all of the actions prior it moving onto the second entry, same with the third, etc..

#In order to write something after the "for" loop, simply write it after the indentation as follows:

for friend in friends:
    print(f"\n\t My dear {friend.title()}, it is a true privilige to have you in my life.")
    print(f"\t When can we meet again, {friend.title()}?  It's been far too long!")

print("\n\t Thank you for your generous response, it wasn't anything short of what I expected!")


#EXERCISE 4-1

pizzas = ["Meateor", "New Yorker", "Texas BBQ"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"\n\t J'adore {pizza.title()}.")

print("\n I just can't help it, all of that doughy good stuff is just too satiating to pass on!")

#EXERCISE 4-2

animals = ["Tiger", "Lion", "Jaguar"]
for animal in animals:
    print(f"\n\t The {animal.title()} is, quite rightly, a famous hunter in the animal kingdom.")

print("\n\t Any one of these creatures would evoke respect from a man appreciative of hunting efficiency.")


#Should one want to generate a series of numbers, the "range()" function is a great way to generate a series of numbers.

for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

#Suppose you only provided the "range()" function with one argument as opposed to two, the code will automatically start
#the sequence of numbers at 0, for example.

for value in range(6):
    print(value)

#Should we want to make a list of numbers, we can convert the "range()" function into a list of numbers by employing the "list()"
#function as follows.

numbers = list(range(1,6))
print(numbers)

#WATERSHED MOMENT IN MY APPROACH TO CODING:
#I am no longer going to plough through any of the examples while learning to code.  In short, I am required to finish the Theory section by 15/02/2022 or else I pay Fergus a £30 fine.
#It seems apparent to me that in the event of me completing the exercises, I shall become sufficiently competent in their application, albeit not as familiar as I otherwise would have been.
#It's high time that I'd started one of these projects already, I am hopeful that this is the little nudge of which I've been in need for some time!

#EXERCISE 4-3

numbers = []
for value in range(1, 21):
    number = value
    numbers.append(value)

print(numbers)

#EXERCISE 4-4

numbers = list(range(1, 10000001))

for value in range(1, 10000001):
    number = value

print(numbers)

#EXERCISE 4-5

digits = list(range(1, 1000001))

print(min(digits))

print(max(digits))

print(sum(digits))

#EXERCISE 4-6

odd_numbers = list(range(1, 21, 2))

for odd_number in odd_numbers:
    print(odd_number)

#EXERCISE 4-7

multiples_of_threes = list(range(0, 31, 3))

for multiples_of_three in multiples_of_threes:
    print(multiples_of_three)

#EXERCISE 4-8

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#EXERCISE 4-9

cubes = [value**3 for value in range(1, 11)]

print(cubes)

#On second thought, it will be wroth me elaborating on the functions and arguments employed while attempting the exercises as opposed to getting rid of them entirely.

#EXERCISE 4-10

#In addition to producing lists, we can also do what's called "slice" them.  For example, below I am slicing the list of the first ten cubes from the "cube" list provided from the last exercise to obtain the first three entries.

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

print("\n\t The first three items in this list are:")
print(cubes[0:3])

print("\n\t The middle three items of this list are:")
print(cubes[5:8])

print("\n\t The last three items in the list are:")
print(cubes[7:])

#N.B. When you want to slice a list by indicating a starting point and demanding that all remaining entries be included, the starting entry is not included, but is indicative of the last item to not be included.

#EXERCISE 4-11

pizzas = ["Meateor", "New Yorker", "Texas BBQ"]
friends_pizzas = ["Meateor", "New Yorker", "Texas BBQ"]

pizzas.append("All The Meats")
friends_pizzas.append("Ham & Pineapple")

print("\n\t My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n\t My friend's favourite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza)

#I should consult the mark scheme for this one given that the final result is not a list in the context of Python, but a sequence of separate items.

#EXERCISE 4-13

#A tuple, indicated by the employment of parentheses "()", is essentially whose items can't be changed.

simple_foods = ("Chips", "Pizza", "Salad", "Soft Drinks", "Condiments")

for simple_food in simple_foods:
    print(simple_food)

#For example, in the event of me writing " simple_foods[0] = "Fries" " the message received when running the code is "TypeError: 'tuple' object does not support item assignment".

updated_simple_foods = ("Chips", "Curry", "Salad", "Soft Drinks", "Cheesecake")

#At the end of this chapter, Matthes states that one should endeavour to write code in a particular way.
#His advice is to consult what is called the Python Enhancement Proposal 8 (PEP 8).
#From what little I gathered from his account of it, it is used widely as a standard template for writing code.
#One might notice that I've been purposefully writing within the indentation set by Pycharm as I write this passage.
#I shall from now on use the vertical line as a visual cue for when I should start a new line, be it in code or notes.
#From now on, base the layout of your code in a similar way to his own.
#This will stand you in good stead as you will spend most of your time reading your code or others' as opposed to
#writing it.