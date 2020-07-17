import sys

# # --- 1st
# def my_range(n: int):
#     print('my_range starts')
#     start = 0
#     while start < n:
#         print(f'my_range is returning {start}')
#         yield start
#         start += 1
#
#
# _ = input('Line 13')
# # big_range = range(1000)
# big_range = my_range(5)
# _ = input('Line 16')
#
# print(f'big_range is {sys.getsizeof(big_range)} bytes')
#
# # create a list containing all the values in big_range
# big_list = []
#
# _ = input('Line 23')
# for val in big_range:
#     _ = input('Line 25 - inside loop')
#     big_list.append(val)
#
# print(f'big_list is {sys.getsizeof(big_list)} bytes')
# print(big_range)
# print(big_list)
#
# # --- complete 1

# # ------ Start second
# def my_range(n: int):
#     print('my_range starts')
#     start = 0
#     while start < n:
#         print(f'my_range is returning {start}')
#         yield start
#         start += 1
#
#
# _ = input('Line 45')
# big_range = my_range(5)
# print(next(big_range))
# _ = input('Line 48')
#
# print(f'big_range is {sys.getsizeof(big_range)} bytes')
#
# # create a list containing all the values in big_range
# big_list = []
#
# _ = input('Line 55')
# for val in big_range:
#     _ = input('Line 57 - inside loop')
#     big_list.append(val)
#
# print(f'big_list is {sys.getsizeof(big_list)} bytes')
# print(big_range)
# print(big_list)
#
# for val in big_range:
#     print('is it print i is {}'.format(val))
# # ----- End second


# ------ Start Third
big_range = range(5)

print(f'big_range is {sys.getsizeof(big_range)} bytes')

# create a list containing all the values in big_range
big_list = []

for val in big_range:
    print('it print')
    big_list.append(val)

print(f'big_list is {sys.getsizeof(big_list)} bytes')
print(big_range)
print(big_list)

for val in big_range:
    print(f'Well it also print {val}')

# ----- End Third


#  Generators and Yield
