# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]

def temperature_differences(highs, lows):
    differences = []
    dif = 0
    for count, i in enumerate(highs):
        dif = i - lows[count]
        differences.append(dif)
    return differences
highs = [80, 81, 75, 80]
lows = [72, 78, 70, 70]
print(temperature_differences(highs, lows))
