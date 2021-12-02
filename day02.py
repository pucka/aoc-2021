with open("inputs/day2.txt") as file:
    data = [line for line in file]

# Part 1
position_matrix = [0, 0]  # [horisontal, depth]
for entry in data:
    [cmd, nr] = [int(x) if x.isdigit() else x for x in entry.split()]

    if cmd == 'down':
        position_matrix[1] += nr
    elif cmd == 'up':
        position_matrix[1] -= nr
    else:
        position_matrix[0] += nr

part1 = position_matrix[0] * position_matrix[1]

# Part 2
position_matrix = [0, 0, 0]  # [horisontal, depth, aim]
for entry in data:
    [cmd, nr] = [int(x) if x.isdigit() else x for x in entry.split()]

    if cmd == 'down':
        position_matrix[2] += nr
    elif cmd == 'up':
        position_matrix[2] -= nr
    else:
        position_matrix[0] += nr
        position_matrix[1] += position_matrix[2] * nr

part2 = position_matrix[0] * position_matrix[1]

print("Part 1:", part1)
print("Part 2:", part2)
