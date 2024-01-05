from sys import stdin, setrecursionlimit
from collections import deque
from itertools import product


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


def is_on_edge(i, j):
    global height, width
    return i == 0 or i == height - 1 or j == 0 or j == width - 1


def get_neighbors(i, j, accept_dot=False):
    global maze
    symbol = maze[i][j]
    if symbol == '.' and not accept_dot:
        return []
    config = valid_neighbors[symbol]
    neighbors = []
    for fn, symbols in config:
        y, x = fn(i, j)
        if is_inside_maze(y, x) and (maze[y][x] in symbols or (accept_dot and maze[y][x] == '.')):
            neighbors.append((y, x))
    return neighbors
    

def visit(tile: tuple, parents: dict, visited: set, onhold: set):
    global entrance
    onhold.add(tile)
    visited.add(tile)
    neighbors = get_neighbors(*tile)
    # For the start pipe, we only visit one of its children.
    if tile == entrance:
        neighbors = neighbors[0:1]
    for tup in neighbors:
        if tup == parents.get(tile, None):
            continue
        if tup not in visited:
            parents[tup] = tile
            visit(tup, parents, visited, onhold)
        elif tup == entrance:
            raise Exception('Loop closed')
    onhold.remove(tile)


def find_loop():
    visited = set()
    parents = {}
    onhold = set()
    try:
        visit(entrance, parents, visited, onhold)
    except Exception:
        pass
    return onhold


def find_tiles_outside_loop():
    global universe, loop
    visited = {(i, j) for i, j in universe if (i, j) not in loop and is_on_edge(i, j)}
    q = deque(visited)
    while len(q) > 0:
        i, j = q.popleft()
        for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if is_inside_maze(u, v) and (u, v) not in loop and (u, v) not in visited:
                visited.add((u, v))
                q.append((u, v))
    return visited


def find_entrance():
    global maze
    for i, j in product(range(height), range(width)):
        if maze[i][j] == 'S':
            return (i, j)


def find_entrance_type(i, j):
    """Note: this won't work if the entrance is on an edge."""
    global maze
    if maze[i-1][j] in '7|F' and maze[i+1][j] in 'J|L':
        return '|'
    elif maze[i][j-1] in 'F-L' and maze[i][j+1] in '7-J':
        return '-'
    elif maze[i-1][j] in '7|F' and maze[i][j+1] in '7-J':
            return 'L'
    elif maze[i][j-1] in 'F-L' and maze[i-1][j] in '7|F':
            return 'J'
    elif maze[i+1][j] in 'J|L' and maze[i][j+1] in '7-J':
            return 'F'
    else:
        return '7'


maze, height, width = read_input()
entrance = find_entrance()
t = find_entrance_type(*entrance)
maze[entrance[0]][entrance[1]] = t

universe = {t for t in product(range(height), range(width))}
loop = find_loop()
outside_loop = find_tiles_outside_loop()
surrounded_by_loop = universe.difference(outside_loop, loop)

jmax = max(j for _, j in loop)
v = 0
for i, j in surrounded_by_loop:
    inside = False
    ls = [k for  k in range(j + 1, jmax + 1) if (i, k) in loop]
    previous = None
    for k in ls:
        symbol = maze[i][k]
        if symbol == '|':
            inside = not inside
        elif symbol == '7' and previous == 'L':
            inside = not inside
        elif symbol == 'J' and previous == 'F':
            inside = not inside
        if symbol != '-':
            previous = symbol 
    v += 1 if inside else 0
print(v)
