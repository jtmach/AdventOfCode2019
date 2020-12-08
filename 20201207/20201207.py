import os

def CanHoldGold(bagContents):
  if "shiny gold bag" in bagContents:
    return True
  else:
    for bag in bagContents:
      if CanHoldGold(BagRules[bag]):
        return True
  return False

def CountOfBags(bagContents):
  contents = 0
  for bag in bagContents:
    contents += bagContents[bag] + (bagContents[bag] * CountOfBags(BagRules[bag]))
  return contents

script_dir = os.path.dirname(os.path.abspath(__file__))
BagRules = {}

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  for line in file:
    bagRule = line.strip('\n').split("contain")
    bagType = bagRule[0].strip().rstrip('s')
    
    contents = {}
    if bagRule[1].strip() != "no other bags.":
      contentRules = bagRule[1].split(",")
      for contentRule in contentRules:
        contentRuleCount = contentRule[contentRule.strip().index(' ')]
        contentRuleBag = contentRule.replace(contentRuleCount, '').strip('.').replace('bags', 'bag').strip()
        contents[contentRuleBag] = int(contentRuleCount) 
    BagRules[bagType] = contents

print ('Processed ' + str(len(BagRules)) + ' bag rules')

valid = 0
for bagRule in BagRules:
  if (CanHoldGold(BagRules[bagRule])):
    valid += 1

print('Solution 1: ' + str(valid) + ' bags')

print('Solution 2: ' + str(CountOfBags(BagRules["shiny gold bag"])) + ' bags needed')