# Conditional Expressions
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append('A meal was skip')
# print(meals)

# x = 12
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

# meals = [meal if 'spam' not in meal else 'a meal skipped' for meal in menu]
# print(meals)


# for meal in menu:
#     print(meal, 'contains sausage' if 'sausage' in meal else 'contains bacon' if 'bacon' in meal else 'contains egg')
# print()

# items = set()
# for meal in menu:
#     for item in meal:
#         items.add(item)
# print(items)
# print()
#
# for meal in menu:
#     for item in items:
#         if item in meal:
#             print(f'{meal} contains {item}')
#             break

# Fizzbuzz
# for x in range(1, 31):
#     fizzbuzz = "Fuzz buzz" if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
#     print(fizzbuzz)

# challange create with list comprehension
fizzbuzz = ['Fuzz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x) for x in
            range(1, 31)]
print(fizzbuzz)
