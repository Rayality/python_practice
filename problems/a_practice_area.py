test = "a   a  a a a a a    a a  a  a a  a a a   a a a a a a"
split_space = print("This is split with explicit space parameter: \n", test.split(" "))
print("If there are multiple spaces in a row, it will create an empty index in the list. denoted by ''.\n")
split_empty = print("This is split with no parameter: \n",test.split())
print("The split function with no arguements treats multiple spaces as junk and doesn't add an empty index.\n")
split_quotes = print("This is split with empty quotes parameter: \n",test.split(""))
print("The split with an empty parameter or empty quotes with no space, throws a ValueError.")
