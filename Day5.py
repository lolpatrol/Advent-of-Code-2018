import string


def part1(data):
    reduced = []
    for letter in data:
        if reduced and abs(ord(letter) - ord(reduced[-1])) == 32:
            reduced.pop()
        else:
            reduced.append(letter)
    return len(reduced)


def part2(data):
    smallest = len(data)
    for letter in string.ascii_lowercase:
        temp = data.replace(letter, '').replace(letter.upper(), '')
        smallest = min(part1(temp), smallest)
    return smallest


data = open('day5_input.txt').read().strip()
ans1 = part1(data)
ans2 = part2(data)
print('Part 1: ', ans1, '\nPart 2: ', ans2)

