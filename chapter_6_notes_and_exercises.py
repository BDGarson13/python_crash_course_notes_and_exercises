#EXERCISE 6-1

#A dictionary can be used to store various items of information about someone or something in such a way that it's easy
#for it to be retrieved.  This is achieved by formatting every item as having a key and an associated value.  For
#example, below we have a dictionary containing the information of Rizzle Jizzle's actual name, age and city of
#residence.

rizzle_jizzle = {"first_name": "Raphael", "last_name": "Jones", "age": "22", "city": "London"}

print(rizzle_jizzle["first_name"])
print(rizzle_jizzle["last_name"])
print(rizzle_jizzle["age"])
print(rizzle_jizzle["city"])


#EXERCISE 6-2

#As well as storing multiple pieces of information about one particular person, we can utilise dictionaries to store
#information about multiple people but pertaining to one association with that person.  For example, let us suppose we
#want to write a dictionary including people's favourite numbers.  This can be written as follows.

favourite_numbers = {
    "Toby": 16,
    "James": 23,
    "Charlie": 18,
    "Joe": 35,
    "Holly": 21
}

print(f"\nCongratulations, Toby!  Today's your lucky day, the prize winner has number {favourite_numbers['Toby']}!")
print(f"Congratulations, James!  Today's your lucky day, the prize winner has number {favourite_numbers['James']}!")
print(f"Congratulations, Charlie!  Today's your lucky day, the prize winner has number {favourite_numbers['Charlie']}!")
print(f"Congratulations, Joe!  Today's your lucky day, the prize winner has number {favourite_numbers['Joe']}!")
print(f"Congratulations, Holly!  Today's your lucky day, the prize winner has number {favourite_numbers['Holly']}!")


#EXERCISE 6-3

#Let us now write an actual dictionary in the form a coding dictionary but, to avoid confusion, we can call it a
#glossary.

glossary = {
    "string": "an immuatble sequence data type.",
    "list": "a mutable, or changeable, ordered sequence of elements.",
    "for loop": "a conditional iterative statement used to check for certain conditions which, if true, runs code.",
    "tuple": "a list whose items can't be changed in any way whatsoever.",
    "dictionary": "an unordered and mutable Python container that stores mappings of unique keys to values.",
}

print("\nstring:")
print(f"\t {glossary['string']}")
print("\nlist:")
print(f"\t {glossary['list']}")
print("\nfor loop:")
print(f"\t {glossary['for loop']}")
print("\ntuple:")
print(f"\t {glossary['tuple']}")
print("\ndictionary:")
print(f"\t {glossary['dictionary']}")


#EXERCISE 6-4

#Fortunately, "for loops" can also be employed for dealing with dictionaries.  For example, we could greatly simplify
#the process by which we can obtain the same outputs as the last exercise's.

glossary = {
    "string": "an immuatble sequence data type.",
    "list": "a mutable, or changeable, ordered sequence of elements.",
    "for loop": "a conditional iterative statement used to check for certain conditions which, if true, runs code.",
    "tuple": "a list whose items can't be changed in any way whatsoever.",
    "dictionary": "an unordered and mutable Python container that stores mappings of unique keys to values.",
}

for term, definition in glossary.items():
    print(f"\n{term}")
    print(f"\t{definition}")

#I shan't bother adding five more key: value items as I doubt that I'll gain any extra uility from doing so for this
#particular exercise.


#EXERCISE 6-5

country_river_list = {
    "nile": "egypt",
    "thames": "united kingdom",
    "loire": "france"
}

for river, country in country_river_list.items():
    print(f"The {river} runs through {country.title()}.")
for river in country_river_list:
    print(f"{river.title()}")

#The method by which one loops through the values as opposed to the keys differs only in regard to the function at the
#end of the dictionary's title.  For example

for country in country_river_list.values():
    print(f"{country.title()}")


#EXERCISE 6-6

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

poll_suggestions = ["jen", "edward", "ben", "joe", "scott"]

for name in favourite_languages.keys():
    if name in poll_suggestions:
        print(f"You should really take the poll, {name.title()}.")
    elif name not in poll_suggestions:
        print(f"Thank you for taking the poll, {name.title()}!")


#EXERCISE 6-7

#It's actually possible to store dictionaries within lists.  This can be achieved by starting with an empty list,
#appending it each time we make a new dictionary.

peoples = []

rizzle_jizzle = {
    "first_name": "Raphael",
    "last_name": "Jones",
    "age": "22",
    "city": "London",
    }

peoples.append(rizzle_jizzle)

luke = {
    "first_name": "Luke",
    "last_name": "Whitehead",
    "age": "23",
    "city": "Chester",
    }

peoples.append(luke)

holly = {
    "first_name": "Holly",
    "last_name": "Thompson",
    "age": "22",
    "city": "Stockport",
    }

peoples.append(holly)

#Now that we've created our list, we can loop through it on order to display all of the desired information.

for people in peoples:
    name = f"{people['first_name'].title()} {people['last_name'].title()}"
    age = people["age"]
    city = people["city"].title()

    print(f"\n{name}, lives in {city} and is {age} years old.")

#It is worth noting that the solution for this exercise was obtained on Eric Matthes' Github page.
#However, the next exercise asks for pretty much the same thing, so we'll see just how well I've understood it now!


#EXERCISE 6-8

pets = []

gnasher = {
    "species": "dog",
    "owner_name": "jane",
}

pets.append(gnasher)

toffee = {
    "species": "cat",
    "owner_name": "holly",
}

pets.append(toffee)

bob = {
    "species": "goldfish",
    "owner_name": "luke",
}

pets.append(bob)

for pet in pets:
    owner = f"{pet['owner_name'].title()}"
    species = f"{pet['species']}"

    print(f"\n{owner} owns a {species}.")


#EXERCISE 6-9

favourite_places = {
    "holly" : {
        "first": "vietnam",
        "second": "japan",
        "third": "barcelona",
        },

    "scott" : {
        "first": "scotland",
        "second": "germany",
        "third": "canada",
        },

    "luke" : {
        "first": "oxford",
        "second": "lake district",
        "third": "germany",
        },

}

for person, places in favourite_places.items():
    print(f"\n{person}'s favourite places to visit are:")
    print(f"{places}")

#Having looked at the solutions for 6-9, I should have included the sub-dictionaries in the form of lists instead.
#Hence, that is the approach that I will be trying from now on.

#EXERCISE 6-10

favourite_numbers = {
    "Toby" : [16, 32],
    "James" : [23, 46],
    "Charlie" : [18, 36],
    "Joe" : [35, 70],
    "Holly" : [21, 42],
}

for person, numbers in favourite_numbers.items():
    print(f"\n{person}'s favourite numbers are given by:")
    for number in numbers:
        print(f"{number}")


#EXERCISE 6-11

cities = {
    "london": {
        "country": "united kingdom",
        "population": "9 million (to 1 sig. fig.)",
        "fun fact": "Was originally called Londinum."
        },
    "barcelona": {
        "country": "spain",
        "population": "1.62 million (to 3 sig. fig.)",
        "fun fact": "Lionel Messi is the closest thing to God in the eyes of its residents.",
        },
    "paris": {
        "country": "france",
        "population": "2.2 million (to 2 sig. fig.)",
        "fun fact": "The area covered by London is considerably larger than that by Paris.",
        },
}

for city, facts in cities.items():
    country = facts["country"].title()
    population  = facts["population"]
    fun_fact = facts["fun fact"]

    print(f"\nThe city of {city.title()} has the following little factoids:")
    print(f"Its country of residence is {country}.")
    print(f"Its population is {population}.")
    print(f"{fun_fact}")


#EXERCISE 6-12

#For this particular exercise, I shall be reviewing my solution to 6-9 as its output is not the desired answer according
#Mattes' solution.

favourite_places = {
    "holly": {
        "first": "vietnam",
        "second": "japan",
        "third": "barcelona",
        },
    "scott": {
        "first": "scotland",
        "second": "germany",
        "third": "canada",
        },
    "luke": {
        "first": "oxford",
        "second": "lake district",
        "third": "germany",
        },
}

for person, places in favourite_places.items():
    first = places["first"].title()
    second = places["second"].title()
    third = places["third"].title()

    print(f"\n{person.title()}'s favourite places are:")
    print(f"{first}")
    print(f"{second}")
    print(f"{third}")

