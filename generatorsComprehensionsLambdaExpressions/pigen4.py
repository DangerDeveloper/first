def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


odd = oddnumbers()
for i in range(100):
    print(next(odd))
