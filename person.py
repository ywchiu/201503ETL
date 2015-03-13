class Person():
    count = 0 # Static/class variable
    def __init__(self, name, city):
        self.name = name # Variable for the instance
        self.city = city # Variable for the instance
        Person.count += 1
    def number_of_persons(self):
        return Person.count
