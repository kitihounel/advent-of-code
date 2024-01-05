from math import sqrt, floor, ceil


def read_input():
    times = [int(chunk) for chunk in input().split(':')[1].split()]
    distances = [int(chunk) for chunk in input().split(':')[1].split()]
    return times, distances


times, distances = read_input()
v = 1
for t, d in zip(times, distances):
    delta = t ** 2 - 4 * d
    if delta < 0:
        pass # no solution for the equation, i.e. impossible to beat the record
    elif delta == 0:
        pass # one solution for the equation, i.e. an infinite number of ways to beat the record
    else:
        x1 = (-t - sqrt(delta)) / -2
        x2 = (-t + sqrt(delta)) / -2
        x1, x2 = min(x1, x2), max(x1, x2)
        # If x1 and x2 are integers, floor and ceil will return the same values, which we don't want.
        # So, we have to increase/decrease them by a small amount before flooring/ceiling them.
        x1 = max(1, ceil(x1 + 0.000001))
        x2 = floor(x2 - 0.000001)
        print(x1, x2)
        v *= x2 - x1 + 1
print(v)
