from oop.game.enemy import Enemy, Troll

random_monster = Enemy('Basic Enemy', 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll()
print('ugly_troll: {}'.format(ugly_troll))

another_troll = Troll('another Troll', 10, 1)
print('Another Troll: {}'.format(another_troll))

brother = Troll('Urg', 23)
print(brother)

print(another_troll)

# from oop.game.player import Player
#
# ajay = Player('Ajay')
#
# print(ajay.name)
# print(ajay.lives)
#
# ajay.lives -= 1
# print(ajay)
#
# ajay.lives -= 1
# print(ajay)
#
# ajay.lives -= 1
# print(ajay)
#
# ajay.lives -= 1
# print(ajay)
#
#
# ajay.level = 2
# print(ajay)
#
# ajay.level = 4
# print(ajay)
#
# ajay.level = 3
# print(ajay)
