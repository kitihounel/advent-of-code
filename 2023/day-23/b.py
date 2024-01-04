from sys import stdin, setrecursionlimit
from collections import namedtuple
from functools import lru_cache


setrecursionlimit(20_000)


Cell = namedtuple('Cell', ['i', 'j'])


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]


@lru_cache
def is_valid(c):
    global height
    return 0 <= c.i < height and 0 <= c.j < height


def visit(c, visited, final_distances, distance):
    global maze, height
    visited.add(c)
    if c.i == height - 1:
        final_distances.add(distance)
    else:
        neighbors = get_neighbors(c)
        for other in neighbors:
            if other not in visited and maze[other.i][other.j] != '#':
                visit(other, visited, final_distances, distance + 1)
    visited.remove(c)


def get_neighbors(c):
    global maze, height
    i, j = c
    candidates = [Cell(i - 1, j), Cell(i + 1, j), Cell(i, j - 1), Cell(i, j + 1)]
    return [other for other in candidates if is_valid(other)]


maze = read_input()
height = len(maze)
start_column, end_column = maze[0].index('.'), maze[-1].index('.')
visited, final_distances = set(), set()
visit(Cell(0, start_column), visited, final_distances, 0)
answer = max(final_distances)
print(answer)
