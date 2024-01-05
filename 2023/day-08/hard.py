from sys import stdin
from re import findall
from itertools import cycle, product
from functools import reduce
from math import gcd
from collections import defaultdict


def read_input():
    instructions = stdin.readline().strip()
    _ = stdin.readline()
    neighbors = {}
    for line in stdin:
        location, left, right = findall('\\w+', line)
        neighbors[location] = (left, right)
    return instructions, neighbors


def is_start_location(location):
    return location[-1] == 'A'


def is_end_location(location):
    return location[-1] == 'Z'


def lcm(a, b):
    return a // gcd(a, b) * b


def magic_lcm(numbers):
    return reduce(lambda a, b: lcm(a, b), numbers)


instructions, neighbors = read_input()
start_locations = [k for k in  neighbors if is_start_location(k)]
end_locations = [k for k in  neighbors if is_end_location(k)]
numbers = {}
reachable = defaultdict(set) # Used for debugging. Maps each start location to end locations that are reachable from it.
for location in start_locations:
    current_location = location
    seen = set()
    steps = []
    for i, instruction in enumerate(cycle(instructions), 1):
        left, right = neighbors[current_location]
        next_location = left if instruction == 'L' else right
        if is_end_location(next_location):
            reachable[location].add(next_location)
            m = i % len(instructions)
            if (next_location, m) in seen:
                break
            seen.add((next_location, m))
            steps.append(i)
        current_location = next_location
    numbers[location] = steps

min_step_count = 10 ** 1000
for tup in product(*numbers.values()):
    min_step_count = min(min_step_count, magic_lcm(tup))
print(min_step_count)
