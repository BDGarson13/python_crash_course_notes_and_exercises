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
