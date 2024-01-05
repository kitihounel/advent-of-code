# Day 25

The solution to this problem is to find a minimum cut in a graph. We will implement it later an efficient solution later
of simply use the `networkx` package.

For now, we ran a very slow algorithm to find the three edges that make the graph disconnected if they were removed.

For each pair of edges, we try to find an edge that is a bridge after the pair has been removed. There is approximatively 3300 edges
in the graph  so the algorithm has a complexity of N^2, which is not that horrible. But sadly it takes a really long time, since we
are using Python. The edges we are looking for are: `('pzv', 'xft')`, `('cbx', 'dqf')`, and `('hbr', 'sds')`.

See the functions `find_triple` and `find_bridge`.
