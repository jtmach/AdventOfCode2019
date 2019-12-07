planets = dict()

def countPlanets(planet, indirectIndex):
    moonCount = 0
    for moon in planet:
        moonCount += 1 + indirectIndex
        if moon in planets:
            moonCount += countPlanets(planets[moon], indirectIndex + 1)
    return moonCount

def getPathToPlanet(moonName, planetName):
    path = []
    if (moonName != planetName):
        planet = getPlanetsWithMoon(moonName)
        path.append(planet)
        for moon in getPathToPlanet(planet, planetName):
            path.append(moon)
    return path

def getPlanetsWithMoon(moonName):
    for planet in planets:
        if moonName in planets[planet]:
            return planet

with open("/Users/a318196/Code/AdventOfCode2020/20191206/input.txt") as file:
    for line in file:
        map = line.split(')')
        if str(map[0]) in planets:
            planets[str(map[0])].append(str(map[1]).strip())
        else:
            planets[str(map[0])] = [str(map[1]).strip()]

orbits = countPlanets(planets['COM'], 0)

print('Solution 1: ' + str(orbits))

youOrbit = getPlanetsWithMoon('YOU')
sanOrbit = getPlanetsWithMoon('SAN')

youPath = getPathToPlanet(youOrbit, 'COM')
sanPath = getPathToPlanet(sanOrbit, 'COM')

intersections = set(youPath) & set(sanPath)

orbitTransfers = 9999999
for intersection in intersections:
    transfers = len(getPathToPlanet(youOrbit, intersection)) + len(getPathToPlanet(sanOrbit, intersection))
    if (transfers < orbitTransfers):
        orbitTransfers = transfers

print('Solution 2: ' + str(orbitTransfers))