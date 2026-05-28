def add(*args):
    total = 0

    for i in args:
        total = total + i

    return total

print(add(1, 2))
print(add(1, 2, 3, 4))
print(add(10, 20, 30))


