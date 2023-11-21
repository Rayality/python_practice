# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"

def num_concat(numerical1, numerical2):
    return f"{numerical1}{numerical2}"


param1 = 3
param2 = 10
print(num_concat(param1, param2))
