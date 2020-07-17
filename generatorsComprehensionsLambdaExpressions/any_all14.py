entries = [1, 2, 3, 4, 5]

print(f'All: {all(entries)}')
print(f'Any: {any(entries)}')

print('Iterable with fals value')
entries_with_zero = [1, 2, 0, 4, 5]

print(f'All: {all(entries_with_zero)}')
print(f'Any: {any(entries_with_zero)}')

# what is this
entries_empty = []

print(f'All: {all(entries_empty)}')
print(f'Any: {any(entries_empty)}')

print()
print('Values interpreted as False in Python')
print(f"""
False: {False}
None: {bool(None)}
0: {bool(0)}
0.0: {bool(0.0)}
empty list []: {bool([])}
empty tuple (): {bool(())}
empty string '': {bool('')}
empty string "": {bool("")}
empty maping {{}}: {bool({})}
""")
