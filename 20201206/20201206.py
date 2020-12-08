import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input = []

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  questionaire = {}
  for line in file:
    if (line.strip('\n') != ""):
      if "People" in questionaire:
        questionaire["People"] += 1
      else:
        questionaire["People"] = 1
      
      for val in list(line.strip('\n')):
        if val in questionaire:
          questionaire[val] += 1
        else:
          questionaire[val] = 1
    else:
      input.append(questionaire)
      questionaire = {}
  input.append(questionaire)

print ('Read ' + str(len(input) - 1) + ' questionaires')

totalQuestions = 0
for questionaire in input:
  totalQuestions += len(questionaire) -1

print('Solution 1: ' + str(totalQuestions) + ' questions')

totalQuestions = 0
for questionaire in input:
  for response in questionaire:
    if response != "People" and questionaire["People"] == questionaire[response]:
      totalQuestions += 1

print('Solution 2: ' + str(totalQuestions) + ' questions')