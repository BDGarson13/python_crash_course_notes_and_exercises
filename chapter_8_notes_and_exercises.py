#The purpose behind our use of functions is in order to condense our written code, much like our reason for denoting
#functions as f(x) in the field of mathematics.
#All functions begin with "def," signifying that you are defining the function.  This is followed by triple quotation
#marks, describing the task of the function.  This is called the "docstring."
#All lines of code following the "def function_name():" are referred to collectively as the "body" of the function.
#The parentheses at the end of a function's name must always be included, even if the function is not dependent on any
#parameters.

#EXERCISE 8-1

def display_message():
    """A function that displays the message given below."""
    print("I am learning about functions - let's hope I finish it by Monday!")

display_message()


#EXERCISE 8-2

#The last exercise had an empty pair of parentheses, however, this time we will have a parameter that we will call
#"title."

def favourite_book(title):
        """A function that prints out a message about my favourite book."""
        print(f"\nMy favourite book of all time is, surprise surprise, {title.title()}.")

favourite_book("the fountainhead")

#Functions need not be restricted to just one parameter, but can be defined by multiple.  Due to every parameter needing
#to be matched to a corresponding argument, it makes most sense for us to write the parameters in the order in which
#they appear in the body of the function.  Values matched up in this way are called "positional arguments."
#In contrast with arguments of the positional type, we have "keyword arguments."  These arguments free you from having
#to worry about the order in which they're written.

#EXERCISE 8-3

def make_shirt(size, text):
    """A function describing the size and text on a shirt."""
    print(f"\nThe shirt is size {size} and features the text {text}.")

make_shirt("large", "Who is John Galt?" )
make_shirt(text = "Who is John Galt?" , size = "large")

#As can be seen from the lines 41 and 42, regardless of the format used to arrange the arguments, the output remains
#the same.

#We can also use default values by equating one of the parameters to a set argument.

#EXERCISE 8-4

def make_shirt(size = "large", text = "I love Python!"):
    """A function that describes the size and text of a shirt, both of which having default values."""
    print(f"\nThe shirt is size {size} and features the text {text}.")
    
make_shirt()
make_shirt(size = "medium")
make_shirt(text = "I love C!")

#EXERCISE 8-5

def describe_city(city, country = "great britain"):
    """A function that provides a city as well as its country of residence."""
    print(f"{city.title()} is a city in {country.title()}.")

describe_city(city = "london")
describe_city(city = "manchester")
describe_city(city = "barcelona", country = "spain")

#We can also use the "return" function in our various functions in the following way.

#EXERCISE 8-6

def city_country(city, country):
    """A function that returns a city, country pair."""
    pair = f"\n{city.title()}, {country.title()}"
    return pair

us_pair = city_country("los angeles", "united states")
uk_pair = city_country("london", "united kingdom")
portugal_pair = city_country("lisbon", "portugal")

#We can also get a function to produce a dictionary, given various parameters by adopting a body of code such as the one
#given below.

#EXERCISE 8-7

def make_album(artist_name, title):
    """A function that returns a dictionary for the above pieces of info."""
    album = {"artist": artist_name.title(), "name": title.title()}
    return album

greatest_rock_album_ever = make_album("pink floyd", "dark side of the moon")
print(greatest_rock_album_ever)

led_zeppelin_4 = make_album("led zeppelin", "led zeppelin 4")
print(led_zeppelin_4)

dire_straits_bangers = make_album("dire straits", "brothers in arms")
print(dire_straits_bangers)

def make_album(artist_name, title, songs=None):
    """A function that returns information about an album."""
    album = {"artist": artist_name.title(), "name": title.title()}
    if songs:
        album["songs"] = songs
    return album

greatest_rock_album_ever = make_album("pink floyd", "dark side of the moon", songs=10)
print(greatest_rock_album_ever)

#I SHALL RETURN TO THIS EXERCISE ONCE I FINALLY LEARN HOW TO USE "while" LOOPS!

#"for" loops can be included in the body of a function's code.

#EXERCISE 8-9

def show_messages(messages):
    """Prints all of the individual messages contained within the list."""
    for message in messages:
        print(message)

messages = ["\nYo yo yo, dude.", "You got any dough that I could lend?", "You had a west one last night."]
show_messages(messages)

#exercise 8-10

def show_messages(messages):
    """Prints all of the individual messages contained within the list."""
    for message in messages:
        print(message)

#One application of functions to lists is to is their ability to move items from one list to another.

def send_messages(messages, sent_messages):
    """Moves all of the messages from one list to another."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["\nYo yo yo, dude.", "You got any dough that I could lend?", "You had a west one last night."]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

#While we moved all of the items of one list to another in the previous example, it is possible for the items to simply
#be copied over instead, i.e. the list need not be modified in order to facilitate the transfer of information.

#EXERCISE 8-11

def send_messages(messages, sent_messages):
    """Moves all of the messages from one list to another."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Yo yo yo, dude.", "You got any dough that I could lend?", "You had a west one last night."]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nThe final lists:")

print(messages)
print(sent_messages)

#A function doesn't have to be written with the number of its arguments already known.  In the event of us wanting to
#write a function with a yet-to-be-confirmed number of arguments in mind, we denote it with an asterisk.

#EXERCISE 8-12

def make_sandwiches(*fillings):
    """Print a list of sandwiches as well as their fillings."""
    print("\nThe sandwich fillings requested are:")
    for filling in fillings:
        print(f" - {filling.title()}")

make_sandwiches("ham", "cheese")
make_sandwiches("mushroom", "halloumi")
make_sandwiches("roasted beef", "horseradish")

#EXERCISE 8-13

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile("Ben", "Garson",
                           location = "Lancaster",
                           field = "physics",
                           age = 23)

print(my_profile)

#EXERCISE 8-14

def car_profile(manufacturer, model, **car_info):
    """Build a dictionary of a car's essential details."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

dream_car_info = car_profile("Aston Martin", "DB5",
                             birth_year = 1963,
                             star_driver = "Sean Connery")
print(dream_car_info)

#EXERCISE 8-15

import printing_models as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)

#EXERCISE 8-16

import sandwiches

make_sandwiches("ham", "cheese")
make_sandwiches("mushroom", "halloumi")
make_sandwiches("roasted beef", "horseradish")

from sandwiches import make_sandwiches

make_sandwiches("ham", "cheese")
make_sandwiches("mushroom", "halloumi")
make_sandwiches("roasted beef", "horseradish")

from sandwiches import make_sandwiches as ms

ms("ham", "cheese")
ms("mushroom", "halloumi")
ms("roasted beef", "horseradish")

import sandwiches as sw

sw.make_sandwiches("ham", "cheese")
sw.make_sandwiches("mushroom", "halloumi")
sw.make_sandwiches("roasted beef", "horseradish")

from sandwiches import*

make_sandwiches("ham", "cheese")
make_sandwiches("mushroom", "halloumi")
make_sandwiches("roasted beef", "horseradish")


