import os

def CheckPath(x, y):
  currentX = 0
  currentY = 0
  treesHit = 0
  arrayWidth = len(inputArray[0])
  while currentX < len(inputArray) - 1:
    currentX += x
    currentY += y
    #print(str(currentX) + ' - ' + str(currentY % arrayWidth))
    if (inputArray[currentX][currentY % arrayWidth] == "#"):
      treesHit += 1
  return treesHit

script_dir = os.path.dirname(os.path.abspath(__file__))
inputArray = []

with open(os.path.join(script_dir, "input1.txt"), "r") as file:
  for line in file:
    inputArray.append(list(line.strip("\n")))

print ('Read ' + str(len(inputArray)) + ' lines of input')

print('Solution 1: ' + str(CheckPath(1, 3)) + ' trees hit')

movesX = [ 1, 1, 1, 1, 2 ]
movesY = [ 1, 3, 5, 7, 1 ]
currentMove = 0
totalTreesHit = 0
while currentMove < len(movesX):
  treesHit = CheckPath(movesX[currentMove], movesY[currentMove])
  #print ('Trees hit: ' + str(treesHit))
  if currentMove == 0:
    totalTreesHit = treesHit
  else:
    totalTreesHit = totalTreesHit * treesHit
  currentMove += 1

print('Solution 2: ' + str(totalTreesHit) + ' trees hit')