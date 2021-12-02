with open("inputs/day2.txt") as file:
    data = [x for x in [line.split() for line in file]]

# Part 1
position_matrix = [0, 0]  # [horisontal, depth]
for [cmd, val] in data:
    nr = int(val)
    if cmd == 'down':
        position_matrix[1] += nr
    elif cmd == 'up':
        position_matrix[1] -= nr
    else:
        position_matrix[0] += nr

part1 = position_matrix[0] * position_matrix[1]

# Part 2
position_matrix = [0, 0]  # [horisontal, depth]
aim = 0
for [cmd, val] in data:
    nr = int(val)
    if cmd == 'down':
        aim += nr
    elif cmd == 'up':
        aim -= nr
    else:
        position_matrix[0] += nr
        position_matrix[1] += aim * nr

part2 = position_matrix[0] * position_matrix[1]

print("Part 1:", part1)
print("Part 2:", part2)
