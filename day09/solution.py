from collections import defaultdict

with open('input.txt') as f:
    lines = [list(map(int, line.split(','))) for line in f.read().splitlines()]


perimeter = set()
areas = []

for i, (ca, ra) in enumerate(lines):
    for j, (cb, rb) in enumerate(lines):
        if i > j:
            area = (abs(ca - cb) + 1) * (abs(ra - rb) + 1)
            areas.append(((ca, ra), (cb, rb), area))
        if ca == cb:
            line = {(ca, num_row) for num_row in range(min(ra, rb), max(ra, rb) + 1)}
        if ra == rb:
            line = {(num_col, ra) for num_col in range(min(ca, cb), max(ca, cb) + 1)}
        perimeter |= line

areas = []
for i, (ca, ra) in enumerate(lines):
    for j, (cb, rb) in enumerate(lines):
        if i > j:
            area = (abs(ca - cb) + 1) * (abs(ra - rb) + 1)
            areas.append((((ca, ra), (cb, rb)), area))

areas = sorted(areas, key=lambda x: x[1], reverse=True)


for area in areas:
    found = True
    ((c1, r1), (c2, r2)), size = area
    min_c, max_c, min_r, max_r = min(c1, c2), max(c1, c2), min(r1, r2), max(r1, r2)

    for cp, rp in perimeter:
        if (min_c < cp < max_c) and (min_r < rp < max_r):
            found = False
            break
    if found:
        print(area)
        break





# track the index of each polygon node in the list

# calculate all of the areas of all possible pairs

# start from the largest areas (so the first valid test will definitely be the largest)

# from the first polygon node, look up the index of the node on the polygon path, then start tracing around it. If any part of the polygon intersects the area rectangle, then we dump it.















# for r in range(max_r + 1):
#     row = []
#     for c in range(max_c + 1):
#         if (c, r) in red_tiles:
#             row.append('#')
#         elif (c, r) in green_tiles:
#             row.append('X')
#         else:
#             row.append('.')
#     print(''.join(row))






















