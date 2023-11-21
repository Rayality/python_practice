# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.


def add_csv_lines(csv_lines):
    added = []
    for set in csv_lines:
        added.append(sum([int(i) for i in set.split(",")]))
    return added


lines = ["1,5,7", "2,4,6", "1,2,3,4,5,6,7,8,9,10", "1"]
print(add_csv_lines(lines))
