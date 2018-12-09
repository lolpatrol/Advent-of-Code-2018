from collections import deque


def solve(players, last_marble):
    circle = deque([0])
    score = [0]*players
    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            circle.rotate(7)
            score[i % players] += i + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(i)
    return max(score)
    
    
    print('Part 1: ', solve(410, 72059), '\nPart 2: ', solve(410, 7205900))
