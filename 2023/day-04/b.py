from sys import stdin
from collections import Counter


lines = [line.strip() for line in stdin]
c = Counter(range(1, len(lines) + 1))
for i, line in enumerate(lines, 1):
    splits = line.split(':')
    relevant_data = splits[1].strip()
    data_splits = [split.strip() for split in relevant_data.split('|')]
    winning_numbers = {int(token) for token in data_splits[0].split()}
    numbers = {int(token) for token in data_splits[1].split()}
    n = len(numbers.intersection(winning_numbers))
    for k in range(i + 1, min(i + n + 1, len(lines) + 1)):
        c[k] += c[i]
print(sum(c.values()))
