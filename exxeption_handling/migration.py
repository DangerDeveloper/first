# import exxeption_handling.ducks as ducks
# import exxeption_handling.ducks
from exxeption_handling import ducks

# from exxeption_handling import ducks as name

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
pursey = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(pursey)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()