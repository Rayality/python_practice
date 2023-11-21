# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
shfifty_five = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calculate_sum(values):
    if len(values) == 0:
        return None
    return sum(values)


print(calculate_sum(shfifty_five))
