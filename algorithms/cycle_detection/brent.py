"""
Brent's Cycle Detection Algorithm

Richard P. Brent described an alternative cycle detection algorithm that, like
the tortoise and hare algorithm, requires only two pointers into the sequence.
However, it is based on a different principle: searching for the smallest power
of two 2i that is larger than both λ and μ.

https://en.wikipedia.org/wiki/Cycle_detection
"""


def brent(f, x0):
    """
    Given a periodic function and the starting number, return the starting
    index and length of the cycle using Brent's cycle detection algorithm.
    """
    power = 1
    lam = 1  # lam is the length of a cycle.
    tortoise = x0
    hare = f(x0)

    while tortoise != hare:
        if lam == power:
            tortoise = hare  # Moves the tortoise to the hare's position.
            power *= 2  # Start a new power of 2.
            lam = 0  # Reset length of cycle.
        hare = f(hare)  # Moves hare forward by 1.
        lam += 1  # Increases length of cycle by 1.

    mu = 0  # Start of the cycle.
    tortoise = x0
    hare = x0
    for i in range(lam):
        hare = f(hare)  # Move hare up to lam.

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return mu, lam


def pseudorand(num):
    random.seed(seed)
    a = int(random.random() * 100)  # Random number between 1 and 100
    rand_num = (num ** 2 + a) % 20   # Pseudorandom formula.
    return rand_num


if __name__ == "__main__":
    import random

    seed = random.random() * 10  # Generate random constant seed.
    print("Seed: {}".format(seed))

    # Print sequence
    val = 10
    print(val, end=", ")
    for _ in range(20):
        val = pseudorand(val)
        print(val, end=", ")
    print()

    x0 = 10  # Starts with 10
    start, length = brent(pseudorand, x0)
    print("Start of Cycle: {}, Length of Cycle: {}".format(start, length))
