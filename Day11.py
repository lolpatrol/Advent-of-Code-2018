import numpy as np
from scipy.ndimage import convolve


def part1(serial_number):
    grid = np.zeros(shape=(300, 300))
    for y in range(300):
        for x in range(300):
            rack_id = x + 10 + 1
            p_level = (rack_id * (y + 1) + serial_number) * rack_id
            grid[y][x] = ((p_level // 100) % 10) - 5
    kernel = np.ones(shape=(3, 3))
    c_seq = convolve(grid, kernel, mode='constant', cval=0.0)
    coords_max = np.unravel_index(np.argmax(c_seq), c_seq.shape)
    return coords_max[1], coords_max[0]


def part2(serial_number):
    grid = np.zeros(shape=(300, 300))
    for y in range(300):
        for x in range(300):
            rack_id = (x + 1) + 10
            p_level = (rack_id * (y + 1) + serial_number) * rack_id
            grid[y][x] = ((p_level // 100) % 10) - 5
    I = np.cumsum(np.cumsum(grid, axis=0), axis=1)
    largest_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            max_sq = min(i, j) + 1
            for k in range(1, max_sq):
                a = I[i][j] - I[i - k][j] - I[i][j - k] + I[i - k][j - k]
                if a > largest_sum:
                    largest_sum = a
                    dim = (j-k+2, i-k+2, k)
    return dim, largest_sum


print('Part 1:', part1(7803), 'Should be: (20, 51)')
print('Part 2:', part2(7803), 'Should be: ((230, 272, 17), 125.0)')

