import re, z3
from  ast import literal_eval
import re


with open('input.txt') as f:
    machines = f.read().splitlines()

c = 0
for machine in machines:
    target = [1 if val == '#' else 0 for val in machine.split(']')[0].split('[')[1]]
    initial_state = [0 for _ in range(len(target))]
    buttons = [[item] if isinstance(item, int) else list(item) for item in list(map(literal_eval, machine.split(' ')[1:-1]))]
    joltages = list(map(int, re.findall('\\d+', machine.split(' ')[-1])))

    # initialize solver
    optimizer = z3.Optimize()

    variables = z3.Ints(f"v{i}" for i in range(len(buttons)))
    for variable in variables:
        optimizer.add(variable >= 0)

    for i, joltage in enumerate(joltages):
        eq = 0
        for bi, button in enumerate(buttons):
            if i in button:
                eq += variables[bi]
        optimizer.add(eq == joltage)
    optimizer.minimize(sum(variables))
    optimizer.check()
    c += optimizer.model().eval(sum(variables)).as_long()

print(c)


