with open('input.txt') as f:
    row_nums = [[char for char in line] for line in f.read().splitlines()]

max_len = 0
for row_num in row_nums:
    max_len = max(max_len, len(row_num))

row_nums = [[char for char in line] for line in row_nums]
row_nums = [[*line, *[" "] * ((max_len + 1) - len(line))] for line in row_nums]
positions = {idx: val for idx, val in enumerate(row_nums[-1]) if val != ' '}

ranges = []
for i in range(len(positions.keys())):
    items = list(positions.keys())
    if i == 0:
        window = (0, items[i] - 1)
    else:
        window = (items[i - 1], items[i] - 1)
        ranges.append(window)
ranges.append((ranges[-1][1] + 1, max_len))

total = 0
for (start, end), operator in zip(ranges, positions.values()):

    c = 1 if operator == '*' else 0
    for i in range(start, end):
        str_num = ''
        if operator == '*':
            for row in row_nums[:-1]:
                if row[i].isdigit():
                    str_num += row[i]
            c *= int(str_num)

        if operator == '+':
            for row in row_nums[:-1]:
                if row[i].isdigit():
                    str_num += row[i]
            c += int(str_num)
    total += c

print(total)













