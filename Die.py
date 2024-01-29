# Didn't know coding was this hard and this fun
# Die.py

import random


def rollFairDie():

    """This function will randomly roll a die fairly. It rolls a number between 0 and 1, and then divides it by 6.
    The fraction is then converted into what whole number the roll would equate to."""

    x = random.random()
    if x <= 1.0 / 6:
        return 1
    elif x <= 2.0 / 6:
        return 2
    elif x <= 3.0 / 6:
        return 3
    elif x <= 4.0 / 6:
        return 4
    elif x <= 5.0 / 6:
        return 5
    else:
        return 6


def rollUnFairDie():

    """This function is unfair, and is slightly weighted towards outputting a 1. It will act similar to rollFairDie,
    but anything equal to 0.2 or below will equal a 1, and so it will always have a higher chance of rolling a 1."""

    x = random.random()
    if x <= 0.2:
        return 1
    elif x <= 2.0 / 6:
        return 2
    elif x <= 3.0 / 6:
        return 3
    elif x <= 4.0 / 6:
        return 4
    elif x <= 5.0 / 6:
        return 5
    else:
        return 6
