def passesRuleCheck(possiblePassword):
    previousDigit = 0
    containsAdjacentDigits = False
    for digit in str(possiblePassword):
        if int(digit) < previousDigit:
            return False
        if int(digit) == previousDigit:
            containsAdjacentDigits = True
        else:
            previousDigit = int(digit)       

    return True and containsAdjacentDigits

possiblePasswords = list(range(152085, 670283))
passingPasswordCount = 0
passingPassword2Count = 0
for possiblePassword in possiblePasswords:
    if passesRuleCheck(possiblePassword):
        passingPasswordCount += 1
        for d in str(possiblePassword):
            if sum(digit == d for digit in str(possiblePassword)) == 2:
                passingPassword2Count += 1
                break

print(len(possiblePasswords))
print('Solution to part 1: ' + str(passingPasswordCount))
print('Solution to part 2: ' + str(passingPassword2Count))