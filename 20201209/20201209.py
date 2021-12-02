import os

def IsSum(preamble, value):
  preambleLenth = len(preamble)
  idx1 = 0
  while idx1 < preambleLenth:
    idx2 = idx1
    while idx2 < preambleLenth:
      if preamble[idx1] + preamble[idx2] == value:
        return True
      idx2 += 1
    idx1 += 1
  return False

script_dir = os.path.dirname(os.path.abspath(__file__))
instructions = []

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  for line in file:
    instructions.append(line.strip('\n'))

print ('Processed ' + str(len(instructions)) + ' instructions')

print (str(IsSum([35, 20, 15, 25, 47], 40)))

idx = 25
while idx < len(instructions):
  

#print('Solution 1: accumulator is ' + str(CheckInstructions(GetAlteredInstructions(-1))[1]))

#accumulatorResult = 0
#infinate = True
#tryIndex = 0
#while infinate and tryIndex < len(instructions):
#  alteredInstructions = GetAlteredInstructions(tryIndex)
#  tryIndex += 1
#  result = CheckInstructions(alteredInstructions)
#  if not result[0]:
#    infinate = result[0]
#    accumulatorResult = result[1]
#    break  

#print('Solution 2: accumulator is ' + str(accumulatorResult))