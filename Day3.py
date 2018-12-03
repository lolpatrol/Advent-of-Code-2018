

def setup():
    input = open('day3_input.txt').read().splitlines()
    data = dict()
    for line in input:
        line = line.split(' ')
        data[line[0]] = dict()
        x = line[2].replace(':', '').replace(',', ' ').split()
        data[line[0]]['x_diff'] = int(x[0])
        data[line[0]]['y_diff'] = int(x[1])
        d = line[3].replace('x', ' ').split()
        data[line[0]]['dim'] = (int(d[0]), int(d[1]))
    return data


def part1(data):
    grid = dict()
    overlaps = 0
    for key in data:
        key = data[key]
        x_start = key['y_diff']
        y_start = key['x_diff']
        dim_x = key['dim'][1]
        dim_y = key['dim'][0]
        for i in range(x_start, x_start + dim_x):  # Visit all coordinates
            for j in range(y_start, y_start + dim_y):
                if (i, j) not in grid:
                    grid[(i, j)] = 1
                else:
                    grid[(i, j)] += 1
    for pos in grid.keys():  # Count the overlaps of all coordinates
        if grid[pos] > 1:
            overlaps += 1
    return overlaps, grid


def part2(data, grid):
    for id in data.keys():
        is_clean = True
        info = data[id]
        x_start = info['y_diff']
        y_start = info['x_diff']
        dim_x = info['dim'][1]
        dim_y = info['dim'][0]
        for i in range(x_start, x_start + dim_x):  # Check if a rectangle has overlaps
            for j in range(y_start, y_start + dim_y):
                if grid[(i, j)] > 1:
                    is_clean = False
        if is_clean:
            return id[1:]
    return 0


data = setup()
ans, grid = part1(data)
id = part2(data, grid)
print('Part 1: ', ans, '\nPart 2: ', id)

