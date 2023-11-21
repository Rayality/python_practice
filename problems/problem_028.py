# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.
s = "this is a test"


def remove_duplicate_letters(s):
    no_duplicates = list(set(s))
    no_duplicates.sort()
    out = ""
    for char in no_duplicates:
        if char.isalpha():
            out += char
    return out


print(remove_duplicate_letters(s))
