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
    occurance = 0
    out_lst = []
    for char1 in s:
        if char1 == ' ':
            continue
        for check in out_lst:
            if char1 == check:
                occurance += 1
                break
        if occurance < 1:
            out_lst.append(char1)
        occurance = 0
    strung = str(out_lst).replace("'","").replace(",","").replace("[","")
    return strung
def clean_list_to_string(text_lst):
    clean = str(text_lst).replace("'","").replace(",","").replace("[","").replace("]","")
    return clean
dirty = remove_duplicate_letters(s)
clean = clean_list_to_string(dirty)
print(clean)
