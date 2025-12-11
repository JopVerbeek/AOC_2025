from collections import defaultdict
from functools import cache


with open('input.txt') as f:
    lines = f.read().replace(':', '').splitlines()

G = defaultdict(list)
for line in lines:
    nodes = line.split(' ')
    parent, children = nodes[0], nodes[1:]
    G[parent].extend(children)

@cache
def paths(node, target):
    if node == target:
        return 1

    total = 0
    for child in G[node]:
        total += paths(child, target)

    return total

p1 = paths('you', 'out')
print(p1)
p2 = (
    (paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')) +
    (paths('svr', 'dac') * paths('dac', 'fft') * paths('fft', 'out'))
)
print(p2)

