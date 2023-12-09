from sys import stdin
from collections import Counter
from itertools import product


cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def plain_hand_score(hand):
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


def hand_score(hand):
    chars = [ch for ch in hand]
    j_indexes = [i for i, ch in enumerate(chars) if ch == 'J']
    if len(j_indexes) == 0:
        return plain_hand_score(hand)

    max_score = -1
    seen = set()
    choices = [ch for  ch in hand if ch != 'J'] + ['J']
    for tup in product(choices, repeat=len(j_indexes)):
        for i, ch in zip(j_indexes, tup):
            chars[i] = ch
        new_hand = ''.join(chars)
        if new_hand not in seen:
            score = plain_hand_score(new_hand)
            max_score = max(score, max_score)
            seen.add(new_hand)
            if max_score == 7:
                break

    return max_score


def card_score(card):
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
