from user import User


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
