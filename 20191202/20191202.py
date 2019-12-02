# Solution 1
with open("/Users/a318196/Code/AdventOfCode2020/20191202/input.txt") as file:
    inputText = file.read()
    inputArray = list(map(int, inputText.split(',')))

position = 0
while position < len(inputArray):
    if (inputArray[position] == 1):
        inputArray[inputArray[position + 3]] = inputArray[inputArray[position + 1]] + inputArray[inputArray[position + 2]]
        position += 4
    if (inputArray[position] == 2):
        inputArray[inputArray[position + 3]] = inputArray[inputArray[position + 1]] * inputArray[inputArray[position + 2]]
        position += 4
    if (inputArray[position] == 99):
        position = len(inputArray)
print('Solution 1: ' + str(inputArray[0]))

# Solution 2
noun = 0
while noun <= 99:
    verb = 0
    while verb <= 99:
        with open("/Users/a318196/Code/AdventOfCode2020/20191202/input.txt") as file:
            inputText = file.read()
            inputArray = list(map(int, inputText.split(',')))
            inputArray[1] = noun
            inputArray[2] = verb

        position = 0
        while position < len(inputArray):
            if (inputArray[position] == 1):
                inputArray[inputArray[position + 3]] = inputArray[inputArray[position + 1]] + inputArray[inputArray[position + 2]]
                position += 4
            if (inputArray[position] == 2):
                inputArray[inputArray[position + 3]] = inputArray[inputArray[position + 1]] * inputArray[inputArray[position + 2]]
                position += 4
            if (inputArray[position] == 99):
                position = len(inputArray)
        if (inputArray[0] == 19690720):
            break
        verb += 1
    if (inputArray[0] == 19690720):
        break
    noun += 1
print('Solution 2: ' + str(100 * noun + verb))
