# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

def sentiment(message):

    happy = len(message.split(":-)"))

    sad = len (message.split(":-)"))

    # for word in sentilist:
    #     if word.find("-)")>=0:
    #         happy += 1
    #     elif word.find("-(")>=0:
    #         sad += 1
    if (happy == 1) and (sad == 1):
        print(f"happy num:{happy} +  sad num:{sad}")
        return "none"
    elif happy > sad:
        print(f"happy num:{happy} +  sad num:{sad}")
        return "happy"
    elif sad > happy:
        print(f"happy num:{happy} +  sad num:{sad}")
        return "sad"
    elif sad == happy:
        print(f"happy num:{happy} +  sad num:{sad}")
        return "unsure"
    else:
        print(happy + sad)
face = ":-:-:(:-)"
wtf1 =":):(-)-:-:)"
wtf2 = ":-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a:-))):-):-((((:-a"
none = "there are no emoticons"
wtf3 = ":-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-:-(:-((()):-))):-"
zero = ".F.F"
print(sentiment(wtf3))
print(wtf3.split(":-)"))
print(wtf3.split(":-("))
