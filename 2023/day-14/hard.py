from sys import stdin
from itertools import product, tee


def pairwise(iterable):
    # I have Python 3.8 on my machine; `pairwise` is not in the itertools module yet.
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def read_input():
    return [[ch for ch in line.strip()] for line in stdin]


def to_north():
    global grid, width, height
    for col, row in product(range(width), range(height)): # Cells are vsited by colum then by row
        if grid[row][col] != 'O':
            continue
        current_row = row
        while current_row > 0 and grid[current_row-1][col] == '.':
            grid[current_row-1][col] = 'O'
            grid[current_row][col] = '.'
            current_row -= 1


def to_south():
    global grid, width, height
    for col, row in product(range(width), range(height - 1, -1, -1)): # Cells are visited by colum then by row (reversed)
        if grid[row][col] != 'O':
            continue
        current_row = row
        while current_row < height - 1 and grid[current_row+1][col] == '.':
            grid[current_row+1][col] = 'O'
            grid[current_row][col] = '.'
            current_row += 1


def to_west():
    global grid, width, height
    for row, col in product(range(height), range(width)): # Cells are visited by row then by column
        if grid[row][col] != 'O':
            continue
        current_col = col
        while current_col > 0 and grid[row][current_col-1] == '.':
            grid[row][current_col-1] = 'O'
            grid[row][current_col] = '.'
            current_col -= 1


def to_east():
    global grid, width, height
    for row, col in product(range(height), range(width - 1, -1, -1)): # Cells are visited by row then by column (reversed)
        if grid[row][col] != 'O':
            continue
        current_col = col
        while current_col < width - 1 and grid[row][current_col+1] == '.':
            grid[row][current_col+1] = 'O'
            grid[row][current_col] = '.'
            current_col += 1


def compute_load():
    global grid, height
    load = 0
    for i, row in enumerate(grid, 0):
        load += (height - i) * sum(1 if ch == 'O' else 0 for ch in row)
    return load


def cycle():
    ls = [to_north, to_west, to_south, to_east]
    for fn in ls:
        fn()


grid = read_input()
height, width = len(grid), len(grid[0])
state = tuple(tuple(row) for row in grid)
state_indexes = {state: 0}
states = [state]
loads = [compute_load()]
limit = 10 ** 9
for i in range(1, limit + 1):
    cycle()
    state = tuple(tuple(row) for row in grid)
    if state in state_indexes:
        first_appareance = state_indexes[state]
        cycle_length = i - first_appareance
        m = (limit - first_appareance) % cycle_length
        print(loads[first_appareance + m])
        break
    state_indexes[state] = i
    states.append(state)
    loads.append(compute_load())
else:
    print('No cycle found. Have to do all the work.')
    print(compute_load())
