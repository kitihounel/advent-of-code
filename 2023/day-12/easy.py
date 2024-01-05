from sys import stdin


def next_permutation(ls):
    """Code from https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py"""
	# Find non-increasing suffix
    i = len(ls) - 1
    while i > 0 and ls[i - 1] >= ls[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(ls) - 1
    while ls[j] <= ls[i-1]:
        j -= 1
    ls[i-1], ls[j] = ls[j], ls[i-1]

    # Reverse suffix
    ls[i:] = ls[len(ls) - 1 : i - 1 : -1]
    return True


def read_input():
    records = []
    for line in stdin:
        chunks = line.strip().split()
        conditions = [ch for ch in chunks[0]]
        numbers = [int(token) for token in chunks[1].split(',')]
        records.append((conditions, numbers))
    return records


records = read_input()
v = 0
for record in records:
    conditions, numbers = record
    unknown_state_indexes = [i for i,ch in enumerate(conditions) if ch == '?']
    damaged_count = sum(numbers)
    missing_damaged_count = damaged_count - sum(1 if ch == '#' else 0 for ch in conditions)
    missing_operational_count = len(unknown_state_indexes) - missing_damaged_count
    dispatched = (['#'] * missing_damaged_count) + (['.'] * missing_operational_count)
    dispatched.sort()
    while True:
        for i, symbol in zip(unknown_state_indexes, dispatched):
            conditions[i] = symbol
        s = ''.join(conditions)
        parts = [len(p) for p in s.split('.') if len(p) > 0]
        v += 1 if parts == numbers else 0
        if not next_permutation(dispatched):
            break
print(v)
