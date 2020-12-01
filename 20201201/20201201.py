import os

script_dir = os.path.dirname(os.path.abspath(__file__))
inputArray = [200]

with open(os.path.join(script_dir, "input1.txt")) as file:
  inputArray = file.readlines().

num1 = 0
num2 = 0
num3 = 0

for i1 in inputArray:
  for i2 in inputArray:
    if int(i1)+int(i2) == 2020:
      num1 = int(i1)
      num2 = int(i2)
      break

print('Solution 1: ' + str(num1) + ' + ' + str(num2) + ' = 2020 Answer = ' + str(int(num1) * int(num2)))

for i1 in inputArray:
  for i2 in inputArray:
    for i3 in inputArray:
      if int(i1)+int(i2)+int(i3) == 2020:
        num1 = int(i1)
        num2 = int(i2)
        num3 = int(i3)
        break

print('Solution 2: ' + str(num1) + ' + ' + str(num2) + ' + ' + str(num3) + ' = 2020 Answer = ' + str(int(num1) * int(num2) * int(num3)))