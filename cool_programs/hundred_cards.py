"""
Given a machine that draws a 100 unique cards, what is the average number
of draws to get a duplicate?
"""

import math

total = 0
for i in range(1, 101):
    total += (i - 1) / (math.factorial(101 - i) * 100 ** (i - 1)) * i  # Probability
total *= math.factorial(99)

print(total)
