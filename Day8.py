

def part1(data):
    a = data.pop(0)                                    # Pop header and metadata count
    b = data.pop(0)
    if a > 0:                                          # If the metadata is not adjacent
        rec_sum = [part1(data) for i in range(a)]       # Pop until the recursive call is not run
        meta_sum = sum(data.pop(0) for i in range(b))  # which is when a = 0
        t = sum(rec_sum) + meta_sum                    # Then sum and return
    else:
        t = sum(data.pop(0) for i in range(b))         # Here a = 0
    return t


# Second part nearly the same.
# Get value of each end node, return the value of the nodes with children, where their
# metadata entries are references to the child nodes they might, or might not have.
# Sum and return until root.
def part2(data):
    a = data.pop(0)
    b = data.pop(0)
    rec_sum = [part2(data) for i in range(a)]
    meta_nums = [data.pop(0) for i in range(b)]
    if a == 0:
        t = sum(meta_nums)
    else:
        t = 0
        for i in meta_nums:
            if i-1 in range(a):
                t += rec_sum[i-1]
    return t


file = open('day8_input.txt').read().split()
data = [int(i) for i in file]
print('Part 1: ', part1(data.copy()))
print('Part 2: ', part2(data.copy()))
