# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.
aht = [1, 2, 3, 4, 5, 6, 7]
mimsy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def has_quorum(attendees_list, members_list):
    if len(attendees_list) >= len(members_list)/2:
        return True
    return False


print(has_quorum(aht, mimsy))
