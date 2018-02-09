# Python OOP Tutorial 3: classmethods and staticmethods
# https://www.youtube.com/watch?v=rq8cL2XMM5M

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

    #
    # Regular methods take the instance as the first argument
    #
    # define a method for the class Employee
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #
    # Classmethods take the class as the first argument
    #
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        """Creates a new Employee from a Hyphen separated string
        Example input: 'John-Doe-5000'"""
        # splits a given string at the "-" character
        first, last, pay = emp_string.split("-")
        # returns a new class instance based on the string input
        return cls(first, last, pay)

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        else:
            return False


emp_1 = Employee("Anna", "Schulz", 30000)
emp_2 = Employee("Hans", "Meier", 35000)

import datetime
my_date = datetime.date(2018, 2, 10)

print (Employee.is_weekend(my_date))
