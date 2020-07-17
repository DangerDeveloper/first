# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)

# type your solution here:
my_output = [len(a) for a in text.split()]  # List Comprehension
# my_output = {len(a) for a in text.split()}  # set Comprehension
# my_output = (len(a) for a in text.split())  # generators
print(my_output)
# print([len(a) for a in text.split()])
# print({len(a) for a in text.split()})
# print(len(a) for a in text.split())

# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

# type the corresponding comprehension here:
my_output = [(a, len(a)) for a in text.split()]
print(my_output)
