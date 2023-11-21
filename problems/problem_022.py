# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear = []
    if not is_sunny:
        gear.append("umbrella-ella-eh-eh-eh")
    if is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")
    return gear


print(gear_for_day(False, False))
print(gear_for_day(False, True))
print(gear_for_day(True, False))
