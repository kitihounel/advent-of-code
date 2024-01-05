from sys import stdin
from itertools import combinations
from collections import namedtuple
from re import findall


Point = namedtuple('Point', ['x', 'y'])
Segment = namedtuple('Segment', ['p', 'q'])


def read_input():
    segments = []
    for line in stdin:
        tokens = findall(r'[\d\-]+', line)
        p = Point(int(tokens[0]), int(tokens[1]))
        q = Point(p.x + int(tokens[3]), p.y + int(tokens[4]))
        segments.append(Segment(p, q))
    return segments


def segment_intersection(a, b):
    """Code from https://rosettacode.org/wiki/Find_the_intersection_of_two_lines"""
    d = (b.q.y - b.p.y) * (a.q.x - a.p.x) - (b.q.x - b.p.x) * (a.q.y - a.p.y)
    if d:
        uA = ((b.q.x - b.p.x) * (a.p.y - b.p.y) - (b.q.y - b.p.y) * (a.p.x - b.p.x)) / d
        uB = ((a.q.x - a.p.x) * (a.p.y - b.p.y) - (a.q.y - a.p.y) * (a.p.x - b.p.x)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = a.p.x + uA * (a.q.x - a.p.x)
    y = a.p.y + uA * (a.q.y - a.p.y)
    return Point(x, y)


def line_intersection(a, b):
    """Code from https://stackoverflow.com/questions/20677795"""
    xdiff = Point(a.p.x - a.q.x, b.p.x - b.q.x)
    ydiff = Point(a.p.y - a.q.y, b.p.y - b.q.y)

    def det(p, q):
        return p.x * q.y - p.y * q.x

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = Point(det(a.p, a.q), det(b.p, b.q))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y)


def colinear(p, q, s):
    return (s.x - q.x) * (q.y - p.y) == (q.x - p.x) * (s.y - q.y)


lo, hi = 2 * 10 ** 14, 4 * 10 ** 14
segments = read_input()
answer = 0
for a, b in combinations(segments, 2):
    i = line_intersection(a, b)
    if i is None:
        continue
    if not (min(a.p.x, i.x) <= a.q.x <= max(a.p.x, i.x) and min(a.p.y, i.y) <= a.q.y <= max(a.p.y, i.y)):
        continue
    if not (min(b.p.x, i.x) <= b.q.x <= max(b.p.x, i.x) and min(b.p.y, i.y) <= b.q.y <= max(b.p.y, i.y)):
        continue
    if lo <= i.x <= hi and lo <= i.y <= hi:
        answer += 1
print(answer)
