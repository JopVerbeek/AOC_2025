with open('input.txt') as f:
    ranges, ingredients = f.read().split('\n\n')

ranges = sorted([list(map(int, line.split('-'))) for line in ranges.splitlines()])
ingredients = list(map(int, ingredients.splitlines()))

c = 0
for ingredient in ingredients:
    for start, end in ranges:
        if start <= ingredient <= end:
            c += 1
            break

c2 = 0
max_end = 0
for idx, (start, end) in enumerate(ranges):
    if idx == 0:
        c2 += end - start + 1
        max_end = end
    else:
        prev_start, prev_end = ranges[idx - 1]
        if start > max_end:
            c2 += end - start + 1
            max_end = end
        elif end > max_end:
            c2 += end - max_end
            max_end = end

print(c2)


