# Write a function that meets these requirements.
#
# Name:       check_input
# Parameters: one parameter that can hold any value
# Returns:    if the value of the parameter is the
#             string "raise", then it should raise
#             a ValueError. otherwise, it should
#             just return the value of the parameter
#
# Examples
#    * input:   3
#      returns: 3
#    * input:   "this is a string"
#      returns: "this is a string"
#    * input:   "raise"
#      RAISES:  ValueError
def check_input(param):
    if param == "raise":
        return ValueError
