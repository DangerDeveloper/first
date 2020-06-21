def python_food():
    width = 80
    text = 'Spam and Eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text(text):  # Parameter variable define in the function
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text_args(*args):  # Parameter variable define in the function
    text = ''
    for arg in args:
        text += str(arg) + ' '
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text_full(*args, sep=' ', end='\n', file=None, flush=False):  # Parameter variable define in the function
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text, end=end, file=file, flush=flush)


# call The Function
centre_text('spam and eggs')  # Argument when function is called
centre_text('spam, spam and eggs')
centre_text('spam, spam, spam and spam')
centre_text(12)

centre_text_args('spam and eggs')  # Argument when function is called
centre_text_args('spam, spam and eggs')
centre_text_args('spam, spam, spam and spam')
centre_text_args(12)
centre_text_args(12, 'spam, spam, spam and spam', 'spam and eggs', 23)

centre_text_full('spam and eggs')  # Argument when function is called
centre_text_full('spam, spam and eggs')
centre_text_full('spam, spam, spam and spam')
centre_text_full(12)
centre_text_full(12, 'spam, spam, spam and spam', 'spam and eggs', 23, sep=':')
# print(self, *args, sep=' ', end='\n', file=None) # *args --> Use unlimited amount of argument eg
# print('hello', 'writer', 1, 4)

with open('centered', 'w') as center_file:
    centre_text_full('spam and eggs', file=center_file)  # Argument when function is called
    centre_text_full('spam, spam and eggs', file=center_file)
    centre_text_full('spam, spam, spam and spam', file=center_file)
    centre_text_full(12, file=center_file)
    centre_text_full(12, 'spam, spam, spam and spam', 'spam and eggs', 23, sep=':', file=center_file)

# a = list()
# print(repr(a))

