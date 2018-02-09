# Python OOP Tutorial 4: Inheritance - Creating Subclasses
# https://www.youtube.com/watch?v=RSl87lqOXDE

class Employee:
    # class variables go here
    # these are accessible using self or the class
    #
    # like this:
    # self.raise_amount
    # Employee.raise_amount
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

class Developer(Employee, object):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

emp_1 = Employee("Anna", "Schulz", 30000)
emp_2 = Employee("Hans", "Meier", 35000)

dev_1 = Developer("John", "Doe", 66666, "C++")
dev_2 = Developer("Tarzan", "Jane", 99966, "Python")

print(dev_1.fullname())
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.pay)
print(str(dev_1.raise_amount) + "\n")

print(dev_2.fullname())
print(dev_2.email)
print(dev_2.prog_lang)
print(dev_2.pay)
print(str(dev_2.raise_amount) + "\n")
