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

for meal in menu:
    if 'spam' not in meal:
        print(meal)

print('-' * 40)

meals = [meal for meal in menu if 'spam' not in meal]
print(meals)

print('-' * 40)


# I do not understand
def not_spam(meal_list: list):
    # print(meal_list)
    return 'spam' not in meal_list


spamless_meal = list(filter(not_spam, menu))
print(spamless_meal)
