with open("inputs/day6.txt") as file:
    data = [int(item) for sublist in [line.strip().split(',') for line in file] for item in sublist] # [1,3,2,4,1,3,....]

def get_nr_of_fishes(days):
    lanterns = [0] * 9
    for nr in data:
        lanterns[nr] += 1
    
    for _ in range(days):
        lanterns[7] += lanterns[0]
        lanterns.append(lanterns.pop(0))
    
    return sum(lanterns)

part1 = get_nr_of_fishes(80)
part2 = get_nr_of_fishes(256)

print("Part 1:", part1)
print("Part 2:", part2)