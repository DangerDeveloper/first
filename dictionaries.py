# fruit = {"orange": "a sweet, orange, citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour, green citrus fruit"}

# del fruit["lemon"]
# del fruit  # delete a dictionary
# fruit.clear()  # clear all the item from the dictionary

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)

# print(fruit)

# # ordered_keys = list(fruit.keys())
# # ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + ' ---- ' + fruit[f])
# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f + ' ---- ' + fruit[f])

# Update behind the seen
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit['tomato'] = 'not nice with ice cream'
# print(fruit_keys)
# -----------

# Join the string best way
# myList = ['a', 'b', 'c', 'd']
# #  not the best way
# # newString = ''
# # for i in myList:
# #     newString += i + ', '
# # print(newString)
# # better way
# newString = ','.join(myList)
# print(newString)
#
# letters = 'abcdefghijklmnopqrstuvwxyz'
# newLetter = ','.join(letters)
# print(newLetter)


# Direction Game
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"W": 2, "S": 1, "Q": 0}]
#
# loc = 1
# while True:
#     availableExits = ', '.join(exits[loc].keys())
#     print(locations[loc])
#     if loc == 0:
#         break
#     direction = input('Available exists are ' + availableExits + ': ').upper()
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print('you Cannot go in that direction')

# Update Game
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {
    'QUIT': 'Q',
    'NORTH': 'N',
    'SOUTH': 'S',
    'EAST': 'E',
    'WEST': 'W'
}

loc = 1
while True:
    availableExits = ', '.join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    direction = input('Available exists are ' + availableExits + ': ').upper()
    print()
    # parse the user input, Using our vocabulary
    if len(direction) > 1:  # more then one letter, so check vocabulary
        # for word in vocabulary:  # does it contain a word we know?
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print('you Cannot go in that direction')
