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
    nums = []
    shifted = ''
    for char in word:
        char_num = ord(char)+1
        new_char = chr(char_num)
        if new_char.isalpha():
            pass
        elif new_char == "{":
            new_char = "a"
        elif new_char == "[":
            new_char = "A"
        nums.append(new_char)
    shifted = shifted.join(nums)
    return shifted





# def shift_letters(word):
#     shifted = str(word)
#     numbered = []
#     for i in shifted:
#         num = ord(i)
#         num += 1
#         if num not in numbered:
#             numbered.append(num)
#     numbered = sorted(numbered)
#     numbered = numbered.reverse()
#     for i in numbered:
#         char = (chr(i))
#         shifted = shifted.replace(i,str(char))
#     if char == '{':
#             char = 'a'
#     shifted.replace('[','A')
#     return shifted

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
