from sys import stdin, setrecursionlimit
from collections import defaultdict


setrecursionlimit(50_000)

valid_neighbors = {
    '|': [
        (lambda i, j: (i - 1, j), '7|F'), # up
        (lambda i, j: (i + 1, j), 'J|L')  # down
    ],
    '-': [
        (lambda i, j: (i, j - 1), 'F-L'), # left
        (lambda i, j: (i, j + 1), '7-J')  # right
    ],
    'L': [
        (lambda i, j: (i - 1, j), '7|F'), # up
        (lambda i, j: (i, j + 1), '7-J')  # right
    ],
    'J': [
        (lambda i, j: (i - 1, j), '7|F'), # up
        (lambda i, j: (i, j - 1), 'F-L')  # left
    ],
    '7': [
        (lambda i, j: (i, j - 1), 'L-F'), # left
        (lambda i, j: (i + 1, j), 'J|L')  # down
    ],
    'F': [
        (lambda i, j: (i + 1, j), 'J|L'), # down
        (lambda i, j: (i, j + 1), 'J-7')  # right
    ],
    '.': [
        (lambda i, j: (i - 1, j), '7|F'), # up
        (lambda i, j: (i + 1, j), 'J|L'), # down
        (lambda i, j: (i, j - 1), 'F-L'), # left
        (lambda i, j: (i, j + 1), 'J-7')  # right
    ]
}


def read_input():
    maze = [[ch for ch in line.strip()] for line in stdin]
    height = len(maze)
    width = len(maze[0])
    return maze, height, width


def is_inside_maze(i, j):
    global height, width
    return 0 <= i < height and 0 <= j < width


def get_neighbors(i, j):
    global maze
    symbol = maze[i][j]
    config = valid_neighbors[symbol]
    neighbors = []
    for fn, symbols in config:
        y, x = fn(i, j)
        if is_inside_maze(y, x) and maze[y][x] in symbols:
            neighbors.append((y, x))
    return neighbors
    

def visit(pipe: tuple, parents: dict, visited: set, onhold: set):
    global start
    onhold.add(pipe)
    visited.add(pipe)
    neighbors = get_neighbors(*pipe)
    # For the start pipe, we only visit one of its children.
    if pipe == start:
        neighbors = neighbors[0:1]
    for tup in neighbors:
        if tup == parents.get(pipe, None):
            continue
        if tup not in visited:
            parents[tup] = pipe
            visit(tup, parents, visited, onhold)
        elif tup == start:
            raise Exception('Loop closed')
    onhold.remove(pipe)


def get_tiles_surrounded_by_loop(loop_pipes):
    sorted_loop_pipes = sorted(loop_pipes)
    groups = defaultdict(list)
    for i, j in sorted_loop_pipes:
        groups[i].append(j)
    surrounded_tiles = []
    for i in groups:
        values = groups[i]
        lo, hi = values[0], values[-1]
        for j in range(lo + 1, hi):
            if maze[i][j] == '.':
                surrounded_tiles.append((i, j))
    return surrounded_tiles


maze, height, width = read_input()
start = (20, 103)   # Position of start pipe
maze[20][103] = '7' # Start pipe is of type '7'.
visited = set()
parents = {}
onhold = set()
try:
    visit(start, parents, visited, onhold)
except Exception as e:
    pass

