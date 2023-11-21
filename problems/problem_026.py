import random
# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average
aint1=[99,99,99,99,99,99,99,99,99,99,99]
def ninety_problems():
    problems = []
    for _ in range(100):
        problems.append(random.choice(range(100)))
        print(problems)
    return (problems)


def calculate_grade(values):
    avg = sum(values)/len(values)
    if avg >= 60:
        if avg >= 70:
            if avg >= 80:
                if avg >= 90:
                    return "A"
                return "B"
            return "C"
        return "D"
    return "F"


probs = ninety_problems()
lst = list(probs)
print(probs)
print(calculate_grade(probs))
