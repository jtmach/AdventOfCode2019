total = 0

# Part 1
with open("/Users/a318196/Code/AdventOfCode2020/20191201/input.txt") as file:
    for line in file:
        total += int((int(line) / 3))-2
print ('Total part 1: ' + str(total))

total = 0
 # Part 2
with open("/Users/a318196/Code/AdventOfCode2020/20191201/input.txt") as file:
    for line in file:
        fuel = int((int(line) / 3))-2
        additionalFuel = 0
        additionalFuel = int(int(fuel / 3) - 2)
        while additionalFuel > 0:
            fuel += additionalFuel
            additionalFuel = int(additionalFuel / 3) - 2
        total += fuel
print ('Total part 2: ' + str(total))