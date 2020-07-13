# Class attribute # Class Method # static Method


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('Ajay')
p2 = Person('Vikram')
print(Person.number_of_people_())


class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print('Run')


print(Math.add5(5))

print(Math.add10(300))

Math.pr()

# Type of Variable
# 1 Instance variable
# 2 Class Variable(static variable)
