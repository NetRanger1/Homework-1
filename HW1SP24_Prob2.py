# HW1SP24_Prob2.py

from Dice import rollDice


def main():

    """This function pulls the function rollDice, but instead of 1 roll, it rolls the dice 1000 times.
    The number of dice can be adjusted as desired, and then the output of the probability of rolling
    each number is outputted."""

    num_dice = int(input("Enter desired num_dice"))
    rolls = 1000
    min_score = num_dice
    max_score = num_dice * 6

    counts = [0] * (max_score - min_score + 1)

    for _ in range(rolls):
        result = rollDice(N=num_dice)
        counts[result - min_score] += 1

    print(f"----After rolling {num_dice} dice {rolls} times:----")
    for i in range(min_score, max_score + 1):
        probability = counts[i - min_score] / rolls
        print(f"Probability of rolling a {i}:  {probability:.4f}")


if __name__ == "__main__":
    main()
