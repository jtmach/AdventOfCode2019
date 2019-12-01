def calculateFuel(weight):
  return int(weight / 3)-2

# Part 1
total = 0
with open("/Users/a318196/Code/AdventOfCode2020/20191201/input.txt") as file:
    for line in file:
        total += calculateFuel(int(line))
print ('Total part 1: ' + str(total))

 # Part 2
total = 0
with open("/Users/a318196/Code/AdventOfCode2020/20191201/input.txt") as file:
    for line in file:
        fuel = calculateFuel(int(line))
        additionalFuel = calculateFuel(fuel)
        while additionalFuel > 0:
            fuel += additionalFuel
            additionalFuel = calculateFuel(additionalFuel)
        total += fuel
print ('Total part 2: ' + str(total))