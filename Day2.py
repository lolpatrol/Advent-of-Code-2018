def has_tuple(letter_dict, num):
    for value in letter_dict.values():
        if value == num:
            return True
    return False


def part1(words):
    has_two = 0
    has_three = 0
    for word in words:
        size = len(word)
        word_dict = dict()
        for i in range(0, size):
            if word[i] not in word_dict:
                word_dict[word[i]] = 1
            else:
                word_dict[word[i]] = word_dict[word[i]] + 1
        if has_tuple(word_dict, 2):
            has_two += 1
        if has_tuple(word_dict, 3):
            has_three += 1
    return has_two*has_three


def part2(words):
    sorted_words = sorted(words)
    word_size = len(sorted_words[0])
    list_size = len(sorted_words)
    for i in range(0, list_size):
        diff = word_size
        correct = ''
        w1 = sorted_words[i]
        w2 = sorted_words[i+1]
        for k in range(0, word_size):
            if w1[k] == w2[k]:
                diff -= 1
                correct += w1[k]
        if diff == 1:  # Let's assume we don't need to run all combinations
            return correct
    return 'Meh'


file = open('day2_input.txt').read().strip().splitlines()
print('Part 1: ', part1(file))
print('Part 2: ', part2(file))
