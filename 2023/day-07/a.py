from sys import stdin
from collections import Counter


def hand_score(hand):
    c = Counter(hand)
    m = c.most_common(2)
    if m[0][1] == 5:
        return 7
    if m[0][1] == 4:
        return 6
    if m[0][1] == 3 and m[1][1] == 2:
        return 5
    if m[0][1] == 3:
        return 4
    if m[0][1] == 2 and m[1][1] == 2:
        return 3
    if m[0][1] == 2:
        return 2
    return 1


def card_score(card):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return cards.index(card)


def hand_key(hand):
    score = hand_score(hand)
    v = tuple(card_score(card) for card in hand)
    return (score, v)


ls = []
for line in stdin:
    chunks = line.split()
    ls.append((chunks[0], int(chunks[1])))

ls.sort(key=lambda t: hand_key(t[0]))
v = 0
for i, (_, b) in enumerate(ls, 1):
    v += i * b
print(v)
