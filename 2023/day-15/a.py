def compute_hash(s):
    h = 0
    for ch in s:
        h = (h + ord(ch)) * 17 % 256
    return h

seq = input().split(',')
print(sum(compute_hash(s) for s in seq))
