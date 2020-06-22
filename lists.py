# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# number = even + odd
#
# print(even)
# print(odd)
# print(number)
#
# numbers_in_order = sorted(number)
#
# print(numbers_in_order)
#
# if numbers_in_order == number:
#     print('The list are equal')
# else:
#     print('They are not')
#
# # sorted(number) is not same as number.sort()
# # sorted(number) create a new list in memory and save into new variable
# # it returns (print(sorted(number))) a list of sorted list which is a copy of old list and
# # do not reference to old allocated space in memory any change in numbers_in_order
# # does not impact a number variable because it has a other allocated space in memory
#
# # number.sort() do not create a new list. It modify the old list present in the memory
# # print(number.sort()) do not return the value as compare to other language like java
# # it print none.
#
# print(list('This is a list'))
#
# # reference Variable
# even = [2, 4, 6, 8]
# another_list = even  # They are reference variable can not create a new list in memory
# # They both variables point the same location in the memory.
# # Any change in any one of the variable reflect to all
#
# print(another_list is even)  # check if they are same return true
# print(another_list == even)  # check if they have same content return true
# another_list.sort(reverse=True)
# print(even)
#
# # reference Variable
# even = [2, 4, 6, 8]
# another_list = list(even)  # Create a new Variable which is a copy of old one
# # i.e. -> allocate a new space in memory they both are different
#
# print(another_list is even)  # check if they are same return false
# print(another_list == even)  # check if they have same content return true
# another_list.sort(reverse=True)
# print(even)
#
# # reference Variable
# even = [2, 4, 6, 8]
# another_list = sorted(even, reverse=True)  # Create a new Variable which is reverse of original
# # and is a copy of old one
# # i.e. -> allocate a new space in memory they both are different
#
# print(another_list is even)  # check if they are same return false
# print(another_list == even)  # check if they have same content return false
#
# # Monty Python example
# menu = list()
# menu.append(['egg', 'spam', 'bacon'])
# menu.append(['egg', 'sausage', 'bacon'])
# menu.append(['egg', 'spam'])
# menu.append(['egg', 'bacon', 'spam'])
# menu.append(['egg', 'sausage', 'bacon', 'spam'])
# menu.append(['spam', 'sausage', 'bacon', 'spam'])
# menu.append(['spam', 'egg', 'sausage', 'bacon', 'spam'])
#
# for meal in menu:
#     if 'spam' not in meal:
#         print(meal)
#         for ingredient in meal:
#             print(ingredient)
#
# # Iterators
# # --> list and Strings are two iterables object called iterable
# # --> iterate (doing iteration)
# string = '1234567890'
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# # print(next(my_iterator))  # create error this line
#
# # both are same but behind the seen python convert string tp iter(string)
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)
#
# # ----
# mye_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#
# mye_iterator = iter(mye_list)
#
# for i in range(0, len(mye_list)):
#     next_item = next(mye_iterator)
#     print(next_item)
#
# # Range
# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 100, 2))
# odd = list(range(1, 100, 2))
#
# print(even)
# print(odd)
#
# small_decimals = range(0, 10)
# print(small_decimals)
# my_range = small_decimals[::2]
# print(small_decimals)
# print(my_range)
# print(my_range.index(4))
#
# print('=' * 40)
# print('++++' * 50)
# decinal = range(0, 100)
# print(decinal)
#
# x = decinal
# print(x is decinal)  # true... so it has a single allocated space in memory
#
# my_new_range = decinal[3:40:3]
# print(my_new_range is decinal)  # false... it create a new copy. allocated a different
# # space in memory do not modify the original
# print(my_new_range)
#
# for i in my_new_range:
#     print(i)
#
# print('=' * 40)
#
# for i in range(3, 40, 3):
#     print(i)
#
# print(my_new_range == range(3, 40, 3))
# print(my_new_range is range(3, 40, 3))
# print(my_new_range in range(3, 40, 3))
#
# print('+' * 40)
#
# x_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#
# z = x_list
# print(z is x_list)
# z.append('zzz')
# print(z is x_list)
# new_x_list = x_list[2:4:2]
# print(new_x_list is x_list)


# s = 'abcdef'
#
# k = s
# print(hex(id(s)))  # allocate a memory
# print(hex(id(k)))  # no allocation of memory only reference the allocated memory by s
# print(k is s)  # true work as a reference variable
# k = 'xyz'
# print(k is s)
# print(hex(id(s)))  # stay in same memory
# print(hex(id(k)))  # allocate a new memory
# k = 'abcdef'
# print(k is s)
# print(hex(id(s)))  # stay in same memory
# print(hex(id(k)))  # destroy the allocated memory and re reference the allocated memory by s
# s = 'ddggggggg'
# print(k is s)
# print(hex(id(s)))  # allocate a new memory
# print(hex(id(k)))  # stay in the memory which is idealized by the s in past
# q = s[4]
# print(q is s)

############################################################################################
# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(hex(id(decimals)))
# print(hex(id(my_range)))
# x = range(3, 40, 3)
# print(my_range == x)
# print(my_range is x)
# print(hex(id(x)))

# it is equal because the return data is same in both
# print(range(0, 5, 2) == range(0, 6, 2))  # return true
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
#
# for i in r[::-2]:
#     print(i)
#
# print('+' * 20)
#
# for i in range(99, 0, -2):
#     print(i)
#
# print('=' * 20)
#
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2):
#     print(i)

backString = 'egaugnal lufrewop yrev a si nohtyp'
print(backString[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)

ss = 'String' # 'String' allocated a space in memory and a variable _name ss point
# the address
print(hex(id(ss)))  # address of memory allocated space
ss = ss[::-1]  # ss[::-1] -> is  creating a new string so it allocate a new space in memory
# then ss de-point the old address and point the new address in memory
print(hex(id(ss))) # new address of memory allocated space
