

def part1(limit):
    a = 0
    b = 1
    recipes = [3, 7]
    while True:
        recipes += [int(i) for i in str(recipes[a] + recipes[b])]
        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)
        if len(recipes) == (limit + 10):
            return ''.join([str(i) for i in recipes[-10:]])


def part2(limit):
    a = 0
    b = 1
    recipes = [3, 7]
    num = [int(i) for i in str(limit)]
    while True:
        recipes += [int(i) for i in str(recipes[a] + recipes[b])]
        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)
        if recipes[-len(num):] == num:
            return len(recipes) - len(num)
        elif recipes[-len(num) - 1: -1] == num:
            return len(recipes) - len(num) - 1


input = 540391
ans1 = part1(input)
print('Part 1: ', ans1)
ans2 = part2(input)
print('Part 2: ', ans2)

