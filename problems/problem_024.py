# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you
lst=[2,4,6,8,10]

def calculate_average(values):
    if len(values)==0:
        return None
    num_of_values = 0
    total = 0
    for num in values:
        num_of_values += 1
        total += num
    return float(total/num_of_values)

print(calculate_average(lst))
