class Kettle(object):
    power_type = 'Thermal'

    # __init__ is a constructor
    # It is called when the class is instantiated
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    # self is use to define it is a class function and called Method
    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 8.03)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.45
print(kenwood.price)

hamilton = Kettle('Hamilton', 4.56)
print('Model {} = {}, {} = {}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print('Model {0.make} = {0.price}, {1.make} = {1.price}'.format(kenwood, hamilton))

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics.
Object: An instance of a class.
Instantiate: create a instance of a class.
Method: A function Defined in a class.
Attribute: A variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Do the same output as above logic but in this we have to provide a self
Kettle.switch_on(kenwood)
print(kenwood.on)

# In the python variable is defined when it comes first contact power is created in this
# and only associated with kenwood object.
kenwood.power = 1.5
print(kenwood.power)
# power variable is not defined in the hamilton object so it cause a error
# print(hamilton.power)

"""
In this a [power_type] attribute is in [Kettle] class and reflected into the
[kenwood] and [hamilton] object. [power_type] is not a attribute of [kenwood] and
[hamilton] object
"""
print(Kettle.power_type)
print(kenwood.power_type)
print(hamilton.power_type)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

# change power_type to nuclear
"""
In this a [power_type] is change to [thermal] to [nuclear] 
in the [kenwood] object. [power_type] is not change in the 
[Kettle] class but create a new attribute in the [kenwood] object
"""
print('*' * 20)
kenwood.power_type = 'nuclear'
print(Kettle.power_type)
print(kenwood.power_type)
print(hamilton.power_type)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
