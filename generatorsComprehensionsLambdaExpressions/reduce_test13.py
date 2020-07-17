import functools


def calc_values(x, y: int):
    return x + y


number = [2, 3, 5, 6, 8, 16]

reduced_value = functools.reduce(calc_values, number)
print(reduced_value)

print(sum(number))
