"""
Pisano Period

In number theory, the nth Pisano period, written π(n), is the period with which
the sequence of Fibonacci numbers taken modulo n repeats.
https://en.wikipedia.org/wiki/Pisano_period
"""

import tortoise_and_hare2 as th


def fib_seq(n):
    """Returns a fibonacci sequence from 1 to n"""
    nums = [0, 1]

    for i in range(2, n - 1):
        nums.append(nums[-1] + nums[-2])

    return nums[1:]  # Omit 0


def pisano(m, seq):
    """
    Given a fibonacci seq and m, return a list where each number in
    seq is mod m.
    """
    return [i % m for i in seq]


pisano_seq = pisano(4, fib_seq(20))
print(fib_seq(20))
print(pisano_seq)
start, length = th.tortoise_and_hare(pisano_seq)
print("Start: {}, Length: {}".format(start, length))
