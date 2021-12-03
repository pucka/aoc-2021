with open("inputs/day3.txt") as file:
    data = [line.strip() for line in file]

nr_length = len(data[0])
list_length = len(data)

# Part 1
bin_list = [0] * list_length
for line in data:
    bin_list = [x + y for x, y in zip(bin_list, [int(x) for x in list(line)])]

gamma_rate = int(
    ''.join(map(str, [1 if x/list_length > 0.5 else 0 for x in bin_list])), 2)
epsilon_rate = int(
    ''.join(map(str, [1 if x/list_length < 0.5 else 0 for x in bin_list])), 2)

# Part 2
def filter_list(l:list, idx:int, invert: bool = False):
    if len(l) < 2 or idx >= len(l[0]):
        return l

    diff = sum([int(x[idx])
                for x in l]) / len(l)

    if invert:
        nr_to_look_for = 0 if diff == 0.5 else 1 if diff < 0.5 else 0
    else:
        nr_to_look_for = 1 if diff == 0.5 else 1 if diff > 0.5 else 0

    return filter_list([x for x in l if int(x[idx]) == nr_to_look_for], idx+1, invert)


oxygen_rating = int(filter_list(data, 0)[0], 2)
co2_scrubber_rating = int(filter_list(data, 0, True)[0], 2)

print("Part 1:", gamma_rate * epsilon_rate)
print("Part 2:", oxygen_rating * co2_scrubber_rating)
