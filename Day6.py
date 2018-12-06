import numpy as np
from scipy.ndimage.measurements import label


def part1(data):
    num_coords = len(data)
    c = []
    for line in data:
        x, y = line.split(', ')
        c.append((int(x), int(y)))
    dim_max = max(max(c[i][0] for i in range(len(c))), max(c[i][1] for i in range(len(c)))) + 1
    grid = [[0 for x in range(dim_max)] for y in range(dim_max)]
    is_inf = [False]*num_coords
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            dists = []
            for i in range(num_coords):
                dists.append(abs(c[i][0] - row) + abs(c[i][1] - col))
            d_min = min(dists)
            if dists.count(d_min) > 1:
                grid[col][row] = -1
            else:
                local_ID = dists.index(d_min)  # Same ID as order in data
                grid[col][row] = local_ID
                if row == 0 or col == 0 or row == dim_max or col == dim_max:
                    is_inf[local_ID] = True
    m = np.array(grid)
    d = dict(zip(*np.unique(m.ravel(), return_counts=True)))
    large = 0
    for ID in d.keys():
        if d[ID] > large and not is_inf[ID]:
            large = d[ID]
    return large


def part2(data):
    x_list = []
    y_list = []
    for line in data:
        x, y = line.split(', ')
        x_list.append(int(x))
        y_list.append(int(y))
    dim_max = max(max(x_list), max(y_list))
    m = np.matrix([[manhattan(x_list, y_list, x, y) for x in range(dim_max + 1)]
                                                    for y in range(dim_max + 1)])
    structure = np.ones((3, 3), dtype=np.int)
    structure.itemset((0, 0), 0)
    structure.itemset((0, 2), 0)
    structure.itemset((2, 2), 0)
    structure.itemset((2, 0), 0)
    labeled, ncomponents = label(m, structure)
    largest_connected = max(np.bincount(labeled.ravel())[1:])
    return largest_connected


def manhattan(xl, yl, x, y):
    ans = sum([abs(xl[i] - x) + abs(yl[i] - y) for i in range(len(xl))])
    if ans < 10000:
        return 1
    return 0


coords = open('day6_input.txt').read().strip().splitlines()
print('Part 1: ', part1(coords))
print('Part 2: ', part2(coords))
