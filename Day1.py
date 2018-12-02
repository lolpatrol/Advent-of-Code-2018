# Part 1 and 2
def parse_freq(freqs):
    f = 0
    f_first = 0
    two = 0
    visited = dict()
    found = False
    index = 0
    size = len(freqs) - 1
    while not found:
        for line in freqs:
            f += int(line)
            if f in visited and two == 0:
                two = f
                found = True
            else:
                visited[f] = 1
            if index == size:
                f_first = f
            index += 1
    return [f_first, two]
  
  
freqs = open('day1_input.txt').read().strip().split()
[frequency, twice] = parse_freq(freqs)
print('f: ', frequency, '\ntwo: ', twice)
