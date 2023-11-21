# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    if 'flour' in ingredients:
        if 'eggs' in ingredients:
            if 'oil' in ingredients:
                return True
    return False


lst = ["flour", "eggs", "oil"]
lst2 = ["french", "toast", "penguin"]
print(can_make_pasta(lst))
print(can_make_pasta(lst2))
