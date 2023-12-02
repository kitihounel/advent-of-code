from sys import stdin


def first_digit(seq):
    for ch in seq:
        if ch.isdigit():
            return ch
    raise Exception('Invalid input!')


v = 0
for line in stdin:
    s = line.strip()
    v += int(first_digit(s) + first_digit(reversed(s)))
print(v)
