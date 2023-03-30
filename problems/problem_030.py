# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    ordered = sorted(values)
    sec_large = ordered.pop(-2)
    return sec_large
lst = [9,1,8,2,7,3,4,14,5,6,7,8,9,0,]
find_second_largest(lst)
