from copy import deepcopy

with open('input.txt') as f:
    G = [[char for char in line] for line in f.read().splitlines()]

R = len(G)
C = len(G[0])

total_roll_counter = 0
while True:
    roll_counter = 0
    temp_G = deepcopy(G)
    for r in range(R):
        for c in range(C):
            loc = G[r][c]
            if loc == '@':
                neighbour_counter = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if not dr == dc == 0:
                            rr = r + dr
                            cc = c + dc
                            if 0 <= rr < R and 0 <= cc < C:
                                if G[rr][cc] == '@':
                                    neighbour_counter += 1
                if neighbour_counter < 4:
                    roll_counter += 1
                    temp_G[r][c] = '.'

    if roll_counter == 0:
        break

    total_roll_counter += roll_counter
    G = temp_G

print(total_roll_counter)










