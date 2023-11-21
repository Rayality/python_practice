# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]
import math


def halve_the_list(single):
    breakpoint = math.ceil(len(single)/2)
    return single[:breakpoint], single[breakpoint:]


test1 = [1, 2, 3, 4]
test2 = [1, 2, 3]
print(halve_the_list(test1))
print(halve_the_list(test2))
