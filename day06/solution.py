with open('input.txt') as f:
    nums_horizontal = [[num for num in line.split(' ') if num != ''] for line in f.read().splitlines()]

nums_vertical = [[] for _ in range(len(nums_horizontal[0]))]

for nums in nums_horizontal:
    for i, num in enumerate(nums):
        nums_vertical[i].append(num)

c_total = 0
for nums in nums_vertical:
    operator = nums[-1]
    numbers = list(map(int, nums[:-1]))

    if operator == '+':
       c = 0
       for num in numbers:
           c += num
    if operator == '*':
       c = 1
       for num in numbers:
           c *= num
    c_total += c

print(c_total)






