def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ Calculate n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(1000))
except RecursionError:
    print('This program cannot calculate factorial that larger ')

print('Program Completed')
