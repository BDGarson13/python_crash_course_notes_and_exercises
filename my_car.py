from car import Car
# The "import" statement tells Python to open the "car" module and import the class "Car."

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# It's worth looking at the advantage of using modules to import classes as opposed to writing out all the classes in
# the same file.  We retain the functionality, however, we end up with a much slicker looking file.


