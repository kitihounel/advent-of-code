from sys import stdin
from itertools import chain
from collections import deque

# We use array indexes to solve this part of the challenge.
moves = {'U': (+1, 0), 'L': (0, -1), 'D': (-1, 0), 'R': (0, +1)}


def read_input():
    ls = []
    for line in stdin:
        chunks = line.split()
        t = (chunks[0], int(chunks[1]), chunks[2][2:-1])
        ls.append(t)
    return ls


instructions = read_input()
shape = [(0, 0)]
for t in instructions:
    ch, n, _ = t
    di, dj = moves[ch]
    for _ in range(n):
        i, j = shape[-1]
        shape.append((i + di, j + dj))

min_i = min(t[0] for t in shape)
max_i = max(t[0] for t in shape)
min_j = min(t[1] for t in shape)
max_j = max(t[1] for t in shape)
height, width = max_i - min_i + 1, max_j - min_j + 1
normalized = {(i - min_i, j - min_j) for i, j in shape}

edge_cubes = chain(
    ((0, j) for j in range(width)),
    ((height - 1, j) for j in range(width)),
    ((i, 0) for i in range(height)),
    ((i, width - 1) for i in range(height))
)
edge_dots = [(i, j) for i, j in edge_cubes if (i, j) not in normalized]
visited = set(edge_dots)
q = deque(visited)
while len(q) != 0:
    i, j = q.popleft()
    for di, dj in moves.values():
        y, x = i + di, j + dj
        if 0 <= y < height and 0 <= x < width and (y, x) not in visited and (y, x) not in normalized:
            visited.add((y, x))
            q.append((y, x))

print(width * height - len(visited))
