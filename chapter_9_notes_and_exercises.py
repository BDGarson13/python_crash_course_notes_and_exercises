# A class describes the general behaviour of a whole category of objects.
# The creation of individual objects from a class is called "instantiation."
# Let us begin by writing a very simple class that will be called "Dog."  When it comes to identifying attributes, we
# can say that every dog has a name, age as well the abilities of rolling over and/or sitting down when told.  These
# pieces of information will be present in the Dog class.

class Dog:
    """Modelling of a dog using classes."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over when ordered to do so."""
        print(f"{self.name} rolled over!")

# A function that's part of a class is called a method.  Except for the way they're called, their workings are basically
# equal.  The __init__() method has at least two parameters, these being self, name and age.  The self parameter is
# always included by the very definition of method.  The later two parameters are assigned the value of a variable later
# on.  Let us now instantiate the Dog class by naming our particular object "my_dog."


my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

# The "." term calls the method that follows the dot.  For example, let us look at the calling of the sit() and
# roll_over() methods.

my_dog = Dog("Willie", 6)
my_dog.sit()
my_dog.roll_over()

# It is perfectly feasible to create multiple instances of a class, such as having a second dog that we'll "your_dog."

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.name}.")
your_dog.sit()

# EXERCISE 9-1


class Restaurant:
    """Modelling a restaurant using classes."""

    def __init__(self, name, cuisine_type):
        """Initialising the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Provides a description of the restaurant."""
        print(f"\nThe restaurant is called {self.name} and belongs to the {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a heart-warming message that the restaurant is open."""
        print(f"\n{self.name} is finally open!")


restaurant = Restaurant("hodgsons", "chippy")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# EXERCISE 9-2

restaurant_1 = Restaurant("blue moon", "thai")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("quarterhouse", "british")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("the mad hunter", "exotic")
restaurant_3.describe_restaurant()

# EXERCISE 9-3


class User:
    """Constructing a class for typical users."""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()

    def describe_user(self):
        print(f"\nThe user's name is {self.first_name} {self.last_name}, is {self.age} years old and is {self.sex}.")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name} to the Social Network!")


user_1 = User("john", "smith", 900, "male")
user_1.describe_user()
user_1.greet_user()

user_2 = User("sarah jane", "smith",  65, "female")
user_2.describe_user()
user_2.greet_user()

# Let us write a new class that represents a car.  This class will store relevant information about the kind of car with
# which we're working.  There will also be a method whose application will provide a summary of the car's details.


class Car:
    """A simple attempt to describe a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

# To make things more interesting, let's add an attribute that can change over time.  For the class "Car," let's set
# this as the mileage.
# The mileage can be measured by what will be called the odometer reading.


class Car:
    """A slightly less simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Unless you're Mr Wormwood, one will not be selling any second hand cars with zero mileage.  It is for this reason that
# we'll need to be able to modify a car's attribute.  This can be done directly as follows.


class Car:
    """A slightly less simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# The value that you want to change can also be altered via the use of a method as opposed to a doing it directly.


class Car:
    """A slightly less simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# The "update_odometer()" method can be extended.  By adding a bit of logic, we can ensure that no tries to roll
# back the odometer!


class Car:
    """A slightly less simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
# The above line sets the odometer reading as the mileage in the event of it being less than or equal to the input.
        else:
            print("You can't roll back an odometer!")
# This line states that in the event of it being lower, i.e. after Mr Wormwood has taken the opportunity to fiddle with
# it, the fraudster will be called out!

# Testing for whether the GitHub repository and Pycharm are fully integrated.

# Sadly, I couldn't easily commit this change to the file.  As a result, I'm just going to continue to working through
# this chapter and deal with the issue pertaining to GitHub another time.

# One can also increment an attribute's value by a certain amount rather than set an entirely new value.  For example,
# suppose one buys a used car and puts 100 miles on it between its purchase and registration.  Here is a method by which
# we can add the value to the odometer reading.


class Car:
    """An even less slightly simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# EXERCISE 9-4


class Restaurant:
    """Modelling a restaurant using classes."""

    def __init__(self, name, cuisine_type):
        """Initialising the attributes of a restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Provides a description of the restaurant."""
        print(f"\nThe restaurant is called {self.name} and belongs to the {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a heart-warming message that the restaurant is open."""
        print(f"\n{self.name} is finally open!")

    def read_number_served(self):
        """Provide the number of people that have been served at a particular point in time."""
        print(f"The restaurant has served {self.number_served} in today's business day.")

    def set_number_served(self, served_customers):
        """Set the number served to a given value."""
        self.number_served = served_customers

    def increment_number_served(self, extra_served):
        """Add the number of extra customers served."""
        self.number_served += extra_served


restaurant = Restaurant("the greasy spoon", "minimalist british")
print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 100
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(150)
restaurant.read_number_served()

# EXERCISE 9-5


class User:
    """Constructing a class for typical users."""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.login_attempts = 0

    def describe_user(self):
        """A function that provides the user's first and last names, age and sex."""
        print(f"\nThe user's name is {self.first_name} {self.last_name}, is {self.age} years old and is {self.sex}.")

    def greet_user(self):
        """A welcoming message to the new user!"""
        print(f"Welcome {self.first_name} {self.last_name} to the Social Network!")

    def increment_login_attempts(self):
        """A function that increments the number of logins by 1."""
        self.login_attempts += 1
        print(f"\nThe number of login attempts now stands at {self.login_attempts}.")

    def reset_login_attempts(self):
        """A function that resets the login attempts back down to zero."""
        self.login_attempts = 0
        print(f"\nThe number of login attempts by {self.first_name} {self.last_name} is now {self.login_attempts}.")


user = User("Joe", "Bloggs", 15, "Male")

# Let us now increment the number of times Joe Bloggs has logged into the social network.

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Having successfully incremented his number of login attempts, let us now reduce it to zero.

user.reset_login_attempts()

# When writing a class, one doesn't always have to start from scratch.  If the class you're using is a specialised
# version of another class that you've written, you can use what is called "inheritance."  As implied by the term, when
# one class inherits from another, it takes on the attributes and methods of the first class.  The original and new
# classes are referred to as the parent and child classes, respectively.

# When writing a new class based on one that exists, you'll want to write the __init__() method from the parent class.
# This will initialise any attributes that were defined in the parent __init__() method and make them available in the
# child class.  A great example of this technique can be utilised by treating the class "ElectricCar" as a child class
# of the parent class Car.  As a result, all we'll need to write is code for the attributes and behaviour specific to
# electric cars.

# Let us begin by copying our most recent version of the Car class in the form of


class Car:
    """The most recent simple attempt at describing a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# In order to create a child class, it must reside within the same file as the parent class.  The name of the parent
# class must be included in the parentheses of the definition of a child class.

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        # The "super()" method highlighted below enables you to call a method from the parent class.
        # Fun fact: the use of the word super is derived from the fact that the parent class used to be called super.
        super().__init__(make, model, year)


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())


# Let us now take a look at the process by which we define attributes for the child class.

class ElectricCar(Car):
    """Represent more aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        # This a new attribute that we have defined for the class of ElectricCar.  This will be an attribute of all
        # instances of the ElectricCar class, however, it won't be an attribute of the Car class.

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print(f"This {self.make} {self.model} doesn't need a gas tank!")
        # The motivation behind this method's inclusion is so that if someone tries to call the method for an electric
        # car, they will be returned with the sobering message given above!


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# In the event of us adding more and more detail to a class, we will find that, we'll find that our files are becoming
# lengthy.  In such situations one might recognise that a part of one class can be written as a separate class.
# For example, if we continue to provide additional details to the ElectricCar class, one will soon realise that we're
# adding many that describe a car's battery.  In the event of this happening, we can create a separate class called
# Battery.


class Battery:
    """A simple attempt at modelling the battery of an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialise the attributes of the parent class.
        Then initialise attributes specific to the electric car.
        """
        super().__init__(make, model, year)
        # This addition of the attribute allows us to use the contents created in the Battery class.
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Let's now look to add another method to the battery class, one that we'll call "get_range."


class Battery:
    """A slightly less simple attempt at modelling the battery of an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_distance_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            distance_range = 260
        elif self.battery_size == 100:
            distance_range = 315

        print(f"This car can go about {distance_range} miles on a full charge.")


my_tesla = ElectricCar("tesla", "model s", 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_distance_range()

# EXERCISE 9-6


class IceCreamStand(Restaurant):
    """A child class of its parent, Restaurant."""

    def __init__(self, name, cuisine_type="ice cream"):
        """
        Initialise the attributes from the parent class, Restaurant.
        The attribute of ice cream flavours will also be introduced.
        """
        super().__init__(name, cuisine_type)
        # I must remember that the list should start off as empty...
        self.flavours = []

    def display_flavour(self):
        """A method whose calling will lead to the listing of ice cream flavours."""
        print("\nWe have the following flavours available:")
        for flavour in self.flavours:
            print(f"\t - {flavour.title()}")


mr_whippy = IceCreamStand("mr whippy")
# ...given that it is here, after I've named the instance, that I should include it.
mr_whippy.flavours = ["vanilla", "strawberry", "mint"]

mr_whippy.describe_restaurant()
mr_whippy.display_flavour()

# EXERCISE 9-7


class Admin(User):
    """A child class of the parent class, User."""

    def __init__(self, first_name, last_name, age, sex):
        """
        Initialise the attributes from the Restaurant.
        Initialise the attributes specific to the administrator.
        """
        super().__init__(first_name, last_name, age, sex)
        self.privileges = []

    def show_privileges(self):
        """A method whose calling will list the privileges."""
        print(f"\nThe privileges held by {self.first_name} {self.last_name} are:")
        for privilege in self.privileges:
            print(f"\t - {privilege}")


admin_1 = Admin("karen", "thompson", 45, "female",)
admin_1.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
    ]

admin_1.describe_user()
admin_1.show_privileges()

# EXERCISE 9-8


class Admin(User):
    """A child class of the parent class, User."""

    def __init__(self, first_name, last_name, age, sex):
        """
        Initialise the attributes from the Restaurant.
        Initialise the attributes specific to the administrator.
        """
        super().__init__(first_name, last_name, age, sex)
        # The presence of the line below tells Python to create a new instance of Privileges and to assign the instance
        # to the self.privileges attribute.
        self.privileges = Privileges()


class Privileges:
    """A separate class devoted to the privileges held by an admin member."""

    def __init__(self, privileges=[]):
        """Initialising the attributes of the class Privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """A method whose calling will list the privileges."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"\t - {privilege}")


admin_2 = Admin("carol", "jones", 50, "female")
admin_2.describe_user()

# Given that we start with an empty list of privileges, we must first add these privileges by writing

admin_2_privileges = [
    "can add post",
    "can delete post",
    "can ban user"
    ]

# From lines 666 to 670, a list of privileges has been made that we will then use to fill the currently empty set of
# privileges for the specified admin member.

admin_2.privileges.privileges = admin_2_privileges

# In plain, simple English, I would translate line 675 as "in the class privileges, the attribute privileges will be set
# to equal the list "admin_2_privileges."

admin_2.privileges.show_privileges()

# EXERCISE 9-9


class Battery:
    """A slightly less simple attempt at modelling the battery of an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_distance_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            distance_range = 260
        elif self.battery_size == 100:
            distance_range = 315

        print(f"\nThis car can go about {distance_range} miles on a full charge.")

    def upgrade_battery(self):
        """Check the battery size and set to 100-kWh if not already."""
        self.battery_size = 100
        print(f"While the battery was of the size 75-kWh, it has now been increased to {self.battery_size}-kWh.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialise the attributes of the parent class.
        Then initialise attributes specific to the electric car.
        """
        super().__init__(make, model, year)
        # This addition of the attribute allows us to use the contents created in the Battery class.
        self.battery = Battery()


my_electric_whip = ElectricCar("tesla", "model s", 2019)

my_electric_whip.battery.get_distance_range()
my_electric_whip.battery.upgrade_battery()

my_electric_whip.battery.get_distance_range()

# As more and more functionality is added to your classes, one's files will become increasingly large.  In order to keep
# at a reasonable length, Python allows one to store classes in modules and import them into your main program.
# Until further notice, the notetaking shall continue in other files.

# EXERCISE 9-10

# Check the file "my_restaurant.py" and the "restaurant.py" class.

# EXERCISE 9-11

# Check "my_admin_1.py" and "social_media_classes.py."

# EXERCISE 9-12

# Check "my_admin_2.py," "user.py" and "

# Let us now actually look at a module that we import from the Python standard library called "random."
# One interesting function we can call upon here is the "randint()" that takes two integer arguments, returning a
# randomly selected integer between (and including) those numbers.

from random import randint

random_integer = randint(1, 6)
print(f"\n{random_integer}")

# Another useful function is "choice()," taking in a list or tuple and returns a randomly chosen element.

from random import choice

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(f"\n{first_up.title()}")

# EXERCISE 9-13


class Die:
    """An attempt at modelling a die."""

    def __init__(self, sides=6):
        """Initialising attributes of a die."""
        self.sides = sides

    def roll_die(self):
        """A method yielding a randomly generated value of the die."""
        return randint(1, self.sides)


d6 = Die()

# We can now make a list of the ten rolls of the die by first creating an empty list that we will name "results."

results = []
for roll_num in range(10):
    result = d6.roll_die()
    # We are appending the empty list to be filled with 10 results that we've called for in the previous line.
    results.append(result)

print("\n10 rolls of a six sided die:")
print(results)

d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print("\n10 rolls of a ten sided die:")
print(results)

d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print("\n10 rolls of a twenty sided die:")
print(results)

# EXERCISE 9-14

lottery_characters = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e")
lottery_character_1 = choice(lottery_characters)
lottery_character_2 = choice(lottery_characters)
lottery_character_3 = choice(lottery_characters)
lottery_character_4 = choice(lottery_characters)

print(f"\nCongratulations to the holder of ticket "
      f"{lottery_character_1}{lottery_character_2}{lottery_character_3}{lottery_character_4}, you are the winner!")

# EXERCISE 9-15

my_ticket = "c"272

