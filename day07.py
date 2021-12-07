import statistics
with open("inputs/day7.txt") as file:
    data = [int(item) for sublist in [line.strip().split(',') for line in file] for item in sublist]

median = int(statistics.median(data))
part1 = 0;
for nr in data:
    part1 += abs(median-nr)

print("Part 1:", part1)