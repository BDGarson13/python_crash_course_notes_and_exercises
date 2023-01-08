# Given that we can import as many classes as we like into a file, if we want to make a regular and electric in the same
# file then we must import both classes.

from car import Car, ElectricCar
# Multiple classes can be imported from a module on the same line of code, all that's required is a comma for their
# separation.

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())

# One can also import an entire module and access the classes within using dot notation.

import car

my_beetle = car.Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())

# The standard syntax used here is of the form "module_name.ClassName."

# In the event of us having two different classes in two different folders, we call for the same commands as follows.

from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())

# One can also use aliases when importing classes.  For example, one can re-express the Electric Car class as

from electric_car import ElectricCar as EC

my_tesla = EC("tesla", "model s", 2019)
