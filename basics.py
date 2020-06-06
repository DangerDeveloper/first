"""
avaliable_exit = ['north', 'south', 'north east']
choosen_exit = ''

while choosen_exit not in avaliable_exit:
    choosen_exit = input('Please choose a direction: ')
    if choosen_exit == 'quit':
        print('Game Over')
        break
else:
    print('You are safe now.')
"""
# First
# import random
#
# highest = 10
# answer = random.randint(1, highest)
#
# print('Please guess a number between 1 and {}:'.format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print('Please guess Higher')
#     else:  # guess must be greater than number
#         print('Please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print('Well done, you guessed it')
#     else:
#         print('Sorry you have not guessed correctly')
# else:
#     print('You got it first time')

# Second
import random

highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}:'.format(highest))
guess = 0  # Initialize to any number outside of the valid range
index = 0
first_time = True
while guess != answer:
    index += 1
    guess = int(input())
    if guess == answer:
        if first_time:
            print('Well done, you guessed it First Time')
            break
        else:
            print('Well done, you guessed it')
            break
    elif index == 10:
        print('You Try 10 Times')
        break
    elif guess < answer:
        print('Please guess higher')
        first_time = False
    elif guess > answer:
        print('Please guess lower')
        first_time = False
