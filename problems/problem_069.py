# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
class Student:
    def __init__(self,name):
        self.scores = []
    def add_score(self,score):
        self.scores.append(score)
    def get_average(self):
        total = 0
        avg = 0
        for entry in self.scores:
            total += entry
        if total == 0:
            return None
        avg = total/len(self.scores)
        return avg



# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
student = Student("Malik")
print(student.get_average())    # Prints None
student.add_score(80)
print(student.get_average())    # Prints 80
student.add_score(90)
student.add_score(82)
print(student.get_average())    # Prints 84
