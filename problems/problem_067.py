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

class Employee:
    def __init__(self, first_name, last_name):
        self.fn = str(first_name)
        self.ln = str(last_name)

    def get_fullname(self):
        return str(f"{self.fn} {self.ln}")

    def get_email(self):
        return str(f"{self.fn.lower()}.{self.ln.lower()}@company.com")


employee = Employee("Duska", "Ruzicka")
name = employee.get_email()
mail = employee.get_fullname()
print(name)
print(mail)
