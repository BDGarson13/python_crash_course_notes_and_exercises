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