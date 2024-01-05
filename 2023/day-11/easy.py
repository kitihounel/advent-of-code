from sys import stdin
from itertools import product, combinations
from bisect import bisect_left, bisect_right


def read_input():
    image = [[ch for ch in line.strip()] for line in stdin]
    height = len(image)
    width = len(image[0])
    return image, height, width


image, height, width = read_input()
rows = [True for _ in range(height)]
cols = [True for _ in range(width)]
galaxies = []
for i, j in product(range(height), range(width)):
    if image[i][j] == '#':
        rows[i] = False
        cols[j] = False
        galaxies.append((i, j))

expanded_rows = [i for i in range(height) if rows[i]]
expanded_cols = [j for j in range(width) if cols[j]]
v = 0
for p, q in combinations(galaxies, 2):
    i1, i2 = min(p[0], q[0]), max(p[0], q[0])
    j1, j2 = min(p[1], q[1]), max(p[1], q[1])
    extra_row_count = bisect_right(expanded_rows, i2) - bisect_left(expanded_rows, i1)
    extra_col_count = bisect_right(expanded_cols, j2) - bisect_left(expanded_cols, j1)
    d = (i2 - i1) + (j2 - j1) + extra_row_count + extra_col_count
    v += d
print(v)
