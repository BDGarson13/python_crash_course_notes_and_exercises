#EXERCISE 5-1

#In spite of what one may be used to, the "=" sign doesn't actually allow us to ask the question of whether A is in fact
#equal to B.
#Should we want to find out using our code that A is equal to B, we must employ the use of "==" instead.
#Hence, we use the "==" notation to determine whether something has a particular identity as opposed to setting a new
#identity entirely.
#If A does in fact equal B, then we are returned with the statement "True".  If not, then one is returned with "False".

print("The test I am running here is whether the specified book is the 'The Fountainhead.'")
book = "The Fountainhead"
print("Is the book 'The Fountainhead?'  I predict True.")
print(book == "The Fountainhead")
print("Is the book 'Crime and Punishment?'  I predict False.")
print(book == "Crime and Punishment")

print("\nThis test concerns whether the food is a member of Indian or Chinese cuisine.")
food = "Indian"
print("Is the food Indian?  I predict True.")
print(food == "Indian")
print("Is the food Chinese?  I predict False.")

print("\nThis test's goal is to discern whether the director is Christopher Nolan or Sam Raimi.")
director = "Christopher Nolan"
print("Is the director Christopher Nolan?  I predict True.")
print(director == "Christopher Nolan")
print("Is the director Sam Raimi?  I predict False.")
print(director == "Sam Raimi")

print("\nThis test is to discover whether I'm listening to Hans Zimmer or Dany Elfman this very second.")
composer = "Hans Zimmer"
print("Is the composer Hans Zimmer?  I predict True.")
print(composer == "Hans Zimmer")
print("Is the composer Dany Elfman?  I predict False.")
print(composer == "Dany Elfman")

print("\nThis test's motivation is to be able to tell me if my favourite Bond movie is Casino Royale or Skyfall.")
film = "Casino Royale"
print("Is my favourite Bond film Casino Royale?  I predict True.")
print(film == "Casino Royale")
print("Is my favourite Bond film Skyfall?  I predict False.")
print(film == "Skyfall")


#EXERCISE 5-2

#Should we want to determine if A is not equal to B, then we can introduce the notation "!=" in order to ask.

pizza_topping = "Truffle"
if pizza_topping == "Truffle":
    print("\nI've got to get me some more of that!")
if pizza_topping != "Truffle":
    print(pizza_topping != "Truffle" "This is seriously lacking in flavour.")

pizza_seasoning = "Black Pepper"
if pizza_seasoning == "MSG":
    print("I ordered Italian food, why does it taste like Golden Dragon?!")
if pizza_seasoning != "MSG":
    print("This is what I call an Italian resturaunt!")


country = "wales"
if country == "Wales":
    print("We are still Six Nations Champions!")
if country != "Wales":
    print("\nCan you even spell, lad?!")

if country.title() == "Wales":
    print("We are still Six Nations Champions!")
if country.title() != "Wales":
    print("Can you even spell, lad?!")


ratio_1 = 3.14
if ratio_1 == 3.14:
    print("\nThis is approximately the ratio between a circle's circumference and diameter!")
if ratio_1 != 3.14:
    print("This is just some boring-ass ratio.")

ratio_2 = 2.73
if ratio_2 == 2.72:
    print("Make note of this constant, this crops up a fair bit in both mathematics and physics!")
if ratio_2 != 2.72:
    print("This has no significant value to me.")

#It has since come to my attention that this exercise was meant to produce either True or False as the output as opposed
#to printing out a personally written statement.  For the rest of the exercise, I shall follow the instructions as they
#should have been from the start.

height = 183
if height > 182:
    print(height > 182)

height = 181
if height < 182:
    print(height > 182)

mass = 100
if mass >= 100:
    print(mass >= 100)

mass = 99
if mass < 100:
    print(mass >= 100)

soldiers = 1000000
if soldiers <= 1000000:
    print(soldiers <= 1000000)

soldiers = 1000001
if soldiers > 1000000:
    print(soldiers <= 1000000)

#As well as test results being dependent on one condition, they can also be dependent on two conditions.  This is where
#the "and" and "or" statements come in.

age_ben = 23
age_luke = 23
if age_ben > 21 and age_luke > 22:
    print(age_ben > 21 and age_luke > 22)

age_ben = 23
age_luke = 23
if age_ben > 21 and age_luke > 22:
    print(age_ben <= 21 and age_luke <= 22)

george = "Available"
morgan = "Available"
if george == "Available" or morgan == "Available":
    print(george == "Available" or morgan == "Available")

george = "Unavailable"
morgan = "Unavailable"
if george == "Unavailable" or morgan == "Unavailable":
    print(george == "Available" or morgan == "Available")

#One can also check to see if an item exists is in a list or not in the following way.

friends = ["George", "Morgan", "Rizzle Jizzle"]
mate = "Rizzle Jizzle"
if mate in friends:
    print(mate in friends)
mate = "Tom West"
if mate not in friends:
    print(mate in friends)

favourite_directors = ["Denis Villeneuve", "Christopher Nolan"]
director = "Michael Bay"
if director not in favourite_directors:
    print(director not in favourite_directors)
director = "Denis Villeneuve"
if director in favourite_directors:
    print(director not in favourite_directors)


#EXERCISE 5-3

alien_colour = "green"
if alien_colour == "green":
    print("\nCongratulations, soldier!  You just won 5 points!")

alien_colour = "green"
if alien_colour == "green":
    print("Congratulations, soldier!  You just won 5 points!")
if alien_colour != "green":
    print("Mission failed, we'll get 'em next time!")


#EXERCISE 5-4

#There are many situations in which we have two possible courses of action, at which point we can write what is called
#an "if-else" chain.
#For example, suppose that we want to produce a message for the player in the event of the alien that was shot down
#during the game not being of said colour, we can write an alternative message.

alien_colour = "green"
if alien_colour == "green":
    print("\nCongratulations, soldier!  You just won 5 points!")

alien_colour = "blue"
if alien_colour != "green":
    print("Even better, you get 10 points!")

alien_colour = "green"
if alien_colour == "green":
    print("Congratulations, soldier!  You just won 5 points!")
elif alien_colour != "green":
    print("Even better, you get 10 points!")

alien_colour = "blue"
if alien_colour == "green":
    print("Congratulations, soldier!  You just won 5 points!")
elif alien_colour != "green":
    print("Even better, you get 10 points!")


#EXERCISE 5-5

#There will be situations in which there are three possible outcomes, in such cases we can employ the use of an
#"if-elif-else" chain.

alien_colour = "green"
if alien_colour == "green":
    print("\nCongratulations, soldier!  You just won 5 points!")
elif alien_colour == "yellow":
    print("Even better, you get 10 points!")
else:
    print("As if you couldn't do the Motherland anymore proud, you're rewarded 15 points!")

alien_colour = "yellow"
if alien_colour == "green":
    print("\nCongratulations, soldier!  You just won 5 points!")
elif alien_colour == "yellow":
    print("Even better, you get 10 points!")
else:
    print("As if you couldn't do the Motherland anymore proud, you're rewarded 15 points!")

alien_colour = "red"
if alien_colour == "green":
    print("\nCongratulations, soldier!  You just won 5 points!")
elif alien_colour == "yelloe":
    print("Even better, you get 10 points!")
else:
    print("As if you couldn't do the Motherland anymore proud, you're rewarded 15 points!")


#EXERCISE 5-6

age = 1
if age < 2:
    print("\nYou've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")

age = 3
if age < 2:
    print("You've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")

age = 7
if age < 2:
    print("You've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")

age = 15
if age < 2:
    print("You've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")

age = 23
if age < 2:
    print("You've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")

age = 70
if age < 2:
    print("You've got your whole life ahead of you, a lot of potential to actualise given that you're a baby!")
elif age >= 2 and age < 4:
    print("You may be able to walk, but you're still pretty much a baby in every way but name only.")
elif age >= 4 and age < 13:
    print("The term used to describe your stage in life is the namesake of the equivalent of a baby goat.")
elif age >= 13 and age < 20:
    print("Let me guess, your parents are you calling you a moody teenager?  We've all been there!")
elif age >= 20 and age < 65:
    print("You're an adult at long last, this is where your life as a truly independent individual begins!")
else:
    print("With your many years of experience, you may be old but you are wise.")


#EXERCISE 5-7

favourite_fruits = ["banana", "mango", "kiwi", "strawberry", "forest fruits"]
if "banana" in favourite_fruits:
    print(f"\nThere is no better fruit than the {favourite_fruits[0]} to add bulk to a smoothie.")
if "mango" in favourite_fruits:
    print(f"{favourite_fruits[1].title()} lassi is a welcome addition to an Indian meal out.")
if "kiwi" in favourite_fruits:
    print(f"The {favourite_fruits[2]} proves to be an elusive fruit at the supermarket, due to its size, I'm sure.")
if "strawberry" in favourite_fruits:
    print(f"The {favourite_fruits[3]} is a fine addition to one's breakfast during the summer.")
if "forest fruits" in favourite_fruits:
    print(f"Every one should add {favourite_fruits[4]} to one's smoothie in the morning - your world will change!")


#EXERCISE 5-8

#We can also check for various items in a list in order to determine different courses of action.

usernames = ["Admin", "Seb", "Max", "Luke", "Tom"]

for username in usernames:
    if username == "Admin":
        print(f"\nHello, {username}, it's always nice to greet the return of the captain of our metaphorical ship.")
    else:
        print(f"Welcome back, {username}, I hope you're ready for a fresh day at work!")


#EXERCISE 5-9

usernames = ["Admin", "Seb", "Max", "Luke", "Tom"]

for username in usernames:
    if username == "Admin":
        print(f"\nHello, {username}, it's always nice to greet the return of the captain of our metaphorical ship.")
    else:
        print(f"Welcome back, {username}, I hope you're ready for a fresh day at work!")

usernames = []

if usernames == []:
    print("\nLooks like we're in need of some new users!")

#EXERCISE 5-10

#On occasion, we will endeavour to find out if there exists the same item in two or more different lists.  For example,
#if we want to filter out usernames that have already been used, we will be required to execute the following course of
#action.

current_users = ["John", "Jack", "Joseph", "Daniel", "Rhys"]
new_users = ["Rhys", "Llewelyn", "Gwilym", "Daniel", "Jack"]

for new_user in new_users:
    if new_user in current_users:
        print(f"I'm afraid that unoriginal name just isn't going to cut it!  Come up with a new username.")
    else:
        print(f"Welcome aboard, {new_user}, at least someone here has a shred of originiality about them!")


#EXERCISE 5-11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


















