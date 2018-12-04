

def part1and2(file):
    file = sorted(file)
    dates = dict()
    guards = []
    for line in file:
        if 'begins' in line:
            guard = line.split(' ')[3]
            if guard not in guards:
                guards.append(guard)
        if 'falls' in line:
            date = line.split(' ')[0][6:]
            if date not in dates:
                dates[date] = dict()
                dates[date][guard] = []
            start = int(line.split(' ')[1][3:-1])
        elif 'wakes' in line:
            stop = int(line.split(' ')[1][3:-1])
            tot = stop - start
            dates[date][guard] += [(start, stop, tot)]
    guard_counter = dict()
    for g in guards:
        g_min = [0]*60
        current = 0
        guard_counter[g] = dict()
        guard_counter[g]['tot'] = 0
        guard_counter[g]['common'] = 0
        guard_counter[g]['all_days'] = [0]*60
        for d in dates.keys():
            if g in dates[d]:
                guard_counter[g]['all_days'] = [x + 1 for x in guard_counter[g]['all_days']]
                for session in dates[d][g]:
                    current += session[2]
                    for i in range(session[0], session[1]):
                        g_min[i] += 1
                        guard_counter[g]['all_days'][i] -= 1
        guard_counter[g]['tot'] = current
        guard_counter[g]['common'] = g_min.index(max(g_min))
    largest = 0
    min_val = 0
    for g in guard_counter:
        if guard_counter[g]['tot'] > largest:
            max_g = g
            max_count = guard_counter[g]['tot']
            largest = max_count
        val = max(guard_counter[g]['all_days']) - min(guard_counter[g]['all_days'])
        if val > min_val:
            min_val = val
            most_freq_g = g
            most_freq_min = guard_counter[g]['all_days'].index(min(guard_counter[g]['all_days']))
    return int(max_g[1:])*guard_counter[max_g]['common'], int(most_freq_g[1:])*most_freq_min


file = open('day4_input.txt').read().splitlines()
ans1, ans2 = part1and2(file)
print('Part1: ', ans1, '\nPart 2: ', ans2)

