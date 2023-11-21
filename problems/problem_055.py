# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"

# def simple_roman(val):
#     numerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
#     return numerals[val-1]

# one = (1,'I')
# five = (5,'V')
# ten = (10,'X')
# fifty = (50,'L')
# one_hundred = (100,'C')
# five_hundred = (500,'D')
# one_thousand = (1000,'M')

# def more_or_less_simple_roman(remaining):
#     numerals = {'M','D','C','L','X','V','I'}
#     ind = 0
#     ones_fives = 1
#     while remaining:
#         if ones_fives:
#             if remaining >= (char_value - char_value*.1):


def less_simple_roman(remaining):
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    value_string = ""
    characters = ["M", "D", "C", "L", "X", "V", "I"]
    char_index = 0
    for roman_char, char_value in numerals.items():
        if remaining > 4:
            char_index += 1
            next_char = characters[char_index]
            next_val = numerals[next_char]
            # catch numbers that need to be written with the larger numeral
            if remaining >= (char_value - char_value * 0.1):
                while remaining >= char_value:
                    remaining -= char_value
                    value_string += roman_char

                if char_value / next_val == 2 and remaining >= (
                    char_value - char_value * 0.1
                ):  # <--runs with M, C, and X if remainder >= 900, 90, 9
                    remaining -= char_value - char_value * 0.1
                    value_string += characters[char_index + 1]
                    value_string += roman_char
                    continue

                elif remaining >= char_value - next_val:
                    remaining -= char_value - next_val
                    value_string += next_char + roman_char
        else:
            if remaining == 4:
                remaining = 0
                value_string += "IV"
                return value_string

            while remaining > 0:
                remaining -= 1
                value_string += "I"

    return value_string


print(less_simple_roman(19))

for i in range(3999):
    print(i, ":", less_simple_roman(i), "__|__", end='')
    if i % 2:
        print()
