# # List Comprehensions
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# # By for loop
# # squares = []
# # for number in numbers:
# #     squares.append(number ** 2)
# # By List Comprehensions
# squares = [number ** 2 for number in numbers]  # Create a List
# # squares = {number ** 2 for number in numbers}  # Create a sets
#
# print(squares)

# Second
# text = 'what have the romans ever done for us'
#
# capitals = [char.upper() for char in text]
# print(capitals)
#
# words = [word.upper() for word in text.split(' ')]
# print(words)
#
# lc_words = text.split(' ')
# print(lc_words)
#
# # It is not use because be can achieve same result by above code
# lc_wordss = [word for word in text.split(' ')]
# print(lc_wordss)
# second Complete

# # Third Section
#
# numbers = [1, 2, 3, 4, 5, 6]
# number = int(input("Please Enter a number, To get a square of this"))
#
# # Always give the same result because the number variable in for loop re-write
# # our input number variable
# # squares = []
# # for number in numbers:
# #     squares.append(number ** 2)
#
# # By this input number variable is not re-write by List Comprehensions number variable
# squares = [number ** 2 for number in numbers]
#
# index_pos = numbers.index(number)
# print(squares[index_pos])
#
# # Third Section Complete


# def square_root():
#     value = []
#     while True:
#         number = int(input("Please Enter a number, To get a square of this"))
#         if number == -1:
#             squares = [number ** 2 for number in value]
#             print(squares)
#         value.append(number)
#
#
# square_root()
