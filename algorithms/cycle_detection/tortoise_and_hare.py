"""
Floyd's Cycle Finding Algorithm: Tortoise and the Hare

A cycle finding pointer algorithm that uses only two pointers, which move
through a given sequence at different speeds. This program only demonstrates
the the tortoise and hare algorithm using a pseudorandom number generator.

https://en.wikipedia.org/wiki/Cycle_detection
https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
"""


def tortoise_and_hare(f, x0):
    """
    Given a periodic function and the starting number, return the starting
    index and length of the cycle using Floyd's tortoise and hare algorithm.
    """
    # Define a seed to get a constant set of values to allow checking.
    val = x0
    numbers = []

    for i in range(50):
        numbers.append(val)
        val = f(val)

    print(numbers)

    # Finding a repetition, where x_i == x_2i
    tortoise = f(x0)  # Tortoise moves 1 step at a time.
    hare = f(f(x0))  # Hare moves 2 steps at a time.

    while tortoise != hare:  # Keep increasing distance until cycle is found.
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Finding the beginning of the cycle.
    mu = 0  # mu is the start of the cycle.
    tortoise = x0

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    # Finding the length of the cycle.
    lam = 1  # lam is the length of the cycle.
    hare = f(tortoise)

    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return mu, lam


def pseudorand(num):
    random.seed(seed)
    a = int(random.random() * 100)  # Random number between 1 and 100
    rand_num = (num ** 2 + a) % 20   # Pseudorandom formula.
    return rand_num


if __name__ == "__main__":
    import random

    seed = random.random() * 10
    print("Seed: {}".format(seed))

    x0 = 10  # Starts with 10
    start, length = tortoise_and_hare(pseudorand, x0)
    print("Start of Cycle: {}, Length of Cycle: {}".format(start, length))
