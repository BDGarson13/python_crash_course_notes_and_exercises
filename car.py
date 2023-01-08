"""A module that contains the class, Car.  This is known as a "module-level docstring," the inclusion of one should
 always be given at the beginning of each module."""


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


# Multiple classes can be stored in the same file, hence, we can include the classes of Battery and ElectricCar in this
# module as well as the standard Car module.


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
