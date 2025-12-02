with open('input.txt') as f:
    ranges = f.read().split(',')

def chunk_data(sequence):
    for ws in range(1, len(sequence)): # range gaat fout
        if len(sequence) % ws == 0:
            found_seq = []
            for i in range(0, len(sequence) - ws + 1, ws):
                window = sequence[i: i + ws]
                found_seq.append(window)
            if len(set(found_seq)) == 1:
                return True

    return False

counter = 0
for r in ranges:
    first, last = map(int,(r.split('-')))
    for num in range(first, last + 1):
        num_char = str(num)
        if chunk_data(num_char):
            counter += num

print(counter)








