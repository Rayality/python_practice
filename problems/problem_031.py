# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def sum_of_squares(values):
    out = ""
    total = 0
    for value in values:
        if value >= 0:
            out += f"{value}*{value}+"
        else:
            out += f"({value})*({value})+"
        total += value**2
    out += "="
    out += total
    print(out)


nums = [2, 5, 7, -1, -10]
sum_of_squares(nums)
