from sys import stdin
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


# We use cartesian coordinates for this part.
moves = { 'U': (0, +1), 'L': (-1, 0), 'D': (0, -1), 'R': (+1, 0) }
directions = ['R', 'D', 'L', 'U']

def read_input():
    ls = []
    for line in stdin:
        s = line.split()[-1]
        i, n = int(s[-2]), int(s[2:7], 16)
        ls.append((directions[i], n))

    return ls


def polygon_area(vertices):
    n = len(vertices)
    a, b = 0, 0

    for i in range(0, n):
        p, q = points[i], points[(i + 1) % n]
        a += p.x * q.y
        b += q.x * p.y

    return abs(a - b) // 2


def count_boundary_points(vertices):
    b, n = 0, len(vertices)
    for i in range(len(vertices)):
        p, q = points[i], points[(i + 1) % n]
        b += abs(p.x - q.x) + abs(p.y - q.y)

    return b


intructions = read_input()
points = [Point(0, 0)]
for t in intructions:
    ch, n = t
    m = moves[ch]
    p = points[-1]
    x, y = (c + n * d for c, d in zip(p, m))
    points.append(Point(x, y))
points.pop()


a = polygon_area(points)
b = count_boundary_points(points)
i = a + 1 - (b // 2)
print(b + i)
