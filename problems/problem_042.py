# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    doodah = zip(list1,list2)
    added=[]
    for tup in doodah:
        total = 0
        for num in tup:
            total += num
        added.append(total)
    return added



list1 = [100, 200, 300]
list2 = [ 10,   1, 180]
print(pairwise_add(list1,list2))
