import os

def GetAlteredInstructions(alterationIndex):
  jmpOrNopIndex = 0
  alteredInstrctions = []
  for instruction in instructions:
    instructionType = instruction[0]
    if instructionType == "jmp" or instructionType == "nop":
      if jmpOrNopIndex == alterationIndex:
        if instructionType == "jmp":
          instructionType = "nop"
        else:
          instructionType = "jmp"
      jmpOrNopIndex += 1

    alteredInstrctions.append([ instructionType, instruction[1], instruction[2] ])
  return alteredInstrctions

def CheckInstructions(instructionList):
  accumulator = 0
  instructionIndex = 0
  infinate = True
  done = False
  while not done:
    if instructionIndex >= len(instructionList):
      infinate = False
      done = True
      break
    instruction = instructionList[instructionIndex]
    if instruction[2] == 1:
      done = True
      break
    elif instruction[0] == "jmp":
      instructionIndex += instruction[1]
    elif instruction[0] == "acc":
      accumulator += instruction[1]
      instructionIndex += 1
    elif instruction[0] == "nop":
      instructionIndex += 1
    instruction[2] += 1
  return [infinate, accumulator]

script_dir = os.path.dirname(os.path.abspath(__file__))
instructions = []

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  for line in file:
    instructionParts = line.strip('\n').split(' ')
    instructions.append([ instructionParts[0], int(instructionParts[1]), 0 ])

print ('Processed ' + str(len(instructions)) + ' instructions')

print('Solution 1: accumulator is ' + str(CheckInstructions(GetAlteredInstructions(-1))[1]))

accumulatorResult = 0
infinate = True
tryIndex = 0
while infinate and tryIndex < len(instructions):
  alteredInstructions = GetAlteredInstructions(tryIndex)
  tryIndex += 1
  result = CheckInstructions(alteredInstructions)
  if not result[0]:
    infinate = result[0]
    accumulatorResult = result[1]
    break  

print('Solution 2: accumulator is ' + str(accumulatorResult))