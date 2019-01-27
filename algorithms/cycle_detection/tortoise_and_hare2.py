"""
Floyd's Cycle Finding Algorithm: Tortoise and the Hare

A cycle finding pointer algorithm that uses only two pointers, which move
through a given sequence at different speeds.

Note: This algorithm only PARTIALLY works and is not optimal.

https://en.wikipedia.org/wiki/Cycle_detection
https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
"""

def tortoise_and_hare(seq):
    """
    Given a periodic sequence of numbers, return the starting index and the
    length of the cycle.
    """
    tortoise = 1  # Start with 1 step.
    hare = 2  # Start with 2 steps.
    try:
        while seq[tortoise] != seq[hare]:
            # ISSUE: In a sequence, equal values do not necessarily mean a cycle.
            tortoise += 1  # Tortoise moves one step at a time.
            hare += 2  # Hare moves twice as fast as tortoise.
    except IndexError:
        print("Could not find cycle. Try extending or providing a different list.")
        return -1, -1

    length = hare - tortoise  # The length of a cycle is hare - tortoise.
    start = 0  # Start of the cycle.
    tortoise = 0  # Move tortoise back to start of sequence.
    while seq[tortoise] != seq[hare]:
        tortoise += 1
        hare += 1
        start += 1

    return start, length
