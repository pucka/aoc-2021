with open("inputs/day5.txt") as file:
    data = [[int(item) for sublist in [x[0].split(','), x[1].split(',')]
             for item in sublist] for x in [line.strip().split(' -> ') for line in file]]

# Part 1
nr_dic = {}
part1 = 0
for line in data:
    y = -1
    x = -1
    if line[0] == line[2]:
        sorted_nrs = sorted([line[1], line[3]])
        x = line[0]
    elif line[1] == line[3]:
        sorted_nrs = sorted([line[0], line[2]])
        y = line[1]
    else:
        continue

    for nr in range(sorted_nrs[0], sorted_nrs[1] + 1):
        key = str(x if x > -1 else nr) + ',' + str(y if y > -1 else nr)
        nr_dic[key] = nr_dic[key] + 1 if key in nr_dic else 1
        if nr_dic[key] == 2:
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
        key = str(x_nrs[idx]) + ',' + str(y_nrs[idx])
        nr_dic[key] = nr_dic[key] + 1 if key in nr_dic else 1
        if nr_dic[key] == 2:
            part2 += 1

# =====================
print("Part 1:", part1)
print("Part 2:", part2)
