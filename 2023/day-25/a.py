from sys import stdin, setrecursionlimit
from collections import defaultdict
from random import choice
from re import findall
from itertools import combinations

setrecursionlimit(10_000)
time = 0


def read_input():
    g = defaultdict(set)
    edges = []
    for line in stdin:
        names = findall("\\w+", line)
        u = names[0]
        for i in range(1, len(names)):
            v = names[i]
            g[u].add(v)
            g[v].add(u)
            edges.append((min(u, v), max(u, v)))
    return g, edges


def find_bridge():
    global g
    start = choice([k for k in g])
    disc, low = {start: 0}, {start: 0}
    parents = defaultdict(lambda: None)
    visited = {start}
    q = [start]
    time = 1
    while len(q) != 0:
        u = q.pop()
        for v in g[u]:
            if v not in visited:
                q.extend([u, v])
                visited.add(v)
                parents[v] = u
                disc[v] = low[v] = time
                time += 1
                break
            elif v != parents[u]:
                low[u] = min(low[u], disc[v]) 
        else:
            p = parents[u]
            if p is None:
                continue
            low[p] = min(low[u], low[p])
            if low[u] > disc[p]:
                return (min(u, p), max(u, p))


def find_triple():
    global g, edges

    def remove_edge(u, v):
        g[u].remove(v)
        g[v].remove(u)

    def restore_edge(u, v):
        g[u].add(v)
        g[v].add(u)

    for e, f in combinations(edges, 2):
        remove_edge(*e)
        remove_edge(*f)
        bridge = find_bridge(g)
        restore_edge(*e)
        restore_edge(*f)
        if bridge is not None:
            return e, f, bridge


def visit(u, visited):
    global g
    visited.add(u)
    for v in g[u]:
        if v not in visited:
            visit(v, visited)


def solve():
    global g
    for u, v in [('pzv', 'xft'), ('cbx', 'dqf'), ('hbr', 'sds')]:
        g[u].remove(v)
        g[v].remove(u)
    visited = set()
    first = True
    for u in g:
        if not first:
            break
        if u not in visited:
            visit(u, visited)
            first = False
    print(len(visited) * (len(g) - len(visited)))


g, edges = read_input()
solve()
