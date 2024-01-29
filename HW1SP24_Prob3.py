# HW1SP24_Prob3.py

import random


def generate_normal_distribution(mean, std_dev, size):
    """This function will generate an array of the distributed values by using the mean, std_dev, and size,
    and then it will output a list of distributed data."""

    data = [random.normalvariate(mean, std_dev) for _ in range(size)]
    return data


def calculate_mean_std_dev(data):
    """This function will calculate the mean and std_dev of the data given from the previous function."""

    sample_mean = sum(data) / len(data)
    sample_std_dev = (sum((x - sample_mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5
    return sample_mean, sample_std_dev


def main():
    """In this function, it takes all the data produced in the previous two functions and uses it to output
    an array and calculate the sample mean and std_dev based on the desired inputs."""

    mean = float(input("Enter desired mean"))
    std_dev = float(input("Enter desired std_dev"))
    size = 1000

    # Generate normally distributed data
    data = generate_normal_distribution(mean, std_dev, size)

    # Print the generated array
    print("Generated Data Array:")
    print(data)

    # Calculate sample mean and standard deviation
    sample_mean, sample_std_dev = calculate_mean_std_dev(data)

    print(f"Sample Mean: {sample_mean:.4f}")
    print(f"Sample Standard Deviation: {sample_std_dev:.4f}")


if __name__ == "__main__":
    main()

"I used ChatGPT to assist me in writing this code."
