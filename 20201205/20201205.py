import os
import math

def FindSeat(boardingPass):
  rowEnd = 127
  rowStart = 0
  seatEnd = 8
  seatStart = 0
  for char in list(boardingPass):
    if (char == 'B'):
      rowStart += math.ceil((rowEnd - rowStart) / 2)

    if (char == 'F'):
      rowEnd -= math.floor((rowEnd - rowStart) / 2)

    if (char == 'R'):
      seatStart += math.ceil((seatEnd - seatStart) / 2)

    if (char == 'L'):
      seatEnd -= math.floor((seatEnd - seatStart) / 2)

  return (rowStart * 8) + seatStart

script_dir = os.path.dirname(os.path.abspath(__file__))
boardingPasses = []

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  for line in file:
    boardingPasses.append(line.strip('\n'))

print ('Read ' + str(len(boardingPasses)) + ' boarding passes')

print ('Test ' + str(FindSeat('BFFFBBFRRR')))
print ('Test ' + str(FindSeat('FFFBBBFRRR')))
print ('Test ' + str(FindSeat('BBFFBBFRLL')))

highestSeat = 0
for boardingPass in boardingPasses:
  seat = FindSeat(boardingPass)
  if seat > highestSeat:
    highestSeat = seat

print('Solution 1: ' + str(highestSeat) + ' is the highest seat')

assignedSeats = []
for boardingPass in boardingPasses:
  assignedSeats.append(FindSeat(boardingPass))

assignedSeats.sort()
start = assignedSeats[0]
for assignedSeat in assignedSeats:
  if start == assignedSeat:
    start += 1
  else:
    break

print('Solution 2: ' + str(start) + ' is your seat')