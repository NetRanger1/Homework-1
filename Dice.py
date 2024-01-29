# Dice.py

from Die import rollFairDie, rollUnFairDie


def rollDice(N=1):

    """This function pulls from rfd, and N is the number of dice that is going to be rolled."""

    total_score = sum(rollFairDie() for _ in range(N))
    return total_score
