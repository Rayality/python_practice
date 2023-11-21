# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x >= 0 and x <= 10:
        print(x, "is in range.")
    else:
        print(x, "is not in range.")
    if y >= 0 and y <= 10:
        print(y, "is in range.")
    else:
        print(y, "is not in range.")
    print("\n")


is_inside_bounds(3, 7)
is_inside_bounds(5, -2)
is_inside_bounds(13, 2)
is_inside_bounds(18, 15)
