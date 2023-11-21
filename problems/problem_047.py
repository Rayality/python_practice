# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digitit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigitit", ".isupper", and ".islower"


def check_password(password):
    pw = str(password)
    if (len(password) > 12) or (len(password) < 6):
        return False

    spec_lst = ["$", "!", "@"]
    sc = False
    for special_char in spec_lst:
        if special_char in pw:
            sc = True
            break

    if not sc:
        return False

    upper_case = False
    lower_case = False
    digit = False
    for place in pw:
        if place.isalnum():
            if place.isupper():
                upper_case = True
            elif place.islower():
                lower_case = True
            elif place.isdigit():
                digit = True
        if (upper_case and lower_case and digit):
            return True
    return False


password = "noupper21!"
word2 = "WHERESLOW!2"
word3 = "NotSpecial1"
word4 = "Srt1!"
word5 = "WayT0Long4Th!5"
correct = "1UP2low!"
print(check_password(password))
print(check_password(word2))
print(check_password(word3))
print(check_password(word4))
print(check_password(word5))
print(check_password(correct))
