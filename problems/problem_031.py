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
def clean_list_to_string(text_lst):
    clean = str(text_lst).replace("'","").replace(",","").replace("[","").replace("]","").replace(" ","")
    return clean
def sum_of_squares(values):
    lst = []
    total = 0
    for value in values:
        lst.append(value)
        lst.append('*')
        lst.append(value)
        lst.append('+')
        total += (value**2)
    lst.append('=')
    lst.append(total)
    out = clean_list_to_string(lst)
    print(out)
nums = [2,5,7,-1,-10]
sum_of_squares(nums)
