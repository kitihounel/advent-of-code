from sys import stdin
from collections import deque


def read_input():
    records = []
    for line in stdin:
        chunks = line.strip().split()
        conditions = [ch for ch in chunks[0]]
        numbers = [int(token) for token in chunks[1].split(',')]
        records.append((conditions, numbers))
    return records


def check_damaged_spring(i, conditions, numbers, q):
    if len(numbers) == 0:
        return
    if numbers[-1] == 0 and not (i == len(conditions) - 1 or conditions[i+1] != '#'):
        return
    copy = numbers.copy()
    copy[-1] -= 1
    if copy[-1] == 0:
        copy.pop()
    q.append((i + 1, copy))


def check_operational_spring(i, conditions, numbers, q):
    i += 1
    while i < len(conditions) and conditions[i] == '.':
        i += 1
    copy = numbers.copy()
    q.append((i, copy))


records = read_input()
v = 0
for record in records:
    conditions, numbers = record
    q = deque()
    q.append((0, list(reversed(numbers))))
    while len(q) != 0:
        i, numbers = q.popleft()
        if i == len(conditions):
            v += 1 if len(numbers) == 0 else 0
        elif conditions[i] == '#':
            check_damaged_spring(i, conditions, numbers, q)
        elif conditions[i] == '.':
            check_operational_spring(i, conditions, numbers, q)
        elif conditions[i] == '?':
            check_damaged_spring(i, conditions, numbers, q)
            check_operational_spring(i, conditions, numbers, q)
print(v)
