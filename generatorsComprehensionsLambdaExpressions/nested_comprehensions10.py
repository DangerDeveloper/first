# 16. Nested Comprehensions
# [ (burger, topping) for burger in burgers for topping in toppings]
# (burger, topping) --> expression
# for burger in burgers for topping in toppings --> iteraters
# beef --> cheese
#      --> egg
#      --> beans
#      --> spam
#
# chicken --> cheese
#         --> egg
#         --> beans
#         --> spam
#
# spicy bean --> cheese
#            --> egg
#            --> beans
#            --> spam
burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

list_meals = [(burger, topping) for burger in burgers for topping in toppings]
print(list_meals)

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)