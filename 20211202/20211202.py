"""
Solves for advent of code 20211202
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = []

with open(os.path.join(SCRIPT_DIR, "input.txt"), "r") as file:
    for line in file:
        INPUT.append(str.split(line.strip('\n'), " "))

print('Processed ' + str(len(INPUT)) + ' instructions')

LENGTH = 0
DEPTH = 0
for instruction in INPUT:
    if instruction[0] == "forward":
        LENGTH += int(instruction[1])
    elif  instruction[0] == "down":
        DEPTH += int(instruction[1])
    elif  instruction[0] == "up":
        DEPTH -= int(instruction[1])

print('Position: ' + str(LENGTH * DEPTH))

AIM = 0
LENGTH = 0
DEPTH = 0
for instruction in INPUT:
    if instruction[0] == "forward":
        LENGTH += int(instruction[1])
        DEPTH += AIM * int(instruction[1])
    elif  instruction[0] == "down":
        AIM += int(instruction[1])
    elif  instruction[0] == "up":
        AIM -= int(instruction[1])

print('Position: ' + str(LENGTH * DEPTH))
