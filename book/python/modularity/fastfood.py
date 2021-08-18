from random import choice

fastfood = ["McDonalds", "KFC", "Burger King", "Wendys",
            "Pizza Hut", "Toby's", "Lawless", "CFC"]

def pick():
    """Return random fast food place."""
    return choice(fastfood)
