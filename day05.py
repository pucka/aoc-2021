with open("inputs/day5.txt") as file:
    data = [[int(item) for sublist in [x[0].split(','), x[1].split(',')]
             for item in sublist] for x in [line.strip().split(' -> ') for line in file]]

# Part 1
nr_dic = {}
part1 = 0
for line in data:
    if line[0] == line[2] or line[1] == line[3]:
        for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
            for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                nr_dic[(x,y)] = nr_dic.get((x,y), 0) + 1
                if nr_dic[(x,y)] == 2:
                    part1 += 1

# Part 2
part2 = part1
for line in data:
    sorted_x = sorted([line[0], line[2]])
    sorted_y = sorted([line[1], line[3]])
    x_nrs = list(range(sorted_x[0], sorted_x[1] + 1))
    y_nrs = list(range(sorted_y[0], sorted_y[1] + 1))

    if len(x_nrs) != len(y_nrs):
        continue

    if line[1] > line[3]:
        y_nrs.reverse()
    
    if line[0] > line[2]:
        x_nrs.reverse()

    for idx, val in enumerate(x_nrs):
        x = x_nrs[idx]
        y = y_nrs[idx]
        nr_dic[(x,y)] = nr_dic.get((x,y), 0) + 1
        if nr_dic[(x,y)] == 2:
            part2 += 1

# =====================
print("Part 1:", part1)
print("Part 2:", part2)
