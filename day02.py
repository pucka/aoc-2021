with open("inputs/day2.txt") as file:
    data = [line for line in file]

# Part 1
position_matrix = [0, 0] #[horisontal, depth]
part1 = 0
for entry in data:
    [cmd, nr] = entry.split()

    if cmd == 'down':
        position_matrix[1] += int(nr)
    elif cmd == 'up':
        position_matrix[1] -= int(nr)
    else:
        position_matrix[0] += int(nr)

part1 = position_matrix[0] * position_matrix[1]

# Part 2
position_matrix = [0, 0, 0] #[horisontal, depth, aim]
part2 = 0

for entry in data:
    [cmd, nr] = entry.split()

    if cmd == 'down':
        position_matrix[2] += int(nr)
    elif cmd == 'up':
        position_matrix[2] -= int(nr)
    else:
        position_matrix[0] += int(nr)
        position_matrix[1] += position_matrix[2] * int(nr)

part2 = position_matrix[0] * position_matrix[1]

print("Part 1:", part1)
print("Part 2:", part2)
