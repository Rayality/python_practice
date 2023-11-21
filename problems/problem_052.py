# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html

import random


def generate_lottery_numbers():
    out = []
    while len(out) < 6:
        num = random.randint(1, 40)
        if num not in out:
            out.append(num)
    out.sort()
    return out


print(generate_lottery_numbers())
