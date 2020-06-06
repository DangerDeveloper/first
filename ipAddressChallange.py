ipAddress = input('Enter IP Address: ')
if len(ipAddress) == 0:
    ipAddress += '.'
else:
    if ipAddress[-1] != '.':
        ipAddress += '.'

segment = 1
segment_length = 0
# character = ''

for character in ipAddress:
    if character == '.':
        print('Segment {} contains {} characters.'.format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# character variable of for loop can be access from outside for loop it is valid in python
# But in java or c it is not valid it scope is limited only inside the loop.
# Unless the final character in the string was a '.' then we have't printed the last segment
# if character != '.':
#     print(f'Segment {segment} contains {segment_length} characters.')
