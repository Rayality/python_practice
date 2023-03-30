# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#
lst = [1,2,3,4,5,6,76,8,8]
def max_in_list(values):
    if len(values)<= 0:
        return None
    maximum = max(values)
    return maximum
print(max_in_list(lst))
