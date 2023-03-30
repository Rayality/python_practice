# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    pw = str(password)
    uc = False
    lc = False
    dig = False
    sc = False
    spec_lst = ['$','!','@']
    if ((len(password)> 12) or (len(password)<6)):
        return False
    for place in pw:
        if place.isalnum and (uc and lc and dig)!= True:
            if place.isupper():
                uc = True
            elif place.islower():
                lc = True
            elif place.isdigit():
                dig = True
        if sc != True:
            for spch in spec_lst:
                if place == spch:
                    sc = True
        # print(uc,lc,dig,sc)
    if (uc and lc and dig and sc)==True:
        return True
    else:
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
