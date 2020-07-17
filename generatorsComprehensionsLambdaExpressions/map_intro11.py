import timeit

text = 'what have the romans ever done for us'


def capitals_function():
    capitals = [char.upper() for char in text]
    return capitals


# use map
def map_capitals_function():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def words_function():
    words = [word.upper() for word in text.split(' ')]
    return words


# use map
def map_words_function():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words


if __name__ == '__main__':
    print(capitals_function())
    print(map_capitals_function())
    print(words_function())
    print(map_words_function())
    print(timeit.timeit(capitals_function, number=100000))
    print(timeit.timeit(map_capitals_function, number=100000))
    print(timeit.timeit(words_function, number=100000))
    print(timeit.timeit(map_words_function, number=100000))

# also like this second start
# text_time = """\
# text = 'what have the romans ever done for us'
# """
#
# capitals_time = """\
# capitals = [char.upper() for char in text]
# """
#
# # use map
# map_capitals_time = """\
# map_capitals = list(map(str.upper, text))
# """
# words_time = """\
# words = [word.upper() for word in text.split(' ')]
# """
#
# # use map
# map_words_time = """\
# map_words = list(map(str.upper, text.split(' ')))
# """
#
# print(timeit.timeit(capitals_time, number=10000000, setup=text_time))
# print(timeit.timeit(map_capitals_time, number=10000000, setup=text_time))
# print(timeit.timeit(words_time, number=10000000, setup=text_time))
# print(timeit.timeit(map_words_time, number=10000000, setup=text_time))
# second finish
