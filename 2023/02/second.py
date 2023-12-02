from sys import stdin
from re import findall
from functools import reduce

count = {'red': 12, 'green': 13, 'blue': 14}
v = 0
for game, line in enumerate(stdin, 1):
    d = {'red': 0, 'green': 0, 'blue': 0}
    info = line.split(':')[1].strip()
    rounds = info.split(';')
    for round in rounds:
        tokens = findall('\\w+', round.strip())
        i = 0
        while i < len(tokens):
            color = tokens[i+1]
            d[color] = max(int(tokens[i]), d[color])
            i += 2
    v += reduce(lambda a, b: a * b, d.values(), 1)
print(v)
