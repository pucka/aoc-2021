with open("inputs/day2.txt") as file:
    # data = [["forward", 2],["down", 4]...]
    data = [[x[0], int(x[1])] for x in [line.split() for line in file]]

# Part 1
pos_part1 = {'horisontal': 0, 'depth': 0}
for cmd, nr in data:
    if cmd == 'down':
        pos_part1['depth'] += nr
    elif cmd == 'up':
        pos_part1['depth'] -= nr
    else:
        pos_part1['horisontal'] += nr

# Part 2
pos_part2 = {'horisontal': 0, 'depth': 0}
aim = 0
for cmd, nr in data:
    if cmd == 'down':
        aim += nr
    elif cmd == 'up':
        aim -= nr
    else:
        pos_part2['horisontal'] += nr
        pos_part2['depth'] += aim * nr

print("Part 1:", pos_part1['horisontal'] * pos_part1['depth'])
print("Part 2:", pos_part2['horisontal'] * pos_part2['depth'])
