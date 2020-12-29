import re

with open("C:\input4.txt") as f:
    input = f.readlines()
    input = [x.strip() for x in input]


REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid, passports, passport = 0, [], {}

input.append('')

for line in input:
    if line == '':
        passports.append(passport)
        passport = {}
    else:
        data = line.split()

        for field in data:
            field = field.split(":")
            passport[field[0]] = field[1]

new = []
for passport in passports:
    keys = passport.keys()
    if all(key in keys for key in REQUIRED_FIELDS):
        valid += 1
        new.append(passport)


legit = 0
eyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for pas in new:

    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    if len(pas.get("byr")) == 4 and 1920 <= int(pas.get("byr")) <= 2002:
        byr = True

    if len(pas.get("iyr")) == 4 and 2010 <= int(pas.get("iyr")) <= 2020:
        iyr = True

    if len(pas.get("eyr")) == 4 and 2020 <= int(pas.get("eyr")) <= 2030:
        eyr = True

    if pas.get("hgt").endswith("cm"):
        temp = pas.get("hgt").split(pas.get("hgt")[-2])[0]
        if 150 <= int(temp) <= 193:
            hgt = True
    if pas.get("hgt").endswith("in"):
        temp = pas.get("hgt").split(pas.get("hgt")[-2])[0]
        if 59 <= int(temp) <= 76:
            hgt = True

    if pas.get("hcl")[0] == '#' and len(pas.get("hcl")[1::]) == 6 and bool(re.match('^[abcdef0123456789]+$', pas.get("hcl")[1::])):
        hcl = True

    if pas.get("ecl") in eyecolor:
        ecl = True

    if len(pas.get("pid")) == 9 and pas.get("pid").isnumeric():
        pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        legit += 1

print(legit)