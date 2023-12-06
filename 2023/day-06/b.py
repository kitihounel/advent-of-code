from math import sqrt, floor, ceil


def solve(t, d):
    delta = t ** 2 - 4 * d
    x1 = (-t - sqrt(delta)) / -2
    x2 = (-t + sqrt(delta)) / -2
    x1, x2 = min(x1, x2), max(x1, x2)
    # If x1 and x2 are integers, floor and ceil will return the same values, which we don't want.
    # So, we have to increase/decrease them by a small amount before flooring/ceiling them.
    x1 = max(1, ceil(x1 + 0.000001))
    x2 = floor(x2 - 0.000001)
    print('lo:', x1, 'hi:', x2, 'possibilities:', x2 - x1 + 1)


solve(71530, 940200) # Sample input
solve(55826490, 246144110121111) # Real problem
