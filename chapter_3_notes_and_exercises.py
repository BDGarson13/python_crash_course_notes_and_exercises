
#A list is a collection of elements, not necessarily related to one another in any particular way.
#It is good practise to name your list after a plural noun.  It is indicated by square brackets "[]," for example:

bicycles = ["trek", "cannondale", "redline", "specialised"]
print(bicycles)

#Should we want to access one of the individual elements of the list, we can do the following:

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

#You may encounter a situation in which you want to access the final element of a list but don't know how many elements there are.
#This is easily achieved by inserting [-1] as follows:

print(bicycles[-1].title())

#Likewise, inserting -2 will yield  the second to last term, -3 the third to last, etc..

#One can also access individual members of the list in the following way:

message = f"My first bike was a {bicycles[3].title()}"
print(message)

#EXERCISE 3-1

friends = ["George", "Holly", "Huw", "Reynolds"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#EXERCISE 3-2

message = f"Life would be immendsely dull without you, {friends[0]}."
print(message)

message = f"Life would be immendsely dull without you, {friends[1]}."
print(message)

message = f"Life would be immendsely dull without you, {friends[2]}."
print(message)

message = f"Life would be immendsely dull without you, {friends[3]}."
print(message)

#EXERCISE 3-3

train_travel = ["Steam", "Maglev", "Electric"]

message = f"The {train_travel[0].lower()} train is a popular tourist attraction in these parts."
print(message)

message = f"While I know very little about the engineering of the {train_travel[1].lower()} trains, they sure do look cool."
print(message)

message = f"I don't know this for sure, but I imagine that most trains in this country are categorised as {train_travel[2].lower()} trains."
print(message)

#What if we wanted to change one of the values of the elements in the list?
#This can be done by writing the name of the list followed by the index of the element you want to change.

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]
print(ice_cream)

ice_cream[0] = "Mint Choc Chip"
print(ice_cream)

#This can be achieved with any item in the list, not just the first.

#As well as replacing certain values of a list with alternatives, one can also add new ones.  For example:

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]

ice_cream.append("Bubblegum")
print(ice_cream)

#What the "append()" method enables us to do is add items even to an empty list.

ice_cream = []

ice_cream.append("Vanilla") 
ice_cream.append("Strawberry") 
ice_cream.append("Mint Choc Chip")

print(ice_cream)

#It's also possible to insert items into lists by specifying their position by the index as well as their newly added value.

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]

ice_cream.insert(0, "Coffee")
print(ice_cream)

#It's possible to remove an item from a list using the "del" statement in the following way:

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]

del ice_cream[0]
print(ice_cream)

#It's occasionally desireable to use the value of an item even after its removal from a list.
#An example of this would be to want to know the x and y coordinates of an alien that's just been shot down to know where one should place an explosion.
#The "pop()" method enables you to remove the last item in a list but continue to work with it.  For example:

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]

print(ice_cream)

popped_ice_cream = ice_cream.pop()
print(ice_cream)        #As can be seen in the terminal below, because you used the "pop()" method in the previous line, "Mint Choc Chip" was subsequently removed.
print(popped_ice_cream)

#How is this useful to us?  Suppose that the list of ice creams was arranged in the order in which we last bought the ice cream.
#In order to access the last flavour of ice cream that we consumed, we can call upon the "pop()" method as follows:

ice_cream = ["Vanilla", "Strawberry", "Chocolate"]

message = f"The last flavour of ice cream that I had was {ice_cream.pop().lower()}.  'Twas indeed splendid!"
print(message)

#N.B.: I've just discovered that one can apply a method straight after another method without any change to the written format!
#In order to decide whether you should use the "del" statement or "pop()" method, consider the following:
#If you have no need to use the element in the list, the call upon the "del" statement.  If you do, then opt for the "pop()" method.

#Occasionally, you'll know the value of the element you want to remove from a list, but not it's position.
#When confronted with this situation, one can call upon the "remove()" method.  For example:

books = ["Stormbreaker", "Point Blanc", "Skeleton Key"]
print(books)

books.remove("Stormbreaker")
print(books)

#Let's now remove one of the items from the list books along with a justification for doing so:

books = ["Stormbreaker", "Point Blanc", "Skeleton Key"]
print(books)

unfinished_books = "Skeleton Key"
books.remove(unfinished_books)
print(books)
print(f"\nI never finished {unfinished_books} in the end.")

#EXERCISE 3-4

guests = ["Ayn Rand", "Steve Jobs", "Jeff Bezos"]
print(guests)

message = f"\n\tIt is my pleasure to invite you, {guests[0]}, to my dinner partay.  \n\tA titan of philosophy will always be a requirement for any event that I host."
print(message)

message = f"\n\tIt would be greatly apprecaited if you, {guests[1]} would be able to \n\tresurrect yourself in time for my gathering of highly admireable people."
print(message)

message = f"\n\tAs a man who revels in the knowledge that man continues to make his \n\tascent from the swamp to stars, I implore you, {guests[2]} to make an entry at my event."
print(message)

#EXERCISE 3-5

guests = ["Ayn Rand", "Steve Jobs", "Jeff Bezos"]
print(guests)

print(guests[1])

new_list = guests.remove("Steve Jobs")
print(guests)

final_list = guests.insert(1, "Bill Gates")
print(guests)

message = f"\n\tIt is my pleasure to invite you, {guests[0]}, to my dinner partay.  \n\tA titan of philosophy will always be a requirement for any event that I host."
print(message)

message = f"\n\tIt would be greatly apprecaited if you, {guests[1]}, would be able to \n\tspare some of your time dedicated to altruistic practices in order to make \n\tmy gathering of highly admireable people."
print(message)

message = f"\n\tAs a man who revels in the knowledge that man continues to make his \n\tascent from the swamp to stars, I implore you, {guests[2]} to make an entry at my event."
print(message)

#EXERCISE 3-6

message = "\n\tI am pleased to let you know that I have in fact found a larger table that \n\tcan accommodate an additional three people."
print(message)

editted_list_1 = guests.insert(0, "Yaron Brook")
print(guests)

editted_list_2 = guests.insert(2, "Tamara de Lempicka")
print(guests)

editted_list_3 = guests.append("Leonardo da Vinci")
print(guests)

message = f"\n\tIt is a privilige for me to invite you, {guests[0]}, to my gathering \n\tin which you'll have the opportunity to meet your all-time hero, {guests[1]}."
print(message)

message = f"\n\tIt is my pleasure to invite you, {guests[1]}, to my dinner partay.  \n\tA titan of philosophy will always be a requirement for any event that I host."
print(message)

message = f"\n\tParis may be a fine place, but it shan't compare to the Garson Annual \n\tDinner Partay, to which you are invited, {guests[2]}."
print(message)

message = f"\n\tIt would be greatly apprecaited if you, {guests[3]}, would be able to \n\tspare some of your time dedicated to altruistic practices in order to make \n\tmy gathering of highly admireable people."
print(message)

message = f"\n\tAs a man who revels in the knowledge that man continues to make his \n\tascent from the swamp to stars, I implore you, {guests[4]} to make an entry at my event."
print(message)

message = f"\n\tNo one individual personifies the Renaissance period better than \n\tyourself, {guests[5]}.  It would be my honour to host you in my home of boundless wealth."
print(message)

#EXERCISE 3-7

message = "\n\tI am pleased to let you know that I have in fact found a larger table that \n\tcan accommodate an additional three people."
print(message)

editted_list_1 = guests.insert(0, "Yaron Brook")
print(guests)

editted_list_2 = guests.insert(2, "Tamara de Lempicka")
print(guests)

editted_list_3 = guests.append("Leonardo da Vinci")
print(guests)

message = f"\n\tIt is a privilige for me to invite you, {guests[0]}, to my gathering \n\tin which you'll have the opportunity to meet your all-time hero, {guests[1]}."
print(message)

message = f"\n\tIt is my pleasure to invite you, {guests[1]}, to my dinner partay.  \n\tA titan of philosophy will always be a requirement for any event that I host."
print(message)

message = f"\n\tParis may be a fine place, but it shan't compare to the Garson Annual \n\tDinner Partay, to which you are invited, {guests[2]}."
print(message)

message = f"\n\tIt would be greatly apprecaited if you, {guests[3]}, would be able to \n\tspare some of your time dedicated to altruistic practices in order to make \n\tmy gathering of highly admireable people."
print(message)

message = f"\n\tAs a man who revels in the knowledge that man continues to make his \n\tascent from the swamp to stars, I implore you, {guests[4]} to make an entry at my event."
print(message)

message = f"\n\tNo one individual personifies the Renaissance period better than \n\tyourself, {guests[5]}.  It would be my honour to host you in my home of boundless wealth."
print(message)

message = "\n\tIt is with great regret that I must inform you all that only two people can join me for dinner."
print(message)

updated_guests_lists_1 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_1.title()}.")

updated_guests_lists_2 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_2.title()}.")

updated_guests_lists_3 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_3.title()}.")

updated_guests_lists_4 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_4.title()}.")

updated_guests_lists_5 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_5.title()}.")

updated_guests_lists_6 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_6.title()}.")

updated_guests_lists_7 = guests.pop()
print(f"\n\tMy deepest apologies for being the bearer of rotten news, but I'm afraid your seat at the party is no longer available, {updated_guests_lists_7.title()}.")

message = f"\n\tI am happy to inform you that you are one of the fortunate few to still be able to make it to my dinner partay, {guests[0]}!"
print(message)

message = f"\n\tI am happy to inform you that you are one of the fortunate few to still be able to make it to my dinner partay, {guests[1]}!"
print(message)

del guests[0]
print(guests)

del guests[0]
print(guests)


#While we've already covered how to edit lists, we also need to know how to organise a list.  
# This will be required by us in order to be able to re-arrange obtained data into a more desireable order with which we can work.  The most obvious of which is to arrange them alphabetically.

cars = ["vw", "vauxhall", "toyota", "izuzu"]
print(cars)

cars.sort()
print(cars)

#N.B.: The "sort()" method acts on the list permenantly, i.e. it cannot be reversed.

#One can also arrange the list such that its entries are arranged in reverse alphabetical order by writing the following.

cars = ["vw", "vauxhall", "toyota", "izuzu"]
cars.sort(reverse=True)
print(cars)

#We will also be required to sort lists in a particular order only for us to then show the original as well.  This can be achieved by applying the "sorted()" function as follows:

cars = ["vw", "vauxhall", "toyota", "izuzu"]

print("\n\tHere is the original list:")
print(cars)

print("\n\tHere is the sorted list:")
print(sorted(cars))

print("\n\tHowever, we can still retrieve our original list just as easily:")
print(cars)

#Should we wish to return a list whose order is in reverse to the original, we employ the "reverse()" method as follows:

cars = ["vw", "vauxhall", "toyota", "izuzu"]
print(cars)

cars.reverse()
print(cars)

#For whatever reason, we may well also want to find the length of the list, the number of entries, by applying the "len()" function.

cars = ["vw", "vauxhall", "toyota", "izuzu"]
print(len(cars))


#Exercise 3-8

places = ["California", "Texas", "New Zealand", "Australia", "Canada"]
print(places)

print(sorted(places))
print(places)

print(sorted(places, reverse=True)) #As can be seen, should one want to print the list in reverse alphabetical order but keep the original list, the "reverse=True" must be included within the second parentheses.
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#Exercise 3-9

guests = ["Ayn Rand", "Steve Jobs", "Jeff Bezos"]

message = f"After a great deal of deliberation, I can confirm that only {len(guests)} will be making it to my fancy dinner partay."
print(message)

#I've opted not to bother with the last exercise as it will take more time than it's worth to complete!