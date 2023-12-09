from sys import stdin
from re import findall
from itertools import cycle


def read_input():
    instructions = stdin.readline().strip()
    _ = stdin.readline()
    neighbors = {}
    for line in stdin:
        location, left, right = findall('\\w+', line)
        neighbors[location] = (left, right)
    return instructions, neighbors


instructions, neighbors = read_input()
location = 'AAA'
step_count = 0
for ins in cycle(instructions):
    left, right = neighbors[location]
    location = left if ins == 'L' else right
    step_count += 1
    if location == 'ZZZ':
        break
print(step_count)
