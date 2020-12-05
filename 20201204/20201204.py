import os

def GetValidPassportsStrict():
  validPassports = 0
  for passport in passports:
    if (not passport.get("byr") or not passport.get("iyr") or not passport.get("eyr") or not passport.get("hgt") or not passport.get("hcl") or not passport.get("ecl") or not passport.get("pid")):
      continue

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if int(passport.get("byr")) < 1920 or int(passport.get("byr")) > 2002:
      continue

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if int(passport.get("iyr")) < 2010 or int(passport.get("iyr")) > 2020:
      continue

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if int(passport.get("eyr")) < 2020 or int(passport.get("eyr")) > 2030:
      continue
    
    # hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    if not str(passport.get("hgt")).endswith("cm") and not str(passport.get("hgt")).endswith("in"):
      continue
    
    if str(passport.get("hgt")).endswith("cm"):
      if int(passport.get("hgt").strip("cm")) < 150 or int(passport.get("hgt").strip("cm")) > 193:
        continue

    if str(passport.get("hgt")).endswith("in"):
      if int(passport.get("hgt").strip("in")) < 59 or int(passport.get("hgt").strip("in")) > 76:
        continue
    
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if len(passport.get("hcl")) != 7 or list(passport.get("hcl"))[0] != '#':
      continue

    invalidHairColor = False
    for char in str(passport.get("hcl")).strip('#'):
      if ord(char) not in [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103 ]:
        break

    if invalidHairColor:
      continue

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not passport.get("ecl") in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]:
      continue
    
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(passport.get("pid")) != 9 or not str(passport.get("pid")).isnumeric():
      continue

    validPassports += 1
  return validPassports

def GetValidPassports():
  validPassports = 0
  for passport in passports:
    if (passport.get("byr") and passport.get("iyr") and passport.get("eyr") and passport.get("hgt") and passport.get("hcl") and passport.get("ecl") and passport.get("pid")):
      validPassports += 1
  return validPassports

script_dir = os.path.dirname(os.path.abspath(__file__))
passports = []

with open(os.path.join(script_dir, "input.txt"), "r") as file:
  passport = {}
  for line in file:
    if (line.strip('\n') != ""):
      for val in line.strip('\n').split(' '):
        passport[val.split(':')[0]] = val.split(':')[1]
    else:
      passports.append(passport)
      passport = {}
  passports.append(passport)

print ('Read ' + str(len(passports)) + ' passports')

print('Solution 1: ' + str(GetValidPassports()) + ' valid passports')

print('Solution 2: ' + str(GetValidPassportsStrict()) + ' valid passports')