from sys import stdin


# We use cartesian coordinates for this part.
moves = { 'U': (0, +1), 'L': (-1, 0), 'D': (0, -1), 'R': (+1, 0) }


def read_input():
    ls = []
    for line in stdin:
        chunks = line.split()
        t = (chunks[0], int(chunks[1]), chunks[2][2:-1])
        ls.append(t)
    return ls


intructions = read_input()
cells = [(0, 0)]
for t in intructions:
    ch, n, _ = t
    dx, dy = moves[ch]
    last_cell = cells[-1]
    next_cell = tuple(c + n * d for c, d in zip(last_cell, moves[ch]))
    cells.append(next_cell)
