import re


def part_1_and_2(data):
    state = data.pop(0).split(' ')[2]
    data.pop(0)
    rules = [data[i].split(' ')[0] for i in range(len(data)) if data[i].split(' ')[-1] == '#']
    plant_index = [m.start() for m in re.finditer('#', state)]  # Index of all plants
    offset = max([rule.index('#') for rule in rules])  # to accommodate space on each side
    old = 0
    diffs = []
    for g in range(50000000000):
        gen_n = []
        for i in range(min(plant_index) - offset, max(plant_index) + offset):
            plant = ['#' if i + j in plant_index else '.' for j in range(-2, 3)]
            if ''.join(plant) in rules:
                gen_n.append(i)
        plant_index = gen_n
        diffs.append(sum(plant_index) - old)
        if g < 20:  # part 1 done, save the result
            ans1 = sum(plant_index)
        elif g >= 20:  # look for repeating diff, because it will be constant at some point
            diff = [True if diffs[k] == diffs[-1] else False for k in range(len(diffs) - 3, len(diffs))]
            if sum(diff) == len(diff):  # found repeating diff
                ans2 = old + diffs[-1] * (50000000000 - g)  # add the number of diffs remaining
                break
        old = sum(gen_n)
        print(g)
    return ans1, ans2


data = open('day12_input.txt').read().strip().splitlines()
ans1, ans2 = part_1_and_2(data)
print('Part 1: ', ans1, '\nPart 2: ', ans2)

