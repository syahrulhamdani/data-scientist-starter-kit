from random import choice

responses = ["Yes!", "No!", "Let me think first", "Sorry, what?"]

def give():
    """Return random response."""
    return choice(responses)
