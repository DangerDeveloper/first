even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
number = even + odd

print(even)
print(odd)
print(number)

numbers_in_order = sorted(number)

print(numbers_in_order)

if numbers_in_order == number:
    print('The list are equal')
else:
    print('They are not')

# sorted(number) is not same as number.sort()
# sorted(number) create a new list in memory and save into new variable
# it returns (print(sorted(number))) a list of sorted list which is a copy of old list and
# do not reference to old allocated space in memory any change in numbers_in_order
# does not impact a number variable because it has a other allocated space in memory

# number.sort() do not create a new list. It modify the old list present in the memory
# print(number.sort()) do not return the value as compare to other language like java
# it print none.

print(list('This is a list'))

# reference Variable
even = [2, 4, 6, 8]
another_list = even  # They are reference variable can not create a new list in memory
# They both variables point the same location in the memory.
# Any change in any one of the variable reflect to all

print(another_list is even)  # check if they are same return true
print(another_list == even)  # check if they have same content return true
another_list.sort(reverse=True)
print(even)

# reference Variable
even = [2, 4, 6, 8]
another_list = list(even)  # Create a new Variable which is a copy of old one
# i.e. -> allocate a new space in memory they both are different

print(another_list is even)  # check if they are same return false
print(another_list == even)  # check if they have same content return true
another_list.sort(reverse=True)
print(even)

# reference Variable
even = [2, 4, 6, 8]
another_list = sorted(even, reverse=True)  # Create a new Variable which is reverse of original
# and is a copy of old one
# i.e. -> allocate a new space in memory they both are different

print(another_list is even)  # check if they are same return false
print(another_list == even)  # check if they have same content return false

# Monty Python example
menu = list()
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'sausage', 'bacon', 'spam'])
menu.append(['spam', 'sausage', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'bacon', 'spam'])

for meal in menu:
    if 'spam' not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
