class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print('I won the lauttry and bought a learjet')


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if type(duck) is Duck: # Not a good approach to use
        # if isinstance(duck, Duck): # Even this is not good
        # maybe best
        # Don't check the type but check if the method is present or not
        # getattr check if fly is present or not if present its of but not it raise a error
        # so use None to prevent from error
        # callable check that it is a method or not i.e fly can be method or property(variable)
        # This is the pythonic way we do not interested in type of duck argument just interested in
        # weather it will fly or not.
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Can't add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError('kk')  # TODO remove in future
            except AttributeError as e:
                print('One Duck Down')
                problem = e
                # raise
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
