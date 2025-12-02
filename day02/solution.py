with open('input.txt') as f:
    ranges = f.read().split(',')

counter = 0
for r in ranges:
    first, last = map(int,(r.split('-')))
    for num in range(first, last + 1):
        num_char = str(num)
        split_index = len(num_char) // 2
        first_seq, sec_seq = num_char[:split_index], num_char[split_index:]
        if first_seq == sec_seq:
            counter += num


print(counter)