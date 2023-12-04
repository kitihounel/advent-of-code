from sys import stdin
from collections import defaultdict


def is_valid(i, j):
    global height, width
    return (0 <= i < height) and (0 <= j < width)


def visit(i, j):
    global grid, last_star_i, last_star_j
    ls = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    for t in filter(lambda t: is_valid(*t), ls):
        x, y = t
        if not grid[x][y].isdigit() and grid[x][y] != '.':
            last_star_i, last_star_j = (x, y) if grid[x][y] == '*' else (None, None)
            return True
    if is_valid(i, j+1) and grid[i][j+1].isdigit():
        return visit(i, j+1)
    return False


grid = list(map(lambda l: l.strip(), stdin))
height, width = len(grid), len(grid[0])
last_star_i = None
last_star_j = None
star_neighbors = defaultdict(list)
for i, line in enumerate(grid):
    j = 0
    while j < len(line):
        if not line[j].isdigit():
            j += 1
            continue
        start = j
        literal = line[j]
        j += 1
        while j < len(line) and line[j].isdigit():
            literal += line[j]
            j += 1
        if visit(i, start):
            g = int(literal)
            if last_star_i is not None:
                star_neighbors[(last_star_i, last_star_j)].append(g)
                last_star_i = None
                last_star_j = None

ratio_sum = 0
for ls in star_neighbors.values():
    if len(ls) == 2:
        ratio_sum += ls[0] * ls[1]
print(ratio_sum)
