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
        if diff == 1:
            return correct
    return 'Meh'
