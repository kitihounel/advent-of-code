from sys import stdin


def is_valid(i, j):
    global height, width
    return (0 <= i < height) and (0 <= j < width)


def visit(i, j):
    global grid
    ls = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    for t in filter(lambda t: is_valid(*t), ls):
        x, y = t
        if not grid[x][y].isdigit() and grid[x][y] != '.':
            return True
    if is_valid(i, j + 1) and grid[i][j + 1].isdigit():
        return visit(i, j + 1)
    return False


grid = list(map(lambda l: l.strip(), stdin))
height, width = len(grid), len(grid[0])
v = 0
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
            v += int(literal)
print(v)
