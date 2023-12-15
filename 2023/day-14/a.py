from sys import stdin
from itertools import tee


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]


def pairwise(iterable):
    # I have Python 3.8 on my machine; `pairwise` is not in the itertools module yet.
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


grid = read_input()
height, width = len(grid), len(grid[0])
v = 0
for j in range(width):
    rows = [-1] + [i for i in range(height) if grid[i][j] == '#'] + [height]
    for p, q in pairwise(rows):
        n = sum(1 if grid[i][j] == 'O' else 0 for i in range(p + 1, q)) # Number of rounded rocks
        a = height - (p + 1) # First row occupied by a rounded rock after the roll in 1-based index
        s = a * n - (n * (n - 1)) // 2
        v += s
print(v)
