# Write a class that meets these requirements.
#
# Name:       Employee
#
# Required state:
#    * first name, a string
#    * last name, a string
#
# Behavior:
#    * get_fullname: should return "«first name» «last name»"
#    * get_email:    should return "«first name».«last name»@company.com"
#                    all in lowercase letters
#
# Example:
#    employee = Employee("Duska", "Ruzicka")
#
#    print(employee.get_fullname())  # prints "Duska Ruzicka"
#    print(employee.get_email())     # prints "duska.ruzicka@company.com"
#
# You may want to look at the ".lower()" method for strings to
# help with this code.
#
# There is pseudocode availabe for you to guide you


# class Employee
    # method initializer method with required state
    # parameters first name and last name
        # set self.first_name = first_name
        # set self.last_name = last_name

    # method get_fullname(self)
        # returns self.first_name + " " + self.last_name

    # method get_email(self)
        # returns self.first_name.lower() + "." + self.last_name.lower()
        #         + "@company.com"
class Employee:
    def __init__(self, first_name, last_name):
        self.fn = str(first_name)
        self.ln = str(last_name)
    def get_fullname(self):
        full = str(f"{self.fn} {self.ln}")
        return full
    def get_email(self):
        email = str(f"{self.fn.lower()}.{self.ln.lower()}@company.com")
        return email
employee = Employee("Duska", "Ruzicka")
name = employee.get_email()
mail = employee.get_fullname()
print(name)
print(mail)
