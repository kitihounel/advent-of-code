from sys import stdin


v = 0
for line in map(lambda line: line.strip(), stdin):
    splits = line.split(':')
    relevant_data = splits[1].strip()
    data_splits = [split.strip() for split in relevant_data.split('|')]
    winning_numbers = {int(token) for token in data_splits[0].split()}
    numbers = {int(token) for token in data_splits[1].split()}
    inter = numbers.intersection(winning_numbers)
    v += 0 if len(inter) == 0 else 2 ** (len(inter) - 1)
print(v)
