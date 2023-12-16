from sys import stdin
from collections import deque


UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]


def is_valid(i, j):
    global height, width
    return 0 <= i < height and 0 <= j < width


def next_cell(i, j, direction):
    d = { UP: (i - 1, j), DOWN: (i + 1, j), RIGHT: (i, j + 1), LEFT: (i, j - 1) }
    return d[direction]


def next_directions(direction, symbol):
    d = {
        '/':  {UP: [RIGHT],         DOWN: [LEFT],           LEFT: [DOWN],       RIGHT: [UP]},
        '\\': {UP: [LEFT],          DOWN: [RIGHT],          LEFT: [UP],         RIGHT: [DOWN]},
        '-':  {UP: [LEFT, RIGHT],   DOWN: [LEFT, RIGHT],    LEFT: [LEFT],       RIGHT: [RIGHT]},
        '|':  {UP: [UP],            DOWN: [DOWN],           LEFT: [UP, DOWN],   RIGHT: [UP, DOWN]},
        '.':  {UP: [UP],            DOWN: [DOWN],           LEFT: [LEFT],       RIGHT: [RIGHT]}
    }
    return d[symbol][direction]


grid = read_input()
height, width = len(grid), len(grid[0])
q = deque([(0, 0, RIGHT)])
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
print(len({ (i, j) for i, j, _ in seen })) 
