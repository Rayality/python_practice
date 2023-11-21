# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function

def biggest_gap(number_list1):
    nums = (number_list1)
    big_gap = 0
    end = len(nums)-1
    for index, num in enumerate(nums):
        if index == end:
            break
        result = abs(num - number_list1[index+1])
        big_gap = max(result, big_gap)
    return big_gap


input = [1, 3, 5, 7]
#       result: 2 because they all have the same gap
input1 = [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
input2 = [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
print(biggest_gap(input))
print(biggest_gap(input1))
print(biggest_gap(input2))
