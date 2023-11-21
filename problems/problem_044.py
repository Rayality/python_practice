# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

def translate(key_list, dictionary):
    vals = []
    for key in key_list:
        vals.append(dictionary.get(key))
    return vals


dictionary = {"name": "Noor", "age": 29}
keys1 = ["name", "age"]
keys2 = ["eye color", "age"]
keys3 = ["age", "age", "age"]
print(translate(keys1, dictionary))
print(translate(keys2, dictionary))
print(translate(keys3, dictionary))
