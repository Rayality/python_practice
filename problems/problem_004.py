# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
def get_in(question):
    out = input(question) + ' '
    return out
def max_of_three(value1, value2, value3):
    num1 = int(value1)
    num2 = int(value2)
    num3 = int(value3)
    max = 0
    if num1 >= num2:
        max = num1
    elif num2 > num1:
        max = num2
    if num3 >= max:
        max = num3
    return max

print(max_of_three(get_in('num1 '),get_in('num2 '),get_in('num3 ')))
