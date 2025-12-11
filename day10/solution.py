from ast import literal_eval
from itertools import combinations

with open('input.txt') as f:
    machines = f.read().splitlines()

total = 0
for machine in machines:
    target = [1 if val == '#' else 0 for val in machine.split(']')[0].split('[')[1]]
    initial_state = [0 for _ in range(len(target))]
    buttons = [[item] if isinstance(item, int) else list(item) for item in list(map(literal_eval, machine.split(' ')[1:-1]))]
    button_vectors = []
    for button in buttons:
        button_vec = [0 for _ in range(len(target))]
        for num in button:
            button_vec[num] = 1
        button_vectors.append(button_vec)

    found = False
    for n in range(1, len(buttons) + 1):
        for combs in combinations(button_vectors, n):
            new_state = initial_state[:]
            for mask in combs:
                for i in range(len(mask)):
                    new_state[i] ^= mask[i]
            if new_state == target:
                found = True
                total += n
                break
        if found:
            break

print(total)



