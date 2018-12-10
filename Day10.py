import re


# Just to get the coordinates and velocities.
def parse_file(data):
    m = re.findall('-?\d+.\s+-?\d+', data)
    coord = [(int(m[i].split(',')[0]), int(m[i].split(',')[1])) for i in range(len(m)) if i % 2 == 0]
    velocity = [(int(m[i].split(',')[0]), int(m[i].split(',')[1])) for i in range(len(m)) if i % 2 != 0]
    return coord, velocity


def part_1_and_2(c, v):
    col = [c[i][0] for i in range(len(c))]
    row = [c[i][1] for i in range(len(c))]
    old = [0, 0]
    timer = 0
    while True:
        old[0] = max(row) - min(row)
        old[1] = max(col) - min(col)
        t_col = [0] * len(c)
        t_row = [0] * len(c)
        for i in range(len(c)):
            t_col[i] = col[i] + v[i][0]
            t_row[i] = row[i] + v[i][1]
        if max(t_col) - min(t_col) > old[1] and max(t_row) - min(t_row) > old[0]:
            break
        else:
            col = t_col
            row = t_row
            timer += 1
    print_ans(row, col)
    print('Time: ', timer)


# Build a string from the winning state of the solver, hopefully containing the answer
def print_ans(row, col):
    c = {(row[i], col[i]): 1 for i in range(len(col))}
    ans = ''
    for i in range(min(row), max(row)+1):
        line = ''
        for j in range(min(col), max(col)+1):
            if (i, j) in c:
                line += '#'
            else:
                line += '.'
        ans += line + '\n'
    print(ans)


file = open('day10_input.txt').read().strip()
c, v = parse_file(file)
part_1_and_2(c, v)

