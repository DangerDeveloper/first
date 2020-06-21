import pickle
import shelve

# jabber = open("sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
# jabber.close()

# with handle error and do not need to close the file
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()  # read single line at a time
#     while line:
#         print(line, end='')
#         line = jabber.readline()  # after printing 1 line next line read

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()  # Read entire content lines and save as list
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.read()  # Read entire content as a single string
#
# for line in lines[::-1]:  # So it reverse every single alphabete in file
#     print(line, end='')

# with open('aa.txt', 'w') as file:
#     for num1 in range(0, 10):
#         for num2 in range(0, 10):
#             for num3 in range(0, 10):
#                 for num4 in range(0, 10):
#                     for num5 in range(0, 10):
#                         for num6 in range(0, 10):
#                             file.write(f'9795{num1}{num2}{num3}{num4}{num5}{num6}\n')
#                             # print(f'9795{num1}{num2}{num3}{num4}{num5}{num6}', file=file)

# with open('binary', 'bw') as bin_file:
#     # for i in range(30):
#     #     bin_file.write(bytes([i]))
#     bin_file.write(bytes(range(17)))
#
# with open('binary', 'br') as binFile:
#     for b in binFile:
#         print(b)

# pickel
# imelda = ('some data ', 'other dath', 2020, ((1, 'king'), (2, 'kong'), (3, 'long')))
#
# with open('imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# with open('imelda.pickle', 'rb') as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#
# print(imelda2)

# shelve
# # blt = ['bacon', 'lettuce', 'tomato', 'bread']
# # beans_on_toast = ['beans', 'bread']
# # scrambled_eggs = ['eggs', 'butter', 'milk']
# soup = ['tin of soup']
# # pasta = ['pasta', 'cheese']
# #
# with shelve.open('recipes', writeback=True) as recipes:
#     # recipes['blt'] = blt
#     # recipes['beans_on_toast'] = beans_on_toast
#     # recipes['scrambled_eggs'] = scrambled_eggs
#     # recipes['pasta'] = pasta
#     # recipes['soup'] = soup
#
#     # recipes['blt'].append('butter')  # No effect we cant append item in the database
#     # recipes['pasta'].append('tomato')
#
#     # We can append item in the list by this method
#     # temp_list = recipes['blt']
#     # temp_list.append('butter')
#     # recipes['blt'] = temp_list
#
#     # temp_list = recipes['pasta']
#     # temp_list.append('tomato')
#     # recipes['pasta'] = temp_list
#
#     # We can also add data by this method by use of extra parameter in open i.e writeback=True
#     # recipes['soup'].append('croutons')
#
#     # I cant understand this method
#     recipes['soup'] = soup  #
#     print(soup)
#     recipes.sync()
#     soup.append('cream')
#     print(soup)
#     # for snack in recipes:
#     #     print(snack, recipes[snack])


# shelve Challange
# books = shelve.open('book')
#
# books['recipes'] = {
#     'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
#     'beans_on_toast': ['beans', 'bread'],
#     'scrambled_eggs': ['eggs', 'butter', 'milk'],
#     'soup': ['tin of soup'],
#     'pasta': ['pasta', 'cheese']
# }
# books['maintenance'] = {
#     'stuck': ['oil'],
#     'loose': ['gaffer tape']
# }
#
# print(books['recipes']['soup'])
# print(books['recipes']['scrambled_eggs'])
# print(books['maintenance']['loose'])
#
# books.close()
