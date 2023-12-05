def read_seed_ranges():
    chunks = input().split()
    numbers = [int(chunks[i]) for i in range(1, len(chunks))]
    ranges = []
    for i in range(0, len(numbers), 2):
        t = (numbers[i], numbers[i] + numbers[i+1] - 1)
        ranges.append(t)
    return ranges


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


def match_range_against_map(seed_range, m):
    lo, hi = seed_range
    d, x, y = m[1] - m[0], m[1], m[1] + m[2] - 1
    if y < lo or hi < x:
        # No intersection
        return None, [seed_range]
    else:
        intersection = (max(lo, x) - d, min(hi, y) - d)
        outside = []
        if lo <= x <= y <= hi:
            outside.extend([(lo, x - 1), (y + 1, hi)])
        if lo <= x <= hi <= y:
            outside.append((lo, x - 1))
        if x <= lo <= y <= hi:
            outside.append((y + 1, hi))
        outside = [t for t in outside if t[0] <= t[1]]
        return intersection, outside


def match_range_against_section(seed_range, section):
    q = [seed_range]
    next_section_input = []
    for m in section:
        next_map_input = []
        for seed_range in q:
            intersection, outside = match_range_against_map(seed_range, m)
            if intersection is not None:
                next_section_input.append(intersection)
            next_map_input.extend(outside)
        q = next_map_input
    else:
        next_section_input.extend(q)
    return next_section_input


seed_ranges = read_seed_ranges()
_ = input()
sections = [read_section() for _ in range(7)]
location_ranges = []
for seed_range in seed_ranges:
    next_section_input = [seed_range]
    for section in sections:
        tmp = []
        for sr in next_section_input:
            tmp.extend(match_range_against_section(sr, section))
        next_section_input = tmp
    location_ranges.extend(next_section_input)

assert sum(sr[1] - sr[0] for sr in seed_ranges) == sum(lr[1] - lr[0] for lr in seed_ranges)
location_ranges.sort()
print(location_ranges[0][0])
