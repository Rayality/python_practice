# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list

class Person:
    def __init__(self,persons_name,hated_foods,loved_foods):
        self.name = persons_name
        self.hated = hated_foods
        self.loved = loved_foods
    def taste(self,food):
        if len(self.loved) >= len(self.hated):
            longest = self.loved
            shortest = self.hated
        else:
            longest = self.hated
            shortest = self.loved
        for count,item in enumerate(longest):
            if food == item:
                return True
            if count < len(shortest):
                for item in shortest:
                    if food == item:
                        return False
        else:
            return None



hated_foods = ["cottage cheese", "sauerkraut"]
loved_foods = ["pizza", "schnitzel"]
person = Person("Malik",hated_foods,loved_foods)

print(person.taste("lasagna"))     # Prints None, not in either list
print(person.taste("sauerkraut"))  # Prints False, in the hated list
print(person.taste("pizza"))       # Prints True, in the loved list
