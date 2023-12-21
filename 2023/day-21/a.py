from sys import stdin
from functools import lru_cache
from collections import deque
from itertools import product


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]


def find_start():
    global garden, height, width
    for i, j in product(range(height), range(width)):
        if garden[i][j] == 'S':
            return i, j


garden = read_input()
height, width = len(garden), len(garden[0])
i, j = find_start()
max_count = 64
q = deque([(i, j, 0)])
visited = {(i, j, 0, -1)}
targets = set()
while len(q) != 0:
    i, j, k = q.popleft()
    p = i * width + j
    if k == max_count:
        if (i, j) not in targets:
            targets.add((i, j))
        continue
    for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= u < height and 0 <= v < width and garden[u][v] != '#' and (u, v, k + 1, p) not in visited:
            visited.add((u, v, k + 1, p))
            q.append((u, v, k + 1))
print(len(targets))
