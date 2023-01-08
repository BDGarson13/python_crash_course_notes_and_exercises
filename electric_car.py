"""A set of classes that can be used to represent electric cars."""

from car import Car
# The subsequent classes explicitly written out in full below can only function with the importing of Car as seen above.
# In addition to this, apparently, one also needs to remove the Battery and ElectricCar class.


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
