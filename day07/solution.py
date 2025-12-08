from collections import deque
from functools import cache

with open('input.txt') as f:
    G = f.read().splitlines()

R = len(G)
C = len(G[0])


# find the starting coordinate

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r, c)

# bfs
queue = deque([start])
seen = set()
split_counter = 0
while queue:
    r, c = queue.popleft()
    if (r, c) in seen: continue
    seen.add((r, c))
    if r + 1 >= R: continue
    if G[r+1][c] == '^':
        split_counter += 1
        queue.append((r + 1, c - 1))
        queue.append((r + 1, c + 1))
    else:
        queue.append((r + 1, c))

print(split_counter)


# part 2
@cache
def paths(r, c):
    if r + 1 >= R:
        return 1
    if G[r + 1][c] == '^':
        return paths(r + 1, c - 1) + paths(r + 1, c + 1)
    else:
        return paths(r + 1, c)

print(paths(start[0], start[1]))
