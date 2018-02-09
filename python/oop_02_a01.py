# Python OOP Tutorial 2: Class Variables
# https://www.youtube.com/watch?v=BJ-VvGyQxho

class Employee:
    # class variables go here
    # these are accessible using self or the class
    #
    # like this:
    # self.raise_amount
    # Employee.raise_amount
    raise_amount = 1.04
    num_of_emps = 0
    # initialize the class and give the class some data
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@irgendwas.de"

        # everytime the class is instanced, increment the class variable
        # and count the number of total employees
        Employee.num_of_emps += 1

    # define a method for the class Employee
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print (Employee.num_of_emps)

emp_1 = Employee("Anna", "Schulz", 30000)
emp_2 = Employee("Hans", "Meier", 35000)

print (Employee.num_of_emps)
