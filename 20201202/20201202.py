import os

class inputLine:
  def __init__(self, min, max, criteria, password):
    self.min = min
    self.max = max
    self.criteria = criteria
    self.password = password

  def IsCountBetweenCriteria(self):
    cnt = self.password.count(self.criteria)
    if cnt >= self.min and cnt <= self.max:
      return True

  def IsCriteriaValid(self):
    passwordArray = list(self.password)
    if passwordArray[self.min - 1] != passwordArray[self.max - 1]:
      if passwordArray[self.min - 1] == self.criteria or passwordArray[self.max - 1] == self.criteria:
        return True

script_dir = os.path.dirname(os.path.abspath(__file__))
inputArray = []

with open(os.path.join(script_dir, "input1.txt"), "r") as file:
  for line in file:
    parts = line.split(' ')
    inputArray.append(inputLine(int(parts[0].split('-')[0]), int(parts[0].split('-')[1]), parts[1].strip(':'), parts[2].strip('\n')))

print ('Read ' + str(len(inputArray)) + ' lines of input')

valid = 0
for line in inputArray:
  if line.IsCountBetweenCriteria():
    valid += 1

print('Solution 1: ' + str(valid) + ' passwords')

valid = 0
for line in inputArray:
  if line.IsCriteriaValid():
      valid += 1

print('Solution 2: ' + str(valid) + ' passwords')