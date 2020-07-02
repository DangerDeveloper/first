from oop.game.player import Player

ajay = Player('Ajay')

print(ajay.name)
print(ajay.lives)

ajay.lives -= 1
print(ajay)

ajay.lives -= 1
print(ajay)

ajay.lives -= 1
print(ajay)

ajay.lives -= 1
print(ajay)


ajay.level = 2
print(ajay)

ajay.level = 4
print(ajay)

ajay.level = 3
print(ajay)
