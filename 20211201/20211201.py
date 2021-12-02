"""
Solves for advent of code 20211201
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = []

with open(os.path.join(SCRIPT_DIR, "input.txt"), "r") as file:
    for line in file:
        INPUT.append(int(line.strip('\n')))

print('Processed ' + str(len(INPUT)) + ' instructions')

DEEPER_COUNT = -1
PREV_DEPTH = 0
for depth in INPUT:
    if depth > PREV_DEPTH:
        DEEPER_COUNT += 1
    PREV_DEPTH = depth

print('Found ' + str(DEEPER_COUNT) + ' deeper depths')

DEEPER_COUNT = -1
INPT_INDEX = 0
PREV_DEPTH = 0
while INPT_INDEX <= len(INPUT) - 3:
    if (INPUT[INPT_INDEX] + INPUT[INPT_INDEX + 1] + INPUT[INPT_INDEX + 2]) > PREV_DEPTH:
        DEEPER_COUNT += 1
    PREV_DEPTH = INPUT[INPT_INDEX] + INPUT[INPT_INDEX + 1] + INPUT[INPT_INDEX + 2]
    INPT_INDEX += 1

print('Found ' + str(DEEPER_COUNT) + ' deeper depths')
