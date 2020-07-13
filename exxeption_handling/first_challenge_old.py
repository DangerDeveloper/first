import sys


# def getint(prompt):
#     while True:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print('Invalid number entered, Please Try again')
#         except EOFError:
#             sys.exit(1)

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:  # if not use it will come under the exception which is a broad and we cant close
            # the program. It must be above the exception other wise it will never execute
            sys.exit(1)
        # except Exception:  # To accept major exception not a good idea different exception has
        except:  # To accept all exception not a good idea different exception has
            # handle with different logic
            print('Invalid number entered, Please Try again')


first_number = getint('Please enter first number ')
second_number = getint('Please enter second number ')

try:
    print(f'{first_number} divided by {second_number} is {first_number / second_number}')
except ZeroDivisionError:
    print("You can't divided by zero")
    sys.exit(2)
else:
    print('Only print when try is succesful if exception occers it will not execute')
finally:
    print('No matter what in the last it will execute')
