import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number == 0:
                raise ZeroDivisionError('you cant use zero')
            return number
        except ValueError:
            print('Invalid number entered, Please Try again')
        except ZeroDivisionError as err:
            print(err)
            sys.exit(2)
        except EOFError:
            sys.exit(1)
        finally:
            print('No Matter what it execute')


first_number = getint('Please enter first number ')
second_number = getint('Please enter second number ')

# try:
print(f'{first_number} divided by {second_number} is {first_number / second_number}')
# except ZeroDivisionError:
#     print("You can't divided by zero")
#     sys.exit(2)
