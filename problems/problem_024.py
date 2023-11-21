# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None

lst = [2, 4, 6, 8, 10]


def calculate_average(values):
    if len(values) == 0:
        return None
    return sum(values)/len(values)


print(calculate_average(lst))
