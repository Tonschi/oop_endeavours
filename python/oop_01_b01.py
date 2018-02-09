# create the class Human
# it is a blueprint for creating instances of the Human class
class Human:
    # initialize the class and give the class some data
    def __init__ (self, first, last, age, lang, country):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + "@irgendwas.de"
        self.lang = lang
        self.country = country

    # define a method for the class human
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def fullprofile(self):
        return "{} {} uses {}, is {} years young and speaks {}.".format(self.first, self.last, self.email, self.age, self.lang)

    def currency(self):
        if self.country == "GER":
            self.currency = "EUR"
        elif self.country == "CZE":
            self.currency = "CZK"
        return self.currency


human_01 = Human("Hans", "Meier", 30, "Czech", "GER")

human_02 = Human("Anna", "Schulz", 26, "German", "CZE")

print (human_02.currency())
