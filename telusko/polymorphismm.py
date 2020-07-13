# Polymorphism
# -- Duck Typing
# -- Operator Overloading
# -- Method Overloading # Not Present in Python
# -- Method Overriding

# -- Duck Typing

class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')


class MyEditer:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class Laptop:
    def code(self, ide):
        ide.execute()

ide = MyEditer()

lap = Laptop()
lap.code(ide)


# Method Overloading
# Not a concept of python
# class x:
#     def a(self, s, d):
#         pass
#
#     def a(self, s, d, r):
#         pass

