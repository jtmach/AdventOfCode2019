def calculatePositions(path, positions):
    positionX = 0
    positionY = 0
    moveIndex = 0
    for move in path:
        if move[0:1] == 'D':
            index = 1
            while index <= int(move[1:]):
                positionX -= 1
                moveIndex += 1
                positions.append(str(positionX) + ',' + str(positionY) + ',' + str(moveIndex))
                index += 1
        if move[0:1] == 'L':
            index = 1
            while index <= int(move[1:]):
                positionY -= 1
                moveIndex += 1
                positions.append(str(positionX) + ',' + str(positionY) + ',' + str(moveIndex))
                index += 1
        if move[0:1] == 'R':
            index = 1
            while index <= int(move[1:]):
                positionY += 1
                moveIndex += 1
                positions.append(str(positionX) + ',' + str(positionY) + ',' + str(moveIndex))
                index += 1
        if move[0:1] == 'U':
            index = 1
            while index <= int(move[1:]):
                positionX += 1
                moveIndex += 1
                positions.append(str(positionX) + ',' + str(positionY) + ',' + str(moveIndex))
                index += 1

def findMatches(oArray, xArray):
    matchArray = []
    for oPos in oArray:
        for xPos in xArray:
            if oPos.split(',')[0] == xPos.split(',')[0] and oPos.split(',')[1] == xPos.split(',')[1]:
                matchArray.append(oPos.split(',')[0] + ',' + oPos.split(',')[1] + ',' + str(int(oPos.split(',')[2]) + int(xPos.split(',')[2])))
    return matchArray

with open("/Users/a318196/Code/AdventOfCode2020/20191203/input.txt") as file:
    #oPath = 'R8,U5,L5,D3'.split(',')
    #xPath = 'U7,R6,D4,L4'.split(',')
    #oPath = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',') 
    #xPath = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
    #oPath = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
    #xPath = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
    oPath = file.readline().split(',')
    xPath = file.readline().split(',')

oPositions = ['0,0,0']
xPositions = ['0,0,0']

calculatePositions(oPath, oPositions)
calculatePositions(xPath, xPositions)

minPosition = 9999999999
minMoveCount = 9999999999
for position in findMatches(oPositions, xPositions): #(set(oPositions) & set(xPositions)):
    moves = abs(int(position.split(',')[0])) + abs(int(position.split(',')[1]))
    if moves != 0 and abs(moves) < abs(minPosition):
        minPosition = moves
    if moves != 0 and int(position.split(',')[2]) < minMoveCount:
        minMoveCount = int(position.split(',')[2])
    print('Moves: ' + str(moves) + ' Move count: ' + position.split(',')[2])
print('Solution 1: ' + str(minPosition))
print('Solution 2: ' + str(minMoveCount))