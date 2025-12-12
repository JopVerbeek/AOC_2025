from math import prod

with open('input.txt') as f:
    presents_inf = f.read().split('\n\n')

presents = presents_inf[:-1]
configs_raw = presents_inf[-1].splitlines()

presents_map = {}
for i, present in enumerate(presents):
    present_inf = present.splitlines()
    presents_map[i] = sum(line.count('#') for line in present_inf[1:])

c = 0
for config in configs_raw:
    area, composition = config.split(': ')
    floor_area = prod(list(map(int, area.split('x'))))
    composition = list(map(int, composition.split()))
    presents_area = sum(presents_map[i] * amount for i, amount in enumerate(composition))
    if floor_area > presents_area:
        c += 1
print(c)



