from car import ElectricCar
# Much like we saw in the my_car file, the import command opens the car file giving us access to the ElectricCar class.

my_tesla = ElectricCar("tesla", "model s", 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_distance_range()
