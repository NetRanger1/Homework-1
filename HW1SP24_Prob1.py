# HW1SP24_Prob1.py

from Die import rollFairDie as rfd, rollUnFairDie


def main():

    """This function pulls 1000 rolls from rfd and calculates the fraction of rolls that yield a 1 through 6.
    It then outputs the probability of rolling each number."""

    rolls = 1000
    counts = [0] * 6

    for _ in range(rolls):
        result = rfd()  # Using the alias rfd
        counts[result - 1] += 1

    print("----After rolling the die 1000 times:----")
    for i in range(6):
        probability = counts[i] / rolls
        print(f"Probability of rolling a {i + 1}:  {probability:.4f}")


def main2():

    """This function does the same thing as main1, but it rolls the die 10,000 times instead."""

    rolls = 10000
    counts = [0] * 6

    for _ in range(rolls):
        result = rfd()  # Using the alias rfd
        counts[result - 1] += 1

    print("----After rolling the die 10,000 times:----")
    for i in range(6):
        probability = counts[i] / rolls
        print(f"Probability of rolling a {i + 1}:  {probability:.4f}")


def main3():

    """This function does the same thing as main2, but it pulls from rollUnFairDie instead."""

    rolls = 10000
    counts = [0] * 6

    for _ in range(rolls):
        result = rollUnFairDie()
        counts[result - 1] += 1

    print("----After rolling the unfair die 10,000 times:----")
    for i in range(6):
        probability = counts[i] / rolls
        print(f"Probability of rolling a {i + 1}:  {probability:.4f}")


if __name__ == "__main__":
    main()
    main2()
    main3()
