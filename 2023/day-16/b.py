from sys import stdin
from collections import deque
from functools import lru_cache

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]

@lru_cache
def is_valid(i, j):
    global height, width
    return 0 <= i < height and 0 <= j < width

@lru_cache
def next_cell(i, j, direction):
    d = { UP: (i - 1, j), DOWN: (i + 1, j), RIGHT: (i, j + 1), LEFT: (i, j - 1) }
    return d[direction]

@lru_cache
def next_directions(direction, symbol):
    d = {
        '/':  {UP: [RIGHT],         DOWN: [LEFT],           LEFT: [DOWN],       RIGHT: [UP]},
        '\\': {UP: [LEFT],          DOWN: [RIGHT],          LEFT: [UP],         RIGHT: [DOWN]},
        '-':  {UP: [LEFT, RIGHT],   DOWN: [LEFT, RIGHT],    LEFT: [LEFT],       RIGHT: [RIGHT]},
        '|':  {UP: [UP],            DOWN: [DOWN],           LEFT: [UP, DOWN],   RIGHT: [UP, DOWN]},
        '.':  {UP: [UP],            DOWN: [DOWN],           LEFT: [LEFT],       RIGHT: [RIGHT]}
    }
    return d[symbol][direction]


def check(i, j, direction):
    global grid
    q = deque([(i, j, direction)])
    seen = set(q)
    while len(q) != 0:
        i, j, d = q.popleft()
        symbol = grid[i][j]
        directions = next_directions(d, symbol)
        for nxt in directions:
            u, v = next_cell(i, j, nxt)
            if is_valid(u, v) and (u, v, nxt) not in seen:
                seen.add((u, v, nxt))
                q.append((u, v, nxt))
    return len({ (i, j) for i, j, _ in seen })


grid = read_input()
height, width = len(grid), len(grid[0])
ls = [
    ([(0, j) for j in range(width)],            DOWN),  # first row
    ([(height - 1, j) for j in range(width)],   UP),    # last row
    ([(i, 0) for i in range(height)],           RIGHT), # first column
    ([(i, width - 1) for i in range(height)],   LEFT)   # last column
]
m = 0
for edge, direction in ls:
    for i, j in edge:
        m = max(m, check(i, j, direction))
        if m == height * width:
            break
print(m)
