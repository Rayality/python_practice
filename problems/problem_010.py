# Complete the is_divisible_by_3 function to return the
# word "fizz" if the value in the number parameter is
# divisible by 3. Otherwise, just return the number.
#
# You can use the test number % 3 == 0 to test if a
# number is divisible by 3.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_3(number):
    if number % 3 == 0:
        return "fizz"
    return number
