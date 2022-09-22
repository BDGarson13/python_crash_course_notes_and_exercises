def make_sandwiches(*fillings):
    """Print a list of sandwiches as well as their fillings."""
    print("\nThe sandwich fillings requested are:")
    for filling in fillings:
        print(f" - {filling.title()}")