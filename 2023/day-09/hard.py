from itertools import tee
from sys import stdin


def pairwise(iterable):
    # I have Python 3.8 on my machine; `pairwise` is not in the itertools module yet.
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def read_input():
    return list(map(lambda line: [int(token) for token in line.split()], stdin))


report = read_input()
v = 0
for history in report:
    numbers = [n for n in history]
    k = numbers[0]
    i = 1
    while True:
        numbers[:] = [b - a for a, b in pairwise(numbers)]
        k += numbers[0] * (-1 if i % 2 == 1 else 1)
        i += 1
        if all(n == 0 for n in numbers):
            break
    v += k
print(v)
