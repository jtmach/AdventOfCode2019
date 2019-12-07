planets = dict()

def countPlanets(planet, indirectIndex):
    moonCount = 0
    for moon in planet:
        moonCount += 1 + indirectIndex
        if moon in planets:
            moonCount += countPlanets(planets[moon], indirectIndex + 1)
    return moonCount

with open("/Users/a318196/Code/AdventOfCode2020/20191206/input.txt") as file:
    for line in file:
        map = line.split(')')
        if str(map[0]) in planets:
            planets[str(map[0])].append(str(map[1]).strip())
        else:
            planets[str(map[0])] = [str(map[1]).strip()]

orbits = countPlanets(planets['COM'], 0)

print('Solution 1: ' + str(orbits))
