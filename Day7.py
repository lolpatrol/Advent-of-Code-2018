

def setup(data):
    children_of = dict()  # children_of[a] => a has the children
    parent_of = dict()  # parent_of[a] => a has the parent
    tasks = set()
    for line in data:
        s = line.split(' ')
        first = s[1]
        second = s[7]
        tasks.add(first)
        tasks.add(second)
        if first not in children_of:
            children_of[first] = []
        children_of[first].append(second)
        if second not in parent_of:
            parent_of[second] = []
        parent_of[second].append(first)
    return sorted(list(tasks)), children_of, parent_of


def part1(tasks, children_of, parent_of):
    done = []
    while len(tasks) > 0:
        for task in tasks:
            if task not in parent_of:
                done.append(task)
                tasks.remove(task)
                break
            else:
                parents = parent_of[task]
                count = 0
                for parent in parents:
                    if parent in done:
                        count += 1
                if count == len(parents):
                    done.append(task)
                    tasks.remove(task)
                    break
    return ''.join(done)


def part2(tasks, children_of, parent_of):
    task_timer = {task: ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(task) + 1 + 60, 0) for task in tasks}
    is_assigned = {task: False for task in tasks}
    done = []
    workers = {i: '' for i in range(1, 6)}
    time_passed = -1
    while len(tasks) > 0:
        workers, tasks, done = update_workers(workers, time_passed, task_timer, tasks, done)
        for task in tasks:
            if task not in parent_of and not is_assigned[task]:
                is_assigned[task] = True
                workers, task_timer = assign_task(task, workers, time_passed, task_timer)
            else:
                for done_task in done:
                    if done_task in children_of:
                        for new_task in sorted(children_of[done_task]):
                            p_counter = len(parent_of[new_task])
                            for parent in parent_of[new_task]:
                                if parent in done:
                                    p_counter -= 1
                            if not is_assigned[new_task] and p_counter == 0:
                                is_assigned[new_task] = True
                                workers, task_timer = assign_task(new_task, workers, time_passed, task_timer)
        time_passed += 1
    return time_passed


def assign_task(task, workers, current_time, task_timer):
    for worker in workers:
        if workers[worker] == '':
            workers[worker] = task
            timer = task_timer[task]
            task_timer[task] = (timer[0], timer[0] + current_time)
            return workers, task_timer
    return workers, task_timer


def update_workers(workers, current_time, task_timer, tasks, done):
    for worker in workers:
        if workers[worker] != '':
            task = workers[worker]
            if current_time == task_timer[task][1]:
                done.append(task)
                tasks.remove(task)
                workers[worker] = ''
    return workers, tasks, done


data = open('day7_input.txt').read().strip().splitlines()
tasks, children_of, parent_of = setup(data)
ans1 = part1(tasks.copy(), children_of, parent_of)
print('Part 1: ', ans1)
ans2 = part2(tasks.copy(), children_of, parent_of)
print('Part 2: ', ans2)

