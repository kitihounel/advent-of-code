from sys import stdin


table = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def first_digit(s: str):
    min_index = len(s)
    symbol = None
    for k in table:
        i = s.find(k)
        if i != -1 and i < min_index:
            min_index = i
            symbol = k
    return table[symbol]


def last_digit(s: str):
    max_index = -1
    symbol = None
    for k in table:
        i = s.rfind(k)
        if i != -1 and i > max_index:
            max_index = i
            symbol = k
    return table[symbol]


v = 0
for line in stdin:
    s = line.strip()
    v += int(first_digit(s) + last_digit(s))
print(v)
