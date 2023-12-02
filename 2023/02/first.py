from sys import stdin
from re import findall


count = {'red': 12, 'green': 13, 'blue': 14}
v = 0
for game, line in enumerate(stdin, 1):
    info = line.split(':')[1].strip()
    rounds = info.split(';')
    possible = True
    for round in rounds:
        s = round.strip()
        tokens = findall('\\w+', s)
        i = 0
        while i < len(tokens) and possible:
            color = tokens[i+1]
            possible = int(tokens[i]) <= count[color]
            i += 2
        if not possible:
            break
    v += game if possible else 0
print(v)
