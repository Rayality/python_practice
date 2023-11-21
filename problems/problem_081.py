# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color


class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.legs = number_of_legs
        self.color = primary_color

    def describe(self):
        return f"{self.__class__.__name__} has {self.legs} legs and is primarily {self.color}."
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"


class Dog(Animal):
    def speak():
        speak = "Bark!"
        return speak


# Name:       Cat, inherits from Animal


class Cat(Animal):
    def speak():
        return "Miao"


class Snake(Animal):
    def speak():
        return "Sssssss!"
