from re import findall

def compute_hash(s):
    h = 0
    for ch in s:
        h = (h + ord(ch)) * 17 % 256
    return h

seq = input().split(',')
boxes = [{} for _ in range(256)]
for instruction in seq:
    s = findall('[a-z]+', instruction)[0]
    h = compute_hash(s)
    box = boxes[h]
    if instruction[-1] == '-':
        if s in box:
            del box[s]
    else:
        f = int(instruction[-1])
        box[s] = f

v = 0
for i, box in enumerate(boxes, 1):
    j = 1
    for k in box:
        v += i * j * box[k]
        j += 1
print(v)
