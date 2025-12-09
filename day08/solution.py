import math
from itertools import combinations


with open('input.txt') as f:
    boxes  = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]


groups = {frozenset([b]) for b in boxes}
combs = sorted(combinations(boxes, 2), key=lambda p: math.dist(*p))

c1 = 0
for i, (b1,b2) in enumerate(combs):
    c2 = b1[0] * b2[0]
    group_1, group_2 = [next(g for g in groups if x in g) for x in (b1, b2)]
    groups -= {group_1, group_2}
    groups.add(group_1 | group_2)

    if i+1 == 1000:
        c1 = math.prod(sorted(map(len, groups), reverse=True)[:3])

    if len(groups) == 1:
        break

print(c1, c2)





