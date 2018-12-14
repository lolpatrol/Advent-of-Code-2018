

class Cart:
    def __init__(self, pos, dir):
        self.id = None
        self.pos = pos  # tuple
        self.dir = dir
        self.standing_on = None
        self.crashed = False
        self.turn = 0


def setup(data):
    carts = []
    cart_id = 1
    width = max([len(line) for line in data])
    height = len(data)
    padding = ' '
    m = [[' ' for j in range(width)] for i in range(height)]
    for i in range(0, height):
        for j in range(0, width):
            if j < len(data[i]):
                if data[i][j] in '><^v':
                    cart = Cart((i, j), data[i][j])
                    cart.id = cart_id
                    cart_id += 1
                    if data[i][j] in '><':
                        cart.standing_on = '-'
                    elif data[i][j] in '^v':
                        cart.standing_on = '|'
                    carts.append(cart)
                m[i][j] = data[i][j]
            else:
                m[i][j] = padding
    return m, carts


def turn(cart):
    turns = {'>': '^>v', '<': 'v<^', 'v': '>v<', '^': '<^>'}
    d = turns[cart.dir][cart.turn]
    cart.turn = (cart.turn + 1) % 3
    return cart, d


def push_the_carts(grid, carts):
    first_crash = False
    while len(carts) > 1:
        grid, carts, crash_pos = tick(grid, carts)
        if crash_pos is not None and first_crash is False:
            first_crash = True
            part1 = (crash_pos[1], crash_pos[0])
    part2 = (carts[0].pos[1], carts[0].pos[0])
    return part1, part2


def tick(grid, carts):
    carts.sort(key=lambda c: c.pos)
    next_direction = {
        '>\\': 'v',
        '>/': '^',
        '<\\': '^',
        '</': 'v',
        '^\\': '<',
        '^/': '>',
        'v\\': '>',
        'v/': '<'
    }
    crashed = set()
    crash_pos = None
    for cart in carts:
        if cart.id in crashed:
            continue
        x = cart.pos[1]
        y = cart.pos[0]
        dir = cart.dir
        dy = 0
        dx = 0
        if dir == '>':
            dx = 1
        elif dir == '<':
            dx = -1
        elif dir == '^':
            dy = -1
        elif dir == 'v':
            dy = 1
        next_pos = (y + dy, x + dx)
        for other_cart in carts:
            if other_cart.id != cart.id:
                if other_cart.pos == next_pos and other_cart.crashed is False:
                    other_cart.crashed = True
                    cart.crashed = True
                    crashed.add(cart.id)
                    crashed.add(other_cart.id)
                    crash_pos = next_pos
        state = cart.dir + grid[y + dy][x + dx]
        if grid[y + dy][x + dx] in '/\\':
            next_dir = next_direction[state]
        elif grid[y + dy][x + dx] == '+':
            cart, next_dir = turn(cart)
        else:
            next_dir = cart.dir
        cart.standing_on = grid[y + dy][x + dx]
        cart.pos = next_pos
        cart.dir = next_dir
    for id in crashed:
        for cart in carts:
            if cart.id == id:
                carts.remove(cart)
    return grid, carts, crash_pos


file = open('day13_input.txt').read().splitlines()
grid, carts = setup(file)
part1, part2 = push_the_carts(grid, carts)
print('Part 1: ', part1, 'Part 2: ', part2)

