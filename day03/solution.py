with open('input.txt') as f:
    batteries = [list(map(int, line)) for line in f.read().splitlines()]

c = 0
for b in batteries:
    first_digit = max(b[:-1])
    second_digit = max(b[b.index(first_digit) + 1:])
    c += int(str(first_digit) + str(second_digit))

c2 = 0
for b in batteries:
    prev_max_i = 0
    arrangement = []
    for i in range(1, 13):
        if i == 12:
            window = b[prev_max_i:]
        else:
            window = b[prev_max_i: -12 + i]
        max_digit = max(window)
        arrangement.append(max_digit)
        max_digit_index = window.index(max_digit)
        prev_max_i += max_digit_index + 1
    c2 += int(''.join([str(num) for num in arrangement]))

print(c)
print(c2)





