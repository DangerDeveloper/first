# # t = 'a', 'b', 'c'
# # print(t)
# #
# # print('a', 'b', 'c')
# # print(('a', 'b', 'c'))
#
# # a = b = c = d = 12  # we can assign single value to multiple variable
# and only one allocated space in memory
# # print(hex(id(a)))
# # print(hex(id(b)))
# # print(hex(id(c)))
# # print(hex(id(d)))
# # x, y = 22, 34  # assign multiple variable in single line with different value
# # print(f'x -> {x} allocated memory address -> {hex(id(x))}')
# # print(f'y -> {y} allocated memory address -> {hex(id(y))}')
#
# check = ('ajay', 'singh', 1994)
# print(check)
# print(f'check -> {check} allocated memory address -> {hex(id(check))}')
# print(check[1])
# # check[1] = 'Somthing'  # Tuple is immutable object so we can't update the content once created
# # String are also immutable but list are mutable i.e we can append, add, remove data from list
# # -----------# check below
# check = (check[0], 'somthing', check[2])
# print(check)
# print(f'check -> {check} allocated memory address -> {hex(id(check))}')
# #  In python programming right side has a value which is stored in memory and take a space
# #  which has a address and left side is a variable which point to the location of the
# #  allocated memory space
# #  But string and Tuples are re created means the same variable can point to different variable in memory
# #  ('ajay', 'singh', 1994) allocated a space in memory and check is point to that location
# #  python allocated a memory first then give a address so variable can point
# #  thus right side run first so it allocated a memory and then left side which then point the
# #  location in memory
# #  (check[0], 'somthing', check[2]) this create a new tuple in memory with old memory data
# #  check[0] when its created then check same variable can point to this new address in memory
# #  and old one is destroyed. we are not updating content in tuple because it is immutable
# #  we create a new tuple which has a different address in memory and point to new address with same variable
# #  so it look that we update a content but this is new.
#
# aa = ['ajay', 'singh', 1994]
# print(aa)
# print(f'aa -> {aa} allocated memory address -> {hex(id(aa))}')
# aa[1] = 'somthing'
# print(aa)
# print(f'aa -> {aa} allocated memory address -> {hex(id(aa))}')
# # In the list it is mutable so the allocated memory is same we are not re create a list
# # but we are updating a list


# ---- Unpacking in tuples ----
# new_tuples = 'ajay', 'singh', 1994  # creating a new tuples
# first_name, second_name, year = new_tuples
# print(first_name)
# print(second_name)
# print(year)

#  If the value is same then the another variable is also point at the same
#  address in the memory for saving the space in memory
# first = 14
# print(f'first -> {first} allocated memory address -> {hex(id(first))}')
# second = 14
# print(f'second -> {second} allocated memory address -> {hex(id(second))}')
# print(first is second)

# print(bin(101))  # to represent the binary digit
# print(hex(101))  # to represent the hexadecimal digit

# ---------------
# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title: {}".format(track, title))
#

# imelda = "More Mayhem", "Imelda May", 2011, (
#     [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
#
# print(imelda)
#
# imelda[3].append((5, "All For You"))
#
# title, artist, year, tracks = imelda
# tracks.append((6, "Eternity"))
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title: {}".format(track, title))
