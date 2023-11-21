# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(word):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "bcdefghijklmnopqrstuvwxyza"
    low_table = str.maketrans(a, b)
    up_table = str.maketrans(a.upper(), b.upper())
    return word.translate(low_table).translate(up_table)


inputs = "import"
#       result:  "jnqpsu"
inputs1 = "ABBA"
#       result:  "BCCB"
inputs2 = "Kala"
#       result:  "Lbmb"
inputs3 = "zap"
#       result:  "abq"
print(shift_letters(inputs))
print(shift_letters(inputs1))
print(shift_letters(inputs2))
print(shift_letters(inputs3))
