from sys import stdin
from collections import namedtuple
from heapq import heapify, heappop


TOP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
B = namedtuple('Block', ['cost', 'i', 'j', 'k', 'direction'])
W = namedtuple('Walk', ['di', 'dj'])
walks = { TOP: W(-1, 0), LEFT: W(0, -1), DOWN: W(+1, 0), RIGHT: W(0, +1) }


def read_input():
    return [[int(ch) for ch in line.strip()] for line in stdin]


grid = read_input()
height, width = len(grid), len(grid[0])
cost = None
seen = { (0, 0, DOWN, 1), (0, 0, RIGHT, 1) }
q = [B(0, 0, 0, 1, DOWN), B(0, 0, 0, 1, RIGHT)]
while len(q) != 0:
    b = heappop(q)
    if b.i == height - 1 and b.j == width - 1:
        cost = b.cost
        break

    list_extended = False
    for direction, w in walks.items():
        if direction == (b.direction + 2) % 4:
            continue
        i, j = b.i + w.di, b.j + w.dj
        if not (0 <= i < height and 0 <= j < width):
            continue
        if direction != b.direction and (i, j, direction, 1) not in seen:
            q.append(B(b.cost + grid[i][j], i, j, 1, direction))
            seen.add(((i, j, direction, 1)))
            list_extended = True
        elif direction == b.direction and b.k < 3 and (i, j, direction, b.k + 1) not in seen:
            q.append(B(b.cost + grid[i][j], i, j, b.k + 1, direction))
            seen.add((i, j, direction, b.k + 1))
            list_extended = True

    if list_extended:
        heapify(q)
print(cost)
