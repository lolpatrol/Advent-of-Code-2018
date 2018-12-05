import string


def part1(data):
    reduced = ''
    for letter in data:
        if reduced and letter.islower() and letter.upper() == reduced[-1]:
            reduced = reduced[:-1]
        elif reduced and letter.isupper() and letter.lower() == reduced[-1]:
            reduced = reduced[:-1]
        else:
            reduced = reduced + letter
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

