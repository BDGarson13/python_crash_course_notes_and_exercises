#A class describes the general behaviour of a whole category of objects.
#The creation of individual objects from a class is called "instantiation."
#Let us begin by writing a very simple class that will be called "Dog."  When it comes to identifying attributes, we can
#say that every dog has a name, age as well the abilities of rolling over and/or sitting down when told.  These pieces
#information will be present in the Dog class.

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

#A function that's part of a class is called a method.  Except for the way they're called, their workings are basically
#equal.  The __init__() method has at least two parameters, these being self, name and age.  The self parameter is
#always included by the very definition of method.  The later two parameters are assigned the value of a variable later
#on.  Let us now instantiate the Dog class by naming our particular object "my_dog."

my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

#The "." term calls the method that follows the dot.  For example, let us look at the calling of the sit() and
#roll_over() methods.

my_dog = Dog("Willie", 6)
my_dog.sit()
my_dog.roll_over()

#It is perfectly feasible to create multiple instances of a class, such as having a second dog that we'll "your_dog."

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.name}.")
your_dog.sit()

#EXERCISE 9-1

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

#EXERCISE 9-2

restaurant_1 = Restaurant("blue moon", "thai")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("quarterhouse", "british")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("the mad hunter", "exotic")
restaurant_3.describe_restaurant()

#EXERCISE 9-3

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

#Let us write a new class that represents a car.  This class will store relevant information about the kind of car with
#which we're working.  There will also be a method whose application will provide a summary of the car's details.

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

#To make things more interesting, let's add an attribute that can change over time.  For the class "Car," let's set
#this as the mileage.
#The mileage can be measured by what will be called the odometer reading.

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

#Unless you're Mr Wormwood, one will not be selling any second hand cars with zero mileage.  It is for this reason that
#we'll need to be able to modify a car's attribute.  This can be done directly as follows.

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

#The value that you want to change can also be altered via the use of a method as opposed to a doing it directly.

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

#The "update_odometer()" method can be extended.  By adding a bit of logic, we can ensure that no tries to roll
#back the odometer!

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
#The above line sets the odometer reading as the mileage in the event of it being less than or equal to the input.
        else:
            print("You can't roll back an odometer!")
#This line states that in the event of it being lower, i.e. after Mr Wormwood has taken the opportunity to fiddle with
#it, the fraudster will be called out!
