#  Inheritence


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I do not know what i say')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


p = Pet('tom', 22)
p.show()
p.speak()

c = Cat('Riku', 44, 'green')
c.speak()
c.show()

d = Dog('Tom', 12)
d.speak()
d.show()
