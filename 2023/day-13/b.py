def read_input():
    notes = []
    current = []
    try:
        while True:
            line = input()
            if line == '':
                notes.append(current)
                current = []
            else:
                current.append(line)
    except EOFError:
        notes.append(current)
    return notes


def get_columns(grid):
    column_count = len(grid[0])
    return [''.join(line[i] for line in grid) for i in range(column_count)]


def find_symmetry(grid):
    n = len(grid)
    for i in range(0, n - 1):
        if grid[i] == grid[i+1]:
            j, k = i - 1, i + 2
            while j >= 0 and k < n and grid[j] == grid[k]:
                j, k = j - 1, k + 1
            if j < 0 or k >= n:
                return i + 1
    return 0


def find_smug_symmetry(grid):
    n = len(grid)
    for i in range(0, n - 1):
        d = sum(1 if a != b else 0 for a, b in zip(grid[i], grid[i+1]))
        if grid[i] == grid[i+1] or d == 1:
            j, k = i - 1, i + 2
            while j >= 0 and k < n:
                if grid[j] != grid[k]:
                    if d == 0 and sum(1 if a != b else 0 for a, b in zip(grid[j], grid[k])) == 1:
                        d = 1
                    else:
                        break
                j, k = j - 1, k + 1
            if (j < 0 or k >= n) and d != 0:
                return i + 1
    return 0

notes = read_input()
v = 0
for note in notes:
    n = find_smug_symmetry(note)
    v += n * 100 if n != 0 else find_smug_symmetry(get_columns(note))
print(v)
