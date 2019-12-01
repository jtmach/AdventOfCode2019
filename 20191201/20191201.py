total = 0

with open("/Users/a318196/Code/AdventOfCode2020/20191201/input.txt") as file:
    for line in file:
        print(int((int(line) / 3))-2)
        total += int((int(line) / 3))-2
print ('Total: ' + str(total))