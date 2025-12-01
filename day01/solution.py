with open('input.txt') as f:
    instructions = f.read().splitlines()

current_pos = 50
counter = 0
for instr in instructions:
    passed_zero = False
    direction, amount = instr[0], int(instr[1:])

    if direction == "R":
        for _ in range(amount):
            current_pos += 1
            if current_pos > 99:
                current_pos = 0
                counter += 1
    if direction == "L":
        for _ in range(amount):
            current_pos -= 1
            if current_pos < 0:
                current_pos = 99
            if current_pos == 0:
                counter += 1

print(counter)

