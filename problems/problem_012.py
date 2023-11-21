# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    out = ''
    if number % 3 == 0:
        out += ("fizz")
    if number % 5 == 0:
        out += ("buzz")
    if out == '':
        return number
    else:
        return out


print(fizzbuzz(15))
print(fizzbuzz(12))
print(fizzbuzz(10))
print(fizzbuzz(8))
