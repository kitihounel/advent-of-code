from sys import stdin


def first_digit(seq):
    for ch in seq:
        if ch.isdigit():
            return ch
    raise Exception('Invalid input!')


def format(s: str):
    d = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    while True:
        min_index = len(s)
        word = None
        for k in d:
            i = s.find(k)
            if i != -1 and i < min_index:
                min_index = i
                word = k
        if word is not None:
            s = s.replace(word, d[word], 1)
        else:
            break
    return s


v = 0
for line in stdin:
    s = format(line.strip())
    first = first_digit(s)
    last = first_digit(reversed(s))
    v += int(first + last)
print(v)
