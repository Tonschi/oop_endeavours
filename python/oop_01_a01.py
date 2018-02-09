# Python OOP Tutorial 1: Classes and Instances
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:

    raise_amount = 1.04

    # initialize the class and give the class some data
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@irgendwas.de"

    # define a method for the class Employee
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Anna", "Schulz", 30000)
emp_2 = Employee("Hans", "Meier", 35000)

print (emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)
