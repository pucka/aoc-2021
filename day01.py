with open("inputs/day1.txt") as file:
    data = [int(line) for line in file]

part1 = 0 
part2 = 0
for i, val in enumerate(data):
    if val > data[i - 1]:
        part1 += 1
    if i > 0 and sum(data[i:i+3]) > sum(data[i-1:i+2]):
        part2 += 1

print("Part 1: ", part1)
print("Part 2: ", part2)
