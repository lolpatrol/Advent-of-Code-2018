import numpy as np
from scipy.ndimage.measurements import label


def part1(data):
    x_list = []
    y_list = []
    num_coords = len(data)
    for line in data:
        x, y = line.split(', ')
        x_list.append(int(x))
        y_list.append(int(y))
    row_max = max(x_list)
    col_max = max(y_list)
    dim_max = max(row_max, col_max)
    grid = [[0 for x in range(dim_max+1)] for y in range(dim_max+1)]
    is_inf = [False]*num_coords
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            dists = []
            for i in range(num_coords):
                d = abs(x_list[i]-row)+abs(y_list[i]-col)
                dists.append(d)
            d_min = min(dists)
            num_of_same = dists.count(d_min)
            if num_of_same > 1:
                grid[col][row] = '.'
            else:
                local_ID = dists.index(d_min)  # Same ID as order in data
                grid[col][row] = local_ID
                if row == 0 or col == 0 or row == dim_max or col == dim_max:
                    is_inf[local_ID] = True
    counts = []
    for ID in range(0, num_coords):
        if is_inf[ID] is not True:
            counter = 0
            for i in range(0, dim_max):
                for j in range(0, dim_max):
                    if grid[i][j] == ID:
                        counter += 1
            counts.append(counter)
    return max(counts)


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
