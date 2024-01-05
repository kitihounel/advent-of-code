def read_seeds():
    chunks = input().split()
    return [int(chunks[i]) for i in range(1, len(chunks))]

def read_section():
    ls = []
    _, s = input(), input()
    try:
        while len(s) != 0:
            t = tuple(int(chunk) for chunk in s.split())
            ls.append(t)
            s = input()
    except EOFError:
        pass
    return ls


seeds = read_seeds()
_ = input()
sections = [read_section() for _ in range(7)]
min_location = 10 ** 20
# It will be tricky to use itertools.product(seeds, maps) here. So we fallback to nested for-loops.
for seed in seeds:
    x = seed
    for section in sections:    
        for m in section:
            d = m[1] - m[0]
            if m[1] <= x < m[1] + m[2]:
                x -= d
                break
    min_location = min(min_location, x)
print(min_location)
