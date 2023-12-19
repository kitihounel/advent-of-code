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
seen = { (3, 0, DOWN, 4), (0, 3, RIGHT, 4) }
q = [B(sum(grid[i][0] for i in range(4)), 0, 0, 4, DOWN), B(sum(grid[0][j] for j in range(4)), 0, 0, 4, RIGHT)]
while len(q) != 0:
    b = heappop(q)
    if b.i == height - 1 and b.j == width - 1:
        cost = b.cost
        break

    list_extended = False
    for direction, w in walks.items():
        if direction == (b.direction + 2) % 4:
            continue

        if direction != b.direction:
            added_cost = 0
            i, j = b.i, b.j
            for _ in range(4):
                i, j = i + w.di, j + w.dj
                if not (0 <= i < height and 0 <= j < width):
                    continue
                added_cost += grid[i][j]
            q.append(B(b.cost + added_cost, i, j, 4, direction))
            seen.add(((i, j, direction, 4)))
            list_extended = True
        elif direction == b.direction and b.k < 10:
            i, j = b.i + w.di, b.j + w.dj
            if not (0 <= i < height and 0 <= j < width):
                continue
            if (i, j, direction, b.k + 1) not in seen:
                q.append(B(b.cost + grid[i][j], i, j, b.k + 1, direction))
                seen.add((i, j, direction, b.k + 1))
                list_extended = True

    if list_extended:
        heapify(q)
print(cost)
