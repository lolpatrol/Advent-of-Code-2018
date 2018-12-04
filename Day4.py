

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


# Slightly shorter version
def shorter(data):
    data = sorted(data)
    g_a = dict()
    g_b = dict()
    for line in data:
        if 'begins' in line:
            guard = line.split(' ')[3]
            if guard not in g_a:
                g_a[guard] = [0]*60
                g_b[guard] = 0
        if 'falls' in line:
            start = int(line.split(' ')[1][3:-1])
        elif 'wakes' in line:
            stop = int(line.split(' ')[1][3:-1])
            g_b[guard] += stop - start
            for i in range(start, stop):
                g_a[guard][i] += 1
    most_sleepy = max(g_b, key=g_b.get)
    most_slept = g_a[most_sleepy].index(max(g_a[most_sleepy]))
    frequent_sleeper = max(g_a, key=lambda k: max(g_a.get(k)))
    frequent_slept = g_a[frequent_sleeper].index(max(g_a[frequent_sleeper]))
    return int(most_sleepy[1:])*most_slept, int(frequent_sleeper[1:])*frequent_slept


file = open('day4_input.txt').read().splitlines()
ans1, ans2 = part1and2(file)
print('Part 1: ', ans1, '\nPart 2: ', ans2)
print('Ans: ', shorter(file))

